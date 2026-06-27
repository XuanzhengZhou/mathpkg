---
name: must-split-by-chapter
description: "CRITICAL lesson: one agent per book fails. Must split into chapters. One agent per chapter."
metadata: 
  node_type: memory
  type: project
  originSessionId: 32b0208b-f009-4db0-9b54-c8a7af2b3275
---

# CRITICAL Lesson: Must Split by Chapter (2026-06-24)

## The Problem

GTM073 (523p, 812KB) was processed in 9 chapters → 486 concepts.  
10-book test processed each book as ONE file → 921 concepts from 10 books (should be ~4,000).

**Root cause**: A single agent reading a 500KB book hits output token limits and stops extracting after ~50-100 concepts. The agent simply cannot produce enough output for a full textbook in one call.

## The Fix

**ONE CHAPTER = ONE AGENT.** Never process an entire book as one unit.

- For books with explicit CHAPTER markers: split at CHAPTER boundaries
- For monographs without chapters: split every ~60KB (roughly the input limit for a single agent call)

## Evidence

| Processing | GTM073 | GTM006 (513KB) |
|---|---|---|
| Per-chapter (correct) | 486 concepts | N/A |
| Per-book (wrong) | N/A | 178 concepts |

Projective Planes (GTM006, 302p) should yield similar density to GTM073 but per-book extraction undercounted by ~60%.

## Implementation

```python
# Split strategy:
# 1. Find CHAPTER markers → split there
# 2. If no markers or too few → split every 60KB
# 3. Each chunk ≤ 80KB
# 4. Each chunk → one agent
```

## Related
- [[v7-test-lessons]] — 10-book test results
- [[pipeline-v3]] — per-chapter pipeline design
