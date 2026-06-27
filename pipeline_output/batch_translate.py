#!/usr/bin/env python3
"""
Batch Lean translation pipeline.
Processes concepts in batches of 5, with checkpointing and cost tracking.
"""
import os, sys, json, time, logging
from datetime import datetime

sys.path.insert(0, "/home/a123/文档/mathpkg")
from mathpkg.pipeline.gap_fill import fill_gaps
from mathpkg.pipeline.lean_translate import translate_to_lean
from mathpkg.pipeline.self_heal import compile_and_heal

logging.basicConfig(level=logging.WARNING, format="%(message)s")
logger = logging.getLogger("batch")

DEDUP_DIR = "/home/a123/文档/mathpkg/pipeline_output/dedup"
RESULT_DIR = "/home/a123/文档/mathpkg/pipeline_output/translations"
os.makedirs(RESULT_DIR, exist_ok=True)

# Load sorted concepts
with open(os.path.join(DEDUP_DIR, "canonical_with_distance.json")) as f:
    canonical = json.load(f)

# Sort: distance=1 concepts by impact score
ready = [c for c in canonical if c.get("mathlib4_distance") == 1]
ready.sort(key=lambda c: -(c["num_books"] * max(1, len(c.get("depends_on",[])))))

# Load checkpoint
CHECKPOINT = os.path.join(RESULT_DIR, "_checkpoint.json")
completed = set()
total_cost = 0.0
if os.path.exists(CHECKPOINT):
    with open(CHECKPOINT) as f:
        cp = json.load(f)
    completed = set(cp.get("completed_ids", []))
    total_cost = cp.get("total_cost_yuan", 0.0)
    print(f"📂 Resuming: {len(completed)} done, ¥{total_cost:.2f} spent")

BATCH_SIZE = 5
MODEL = "deepseek-v4-pro"

# Filter to remaining
remaining = [c for c in ready if c["id"] not in completed]
total_remaining = len(remaining)

print(f"🎯 {total_remaining} concepts remaining, processing in batches of {BATCH_SIZE}")
print(f"   Model: {MODEL} (thinking mode)")
print(f"   Results: {RESULT_DIR}/")
print(f"{'='*60}")

batch_num = (len(completed) // BATCH_SIZE) + 1 if completed else 1

for batch_start in range(0, len(remaining), BATCH_SIZE):
    batch = remaining[batch_start:batch_start + BATCH_SIZE]
    batch_costs = []
    
    print(f"\n── Batch {batch_num} ({len(batch)} concepts) ──")
    t_batch = time.time()
    
    for i, concept in enumerate(batch):
        cid = concept["id"]
        name = concept["name"]
        statement = concept.get("statement", "")
        sketch = concept.get("proof_sketch", "")
        deps = concept.get("depends_on", [])
        
        print(f"\n  [{i+1}/{len(batch)}] {name[:60]}")
        print(f"    Deps: {deps}")
        
        if not sketch:
            print(f"    ⚠️  No proof sketch — skipping Lean translation")
            completed.add(cid)
            continue
        
        cost_before = total_cost
        
        try:
            # Step 1: Gap-fill
            print(f"    [1/3] Gap-filling...", end=" ", flush=True)
            t1 = time.time()
            gap = fill_gaps(cid, statement, sketch, model=MODEL)
            total_cost += gap.cost_yuan
            print(f"{gap.steps_count} steps, ¥{gap.cost_yuan:.4f} ({time.time()-t1:.0f}s)")
            
            # Step 2: Lean translate
            print(f"    [2/3] Lean translating...", end=" ", flush=True)
            t2 = time.time()
            ctx = ""
            if deps:
                ctx = "These concepts are already in Mathlib4: " + ", ".join(deps[:5])
            lean = translate_to_lean(cid, statement, gap.expanded_proof, 
                                     lean_context=ctx, model=MODEL)
            total_cost += lean.cost_yuan
            print(f"{len(lean.lean_code)} chars, ¥{lean.cost_yuan:.4f} ({time.time()-t2:.0f}s)")
            
            # Step 3: Compile + self-heal
            print(f"    [3/3] Compiling...", end=" ", flush=True)
            t3 = time.time()
            heal = compile_and_heal(cid, lean.lean_code, max_rounds=10, model=MODEL)
            total_cost += heal.total_cost_yuan
            status = "✅" if heal.success else "❌"
            print(f"{status} {heal.rounds} rounds, ¥{heal.total_cost_yuan:.4f} ({time.time()-t3:.0f}s)")
            
            # Save individual result
            result = {
                "id": cid,
                "name": name,
                "gap_fill": {"steps": gap.steps_count, "cost": gap.cost_yuan, "expanded_proof": gap.expanded_proof[:2000]},
                "lean_translate": {"code": lean.lean_code, "cost": lean.cost_yuan, "theorems_used": lean.mathlib4_theorems_used},
                "self_heal": {"success": heal.success, "rounds": heal.rounds, "cost": heal.total_cost_yuan,
                              "errors": heal.errors[:10], "final_code": heal.final_code[:2000] if heal.success else None},
                "total_cost": gap.cost_yuan + lean.cost_yuan + heal.total_cost_yuan,
                "timestamp": datetime.now().isoformat(),
            }
            with open(os.path.join(RESULT_DIR, f"{cid}.json"), "w") as f:
                json.dump(result, f, indent=1, ensure_ascii=False)
            
        except Exception as e:
            print(f"\n    ❌ ERROR: {e}")
            result = {"id": cid, "name": name, "error": str(e), "timestamp": datetime.now().isoformat()}
            with open(os.path.join(RESULT_DIR, f"{cid}.json"), "w") as f:
                json.dump(result, f, indent=1)
        
        completed.add(cid)
        step_cost = total_cost - cost_before
        batch_costs.append(step_cost)
        print(f"    💰 Step cost: ¥{step_cost:.4f} | Total: ¥{total_cost:.4f}")
        
        # Save checkpoint after EVERY concept
        with open(CHECKPOINT, "w") as f:
            json.dump({
                "completed_ids": list(completed),
                "total_cost_yuan": total_cost,
                "last_updated": datetime.now().isoformat(),
                "remaining": total_remaining - len(completed) + (len(completed) - batch_start - i - 1)
            }, f, indent=1)
    
    batch_time = time.time() - t_batch
    batch_cost = sum(batch_costs)
    print(f"\n  📊 Batch {batch_num} done: ¥{batch_cost:.4f} in {batch_time:.0f}s")
    batch_num += 1

# Final report
succeeded = 0
failed = 0
for cid in completed:
    rpath = os.path.join(RESULT_DIR, f"{cid}.json")
    if os.path.exists(rpath):
        with open(rpath) as f:
            r = json.load(f)
        if r.get("self_heal", {}).get("success"):
            succeeded += 1
        elif "error" in r:
            failed += 1

print(f"\n{'='*60}")
print(f"  BATCH COMPLETE")
print(f"{'='*60}")
print(f"  Completed: {len(completed)} concepts")
print(f"  ✅ Compiled: {succeeded}")
print(f"  ❌ Failed:   {failed}")
print(f"  💰 Total cost: ¥{total_cost:.4f}")
print(f"  📁 Results: {RESULT_DIR}/")
print(f"{'='*60}")
