---
name: file-naming-and-content-spec
description: "Complete spec: file naming conventions, .md template, .yaml format, Agent prompts for pipeline V3"
metadata: 
  node_type: memory
  type: project
  originSessionId: 32b0208b-f009-4db0-9b54-c8a7af2b3275
---

# File Naming & Content Specification (V3)

## 1. File Naming Convention

### Level 0: Book ID

`{series}-{nnnn}` — ASCII-safe, sortable.

| Code | Series | Count |
|---|---|---|
| `gtm` | Graduate Texts in Mathematics | ~305 |
| `utm` | Undergraduate Texts in Mathematics | ~409 |
| `utx` | Universitext | ~435 |
| `smm` | Springer Monographs in Mathematics | ~324 |
| `hzm` | 华章数学译丛 | ~82 |
| `etc` | 散装经典教材 | ~10 |

Example: `gtm-0073` = GTM 73: Hungerford, Algebra.

### Level 1-3: OCR, Chapters, Extractions

```
ocr/{book_id}/{book_id}_p{nnnn}.json         ← per-page OCR
chapters/{book_id}/{book_id}_ch{nn}.md       ← stitched chapters
extracted/{book_id}/{book_id}_ch{nn}_concepts.json  ← concept extraction
```

### Level 4: Canonical Concepts

```
concepts/{topic}/{slug}/
├── {slug}.md         ← encyclopedia page (6 sections)
├── {slug}.lean       ← Lean 4 formal verification
└── concept.yaml      ← apt control file (deps, sources, versions)
```

**Slug rules:** lowercase, hyphens, max 64 chars. English name for all concepts (Chinese stored in YAML `name.zh`). Collision → append author/year hash.

---

## 2. Concept .md Specification (6 Sections)

Fixed heading names, machine-parseable.

### YAML Frontmatter

```yaml
---
id: lagrange_theorem
name_en: "Lagrange's Theorem"
name_zh: "拉格朗日定理"
type: theorem
difficulty: basic

depends:
  required: [subgroup, coset]
  recommended: [group_action]
  suggested: [first_isomorphism_theorem]

versions:
  - source: gtm-0073, author: Hungerford, chapter: I, section: I.4, pages: 38-42
  - source: gtm-0080, author: Robinson, chapter: 1, section: 1.3, pages: 15-17

lean:
  mathlib4_path: Mathlib.GroupTheory.Coset.Card
  status: complete
---
```

### Section 1: Statement
LaTeX theorem statement + notation definitions + informal description.

### Section 2: Proof
Numbered steps. Each step references a theorem/definition. NO "clearly/obviously".

### Section 3: Textbook Comparison
Table: Source | Author | Approach | Difficulty | Pages. Plus narrative on *why* approaches differ.

### Section 4: Dependencies
ASCII tree: what this depends on → what depends on this.

### Section 5: Lean Verification
Status table + illustrative code block. Full code in `{slug}.lean`, NOT inline.

### Section 6: Exercises
Three tiers: Basic | Intermediate | Advanced. Each tagged with `connects:` field.

---

## 3. concept.yaml Format

```yaml
id: lagrange_theorem
canonical_id: c-a3f2b1c0        # SHA256 first 8 chars
name: {en: "Lagrange's Theorem", zh: "拉格朗日定理"}
type: theorem
topic: group-theory

depends:
  required: [subgroup, coset]
  recommended: [group_action]

versions:
  - source: gtm-0073, author: Hungerford, chapter: I.4, pages: 38-42

lean:
  mathlib4_path: Mathlib.GroupTheory.Coset.Card
  mathlib4_theorem: Subgroup.card_subgroup_dvd_card
  status: complete
```

---

## 4. Agent Prompt Summaries

### Agent A: Concept Extractor (Pro, thinking=true)
- Input: chapter .md (~70K chars)
- Output: `extracted/{book_id}_ch{nn}_concepts.json` + per-concept `.md` files
- Must handle: Chinese+English mixed texts, mixed notation
- Cost: ~¥0.80/chapter

### Agent B: Dedup Checker (Flash, no thinking)
- Input: ALL concept names (~5000 entries)
- Output: `{duplicate_groups: [], singletons: [], ambiguous: []}`
- One batch call, ~¥0.06 total
- Aggressive grouping: flag borderline cases

### Agent C: Dedup Verifier (Pro, thinking=true)
- Input: two concept .md files
- Output: `{decision: merge|separate, merged_content?: ...}`
- Conservative bias: when uncertain, keep separate
- Cost: ~¥0.03/pair

### Agent D: Lean Translator (Pro, thinking=true)
- Input: concept .md (statement + detailed proof)
- Output: `{slug}.lean` (compilable), `.done` marker
- Checker+Fixer v4: local compile check → fix only on .fail
- grep Mathlib4 BEFORE writing code
- Up to 10 self-heal rounds
- Cost: ~¥0.02-0.08/concept

---

## 5. Merge Strategy (Agent C output → Python script)

When Agent C decides "merge":
1. Python reads both concept directories
2. Merges `versions:` lists, `depends:` unions
3. Generates merged `.md` and `.yaml`
4. Moves originals to `_merged_archive/`
5. Writes `merged_log.json` for audit

No agent touches files during merge — deterministic Python script only.

## Related
- [[pipeline-v3]] — full pathway design
- [[concept-format-v2]] — original three-file format
- [[agent-prompt-design]] — detailed prompt templates
