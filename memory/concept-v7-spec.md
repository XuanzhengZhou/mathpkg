---
name: concept-format-v7-final
description: "V7 final spec: SQLite derived from filesystem, slug disambig, merge procedure, domain+vector dedup"
metadata: 
  node_type: memory
  type: project
  originSessionId: 32b0208b-f009-4db0-9b54-c8a7af2b3275
---

# Concept Format V7 — Final Specification (2026-06-24)

## 0. Core Principle

**Filesystem is the source of truth. SQLite is a derived view.**

Like apt: `/var/lib/dpkg/status` is source, `pkgcache.bin` is cache.
Files on disk are always authoritative. `generate_index.py` rebuilds graph.db from them.
If graph.db is lost or corrupted: run `generate_index.py` to regenerate it.

---

## 1. File Structure

### 1.1 Directory Layout

```
concepts/{domain}/{subdomain}/{slug}/

Domains: algebra, analysis, topology, geometry, number-theory,
         logic-foundations, probability-statistics, combinatorics,
         applied-math, algebraic-geometry

Example:
  concepts/algebra/group-theory/lagrange-theorem/
  concepts/algebra/ring-theory/noetherian-ring/
  concepts/analysis/real/bolzano-weierstrass/
```

### 1.2 Files Per Concept

```
lagrange-theorem/
├── concept.yaml                  ← ONE. Metadata for core file.
├── theorem.tex                   ← PURE LaTeX. Zero frontmatter. Zero natural language.
├── proof_gtm-0073_I.4_coset-partition.en.md  ← One proof per book+technique
├── proof_gtm-0080_1.3_index-mult.en.md
├── introduce.en.md               ← Natural language intro (English)
├── introduce.zh.md               ← Natural language intro (Chinese)
├── exercise_gtm-0073_I.4.8.en.md ← One exercise per file
└── verify.lean                   ← Lean formalization
```

### 1.3 Rules

1. **Exactly one core file per concept**: `theorem.tex`, `definition.tex`, `lemma.tex`, `proposition.tex`, `corollary.tex`, `axiom.tex`.
2. **Core file = pure LaTeX.** No YAML frontmatter. No markdown.
3. **Exactly one concept.yaml per concept.** Carries metadata the core .tex can't express.
4. **All secondary files (.md, .lean) have YAML frontmatter.**
5. **Files are grouped by being in the same folder.** No `attaches_to` field.
6. **Naming: `{role}_{book-id}_{chapter.section}_{technique}.{locale}.{ext}`.** Locale REQUIRED for language-specific files (proofs, exercises). For introduce files: `introduce.{locale}.md`. For verify.lean: `verify.lean` (no locale, no book-id — only ONE per concept).
7. **Conjectures, examples, remarks are NOT standalone.** Folded into nearest theorem/definition, UNLESS a conjecture itself is the central object (e.g., Riemann Hypothesis).
8. **Staging area**: Extraction agents write to `extracted/{book_id}/{book_id}_ch{nn}_concepts/` (nn = zero-padded Arabic chapter number). A post-extraction Python script (`stage_to_concepts.py`) moves them into the canonical `concepts/` tree. If a destination folder already exists, the script applies slug disambiguation (Section 2) and moves the staging copy to the disambiguated path. It does NOT merge — dedup+merge is a separate pipeline phase (Steps 4-7).

---

## 2. Naming Convention (Authoritative)

| Role | Pattern | Example | Locale? |
|---|---|---|---|
| Core | `{role}.tex` | `theorem.tex`, `definition.tex` | N/A |
| Proof | `proof_{book-id}_{ch.sec}_{technique}.{locale}.md` | `proof_gtm-0073_I.4_coset-partition.en.md` | REQUIRED |
| Introduce | `introduce.{locale}.md` | `introduce.zh.md` | REQUIRED |
| Exercise | `exercise_{book-id}_{ch.sec.num}.{locale}.md` | `exercise_gtm-0073_I.4.8.en.md` | REQUIRED |
| Lean | `verify.lean` | `verify.lean` | OMITTED |
| Concept metadata | `concept.yaml` | `concept.yaml` | N/A |

**Book ID**: `{series}-{number}`, zero-padded to 4 digits: `gtm-0073`, `utm-0001`, `hzm-0003`.

**Technique slug**: Short keyword distinguishing proofs from the same book+section. If no distinguishing technique: use page number or `alt1`/`alt2`.

**Locale**: `en`, `zh`, `fr`, `de`, `ru`, etc. OMITTED only for language-agnostic files (verify.lean).

**Slug** (concept folder name): `{title_en}` lowercased, hyphenated, max 64 chars. Slugs are GLOBALLY unique across all domains. If collision: append author surname: `cayley-theorem-hungerford` vs `cayley-theorem-bondy`. If STILL ambiguous: append first 6 chars of SHA256(title_en.lower() + "|" + first_author.lower()).

---

## 3. concept.yaml Schema

```yaml
# concept.yaml — single source of metadata for core .tex file
id: lagrange-theorem                    # slug (matches folder name)
title_en: "Lagrange's Theorem"          # canonical English name
title_zh: "拉格朗日定理"                 # Chinese name ("" if unknown)
type: theorem                           # theorem|lemma|proposition|corollary|definition|axiom
domain: algebra                         # from domain enum
subdomain: group-theory                 # lowercase-hyphen
difficulty: basic                       # basic|intermediate|advanced
tags: [finite-groups, cosets]           # optional

depends_on:
  required: [subgroup, coset]           # concept slugs
  recommended: [group-action]
  suggested: [first-isomorphism-theorem]
  # NOTE: dependencies may be UNRESOLVED during extraction.
  # They are filled/resolved during the dedup+merge phase.

proof_deps:                             # extra deps per proof file
  proof_gtm-0073_I.4_coset-partition.en.md:
    recommended: [cauchy-theorem]

source_books:
  - book_id: gtm-0073
    author: "Hungerford, Thomas W."
    title: "Algebra"
    chapter: I
    section: "I.4"
    pages: "38-42"
    role_in_book: "Theorem I.4.7"

content_hash: ""                        # SHA256 of core .tex file, filled by compute_hashes.py, empty on creation
extraction_date: "2026-06-24"
extraction_agent: "pro-v4"

# Domain enum: algebra, analysis, topology, geometry, number-theory,
#   logic-foundations, probability-statistics, combinatorics,
#   applied-math, algebraic-geometry
```

**Dependency resolution** (two-pass):
- **Extraction pass**: Agent writes concept.yaml with `depends_on` using its best guess. Unresolved deps are written as slugs — they may not exist yet.
- **Dedup+merge pass**: After ALL concepts are extracted and deduped, a Python script resolves every `depends_on` slug against the final registry. Unresolved deps → flagged for review. This is when the DAG is locked.

---

## 4. Secondary File YAML Frontmatter

### 4.1 Proof File

```yaml
---
role: proof
source_book: gtm-0073
chapter: I
section: "I.4"
proof_technique: coset-partition
locale: en
content_hash: ""                        # SHA256 of this file, filled by compute_hashes.py
written_against: ""                    # SHA256 of core .tex when written, filled by compute_hashes.py
---
```

### 4.2 Introduce File

```yaml
---
role: introduce
locale: zh
content_hash: ""
written_against: ""
---
```

### 4.3 Exercise File

```yaml
---
role: exercise
source_book: gtm-0073
chapter: I
section: "I.4"
number: 8
tier: intermediate
locale: en
connects: []                           # concept slugs this exercise bridges to
content_hash: ""
written_against: ""
---
```

### 4.4 Lean File

```yaml
---
role: lean
mathlib4_deps: [Mathlib.GroupTheory.Coset.Card]
content_hash: ""
written_against: ""
---
```

---

## 5. SQLite Schema (graph.db)

Derived from filesystem. Regenerated by `generate_index.py`.

```sql
PRAGMA journal_mode = WAL;
PRAGMA foreign_keys = ON;

CREATE TABLE concepts (
    id TEXT PRIMARY KEY,
    title_en TEXT NOT NULL,
    title_zh TEXT NOT NULL DEFAULT '',
    type TEXT NOT NULL CHECK(type IN ('theorem','lemma','proposition','corollary','definition','axiom')),
    domain TEXT NOT NULL,
    subdomain TEXT NOT NULL,
    difficulty TEXT NOT NULL CHECK(difficulty IN ('basic','intermediate','advanced')),
    content_hash TEXT NOT NULL DEFAULT '',
    folder_path TEXT NOT NULL UNIQUE,
    extraction_date TEXT NOT NULL,
    extraction_agent TEXT NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE deps (
    from_id TEXT NOT NULL REFERENCES concepts(id) ON DELETE CASCADE,
    to_id TEXT NOT NULL REFERENCES concepts(id) ON DELETE CASCADE,
    dep_type TEXT NOT NULL CHECK(dep_type IN ('required','recommended','suggested','proof_extra')),
    proof_file TEXT NOT NULL DEFAULT '',   -- '' = concept-level dep
    PRIMARY KEY (from_id, to_id, dep_type, proof_file)
);

CREATE TABLE files (
    concept_id TEXT NOT NULL REFERENCES concepts(id) ON DELETE CASCADE,
    filename TEXT NOT NULL,
    role TEXT NOT NULL CHECK(role IN ('theorem','definition','lemma','proposition','corollary','axiom','proof','introduce','exercise','lean')),
    locale TEXT,                          -- NULL = language-agnostic
    source_book TEXT,
    proof_technique TEXT,
    chapter TEXT,
    section TEXT,
    exercise_number TEXT,
    exercise_tier TEXT,
    connects_to TEXT,                     -- JSON array of concept IDs (for exercises)
    written_against TEXT NOT NULL DEFAULT '',
    content_hash TEXT NOT NULL DEFAULT '', -- SHA256 of this file's own content
    PRIMARY KEY (concept_id, filename)
);

CREATE TABLE source_books (
    concept_id TEXT NOT NULL REFERENCES concepts(id) ON DELETE CASCADE,
    book_id TEXT NOT NULL,
    author TEXT DEFAULT '',
    title TEXT DEFAULT '',
    chapter TEXT DEFAULT '',
    section TEXT DEFAULT '',
    pages TEXT DEFAULT '',
    role_in_book TEXT DEFAULT '',
    PRIMARY KEY (concept_id, book_id)
);

CREATE TABLE tags (
    concept_id TEXT NOT NULL REFERENCES concepts(id) ON DELETE CASCADE,
    tag TEXT NOT NULL,
    PRIMARY KEY (concept_id, tag)
);

CREATE TABLE rename_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    old_id TEXT NOT NULL,
    new_id TEXT NOT NULL,
    renamed_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE validation_errors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    concept_id TEXT,                      -- NULL for global errors
    error_type TEXT NOT NULL,
    message TEXT NOT NULL,
    detected_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- Trigger for updated_at
CREATE TRIGGER update_concepts_ts AFTER UPDATE ON concepts
BEGIN UPDATE concepts SET updated_at = CURRENT_TIMESTAMP WHERE id = NEW.id; END;

-- Essential indexes
CREATE INDEX idx_concepts_domain_subdomain ON concepts(domain, subdomain);
CREATE INDEX idx_concepts_type ON concepts(type);
CREATE INDEX idx_deps_to_id ON deps(to_id);
CREATE INDEX idx_deps_dep_type ON deps(dep_type);
CREATE INDEX idx_files_role ON files(role);
CREATE INDEX idx_files_written_against ON files(written_against);
CREATE INDEX idx_source_books_book_id ON source_books(book_id);
CREATE INDEX idx_tags_tag ON tags(tag);
```

---

## 6. Dedup Strategy (Scalable to Millions)

### Phase 1: Domain partitioning
- Each domain is independently deduped in parallel
- Average concepts per domain: N/10

### Phase 2: Within-domain name dedup (Flash Agent)
- Flash compares ONLY concept names (title_en, title_zh) within the same domain
- Matching rule: title_en lowercased, punctuation removed, word-level Jaccard similarity > 0.8 → candidate duplicate. title_zh exact match after removing punctuation → candidate duplicate.

### Phase 3: Within-domain content dedup (vector embedding)
- For each candidate group or singleton: compute embedding of theorem.tex via small embedding model (local GPU or cheap API)
- Embedding cosine similarity > 0.95 → content-level duplicate candidate
- This is O(N per domain), not O(N^2) — we only compare against same-domain embeddings and flag the closest matches

### Phase 4: Pro Agent verification
- For high-similarity pairs: Pro Agent reads BOTH theorem.tex files, decides merge vs separate

### Complexity
- Domain partitioning → O(D × (N/D)) = O(N)
- Embedding → O(N) per domain
- Neighbor search → O(N log N) with FAISS or similar
- Scalable to 100K, 1M, even 100M concepts with sharding

---

## 7. Merge Procedure

When Agent C (dedup verifier) decides "merge":

1. **Select primary**: folder with MORE source_books wins. Tie: alphabetically lower slug.
2. **Preserve losing core .tex**: Rename to `{role}_merged_{losing_slug}.tex` where `{role}` = losing concept's `type` field (theorem/definition/lemma/...).
3. **Copy secondary files**: All secondary files from the losing folder are copied to the winning folder.
   - Proof and exercise files: book-id in filename ensures uniqueness.
   - `introduce.{locale}.md`: if both folders have one, rename the loser's to `introduce_{losing_slug}.{locale}.md`.
   - `verify.lean`: the winning folder's verify.lean is kept. The loser's is renamed to `verify_{losing_slug}.lean` for reference.
4. **Merge concept.yaml**:
   - `type`: winning concept's type is kept. Reason recorded in merge log.
   - `title_en`/`title_zh`: winning concept's title is kept.
   - `difficulty`: higher difficulty wins (advanced > intermediate > basic).
   - `tags`: union, deduped.
   - `source_books`: arrays concatenated.
   - `depends_on`: union (deduped, self-references removed).
   - `proof_deps`: merged by proof filename.
   - `extraction_date`/`extraction_agent`: winning concept's values kept.
5. **Move losing folder**: Renamed to `concepts/_merged/{losing_slug}-{timestamp}/`.
6. **Update all references**: Every concept.yaml's `depends_on.*` referencing the losing slug → winning slug. All `proof_deps` values and exercise `connects` arrays are also scanned and updated.
7. **Run compute_hashes.py**: Recomputes content_hash and all written_against fields on the winning folder.
8. **Regenerate graph.db**: `generate_index.py` rebuilds from updated filesystem.
9. **Log**: Entry in `rename_log` table.

---

## 8. Tooling

| Tool | Function | Runs |
|---|---|---|
| `stitch_chapters.py` | OCR pages → chapter .md | Once per book |
| `extract_concepts.py` | Pro Agent: chapter → concept folders | Parallel per chapter |
| `compute_hashes.py` | SHA256 of core .tex + all secondary files → fills content_hash and written_against | After extraction |
| `generate_index.py` | Scans filesystem → (re)builds graph.db | After any change |
| `validate_deps.py` | Cross-checks depends_on, finds cycles, flags orphans | After index |
| `resolve_deps.py` | Resolves unresolved depends_on slugs against post-merge registry | After merge + index rebuild |
| `stage_to_concepts.py` | Moves extracted concepts from staging to canonical tree | After extraction |
| `merge_concepts.py` | Executes merge procedure (Section 7) when Pro Agent decides "merge" | During dedup |
| `rename_concept.py <old> <new>` | Renames concept, updates ALL references in concept.yaml files, rebuilds index | On demand |
| `check_staleness.py` | Compares written_against vs current content_hash | After any theorem.tex edit |
| `flash_dedup.py` | Domain-partitioned + name-match + embedding dedup | After extraction |

---

## 9. Pipeline

```
Step 0:  GLM-OCR pages → stitch_chapters.py → chapter.md

Step 1:  Pro Agent (per chapter, parallel)
         chapter.md → concept folders (in staging area)
         concept.yaml: depends_on = best guess (may be unresolved)
         content_hash = "" (empty placeholder)

Step 2:  stage_to_concepts.py
         → moves concepts from staging to canonical concepts/ tree
         → slug disambiguation on collision, no merging

Step 3:  compute_hashes.py
         → fills content_hash on all concept.yaml
         → fills written_against on all secondary files
         → fills content_hash on all secondary files

Step 4:  generate_index.py → builds graph.db from filesystem

Step 5:  flash_dedup.py (domain-partitioned + embedding)
         → candidate duplicate groups

Step 6:  Pro Agent (per candidate group)
         → merge/separate decision
         → merge_concepts.py executes merge (see Section 7)

Step 7:  compute_hashes.py (re-run)
         → recomputes content_hash on merged concepts
         → updates written_against on relocated secondary files
         → recomputes content_hash on all secondary files

Step 8:  generate_index.py → rebuild graph.db with merged concepts

Step 9:  resolve_deps.py
         → reads all concept.yaml files
         → resolves depends_on slugs against final (post-merge) concept ID registry
         → flags unresolved deps → _review_queue.json

Step 10: validate_deps.py
         → broken deps, cycles, orphans → validation_errors table

Step 11: Pro Agent (per concept, parallel)
         → writes verify.lean (grep Mathlib4, self-heal up to 10 rounds)
         → on success: writes `concepts/{domain}/{subdomain}/{slug}/.lean-status` as plain text file containing `done`
         → on exhaustion: writes `.lean-status` containing `fail:{error_summary}`

Step 12: verify_env.py
         → symlinks all verify.lean into lean/MathPkg/MathPkg/Concepts/
         → lake build → all Lean verified

Step 13: generate_encyclopedia.py
         → reads concept.yaml + all secondary files
         → compiles _compiled/{slug}.md per concept
```

---

## 10. Concept ID Resolution (Two-Pass)

**Pass 1 (Extraction):**
- Agent writes `depends_on: [subgroup, coset]` using its best guess
- Slugs are WRITTEN but may not exist yet
- concept.yaml has `content_hash: ""` (empty)

**Pass 2 (Post-dedup):**
- After ALL concepts extracted and deduped, a global concept ID registry exists
- `resolve_deps.py` reads every concept.yaml AND every secondary file YAML frontmatter
- Slug-containing fields processed: `depends_on.*`, `proof_deps.*.*`, exercise `connects`
- For each slug: resolve against the registry
- If a slug matches multiple concepts across different domains → flagged as ambiguous in `_review_queue.json`
- Unresolved → `_review_queue.json` for manual attention
- Resolved → field updated with canonical slug

This eliminates the chicken-and-egg problem.

---

## 11. Lake Workspace

```
lean/MathPkg/
├── lakefile.toml          ← depends on mathlib v4.31.0
├── MathPkg.lean
├── MathPkg/
│   └── Concepts/
│       └── verify_env.py generates symlinks here:
│           algebra/group-theory/lagrange-theorem.lean → concepts/.../verify.lean
│           algebra/group-theory/subgroup.lean → concepts/.../verify.lean
└── .lake/
    └── build/             ← compiled .olean files
```

`verify_env.py` creates symlinks from the concept folder tree into `lean/MathPkg/MathPkg/Concepts/`. Lake builds this like a normal Lean project. One `lake build` validates all Lean files. Individual concept compilation uses `lake env lean path/to/file.lean`.

---

## 12. Cost

| Step | Tool | Per-concept cost | Parallel |
|---|---|---|---|
| OCR | GLM (local GPU) | ¥0 | N/A |
| Stitch | Python | ¥0 | N/A |
| Extract | Pro Agent | ~¥0.05-0.10 | Yes |
| Hashes + Index | Python | ¥0 | N/A |
| Resolve deps | Python | ¥0 | N/A |
| Flash dedup (name) | Flash | ~¥0.00001 | N/A |
| Embedding dedup | Local/small API | ~¥0.001 | Yes |
| Pro dedup verify | Pro Agent | ~¥0.03/pair | Yes |
| Validate | Python | ¥0 | N/A |
| Lean translate | Pro Agent | ~¥0.05 | Yes |
| lake build | Local | ¥0 | N/A |
| Encyclopedia | Python | ¥0 | N/A |

**For 10,000 concepts: ~¥1,500-2,000 total.**
