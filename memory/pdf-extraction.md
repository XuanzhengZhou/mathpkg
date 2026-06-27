---
name: pdf-extraction-strategy
description: "How to extract text from Springer PDFs — fitz vs pymupdf4llm, quality tiers"
metadata: 
  node_type: memory
  type: project
  originSessionId: bfc46d42-3656-4af8-b6a8-57278284f040
---

# PDF Extraction Strategy

## The Big Mistake

**pymupdf4llm.to_markdown() does NOT work on scanned+OCR PDFs.** It only extracts visible text, not hidden OCR layers. For 80% of our books (scanned pages with invisible OCR text), pymupdf4llm returned only image placeholders and front matter.

## Correct Approach

Use `fitz` (pymupdf) directly with `page.get_text("text")`:

```python
import fitz
doc = fitz.open("book.pdf")
text = doc[page_num].get_text("text")
```

This reads the hidden OCR text layer that pymupdf4llm misses.

## Quality Tiers (from 414-book study, ¥2 DeepSeek Flash evaluation)

| Tier | Score | Count | Action |
|---|---|---|---|
| Excellent (4-5) | Clean formulas, readable | 48 (12%) | Direct pipeline |
| Good (3) | Some OCR errors, LLM-fixable | 285 (69%) | Direct pipeline |
| Poor (1-2) | Garbled, unreadable | 81 (20%) | Local GLM-OCR on 5060Ti |

## Extraction Performance

- 409 books extracted in 8 minutes (52/min) with sequential fitz.get_text()
- 80 books have no text layer at all (pure image scans)
- Total output: 298 MB of Markdown

## Chapter Splitting

Use regex to find "CHAPTER X" markers after position 50000 (skip TOC):
```python
for m in re.finditer(r'(?:^|\n)\s*(CHAPTER\s+[IVX]+)\b', text, re.MULTILINE):
    if m.start() > 50000:
        # Real chapter start
```

10 chapters found in GTM073 (Hungerford), sizes 44K-221K chars.

## Critical: Memory Management

Comsol simulation was running (53 GB RSS). Must process one PDF at a time with `gc.collect()` between books. Don't use multiprocessing for PDF extraction — it's I/O bound, not CPU bound.
