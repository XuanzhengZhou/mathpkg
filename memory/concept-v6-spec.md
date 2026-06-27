---
name: concept-format-v6
description: "V6 final spec: SQLite + flat DAG folders, one concept.yaml per concept, theorem.tex pure LaTeX"
metadata: 
  node_type: memory
  type: project
  originSessionId: 32b0208b-f009-4db0-9b54-c8a7af2b3275
---

# Concept Format V6 — Final Specification (2026-06-24)

## 0. Architecture

```
文件系统:    只存内容 (.tex, .md, .lean, concept.yaml)
SQLite:      graph.db = 全局索引 (concepts, deps, files, hashes)
            改名=UPDATE, 去重=SELECT, 依赖检查=JOIN
```

和 apt 模型完全一致——SQLite 是 pkgCache，文件是 Package。Phase 0 已实现基础版。

---

## 1. File Structure

### 1.1 Directory Layout

```
concepts/{domain}/{subdomain}/{slug}/

Example:
  concepts/algebra/group-theory/lagrange-theorem/
  concepts/algebra/ring-theory/noetherian-ring/
  concepts/analysis/real/bolzano-weierstrass/
```

### 1.2 Files Per Concept

```
lagrange-theorem/
├── concept.yaml               ← ONE concept.yaml (only for core .tex)
├── theorem.tex                ← PURE LaTeX. Zero metadata. Zero frontmatter.
├── proof_gtm-0073_I.4.md      ← YAML frontmatter self-declares
├── proof_gtm-0080_1.3.md      ← Different proof approach
├── introduce.md               ← English natural language
├── introduce.zh.md             ← Chinese
├── exercise_gtm-0073_I.4.8.md ← One exercise per file
└── verify.lean                ← Lean formalization
```

### 1.3 Rules

1. **Exactly one core file per concept**: one of `theorem.tex`, `definition.tex`, `lemma.tex`, `proposition.tex`, `corollary.tex`, `axiom.tex`.
2. **Core file = pure LaTeX.** No YAML frontmatter. No markdown. No natural language. Pure mathematical statement.
3. **Exactly one concept.yaml per concept.** Carries ALL metadata that the core .tex can't express.
4. **All other files (.md, .lean) have YAML frontmatter** that self-declares role, source, locale, and written_against hash.
5. **No `attaches_to` field.** Files are grouped by being in the same folder.
6. **Naming:** `{role}_{book-id}_{chapter.section}_{descriptor}.{lang}.{ext}`. Lang tag omitted if language-agnostic.
7. **Conjectures, examples, remarks are NOT standalone concepts.** Folded into nearest theorem/definition.

---

## 2. concept.yaml Schema

```yaml
# concept.yaml — ONE per concept. Contains all metadata the core .tex can't express.
id: lagrange-theorem                    # slug, lowercase-hyphen, max 64 chars
title_en: "Lagrange's Theorem"          # canonical English name
title_zh: "拉格朗日定理"                 # Chinese name (empty string if unknown)
type: theorem                           # theorem|lemma|proposition|corollary|definition|axiom
domain: algebra                         # see domain enum below
subdomain: group-theory                 # lowercase-hyphen
difficulty: basic                       # basic|intermediate|advanced
tags: [finite-groups, cosets, order]    # optional array
depends_on:
  required: [subgroup, coset]           # concept IDs (slugs)
  recommended: [group-action]           # optional
  suggested: [first-isomorphism-theorem] # optional
proof_deps:                             # optional: extra deps per proof file
  proof_gtm-0073_I.4.md:                # filename in this folder
    required: []
    recommended: [cauchy-theorem]
source_books:
  - book_id: gtm-0073
    author: "Hungerford, Thomas W."
    title: "Algebra"
    chapter: 1
    section: "I.4"
    pages: "38-42"
    role_in_book: "Theorem I.4.7"
  - book_id: gtm-0080
    author: "Robinson, Derek J.S."
    title: "A Course in the Theory of Groups"
    chapter: 1
    section: "1.3"
    pages: "15-17"
    role_in_book: "Theorem 1.3.6"
content_hash: "sha256:abc123..."        # auto-computed from theorem.tex
extraction_date: "2026-06-24"
extraction_agent: "pro-v4"

# Domain enum: algebra, analysis, topology, geometry, number-theory,
#   logic-foundations, probability-statistics, combinatorics,
#   applied-mathematics, algebraic-geometry
```

---

## 3. Secondary File YAML Frontmatter

Every .md and .lean file (except core .tex) starts with YAML frontmatter:

### 3.1 Proof File
```yaml
---
role: proof
source_book: gtm-0073
chapter: I
section: "I.4"
proof_technique: coset-partition
locale: en                                   # omitted if language-agnostic
written_against: "sha256:abc123..."           # hash of theorem.tex when written
proves_also: []                               # optional: other concepts proved
---
```

### 3.2 Introduce File
```yaml
---
role: introduce
locale: zh
written_against: "sha256:abc123..."
---
```

### 3.3 Exercise File
```yaml
---
role: exercise
source_book: gtm-0073
chapter: I
section: "I.4"
number: 8
connects: [cyclic-group]                     # concepts this exercise bridges to
locale: en
tier: intermediate
---
```

### 3.4 Lean File
```yaml
---
role: lean
written_against: "sha256:abc123..."
mathlib4_deps: [Mathlib.GroupTheory.Coset.Card]
---
```

---

## 4. SQLite Schema (graph.db)

```sql
-- Concepts table (one row per concept)
CREATE TABLE concepts (
    id TEXT PRIMARY KEY,                  -- slug
    title_en TEXT NOT NULL,
    title_zh TEXT NOT NULL DEFAULT '',
    type TEXT NOT NULL,                   -- theorem|lemma|definition|...
    domain TEXT NOT NULL,
    subdomain TEXT NOT NULL,
    difficulty TEXT NOT NULL,
    content_hash TEXT NOT NULL,           -- SHA256 of core .tex
    folder_path TEXT NOT NULL,            -- relative path
    extraction_date TEXT NOT NULL,
    extraction_agent TEXT NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- Dependencies (edges in the DAG)
CREATE TABLE deps (
    from_id TEXT NOT NULL,
    to_id TEXT NOT NULL,
    dep_type TEXT NOT NULL,               -- required|recommended|suggested|proof_extra
    proof_file TEXT,                       -- NULL for concept-level deps
    PRIMARY KEY (from_id, to_id, dep_type, COALESCE(proof_file, ''))
);

-- Files in each concept folder
CREATE TABLE files (
    concept_id TEXT NOT NULL,
    filename TEXT NOT NULL,               -- e.g., proof_gtm-0073_I.4.md
    role TEXT NOT NULL,                   -- theorem|proof|introduce|exercise|lean
    locale TEXT,                           -- NULL if language-agnostic
    source_book TEXT,                      -- NULL for non-book-specific files
    written_against TEXT,                  -- content hash when written
    PRIMARY KEY (concept_id, filename)
);

-- Source books
CREATE TABLE source_books (
    concept_id TEXT NOT NULL,
    book_id TEXT NOT NULL,
    author TEXT,
    title TEXT,
    chapter TEXT,
    section TEXT,
    pages TEXT,
    role_in_book TEXT
);

-- Rename log (audit trail)
CREATE TABLE rename_log (
    old_id TEXT NOT NULL,
    new_id TEXT NOT NULL,
    renamed_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- Validation errors
CREATE TABLE validation_errors (
    concept_id TEXT,
    error_type TEXT NOT NULL,
    message TEXT NOT NULL,
    detected_at TEXT DEFAULT CURRENT_TIMESTAMP
);
```

---

## 5. Tooling

| Tool | Function |
|---|---|
| `stitch_chapters.py` | OCR pages → chapter .md |
| `extract_concepts.py` | Agent caller: chapter → concept folders |
| `compute_hashes.py` | SHA256 of core .tex → concept.yaml.content_hash |
| `generate_index.py` | Scan folders → populate graph.db |
| `validate_deps.py` | Check all deps resolve, no cycles, no self-loops |
| `rename_concept.py` | Rename concept, update all references, log |
| `check_staleness.py` | Compare written_against vs current hash, flag stale |
| `flash_dedup.py` | Flash Agent: scan all core .tex, find duplicates |

---

## 6. Pipeline

```
OCR pages → stitch_chapters.py → chapter.md
    ↓ (Pro Agent, per chapter)
concept folders (concept.yaml + theorem.tex + secondary files)
    ↓ (compute_hashes.py)
content_hash filled
    ↓ (generate_index.py)
graph.db populated
    ↓ (flash_dedup.py — Flash Agent)
duplicate groups identified
    ↓ (Pro Agent + Python merge script)
folders merged, graph.db updated
    ↓ (validate_deps.py)
dependency integrity verified
    ↓ (Pro Agent, per concept)
verify.lean written (grep Mathlib4, self-heal up to 10 rounds)
    ↓ (lake build)
all Lean verified
    ↓ (generate_encyclopedia.py)
_compiled.md generated from all source files
```

---

## 7. Naming Convention Summary

| Pattern | Example |
|---|---|
| Core .tex | `theorem.tex`, `definition.tex`, `lemma.tex` |
| Proof | `proof_gtm-0073_I.4_coset-partition.md` |
| Introduce | `introduce.md`, `introduce.zh.md` |
| Exercise | `exercise_gtm-0073_I.4.8.md` |
| Lean | `verify.lean` |
| Book ID | `{series}-{number}`: `gtm-0073`, `utm-0213`, `hzm-0032` |

---

## 8. Validation Rules

`validate_deps.py` checks:
1. Every `depends_on.*` slug resolves to an existing concept ID in graph.db
2. No circular dependencies (DFS cycle detection)
3. No self-dependency
4. Every `proof_deps` key matches an existing file in the folder
5. Every `written_against` hash matches current `content_hash` (or flag as stale)
6. Every `attaches_to` reference (if reintroduced) resolves within same folder

**Failures do NOT block the pipeline — they flag for manual review.**

---

## 9. Cost

| Step | Tool | Cost |
|---|---|---|
| Stitch | Python | ¥0 |
| Extract (1,565 books) | Pro Agent | ~¥700 |
| Hashes + Index | Python | ¥0 |
| Flash dedup | Flash Agent | ~¥0.06 |
| Pro dedup verify | Pro Agent | ~¥3 |
| Lean translate (per concept) | Pro Agent | ~¥0.05 |
| lake build | Local | ¥0 |
| Encyclopedia compile | Python | ¥0 |
