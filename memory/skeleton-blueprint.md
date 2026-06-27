---
name: skeleton-dependency-blueprint
description: "Lean skeleton build: 240 distance=1 concepts → lake build verified dependency DAG"
metadata: 
  node_type: memory
  type: project
  originSessionId: 32b0208b-f009-4db0-9b54-c8a7af2b3275
---

# Skeleton Dependency Blueprint (2026-06-23)

## Achievement

240 distance=1 concepts → 231 skeleton .lean files → **lake build passed**.
The Lean compiler verified the dependency structure: types are correct, no circular deps, no name collisions.

## What We Did

1. **Generated skeletons**: Each concept → `import Mathlib` + type signature + `:= by sorry`
2. **lake build**: 231 files, 85 type errors found
3. **Fixed type signatures**: 4 Workflows × 22 concepts, Checker+Fixer pattern
4. **Resolved name conflicts**: 4 auto-renamed (IsOmegaSubgroup, coordinateRing, etc.)
5. **Final build**: ✅ passed

## Key Insight

**The Lean compiler IS the dependency validator.** Python graph algorithms can miss:
- Type mismatches between concepts
- Name collisions across independent modules
- Implicit dependencies not declared in YAML

Only the Lean type checker catches ALL of these.

## Auto-Conflict Resolution Script

```python
# Resolves "environment already contains 'X'" errors
for iteration in range(20):
    output = lake_build()
    conflicts = re.findall(r"environment already contains '(\w+)' from MathPkg\.Skeleton\.(\w+)", output)
    if not conflicts: break
    name, source_file = conflicts[0]
    new_name = f'{source_file}_{name}'
    # Replace ALL occurrences in the offending file
    content = re.sub(rf'\b{name}\b', new_name, content)
```

## Stats

| Metric | Value |
|---|---|
| Total distance=1 concepts | 240 |
| Skeleton files created | 231 |
| Initial type errors | 85 (37%) |
| Type errors fixed | 85 |
| Name conflicts resolved | 4 |
| Final build | ✅ |
| Agent calls (skeleton gen) | 423 |
| Agent calls (type fix) | 272 |
| Agent calls (definition fix) | 14 |

## Related

- [[batch1-translation]] — full translation pipeline
- [[resilient-workflow]] — Checker+Fixer pattern
- [[subagent-workflow]] — agent workflow lessons
