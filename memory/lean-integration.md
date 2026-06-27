---
name: lean4-integration-lessons
description: "Mathlib4 integration — API naming, compilation pitfalls, self-heal patterns"
metadata: 
  node_type: memory
  type: project
  originSessionId: bfc46d42-3656-4af8-b6a8-57278284f040
---

# Lean 4 + Mathlib4 Integration

## Environment

- Lean 4.31.0, Lake 5.0.0, Mathlib4 v4.31.0
- Mathlib4: 6.8 GB source + 5.8 GB cached .olean files (8175 modules)
- Location: `~/lean-demo/.lake/packages/mathlib/`

## Critical: Use lake build, NOT lean command

```bash
# ❌ WRONG — recompiles ALL of Mathlib from scratch
lean myfile.lean

# ✅ CORRECT — reuses 8175 cached .olean files
lake build
```

## `#check` Doesn't Work in Compiled Modules

When a .lean file is imported by another module, `#check` commands cause `unexpected token '#check'; expected 'lemma'` errors.

**Fix**: Use `example` instead:
```lean
-- ❌ Before
#check Group

-- ✅ After
example : Group ℤ := by infer_instance
```

## Mathlib4 API Naming Traps

1. **ZMod 7 is an ADDITIVE group**: `Group (ZMod 7)` fails. Use `(ZMod 7)ˣ` for multiplicative group.
2. **Namespace vs top-level**: `card_sylow_modEq_one` is top-level, NOT `Sylow.card_sylow_modEq_one`
3. **Nat.card vs Fintype.card**: Mathlib4 uses `Nat.card` by default. Add `[Fintype G]` and use `Fintype.card`.
4. **Fintype instance for subgroups**: Need explicit `[Fintype H]` argument.

## Self-Heal Compilation Pattern

The Python `self_heal.py` was unreliable because DeepSeek API doesn't understand Lean errors well enough.

**Better approach**: Claude subagents. They can:
1. Read the .lean file
2. Run `lake build`
3. Read the error messages
4. grep Mathlib4 for correct theorem names
5. Edit and recompile

This is what made the Sylow theorems compile after 3 manual fixes.

## Mathlib4 Full Index (2026-06-25)

Built a complete parse of all 8,169 .lean files:
- **204,000 entries**: 120,099 theorems, 54,409 lemmas, 29,492 defs
- Index file: `pipeline_output/mathlib4_index.json` (50.9MB)
- Each entry: `{kind, name, file, type_sig, doc}`

### 3-Tier Concept Matching (10 books, 3,174 concepts)

| Tier | Strategy | Hit | Rate |
|---|---|---|---|
| 1 | Exact name match (slug→snake_case) | 32 | 1% |
| 2 | Keyword intersection (slug words all in mathlib name) | 46 | 1.4% |
| 3 | Signature words + domain filter | 2,193 | 69% |
| **Total** | | **2,271** | **71.6%** |

**Key insight**: Exact name matching is nearly useless (1%). Semantic matching via type signature keywords + domain filtering is what works. The remaining 903 concepts (~28%) need Flash-level semantic matching.

### Matching Architecture

```
concept (slug + title_en + domain)
    ↓
Pre-built inverted indexes:
  1. exact_lookup: name → entry_idx (130K entries)
  2. word_index:  keyword → {entry_indices} (21K words)
  3. sig_word_index: type_sig_word → {entry_indices} (18K words)
  4. file_domain: Mathlib_dir → {entry_indices}
    ↓
O(1) lookup per concept, no linear scan
```

### Known Mathlib4 Theorem Examples

| Concept | Theorem | File |
|---|---|---|
| Lagrange | `Subgroup.card_subgroup_dvd_card` | `GroupTheory/Coset/Card.lean` |
| Sylow 1 | `Sylow.exists_subgroup_card_pow_prime` | `GroupTheory/Sylow.lean` |
| First Isomorphism | `QuotientGroup.quotientKerEquivRange` | `GroupTheory/QuotientGroup/Basic.lean` |
