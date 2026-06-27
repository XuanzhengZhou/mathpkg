---
name: v7-pipeline-test-lessons
description: "10-book V7 pipeline test: quality issues found, fixes, cost data, concurrent workflow results"
metadata: 
  node_type: memory
  type: project
  originSessionId: 32b0208b-f009-4db0-9b54-c8a7af2b3275
---

# V7 Pipeline — 10-Book Test Lessons (2026-06-24)

## Results

| Metric | Value |
|---|---|
| Books | 10 (2 simple, 6 medium, 2 complex) |
| Concepts extracted | 936 (disk truth) |
| Avg concepts/book | 93.6 |
| Files per concept | 3 (theorem.tex + introduce.en.md + concept.yaml) |
| Total files | ~2,808 |
| Duration | 8 minutes (10 agents parallel) |
| Cost | ¥7.68 (1,280,097 tokens) |
| Per-book cost | ¥0.77 |

## Quality Issues Found

### Issue 1: Slug inconsistency (CRITICAL)

Different agents chose different naming conventions:
- ✅ GOOD: `kummers_theorem_regular_primes` (GTM050)
- ❌ BAD: `gtm006_theorem_4_6` (GTM006) — book-reference style
- ❌ BAD: `chii_defn_1_1` (GTM065) — abbreviated chapter reference

**Root cause**: Prompt template was too loose. Agent fell back to book-reference slugs when uncertain.

### Issue 2: Proof in theorem.tex (HIGH)

GTM006 agent included proof text in theorem.tex:
```latex
\begin{theorem}[Theorem 4.6]
A proper closed Baer subset...
\textbf{Proof.} Let $\mathcal{C}$ be the intersection...  ← SHOULD NOT BE HERE
```

**Root cause**: Agent didn't understand "pure LaTeX statement" means statement ONLY, not proof.

### Issue 3: Counting agents unreliable (MEDIUM)

4/10 books reported 0 concepts but had substantial disk output (115-194 concepts). Count agents failed due to API errors but extract agents succeeded.

**Fix**: Never trust agent-reported counts. Always count from disk.

## Fixes Applied

1. **Stricter prompt**: Added explicit examples of GOOD/BAD slugs. Added WARNING about proofs in theorem.tex.
2. **Disk-based counting**: Post-extraction, verify with `find -name concept.yaml | wc -l`.
3. **Standardized template**: Single prompt for all books, no variation.

## Concurrent Workflow Performance

- 10 books → 20 agent calls (10 extract + 10 count)
- All extract agents ran in parallel (~8 minutes wall time)
- No file conflicts (each book → separate staging directory)
- Network-related API errors caused 4 count agents to fail, but files were written successfully

## Related
- [[pipeline-v3]] — pipeline design
- [[concept-v7-spec]] — V7 file format specification
- [[batch1-translation]] — earlier Batch 1 translation lessons
