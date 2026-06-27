# mathpkg — Technical Documentation

> Mathematical Knowledge Package Manager  
> Phase 0 Complete · June 2026

---

## 1. Project Overview

**mathpkg** builds a machine-verifiable, dependency-managed knowledge graph of mathematics from Springer's Graduate Texts in Mathematics (GTM) and Undergraduate Texts in Mathematics (UTM) series — 489 textbooks spanning algebra, analysis, geometry, topology, and number theory.

The system models mathematical knowledge management after **apt** (Debian's package manager): concepts are packages, theorems have dependencies, and `math install <concept>` resolves the complete learning path.

### Key Numbers (Phase 0)

| Metric | Value |
|---|---|
| PDFs processed | 489 (303 GTM + 186 UTM) |
| Text extracted | 409 books (298 MB Markdown) |
| Quality classification | 414 books evaluated (Flash, ¥2) |
| Concepts extracted | 5,779 from 20 strategic books (Pro+Thinking, ¥40) |
| Canonical concepts | 5,527 after dedup |
| Lean-ready (distance=1) | 240 concepts |
| Lean verified | Sylow I & III compiled ✅ |
| Python tests | 28/28 passing |
| CLI commands | 8 (source, update, show, install, mark, status, verify, lean) |

---

## 2. Architecture

### 2.1 apt Model Mapping

```
apt component              mathpkg
───────────────────────────────────────────
sources.list               sources.yaml
Packages.gz                index.yaml (per topic)
pkgCache (mmap binary)     SQLite (concepts + deps + versions)
DepCache + SAT Solver      LearningPathResolver
dpkg status                ~/.mathpkg/status.yaml
apt-get install            math install <concept>
Transport Methods          SourceAdapter plugins
```

### 2.2 Knowledge Graph Data Model

```yaml
# concepts/algebra/group_theory/nodes/lagrange_theorem.yaml
id: lagrange_theorem
name: {en: "Lagrange's Theorem", zh: "拉格朗日定理"}
type: theorem

depends:
  required: [subgroup, coset]
  recommended: [group_action]
  suggested: [cyclic_group]

versions:                    # Cross-book references
  - source: GTM073, author: Hungerford, chapter: I, section: I.4, pages: 38-42
  - source: GTM080, author: Robinson, chapter: 1, section: 1.3, pages: 15-17
  - source: GTM148, author: Rotman, chapter: 2, section: 2.4, pages: 34-36

statements:
  - type: theorem
    latex: "Let G be a finite group and H ≤ G. Then |H| ∣ |G|."
    proof_sketch: "1. Define left cosets... 2. Prove partition... 3. Count..."

lean:
  mathlib4_path: Mathlib.GroupTheory.Coset.Card
  mathlib4_theorem: Subgroup.card_subgroup_dvd_card
  status: complete

exercises:
  - type: bridge, source: GTM073, number: I.4.8
    description: "Prove any group of prime order p is cyclic"
    connects: [cyclic_group]
```

### 2.3 CLI Commands

```bash
math source list              # List knowledge sources
math update                   # Rebuild SQLite cache from sources
math show <concept>           # Display concept details
math install <concept>        # Generate learning path with topological sort
math mark <concept> mastered  # Update user knowledge state
math status                   # Show learning progress
math verify <concept>         # Verify Lean theorem exists in Mathlib4
math lean <concept>           # Show Lean code and build status
```

---

## 3. Automated Pipeline

### 3.1 Six-Stage Pipeline

```
PDF → Markdown → Chapter Split → Concept Extract → Dedup → Mathlib4 Check → Priority Sort
│        │            │               │              │          │              │
│  fitz  │  regex     │  Pro+Thinking │  exact+LLM   │  grep    │  distance    │
│  8min  │  local     │  ¥4/book      │  ¥0.50        │  local   │  compute     │
└────────┴────────────┴───────────────┴───────────────┴──────────┴──────────────┘
```

### 3.2 Concept Extraction (Per-Chapter)

**Best practice**: Split books into chapters, then extract concepts per chapter with Pro+Thinking model.

- Prompt: "Extract ALL theorems, definitions, lemmas. Give DESCRIPTIVE names, depends_on, proof_sketch."
- Chunks per chapter: ~8-15 (depends on chapter size)
- Expected output: 40-90 concepts per chapter for GTM-sized books
- Total: ~600 concepts per graduate textbook

### 3.3 Cross-Book Deduplication

1. **Exact name match**: ~95 concepts appear in ≥2 books (free)
2. **Fuzzy match** (LLM Flash): handle minor variations (~¥0.50)
3. **Canonical ID assignment**: merge deps from all occurrences

### 3.4 Mathlib4 Coverage Check

Multi-strategy grep against Mathlib4 source tree:
1. Exact name match → exact name with underscores → alphanumeric only
2. PascalCase and camelCase variants
3. For misses: LLM Flash semantic matching

Result: 240 concepts with distance=1 (all deps in Mathlib4 → ready to translate)

---

## 4. PDF Extraction

### 4.1 Correct Method

```python
import fitz  # NOT pymupdf4llm!
doc = fitz.open("book.pdf")
text = doc[page].get_text("text")  # reads hidden OCR layer
```

### 4.2 Quality Tiers

| Grade | Score | Count | Pipeline |
|---|---|---|---|
| Excellent | 4-5/5 | 48 (12%) | Direct |
| Good | 3/5 | 285 (69%) | Direct (LLM self-corrects OCR) |
| Poor | 1-2/5 | 81 (20%) | Re-OCR with GLM on 5060Ti |

---

## 5. DeepSeek API Configuration

### 5.1 Model Selection

| Stage | Model | Thinking | Max Tokens | Timeout |
|---|---|---|---|---|
| Concept extraction | Pro | ✅ | 393216 | 1200s |
| Gap-fill | Pro | ✅ | 393216 | 1200s |
| Lean translate | Pro | ✅ | 393216 | 1200s |
| Quality check | Flash | ❌ | 16384 | 300s |
| Dedup fuzzy match | Flash | ❌ | 16384 | 300s |

### 5.2 Critical Rules

1. **Never limit max_tokens** — thinking shares the token budget. 393216 (384K) is effectively unlimited.
2. **Never add retry logic for thinking exhaustion** — just set max_tokens high enough.
3. **Network retries**: 5 attempts with exponential backoff (5s, 10s, 20s, 40s).
4. **Parallelism**: DeepSeek supports 2500 concurrent. Use 50-100 workers.

### 5.3 Cost Tracking

Token costs are tracked per-API-call and accumulated. The DeepSeekClient automatically computes:
```python
cost = (prompt_tokens * price_in + completion_tokens * price_out) / 1_000_000
```

---

## 6. Lean 4 Integration

### 6.1 Environment

- Lean 4.31.0, Lake 5.0.0
- Mathlib4 v4.31.0: 8175 pre-compiled .olean files
- Project: `lean/MathPkg/` with lakefile.toml

### 6.2 Best Practice: Claude Subagent Workflow

```javascript
// Workflow script for parallel Lean translation
export const meta = { name: 'lean-translate-batch', ... }

phase('Gap-fill + Translate')
const results = await parallel(concepts.map(c => () =>
  agent(`For concept ${c.name}:
    1. Expand proof sketch into detailed steps
    2. Translate to Lean 4 using Mathlib4
    3. Write to Pipeline.lean
    4. Run lake build
    5. If errors: grep Mathlib4, fix, recompile (max 3 attempts)
  `)
))
```

### 6.3 Common Lean Compilation Errors

| Error | Cause | Fix |
|---|---|---|
| `failed to synthesize Fintype H` | Missing typeclass | Add `[Fintype H]` |
| `Nat.card vs Fintype.card` | Wrong cardinal | `simpa [Nat.card_eq_fintype_card]` |
| `Unknown constant X.Y` | Wrong API name | grep Mathlib4 for correct name |
| `#check` not allowed | In imported module | Use `example` instead |

---

## 7. Key Files Reference

| File | Purpose | Lines |
|---|---|---|
| `mathpkg/graph/concept.py` | Concept dataclass + YAML loading | ~180 |
| `mathpkg/graph/cache.py` | SQLite knowledge cache | ~270 |
| `mathpkg/resolver/solver.py` | LearningPathResolver (Kahn) | ~220 |
| `mathpkg/pipeline/deepseek_client.py` | DeepSeek API client | ~140 |
| `mathpkg/pipeline/gap_fill.py` | Proof expansion (Layer 1) | ~120 |
| `mathpkg/pipeline/lean_translate.py` | Lean translation (Layer 2) | ~120 |
| `mathpkg/pipeline/self_heal.py` | Compile + fix (Layer 3-4) | ~200 |
| `cmd/math` | CLI entry point | ~380 |
| `lean/MathPkg/.../Pipeline.lean` | Verified Lean theorems | ~30 |
| `pipeline_output/dedup/canonical_with_distance.json` | 5527 concepts with priority | ~12MB |

---

## 8. Lessons Learned

1. **pymupdf4llm fails on scanned PDFs** — use fitz.get_text("text") instead
2. **Thinking mode IS necessary** for math — don't disable it
3. **max_tokens=393216 is the fix** for empty responses — thinking shares the token budget
4. **Claude subagents beat Python API calls** for Lean translation — they understand errors
5. **Serial is death** — always use ThreadPoolExecutor or Workflow.parallel()
6. **Checkpoint everything** — network is unreliable, API calls fail, save after each concept
7. **Grep Mathlib4 BEFORE translating** — many theorems already exist with different names
8. **UTM books have worse OCR** than GTM (27% pure scanned vs 6%)
