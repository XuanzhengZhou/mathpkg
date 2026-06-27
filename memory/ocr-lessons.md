---
name: ocr-strategy-lessons
description: "GLM-OCR vs fitz vs digital PDF — quality comparison, per-page checkpoint, batch optimization"
metadata: 
  node_type: memory
  type: project
  originSessionId: 32b0208b-f009-4db0-9b54-c8a7af2b3275
---

# OCR Strategy Lessons

## Quality Comparison (2026-06-24)

Tested on GTM073 Algebra (Hungerford):

| Method | Quality | Math | Example |
|---|---|---|---|
| fitz.get_text (scanned PDF) | ❌ Poor | Garbled | `IGI = [G : H]IHI` `lal ofa E G` |
| fitz.get_text (digital PDF) | ⚠️ Mediocre | Lost | `"~i of C9(W)"` `"t9(V)"` — raw glyph codes |
| **GLM-OCR** | ✅ Best | LaTeX | `$f(e_G) = e_H$` `$Z \rightarrow Z_m$` |

**Key finding: Even digital PDFs degrade math symbols.** Vector glyphs don't map 1:1 to Unicode — `∫` may be stored as character `C9`. GLM-OCR is a visual model; it sees the rendered image and outputs LaTeX, avoiding glyph encoding issues entirely.

**Conclusion: All 1,565 books → GLM-OCR. No exceptions.**

## GLM-OCR Performance

- GPU: RTX 5060 Ti 16GB
- Model: ZhipuAI GLM-OCR (2.2GB VRAM)
- Speed: ~22 pages/min (batch=2), ~74 pages/min (batch=8 + pre-rendering)
- Real-world rate: ~5.7 books/hour
- Full collection: ~1,565 books × 350 avg pages = ~548,000 pages → ~10 days

## Optimization History

1. v1: batch=2 → GPU 49% utilization → 30 pages/min
2. v2: batch=8 + threaded pre-rendering → GPU 72% → 74 pages/min
3. v3 (current): batch=8 + pre-render + full list → GPU 95% → 5.7 books/h

## Checkpoint Design

- Per-page JSON files (`page_0001.json`, `page_0002.json`, ...)
- `ocr_checkpoint.json`: `{book_name: [done_page_numbers]}`
- Updated after every batch (every 2 pages)
- Survives crash/restart: skipped pages instant on resume
- Book directory: `ocr_output/<book_name>/`

## Related
- [[pdf-extraction]] — Phase 0 fitz extraction history
