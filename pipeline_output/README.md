# Pipeline Tools

Python scripts for the mathpkg pipeline.

## Section Splitting
- **stitch_by_section.py**: 4-tier section detection (regex→chapter→Flash→size)
- **stitch_chapters_v2.py**: Chapter-level fallback
- **flash_full_section.py**: DeepSeek Flash full-text section boundary detection

## OCR
- **ocr_healthcheck.py**: Hourly OCR health monitor with auto-recovery
- **ocr_output/**: Per-page OCR JSON (runtime, growing)

## Mathlib4
- **grep_mathlib4.py**: Multi-strategy grep against Mathlib4 (204K entries)

## Production Output
- **math_pkg_release/**: 正式版文件夹
  - `concepts_v7/`: 6,374 extracted concepts (concept.yaml + theorem.tex + introduce.en.md)
- **stitched_sections/**: Section-split .md files (172 books)
- **data/**: Reference data (Mathlib4 index, book lists)

## Archived
- `../legacy/pipeline_scripts/`: Historical one-off extraction scripts
- `../legacy/outputs/`: Old stitch outputs and section indexes
