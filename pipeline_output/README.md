# Pipeline Tools

Python scripts for the mathpkg pipeline.

## Section Splitting
- **stitch_by_section.py**: 4-tier section detection (regex→chapter→Flash→size)
- **stitch_chapters_v2.py**: Chapter-level fallback
- **flash_full_section.py**: DeepSeek Flash full-text section boundary detection

## OCR
- **ocr_healthcheck.py**: Hourly OCR health monitor with auto-recovery

## Mathlib4
- **grep_mathlib4.py**: Multi-strategy grep against Mathlib4 (204K entries)
- **mathlib4_index.json** (not in repo, 50MB): Full parse of 8,169 .lean files

## Concept Extraction
- **concepts_v7/**: 6,374 extracted concepts (concept.yaml + theorem.tex + introduce.en.md)

