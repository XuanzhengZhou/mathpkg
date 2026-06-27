---
name: section-strategy
description: "Final section splitting: 4-tier strategy. regex→chapter→Flash→size. 131 books, 4,482 chunks, avg 34/book."
metadata:
  type: project
  originSessionId: current
---

# Section-Level Splitting Strategy (Final, 2026-06-25)

## Core Discovery

**Pages per section ≈ 10, regardless of book length.** Tested across 131 OCR'd books.

| Book length | Books | Avg sections/book | Pages/section |
|---|---|---|---|
| Short (100-200p) | 19 | 20 | **8** |
| Medium (200-350p) | 57 | 30 | **9** |
| Long (350-550p) | 51 | 37 | **12** |

## 4-Tier Fallback Strategy (Final)

```
OCR pages → regex section detection (6 patterns)
              ↓ failed (<50% of pages/10 expected)
           chapter detection (CHAPTER/Chapter/Kapitel patterns)
              ↓ still failed
           Flash full-text analysis (DeepSeek Flash, ~¥0.15/book)
              ↓ still failed (OCR too poor or book has no subsection structure)
           size-based fallback (~60KB chunks)
```

## Final Results (131 OCR'd books)

| Strategy | Books | % | Quality |
|---|---|---|---|
| **regex section** | 102 | 78% | ✅ avg 10p/chunk |
| **Flash full-text** | 20 | 15% | ✅ avg 8-15p/chunk |
| **chapter fallback** | 1 | 1% | ✅ GTM001, 13 chunks |
| **size fallback** | 8 | 6% | ❌ need manual/re-OCR |
| **Total** | **131** | | **4,482 chunks, 55 MB** |

Average: 34 chunks/book, 12 KB/chunk.

## 8 Books Needing Manual Attention

All 8 share root cause: OCR quality too poor, or book has no subsection structure.

| Book | Pages | OCR chars | Why failed |
|---|---|---|---|
| GTM078 Universal Algebra | 331 | 24K | OCR nearly empty |
| GTM101 Galois Theory (Edwards) | 164 | 3K | OCR severely missing |
| GTM127 Algebraic Topology (Massey) | 445 | 40K | OCR mostly blank |
| GTM124 Modern Geometry Vol3 | 430 | 78K | OCR poor |
| GTM056 Algebraic Topology (Massey) | 282 | 15K | OCR nearly empty |
| GTM025 Real & Abstract Analysis | 487 | 643K | Book has no subsection structure |
| GTM061 Homotopy Theory | 764 | 1014K | Book has no subsection structure |
| GTM119 Algebraic Topology | 447 | 613K | Book has no subsection structure |
| GTM071 Riemann Surfaces | 379 | 528K | Book has no subsection structure |

## Detection Patterns (6 regex + Flash)

Regex patterns (in priority order):
1. `Part X: Title` — "Part 2: Elements of Logic"
2. `X.Y.Z Title` — subsubsection numbering
3. `X.Y Title` — subsection numbering  
4. `X. Title` — simple numbered sections (title ≥12 chars)
5. `§X.Y Title` — section symbol notation
6. `IX. Title` — bare Roman numerals (≥2 chars)
7. `ALL CAPS LINE` — all-caps standalone titles (≥15 chars)

Flash: sends complete OCR text (~150K tokens avg) with page markers. Cost ~¥4 for 28 books.

## Scripts

| Script | Purpose | Output |
|---|---|---|
| `stitch_by_section.py` | 4-tier detection + assembly | `stitched_sections/` |
| `stitch_chapters_v2.py` | Chapter-level detection (tier 2) | `stitched_v2/` |
| `flash_full_section.py` | Flash full-text bulk analysis | `section_indexes/_flash_full/` |

## Cost

| Step | Cost |
|---|---|
| Regex detection | ¥0 (local Python) |
| Flash full-text (28 books) | ~¥4 total |
| Size fallback | ¥0 (local Python) |
| **Total splitting cost** | **~¥4** for all 131 books |

## 10-Book Concept Extraction Test (2026-06-25)

| Book | Sections | Concepts | Domain | Cost |
|---|---|---|---|---|
| gtm004 Homological Algebra | 67 | 1,217 | Algebra | ~¥16 |
| gtm077 Algebraic Numbers | 38 | 805 | Number Theory | ~¥9 |
| gtm035 Complex Variables | 30 | 782 | Complex Analysis | ~¥7 |
| gtm027 General Topology | 37 | 763 | Topology | ~¥9 |
| gtm012 Advanced Analysis | 38 | 756 | Analysis | ~¥9 |
| gtm053 Mathematical Logic | 28 | 532 | Logic | ~¥7 |
| gtm033 Differential Topology | 35 | 512 | Geometry | ~¥8 |
| gtm095 Probability | 50 | 473 | Probability | ~¥12 |
| gtm015 Functional Analysis | 21 | 425 | Functional Analysis | ~¥5 |
| gtm044 Algebraic Geometry | 21 | 109 | Algebraic Geometry | ~¥5 |
| **Total** | **365** | **6,374** | | **~¥78.70** |

Key findings:
- **¥8/book average**, 17.5 concepts/section
- Each concept: concept.yaml + theorem.tex + introduce.en.md
- Dependencies inline in concept.yaml (required/recommended/suggested), semantic slug references
- No separate require.txt — all in YAML
- Network drops handled by automatic retry, 0 books lost
- 10 workflows × ~287 agents ran concurrently

## OCR Progress
- 171/1,565 books done (60,400 pages)
- Rate: 7.4 books/hour, ETA ~8 days for full collection

## Related
- [[ocr-lessons]] — OCR pipeline
- [[resilient-workflow]] — downstream Agent processing
- [[pipeline-v4-spec]] — concept extraction pipeline
- [[lesson-must-split-by-chapter]] — superseded by section splitting
