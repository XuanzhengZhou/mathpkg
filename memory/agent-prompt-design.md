---
name: agent-prompt-design
description: "Prompt templates, output schemas, I/O instructions, retry strategy, and token budgets for the 4-agent mathematical knowledge pipeline"
metadata:
  node_type: memory
  type: project
  originSessionId: current
---

# Agent Prompt Design: Mathematical Knowledge Pipeline

## Architecture Overview

```
Chapter MD (~70K chars)
    │
    ▼
┌──────────────────────────────┐
│ Agent A: Concept Extractor   │  DeepSeek Pro + thinking
│ chapter → concepts.json      │  ~100 concepts per chapter
│         → concepts/*.md      │  6-section encyclopedia pages
└──────────┬───────────────────┘
           │ per-book concepts.json
           ▼
┌──────────────────────────────┐
│ Agent B: Dedup Checker       │  DeepSeek Flash (no thinking)
│ all names → duplicate groups │  cross-book, batch mode
└──────────┬───────────────────┘
           │ suspected duplicate pairs
           ▼
┌──────────────────────────────┐
│ Agent C: Dedup Verifier      │  DeepSeek Pro + thinking
│ pair → merge/separate        │  one pair at a time
│      → merged content        │
└──────────┬───────────────────┘
           │ canonical concepts
           ▼
┌──────────────────────────────┐
│ Agent D: Lean Translator     │  DeepSeek Pro + thinking
│ concept → {name}.lean        │  Checker+Fixer v4 pattern
│         → .done / .fail      │  up to 10 self-heal rounds
└──────────────────────────────┘
```

---

## Agent A: Concept Extractor

### Model: DeepSeek Pro (thinking: true)

### Prompt Template

```
You are a mathematical knowledge engineer. Your task is to read a chapter from a mathematics textbook,
extract every mathematical concept (definitions, theorems, propositions, lemmas, corollaries, examples,
algorithms), and produce structured entries for each one.

## Input

The chapter is a Markdown file extracted from a PDF via OCR. It may contain:
- Chinese text (华章数学译丛 series) with mixed English math notation
- OCR artifacts (stray characters, broken formulas, merged symbols)
- TOC/front matter noise at the beginning (ignore everything before the first real section)
- Theorem statements labeled as "定理", "Theorem", "命题", "Proposition", "引理", "Lemma", etc.

## Your Task

For EVERY mathematical concept in the chapter, you must produce TWO outputs:

### Output 1: A JSON array `concepts.json`

Each entry has these fields:

{
  "id": "snake_case_english_name",           // unique within this book
  "name": {
    "en": "English Name",                    // canonical English name
    "zh": "中文名称"                          // Chinese name if present, else ""
  },
  "type": "definition|theorem|proposition|lemma|corollary|example|algorithm",
  "statement": "Full LaTeX statement. Use \\text for English in Chinese context.",
  "proof_sketch": "3-5 sentence proof summary. If definition, write 'N/A (definition)'",
  "depends_on": ["concept_id_1", "concept_id_2"],  // IDs of concepts this one uses
  "source": {
    "book_id": "GTM073",                     // short book identifier
    "chapter": "Chapter I",                  // chapter number/title
    "section": "I.4",                        // section number
    "page_hint": "pp. 38-42",                // approximate page range
    "theorem_number": "Theorem 4.6"          // label in the source
  },
  "tags": ["group_theory", "finite_groups"], // 1-3 topic tags
  "difficulty": 1-5,                         // 1=trivial, 5=research level
  "is_fundamental": true|false               // core concept that many others depend on
}

### Output 2: A markdown encyclopedia page `{id}.md`

For EACH concept, write a markdown file with these 6 sections:

## {English Name} / {中文名称}

**Type**: {type}
**Source**: {book_id}, {chapter}, {section}, {theorem_number}
**Difficulty**: {difficulty}/5
**Tags**: {comma-separated tags}

---

### 1. Statement

The complete, self-contained statement in LaTeX.

### 2. Why This Matters

One paragraph explaining the significance: what problem does this solve? Why is it named?
Why should a student care?

### 3. Proof Sketch

A longer proof outline (5-10 steps). Include the key insight or trick.
If a definition, explain the motivation for defining it this way.

### 4. Prerequisites

What the reader must know before understanding this concept.
List specific concept names (not just topics).

### 5. Connections

- **Generalizes**: ...
- **Specialized by**: ...
- **Used in**: ...
- **Related to**: ...

### 6. What If Not

What breaks or becomes false if the hypotheses are weakened?
Provide a concrete counterexample.

## Rules

1. Do NOT skip any concept. Even "obvious" lemmas get entries.
2. Use LaTeX math mode ($...$ for inline, $$...$$ for display).
3. Snake_case IDs must be unique within this book. If two concepts have the same name,
   append a disambiguator: "lagrange_theorem_finite" vs "lagrange_theorem_general".
4. depends_on must reference IDs already extracted from THIS chapter.
   If a dependency is from a previous chapter, mark it as ["EXT:concept_name"].
5. If a statement contains Chinese, wrap it in \\text{...}.
6. For definitions: proof_sketch = "N/A (definition)".
7. The chapter may have OCR errors. Use mathematical reasoning to reconstruct
   the correct formulas. If you are uncertain, mark the field with [UNCERTAIN: ...].
8. Write in English for the encyclopedia pages. Include Chinese name in the title if available.

## Output File Writing

After generating all entries, write the following files to disk:

1. Write the FULL JSON array to: pipeline_output/concepts_v2/book_{book_id}_chapter_{N}.json
2. Write each encyclopedia page to: pipeline_output/concepts_v2/pages/{id}.md
3. Write a completion marker to: pipeline_output/concepts_v2/book_{book_id}_chapter_{N}.done

Use the Write tool for each file.

## Token Budget

Input: ~70K chars (~25K tokens)
Output: ~100 concepts × ~500 words each = ~50K words → ~65K output tokens
Total: ~90K tokens. Well within DeepSeek Pro 1M context / 384K output limits.

DO NOT truncate. Output ALL concepts.
```

### Structured Output Schema (JSON)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "array",
  "items": {
    "type": "object",
    "required": ["id", "name", "type", "statement", "proof_sketch", "depends_on", "source"],
    "properties": {
      "id": {
        "type": "string",
        "pattern": "^[a-z][a-z0-9_]*$",
        "description": "Unique snake_case identifier within this book"
      },
      "name": {
        "type": "object",
        "required": ["en"],
        "properties": {
          "en": {"type": "string", "minLength": 1},
          "zh": {"type": "string", "default": ""}
        }
      },
      "type": {
        "type": "string",
        "enum": ["definition", "theorem", "proposition", "lemma", "corollary", "example", "algorithm"]
      },
      "statement": {
        "type": "string",
        "description": "Full LaTeX statement with \\text for non-math text"
      },
      "proof_sketch": {
        "type": "string",
        "description": "3-5 sentence proof summary, or 'N/A (definition)'"
      },
      "depends_on": {
        "type": "array",
        "items": {"type": "string"},
        "description": "IDs this concept depends on. Prefix EXT: for cross-chapter deps"
      },
      "source": {
        "type": "object",
        "required": ["book_id", "chapter", "section"],
        "properties": {
          "book_id": {"type": "string"},
          "chapter": {"type": "string"},
          "section": {"type": "string"},
          "page_hint": {"type": "string", "default": ""},
          "theorem_number": {"type": "string", "default": ""}
        }
      },
      "tags": {
        "type": "array",
        "items": {"type": "string"},
        "minItems": 1,
        "maxItems": 5
      },
      "difficulty": {
        "type": "integer",
        "minimum": 1,
        "maximum": 5
      },
      "is_fundamental": {
        "type": "boolean"
      }
    }
  }
}
```

### File Read/Write Instructions

| Operation | Path | Tool | Notes |
|---|---|---|---|
| Read chapter | `pipeline_output/books/{book_md}.md` | Read | Provided as context, not read by agent |
| Write JSON | `pipeline_output/concepts_v2/book_{book_id}_chapter_{N}.json` | Write | One file per chapter |
| Write pages | `pipeline_output/concepts_v2/pages/{id}.md` | Write | One file per concept |
| Write marker | `pipeline_output/concepts_v2/book_{book_id}_chapter_{N}.done` | Write | Empty file, signals completion |

### Error Handling / Retry Strategy

```
MAX_RETRIES = 3

for attempt in 1..MAX_RETRIES:
    1. Remove any partial output from previous failed attempt
    2. Launch Agent A with full prompt
    3. Check: does book_{book_id}_chapter_{N}.done exist?
       YES → count entries in JSON, verify it matches pages/ count
       NO  → retry with shorter chapter (split into 2 halves if >100 concepts)

If chapter has >120 concepts: split into two sub-chapters at a natural section boundary.
Process each half independently, then concatenate JSON arrays.
```

**Common failure modes:**
- Thinking exhaustion → output truncated mid-entry. Fix: count JSON entries vs pages. If mismatch, retry with explicit "you must produce exactly N concepts" instruction.
- OCR corruption → agent produces nonsense statement. Fix: QC pass after extraction flags entries with [UNCERTAIN] markers for manual review.
- Chinese name missing → agent skips zh field. Fix: post-processing Python script fills zh from a lookup table of known translations.

### Token Budget

| Component | Estimated Tokens |
|---|---|
| Prompt (instructions) | ~1,500 |
| Chapter markdown | ~25,000 |
| Output: 100 concepts JSON | ~40,000 |
| Output: 100 encyclopedia pages | ~80,000 |
| **Total input** | **~27,000** |
| **Total output** | **~120,000** |
| **Cost (Pro, ¥3/¥6)** | **¥0.80** |

Strategy: One chapter per agent call. 10 chapters = 10 parallel agents. Total ~¥8/book.

---

## Agent B: Dedup Checker

### Model: DeepSeek Flash (thinking: false)

### Prompt Template

```
You are a duplicate detector for a mathematical knowledge base. Your task is to find
concepts that are likely the same theorem/definition appearing under different names
or in different languages.

## Input

A JSON array of ALL concept names from all books. Each entry has:
{
  "id": "lagrange_theorem",
  "name_en": "Lagrange's Theorem",
  "name_zh": "拉格朗日定理",
  "book_id": "GTM073",
  "type": "theorem"
}

Total concepts: ~{N} (from {M} books)

## Your Task

Group concepts that are likely DUPLICATES. Two concepts might be duplicates if:
- They have the same name in different languages ("拉格朗日定理" = "Lagrange's Theorem")
- They have naming variants ("Fundamental Theorem of Galois Theory" ≈ "Galois Correspondence")
- They have minor word-order differences ("Theorem of Lagrange" = "Lagrange's Theorem")
- They have abbreviation/expansion ("FTGT" = "Fundamental Theorem of Galois Theory")
- One is a more specific name for the same theorem
- They share the same Chinese name but different English names (translation variants)

## Output Format

Return a JSON object:

{
  "duplicate_groups": [
    {
      "canonical_name_en": "Lagrange's Theorem",
      "canonical_name_zh": "拉格朗日定理",
      "members": [
        {"id": "lagrange_theorem", "book_id": "GTM073", "name_en": "Lagrange's Theorem"},
        {"id": "lagranges_theorem", "book_id": "GTM080", "name_en": "Lagrange's Theorem"},
        {"id": "theorem_of_lagrange", "book_id": "GTM148", "name_en": "Theorem of Lagrange"}
      ],
      "confidence": 0.95,
      "match_reason": "same theorem, minor naming variation"
    }
  ],
  "singletons": ["unique_concept_id_1", "unique_concept_id_2"],
  "ambiguous": [
    {
      "members": [...],
      "note": "might be the same, needs Pro verification"
    }
  ]
}

## Rules

1. Be AGGRESSIVE in grouping. It's better to flag borderline cases for Agent C
   verification than to miss a duplicate. Put uncertain cases in "ambiguous".
2. Chinese-English name pairs are strong duplicates. If zh matches, group them.
3. Canonical name should be the most common/precise English name.
4. Confidence 0.9+ = almost certainly same. 0.7-0.9 = probably same. <0.7 = put in ambiguous.
5. Concepts with the same name but DIFFERENT types (e.g., "Group" as definition
   in two books) are still duplicates — put them in the same group.
6. SINGLETONS: concepts that appear in only one book and have no likely match.
7. Process the entire list in one pass. Do not truncate.

## Output File

Write the result to: pipeline_output/dedup/dedup_check_result.json
Write a completion marker: pipeline_output/dedup/dedup_check_result.done
```

### Structured Output Schema (JSON)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": ["duplicate_groups", "singletons", "ambiguous"],
  "properties": {
    "duplicate_groups": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["canonical_name_en", "members", "confidence", "match_reason"],
        "properties": {
          "canonical_name_en": {"type": "string"},
          "canonical_name_zh": {"type": "string", "default": ""},
          "members": {
            "type": "array",
            "minItems": 2,
            "items": {
              "type": "object",
              "required": ["id", "book_id", "name_en"],
              "properties": {
                "id": {"type": "string"},
                "book_id": {"type": "string"},
                "name_en": {"type": "string"},
                "name_zh": {"type": "string", "default": ""},
                "type": {"type": "string"}
              }
            }
          },
          "confidence": {"type": "number", "minimum": 0.0, "maximum": 1.0},
          "match_reason": {"type": "string"}
        }
      }
    },
    "singletons": {
      "type": "array",
      "items": {"type": "string"},
      "description": "IDs of concepts with no likely duplicates"
    },
    "ambiguous": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["members", "note"],
        "properties": {
          "members": {"type": "array", "minItems": 2},
          "note": {"type": "string"}
        }
      }
    }
  }
}
```

### File Read/Write Instructions

| Operation | Path | Tool | Notes |
|---|---|---|---|
| Read concept names | `pipeline_output/dedup/all_concept_names.json` | Read | Generated by Python preprocessor, not by agent |
| Write result | `pipeline_output/dedup/dedup_check_result.json` | Write | The grouping result |
| Write marker | `pipeline_output/dedup/dedup_check_result.done` | Write | Empty marker file |

**Preprocessor Python script** (generates `all_concept_names.json`):
```python
# collect_names.py — run BEFORE Agent B
import json, glob

names = []
for f in sorted(glob.glob("pipeline_output/concepts_v2/book_*.json")):
    book_id = f.split("book_")[1].split("_chapter")[0]
    for c in json.load(open(f)):
        names.append({
            "id": c["id"],
            "name_en": c["name"]["en"],
            "name_zh": c["name"].get("zh", ""),
            "book_id": book_id,
            "type": c["type"]
        })

json.dump(names, open("pipeline_output/dedup/all_concept_names.json", "w"),
          indent=2, ensure_ascii=False)
print(f"Collected {len(names)} concept names")
```

### Batch Splitting Strategy

If total concepts exceed ~2000 (Flash's effective comparison limit), split by topic tag:

```python
# Split by tag before sending to Agent B
groups = group_by_tag(all_concepts)
for tag, concepts in groups.items():
    dedup_result = agent_b(concepts)
    merge across tags later (rare: cross-topic duplicates)
```

### Error Handling / Retry Strategy

```
- Flash is fast and reliable. Retry once on API error.
- Main failure mode: output truncated (too many groups).
  Fix: if dedup_check_result.done is missing after agent call,
  split input into halves and process separately, then merge results.
- Post-processing: Python script verifies that every input ID appears
  in exactly one duplicate_group OR singletons OR ambiguous.
  Missing IDs → re-run with those IDs only.
```

### Token Budget

| Component | Estimated Tokens |
|---|---|
| Prompt | ~800 |
| Input: 5000 concept names | ~25,000 |
| Output: grouping result | ~15,000 |
| **Total input** | **~26,000** |
| **Total output** | **~15,000** |
| **Cost (Flash, ¥1/¥2)** | **¥0.06** |

Single call for up to ~5000 concepts. Well within Flash limits.

---

## Agent C: Dedup Verifier

### Model: DeepSeek Pro (thinking: true)

### Prompt Template

```
You are a mathematical arbiter. Two concept entries may be duplicates. Your job is to
read BOTH entries in full, compare them carefully, and decide: MERGE or SEPARATE.

## Input

You will receive TWO concept entries. Each includes the full encyclopedia page
(6 sections: Statement, Why This Matters, Proof Sketch, Prerequisites, Connections, What If Not).

### Concept A
{full markdown of concept A}

### Concept B
{full markdown of concept B}

## Decision Criteria

### MERGE if:
- Same theorem stated with equivalent hypotheses (minor notational differences OK)
- Same theorem with different proof approaches (proof sketch differs, but THEOREM is the same)
- One is a special case that is ALWAYS presented as the main theorem in some books
- Definition with identical meaning, different wording
- Same Chinese name refers to the exact same mathematical object

### SEPARATE if:
- Same name but DIFFERENT theorems (e.g., "Fundamental Theorem of Algebra"
  in different contexts might mean different things — but note: in practice this is rare)
- One generalizes the other in a NON-TRIVIAL way (significant new hypotheses/conclusions)
- Different mathematical objects that happen to share a name
- One is a definition and the other is a theorem USING that definition
- Different domains: one applies to groups, the other to rings (even if similar structure)

## Output Format

### If MERGE:
{
  "decision": "merge",
  "canonical_id": "chosen_id",
  "merged_concept": {
    "id": "canonical_id",
    "name": {"en": "...", "zh": "..."},
    "type": "...",
    "statement": "...",         // The most precise/complete statement from either
    "proof_sketch": "...",      // The best proof sketch (more detailed / clearer)
    "depends_on": [...],         // Union of both, deduplicated
    "source": {...},             // Primary source (most authoritative book)
    "alternate_sources": [{...}, {...}],  // Other books that contain this concept
    "tags": [...],               // Union of both tags
    "merge_note": "Why these were merged and what differed between sources"
  }
}

### If SEPARATE:
{
  "decision": "separate",
  "reason": "Detailed explanation of why these are different concepts",
  "distinction": "How to tell them apart: key difference in hypotheses/conclusions/domain"
}

## Rules

1. Read BOTH proof sketches fully. Different proofs do NOT make different theorems.
2. Check the "What If Not" sections. If the counterexamples are the same, strong merge signal.
3. Check the "Prerequisites" sections. Overlapping prerequisites = merge signal.
4. Be CONSERVATIVE: when in doubt, SEPARATE. It's easier to manually merge later
   than to un-merge incorrectly merged concepts.
5. If merging, the merged statement must be the MOST PRECISE version.
   Prefer the version with explicit quantifiers and complete hypotheses.
6. If one source has a significantly better (clearer, more rigorous) proof sketch,
   use that one in the merged output. Add a note about the alternative approach.

## Output File

Write result to: pipeline_output/dedup/verifications/{id_a}_vs_{id_b}.json
Write marker:     pipeline_output/dedup/verifications/{id_a}_vs_{id_b}.done
```

### Structured Output Schema (JSON)

```json
{
  "oneOf": [
    {
      "type": "object",
      "required": ["decision", "canonical_id", "merged_concept"],
      "properties": {
        "decision": {"const": "merge"},
        "canonical_id": {"type": "string"},
        "merged_concept": {
          "type": "object",
          "required": ["id", "name", "type", "statement", "proof_sketch", "depends_on", "source"],
          "properties": {
            "id": {"type": "string"},
            "name": {
              "type": "object",
              "required": ["en"],
              "properties": {
                "en": {"type": "string"},
                "zh": {"type": "string", "default": ""}
              }
            },
            "type": {"type": "string"},
            "statement": {"type": "string"},
            "proof_sketch": {"type": "string"},
            "depends_on": {"type": "array", "items": {"type": "string"}},
            "source": {"type": "object"},
            "alternate_sources": {"type": "array", "items": {"type": "object"}},
            "tags": {"type": "array", "items": {"type": "string"}},
            "merge_note": {"type": "string"}
          }
        }
      }
    },
    {
      "type": "object",
      "required": ["decision", "reason", "distinction"],
      "properties": {
        "decision": {"const": "separate"},
        "reason": {"type": "string"},
        "distinction": {"type": "string"}
      }
    }
  ]
}
```

### File Read/Write Instructions

| Operation | Path | Tool | Notes |
|---|---|---|---|
| Read concept A | `pipeline_output/concepts_v2/pages/{id_a}.md` | Read | Full encyclopedia page |
| Read concept B | `pipeline_output/concepts_v2/pages/{id_b}.md` | Read | Full encyclopedia page |
| Write decision | `pipeline_output/dedup/verifications/{id_a}_vs_{id_b}.json` | Write | Merge or separate |
| Write marker | `pipeline_output/dedup/verifications/{id_a}_vs_{id_b}.done` | Write | Empty marker |

### Error Handling / Retry Strategy

```
- MAX_RETRIES = 2.
- Main failure: thinking exhaustion before completing merged concept.
  Fix: if .done missing, check if partial output exists. If so, launch a
  second agent that reads the partial output and completes the merged concept.
- QC: After merge, verify merged_concept has all required fields.
  If fields are empty strings, mark for manual review.
```

### Token Budget

| Component | Estimated Tokens |
|---|---|
| Prompt | ~1,200 |
| Concept A (full .md) | ~2,000 |
| Concept B (full .md) | ~2,000 |
| Output (merge decision + merged content) | ~2,500 |
| **Total input** | **~5,000** |
| **Total output** | **~2,500** |
| **Cost (Pro, ¥3/¥6)** | **¥0.03** |

~100 verification pairs per batch. Cost: ~¥3/batch.

---

## Agent D: Lean Translator

### Model: DeepSeek Pro (thinking: true)

### Prompt Template

This agent uses the **Checker+Fixer v4 pattern**. It is invoked as the **Fixer** in the
retry loop. The Checker is a local Python script (not an agent).

#### Fixer Prompt (called when .fail exists)

```
You are a Lean 4 expert specializing in Mathlib4. Your task is to write CORRECT,
COMPILABLE Lean 4 code for a mathematical concept, or fix compilation errors in
existing code.

## Input

### The Concept
{full encyclopedia markdown: statement + proof sketch + prerequisites}

### Existing Mathlib4 Coverage
{grep results for related theorems in Mathlib4}

### Current Status
- Existing .lean file: {path} (may contain previous attempt, may be empty)
- Compilation errors: {contents of .fail file, or "N/A - starting from scratch"}

## Your Task

### Phase 1: Search Mathlib4 (MANDATORY first step)
Before writing ANY code, grep Mathlib4 for existing theorems:
```bash
grep -r "keyword" ~/lean-demo/.lake/packages/mathlib/Mathlib/ --include="*.lean" | head -20
```

Search for at least 3 name variants:
- Exact name: "lagrange_theorem"
- PascalCase: "LagrangeTheorem"
- camelCase: "lagrangeTheorem"
- Keyword from statement: "card_subgroup_dvd"
- Module path guess: "GroupTheory/Coset/"

DOCUMENT what you found. If Mathlib4 already has the exact theorem, your job
is just to write a thin wrapper or re-export.

### Phase 2: Write/Edit the .lean file

Rules for writing Lean 4 code:

1. **File header**: Always include copyright and import block:
```lean
/-
Copyright (c) 2026 MathPkg. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib
```

2. **Use existing Mathlib4 theorems** whenever possible. Do not reprove
   theorems that already exist. Import the relevant module and provide
   an example or alternative statement form.

3. **#check is FORBIDDEN in compiled modules.** Use `example` instead:
```lean
-- ❌ WRONG
#check Subgroup.card_subgroup_dvd_card

-- ✅ CORRECT
example (G : Type*) [Group G] [Fintype G] (H : Subgroup G) :
    Nat.card H ∣ Nat.card G := by
  exact Subgroup.card_subgroup_dvd_card H
```

4. **Use ZMod correctly**: ZMod 7 is additive. For multiplicative group, use `(ZMod 7)ˣ`.

5. **Namespace awareness**: Many theorems are top-level, not namespaced.
   `card_sylow_modEq_one` is correct, NOT `Sylow.card_sylow_modEq_one`.

6. **Fintype instances**: When using `Fintype.card`, add `[Fintype G]` argument.

7. **Write ONE theorem/definition per concept file.**
   The file should be self-contained and compilable with `lake build`.

8. **Use `Nat.card` not `Fintype.card`** unless you explicitly need the Fintype instance.

9. **Do not use `sorry`.** If something cannot be proven, wrap it in a commented
   `example` block with a note about what's needed:
```lean
/-- This would require developing the theory of X first. -/
-- example : ... := by
--   ...
```

10. **For definitions**: Translate as `def`, `structure`, `class`, or `inductive` as appropriate.
    Add `@[simp]` where useful. Add docstrings with `--` comments.

### Phase 3: Compile and fix errors

After writing, write the file to disk at:
`lean/MathPkg/MathPkg/{Topic}/{concept_id}.lean`

Then run the Checker:
```bash
python3 checker.py {index}
```

Read the result. If .fail exists:
1. Read the error messages carefully
2. Identify the root cause (API name typo, missing import, type mismatch, etc.)
3. Fix EXACTLY the errors, don't rewrite everything
4. Re-run the checker

Repeat up to 10 rounds. Each round, focus ONLY on the errors reported.

## Common Mathlib4 API Name Corrections

| Wrong | Correct |
|---|---|
| `Sylow.card_sylow_modEq_one` | `card_sylow_modEq_one` (top-level) |
| `GroupTheory.Coset.card_subgroup_dvd_card` | `Subgroup.card_subgroup_dvd_card` |
| `QuotientGroup.quotientKerEquivRange` | `QuotientGroup.quotientKerEquivRange` (correct) |
| `MulAction.orbit_stabilizer` | `MulAction.card_orbit_mul_card_stabilizer_eq_card_group` |

## Output

After successful compilation, ensure the .lean file is written with correct code.
The Checker will write the .done file automatically.
```

#### Checker Script (local Python, not an agent)

```python
#!/usr/bin/env python3
"""checker.py — local compilation checker for Lean 4 concept files.
Usage: python3 checker.py <index>
Reads pipeline_output/translations/{index}.json to get concept info.
Compiles the .lean file with lake env lean.
Writes pipeline_output/translations/{index}.done on success.
Writes pipeline_output/translations/{index}.fail on failure (with error messages).
"""

import json, os, sys, subprocess

INDEX = int(sys.argv[1])
TRANSLATION_DIR = "pipeline_output/translations"
LEAN_PROJECT_DIR = "lean/MathPkg"

# Read concept info
info = json.load(open(f"{TRANSLATION_DIR}/{INDEX}.json"))
lean_file = info["lean_file"]  # e.g., "lean/MathPkg/MathPkg/Algebra/Group/lagrange_theorem.lean"

# Ensure file exists
if not os.path.exists(lean_file):
    with open(f"{TRANSLATION_DIR}/{INDEX}.fail", "w") as f:
        f.write(f"FATAL: Lean file not found: {lean_file}")
    sys.exit(1)

# Clean up previous markers
for suffix in [".done", ".fail"]:
    try:
        os.remove(f"{TRANSLATION_DIR}/{INDEX}{suffix}")
    except FileNotFoundError:
        pass

# Compile with lake env lean (uses cached .olean files)
try:
    result = subprocess.run(
        ["lake", "env", "lean", lean_file],
        cwd=LEAN_PROJECT_DIR,
        capture_output=True,
        text=True,
        timeout=120  # 2 min timeout
    )
except subprocess.TimeoutExpired:
    with open(f"{TRANSLATION_DIR}/{INDEX}.fail", "w") as f:
        f.write("TIMEOUT: Compilation exceeded 120 seconds")
    sys.exit(1)

if result.returncode == 0:
    # Success — but verify no #check commands snuck through
    if "#check" in open(lean_file).read():
        with open(f"{TRANSLATION_DIR}/{INDEX}.fail", "w") as f:
            f.write("WARNING: File contains #check commands which will fail in lake build.\n"
                    "Replace #check with example blocks.")
        sys.exit(1)

    with open(f"{TRANSLATION_DIR}/{INDEX}.done", "w") as f:
        f.write(f"PASS: {lean_file}")
    print(f"[{INDEX}] PASS")
else:
    # Failure — extract last 20 lines of error
    error_lines = result.stderr.strip().split("\n")
    last_errors = error_lines[-20:] if len(error_lines) > 20 else error_lines
    with open(f"{TRANSLATION_DIR}/{INDEX}.fail", "w") as f:
        f.write("COMPILATION ERROR:\n")
        f.write("\n".join(last_errors))
    print(f"[{INDEX}] FAIL: {len(error_lines)} error lines")
    sys.exit(1)
```

### Structured Output

Agent D does NOT use StructuredOutput. It writes files directly to disk:

| File | Path | Content |
|---|---|---|
| Lean code | `lean/MathPkg/MathPkg/{Topic}/{concept_id}.lean` | Compilable Lean 4 file |
| Success marker | `pipeline_output/translations/{index}.done` | "PASS: {path}" |
| Failure marker | `pipeline_output/translations/{index}.fail` | Error messages |
| Status JSON | `pipeline_output/translations/{index}.json` | Concept metadata + lean_file path |

The status JSON is written by the orchestrator BEFORE invoking the agent:
```json
{
  "index": 0,
  "concept_id": "lagrange_theorem",
  "lean_file": "lean/MathPkg/MathPkg/Algebra/Group/lagrange_theorem.lean",
  "status": "pending",
  "attempts": 0,
  "max_attempts": 10,
  "mathlib4_hits": ["Subgroup.card_subgroup_dvd_card"]
}
```

### Resilient v4 Loop (orchestrator pseudocode)

```javascript
// resilient_v4.js pattern for Agent D
async function translateConcept(idx, conceptMd, mathlib4GrepResults) {
  const statusFile = `pipeline_output/translations/${idx}.json`;
  const doneFile  = `pipeline_output/translations/${idx}.done`;
  const failFile  = `pipeline_output/translations/${idx}.fail`;

  for (let attempt = 0; attempt < 10; attempt++) {
    // Update status
    let status = JSON.parse(await read(statusFile));
    status.attempts = attempt;
    await write(statusFile, JSON.stringify(status));

    // CHECKER: local compilation
    try {
      await agent(`python3 checker.py ${idx}`, {
        label: `check-${idx}`,
        model: 'flash'  // Flash is enough to run a single command
      });
    } catch(e) {
      // agent() throws on API error — that's OK, checker runs locally
    }

    // Check .done
    if (await fileExists(doneFile)) {
      status.status = 'done';
      await write(statusFile, JSON.stringify(status));
      return { idx, status: 'done', attempts: attempt + 1 };
    }

    // Check .fail
    if (await fileExists(failFile)) {
      const errors = await read(failFile);
      // FIXER: Pro agent with full prompt
      try {
        await agent(fixerPrompt(conceptMd, mathlib4GrepResults, errors, idx), {
          label: `fix-${idx}-${attempt}`,
          model: 'pro'
        });
      } catch(e) {
        // API error during fix — don't count as attempt failure
        // Checker will re-evaluate next round
      }
      // Remove .fail so checker re-evaluates
      await run(`rm -f ${failFile}`);
    }
    // If neither .done nor .fail, checker was interrupted → retry
  }

  // Exhausted retries
  status.status = 'exhausted';
  await write(statusFile, JSON.stringify(status));
  return { idx, status: 'exhausted', attempts: 10 };
}
```

### Token Budget

| Component | Estimated Tokens |
|---|---|
| Fixer prompt | ~2,000 |
| Concept markdown | ~2,000 |
| Mathlib4 grep results | ~1,000 |
| Compilation errors (from .fail) | ~500 |
| Output: Lean code + compilation attempts | ~3,000 |
| **Total input per fix** | **~5,500** |
| **Total output per fix** | **~3,000** |
| **Cost per fix (Pro, ¥3/¥6)** | **¥0.04** |

Checker: ~500 chars input, "PASS" or "FAIL: N errors" output. ~2000 tokens/call.
Cost: ¥0.006/call (Pro pricing, but checker is just a python command run by flash).

Typical concept: 1-3 fix rounds. Total ~¥0.02-0.08/concept.
200 concepts: ~¥4-16 for translation phase.

---

## Merge Handling (Agent C output → canonical concepts)

When Agent C decides "merge", the question is: how to merge the two concepts'
.md encyclopedia pages and .yaml files WITHOUT agent interference.

### Design Principle

The merge of files should be DETERMINISTIC, implemented as a Python script.
Agent C provides the DECISION and the merged CONTENT (as JSON). The Python
script mechanically applies that decision to the filesystem.

### Python Merge Script

```python
#!/usr/bin/env python3
"""merge_concepts.py — Apply Agent C merge decisions to filesystem.
Reads verification JSONs from pipeline_output/dedup/verifications/
For each "merge" decision, merges the two .md and .yaml files.
For "separate" decisions, just logs the result.
"""

import json, os, shutil, yaml
from pathlib import Path

PAGES_DIR = Path("pipeline_output/concepts_v2/pages")
VERIFICATIONS_DIR = Path("pipeline_output/dedup/verifications")
CANONICAL_DIR = Path("pipeline_output/concepts_v2/canonical")
MERGED_LOG = Path("pipeline_output/dedup/merged_log.json")

CANONICAL_DIR.mkdir(parents=True, exist_ok=True)

merged_log = []

for vf in sorted(VERIFICATIONS_DIR.glob("*.json")):
    if not vf.with_suffix(".done").exists():
        print(f"SKIP {vf.name}: no .done marker")
        continue

    decision = json.load(open(vf))

    if decision["decision"] == "separate":
        merged_log.append({
            "pair": vf.stem,
            "decision": "separate",
            "reason": decision["reason"]
        })
        continue

    # MERGE
    merged = decision["merged_concept"]
    canonical_id = merged["id"]

    # 1. Write the merged encyclopedia page (.md)
    md_content = generate_merged_md(merged)  # deterministic function
    (CANONICAL_DIR / f"{canonical_id}.md").write_text(md_content)

    # 2. Write the merged YAML
    yaml_content = generate_merged_yaml(merged)  # deterministic function
    (CANONICAL_DIR / f"{canonical_id}.yaml").write_text(yaml_content)

    # 3. Record which original IDs were merged into this canonical
    # (extract from verification filename: "id_a_vs_id_b.json")
    ids = vf.stem.split("_vs_")
    merged_log.append({
        "pair": vf.stem,
        "decision": "merge",
        "canonical_id": canonical_id,
        "merged_from": ids,
        "canonical_md": f"canonical/{canonical_id}.md",
        "canonical_yaml": f"canonical/{canonical_id}.yaml"
    })

    # 4. Move original files to _merged archive (don't delete)
    archive_dir = PAGES_DIR.parent / "_merged_archive" / vf.stem
    archive_dir.mkdir(parents=True, exist_ok=True)
    for id_ in ids:
        src_md = PAGES_DIR / f"{id_}.md"
        if src_md.exists():
            shutil.move(str(src_md), str(archive_dir / f"{id_}.md"))
        # Also move any corresponding .yaml if it exists
        src_yaml = PAGES_DIR.parent / f"{id_}.yaml"
        if src_yaml.exists():
            shutil.move(str(src_yaml), str(archive_dir / f"{id_}.yaml"))

# Write merge log
json.dump(merged_log, open(MERGED_LOG, "w"), indent=2, ensure_ascii=False)

print(f"Processed {len(list(VERIFICATIONS_DIR.glob('*.json')))} verifications")
print(f"Merges: {sum(1 for m in merged_log if m['decision']=='merge')}")
print(f"Separates: {sum(1 for m in merged_log if m['decision']=='separate')}")
print(f"Log: {MERGED_LOG}")
```

### Deterministic .md Generator

```python
def generate_merged_md(merged: dict) -> str:
    """Generate the 6-section encyclopedia page from merged concept data."""

    name_en = merged["name"]["en"]
    name_zh = merged["name"].get("zh", "")
    title = f"{name_en} / {name_zh}" if name_zh else name_en

    tags = ", ".join(merged.get("tags", []))

    # Build sources list
    primary = merged["source"]
    sources_text = f"- **Primary**: {primary.get('book_id', '?')}, {primary.get('chapter', '?')}, {primary.get('section', '?')}"
    for alt in merged.get("alternate_sources", []):
        sources_text += f"\n- **Also in**: {alt.get('book_id', '?')}, {alt.get('chapter', '?')}, {alt.get('section', '?')}"

    md = f"""## {title}

**Type**: {merged['type']}
**Sources**: 
{sources_text}
**Tags**: {tags}

---

### 1. Statement

{merged['statement']}

### 2. Why This Matters

{merged.get('why_matters', '(Consolidated from merged sources)')}

### 3. Proof Sketch

{merged['proof_sketch']}

### 4. Prerequisites

{chr(10).join('- ' + d for d in merged.get('depends_on', []))}

### 5. Connections

{merged.get('connections', '(See merged sources for detailed connections)')}

### 6. What If Not

{merged.get('what_if_not', '(See merged sources for counterexamples)')}

---

*Merged from {len(merged.get('alternate_sources', [])) + 1} sources*
*Merge note: {merged.get('merge_note', 'N/A')}*
"""
    return md
```

### Deterministic .yaml Generator

```python
def generate_merged_yaml(merged: dict) -> str:
    """Generate YAML concept file from merged data."""
    data = {
        "id": merged["id"],
        "name": merged["name"],
        "type": merged["type"],
        "description": {
            "en": merged.get("description_en", f"See encyclopedia page for {merged['id']}"),
            "zh": merged.get("description_zh", "")
        },
        "depends": {
            "required": merged.get("depends_on", []),
            "recommended": merged.get("depends_recommended", []),
            "suggested": merged.get("depends_suggested", [])
        },
        "versions": [
            merged["source"],
            *merged.get("alternate_sources", [])
        ],
        "statements": [
            {
                "type": merged["type"],
                "name": merged["name"]["en"],
                "latex": merged["statement"],
                "proof_sketch": merged["proof_sketch"]
            }
        ],
        "merge_info": {
            "merged_from": merged.get("merged_from_ids", []),
            "merge_note": merged.get("merge_note", ""),
            "merged_by": "Agent C (Dedup Verifier)"
        }
    }
    return yaml.dump(data, allow_unicode=True, default_flow_style=False, sort_keys=False)
```

### Why Deterministic Merging Matters

1. **Agent C focuses on what it does best**: semantic comparison, deciding merge vs separate, producing merged mathematical content.
2. **File operations are mechanical**: moving files, writing YAML/MD from JSON → no room for agent hallucination.
3. **Reproducibility**: the merge script can be re-run to regenerate all merged files from verification JSONs.
4. **Audit trail**: `merged_log.json` records every merge decision with source IDs.
5. **No data loss**: original files are moved to `_merged_archive/`, not deleted.

### Merge Conflict Resolution

If a canonical_id already exists in CANONICAL_DIR (e.g., three concepts merge into one),
handle as follows:

```python
def handle_collision(canonical_id, new_merged):
    """Merge-in additional sources to an existing canonical concept."""
    existing = json.load(open(CANONICAL_DIR / f"{canonical_id}.json"))

    # Add new alternate sources
    existing_ids = {s.get("book_id") for s in existing.get("alternate_sources", [])}
    for alt in new_merged.get("alternate_sources", []):
        if alt.get("book_id") not in existing_ids:
            existing.setdefault("alternate_sources", []).append(alt)

    # Take the better statement (heuristic: prefer longer = more precise)
    if len(new_merged["statement"]) > len(existing["statement"]):
        existing["statement"] = new_merged["statement"]
        existing["proof_sketch"] = new_merged["proof_sketch"]

    # Union of depends_on
    existing["depends_on"] = list(set(existing.get("depends_on", []) +
                                      new_merged.get("depends_on", [])))

    # Append merge note
    existing["merge_note"] = (existing.get("merge_note", "") +
                              f"\nAdditional merge: {new_merged.get('merge_note', '')}")

    return existing
```

---

## Cross-Cutting Concerns

### Prompt Engineering Principles (from Phase 0/1 lessons)

1. **Keep prompts SHORT.** Monolithic ~1500 word prompts caused thinking exhaustion.
   Target: 500-1200 words per agent prompt. The concept data itself provides the
   detailed context the agent needs.

2. **Separate concerns.** Agent A extracts concepts. Agent B finds duplicates. Agent C
   verifies them. Agent D translates. Each has ONE clear goal.

3. **Disk files as truth.** Never depend on agent return values or StructuredOutput.
   Always check for .done/.fail files on disk after the agent completes.

4. **Checker is NOT an agent.** The compilation checker is a local Python script
   (~100 lines) that runs `lake env lean`. It's fast (~5s), free, and reliable.

5. **Fixer only runs when needed.** The Fixer (Agent D's full prompt) is only
   invoked when .fail exists. This saves ~80% of API costs.

6. **Parallelize aggressively.** All agents operate on independent data. Launch
   16-50 agents simultaneously using multi-workflow.

### API Configuration

```python
# DeepSeek API client configuration
DEEPSEEK_CONFIG = {
    "pro": {
        "model": "deepseek-chat",  # or deepseek-reasoner for thinking
        "max_tokens": 393216,       # 384K — NEVER set lower
        "temperature": 0.1,         # Low for precise math
        "timeout": 1200,            # 20 minutes for complex proofs
        "thinking": True
    },
    "flash": {
        "model": "deepseek-chat",
        "max_tokens": 65536,
        "temperature": 0.1,
        "timeout": 300,             # 5 minutes
        "thinking": False
    }
}

# Retry configuration
RETRY_CONFIG = {
    "max_retries": 5,
    "base_delay": 5,       # seconds
    "max_delay": 120,      # seconds
    "backoff_factor": 2.0,
    "retryable_errors": [
        "rate_limit",
        "server_error",
        "timeout",
        "connection_error"
    ]
}
```

### Cost Summary (per book, ~100 concepts)

| Phase | Agent | Model | Cost |
|---|---|---|---|
| Concept extraction (10 chapters) | A | Pro | ~¥8.00 |
| Concept name collection | Python | N/A | ¥0 |
| Dedup check (5000 names) | B | Flash | ~¥0.06 |
| Dedup verify (~100 pairs) | C | Pro | ~¥3.00 |
| Merge execution | Python | N/A | ¥0 |
| Lean translate (~100 concepts) | D | Pro | ~¥6.00 |
| Compilation check | Python (local) | N/A | ¥0 |
| **Total per book** | | | **~¥17.00** |

For 20 books: ~¥340. Realistic given the ~¥100 budget constraint.

### Quality Control Gates

```
Gate 1 (after Agent A): concepts.json has N entries, pages/ has N .md files
Gate 2 (after Agent A): random sample of 10 entries → manual review statement quality
Gate 3 (after Agent B): every input ID appears in exactly one group (duplicate/singleton/ambiguous)
Gate 4 (after Agent C): every verification pair has .done file
Gate 5 (after merge script): canonical/ has coherent .md + .yaml files
Gate 6 (after Agent D): .done exists for every concept, no .fail files remain
Gate 7 (final): `lake build` passes for entire MathPkg project
```

### Directory Structure After Pipeline Run

```
pipeline_output/
├── concepts_v2/
│   ├── book_073_chapter_1.json          # Agent A output
│   ├── book_073_chapter_1.done
│   ├── book_073_chapter_2.json
│   ├── ...
│   ├── pages/
│   │   ├── lagrange_theorem.md          # Agent A output
│   │   ├── ...
│   ├── canonical/                        # After merge
│   │   ├── lagrange_theorem.md
│   │   ├── lagrange_theorem.yaml
│   │   └── ...
│   └── _merged_archive/                  # Original files from merged concepts
│       └── ...
├── dedup/
│   ├── all_concept_names.json            # Preprocessor output
│   ├── dedup_check_result.json           # Agent B output
│   ├── dedup_check_result.done
│   ├── verifications/
│   │   ├── id_a_vs_id_b.json             # Agent C output
│   │   ├── id_a_vs_id_b.done
│   │   └── ...
│   └── merged_log.json                   # Merge script output
└── translations/
    ├── 0.json                            # Status file (pre-agent)
    ├── 0.done                            # Checker output
    ├── 0.fail                            # Checker output (if failed)
    └── ...
```

---

## References

- [[architecture]] — mathpkg project design
- [[deepseek-api]] — API configuration, thinking mode, token limits
- [[resilient-workflow]] — Checker+Fixer v4 pattern
- [[lean-integration]] — Mathlib4 coverage, API naming traps
- [[batch1-translation]] — 49-concept translation: strategy evolution
- [[phase0-lessons]] — what worked, what didn't
