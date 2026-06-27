#!/usr/bin/env python3
"""Smart stitch: detect chapters using multiple patterns, clean endoftext, split properly."""
import json, os, re

OCR_DIR = '/home/a123/文档/mathpkg/pipeline_output/ocr_output'
STITCH_DIR = '/home/a123/文档/mathpkg/pipeline_output/stitched'

os.makedirs(STITCH_DIR, exist_ok=True)

# Chapter detection patterns (tried in order)
CHAPTER_PATTERNS = [
    (r'(?:^|\n)\s*CHAPTER\s+([IVX\d]+)\b', 'CHAPTER'),     # ALL CAPS
    (r'(?:^|\n)\s*Chapter\s+(\d+)\b', 'chapter'),           # Title case + number
    (r'(?:^|\n)\s*(\d+)\.\s+([A-Z][A-Za-z ]{10,})', 'numbered'),  # "1. Introduction to..."
]

stitched = 0

for book_name in sorted(os.listdir(OCR_DIR)):
    book_path = os.path.join(OCR_DIR, book_name)
    if not os.path.isdir(book_path): continue

    # Collect pages
    pages = []
    for f in sorted(os.listdir(book_path)):
        if f.startswith('page_') and f.endswith('.json'):
            pages.append(json.load(open(os.path.join(book_path, f))).get('text', ''))
    if not pages: continue

    full_text = '\n\n'.join(pages)
    # Clean endoftext tokens
    full_text = re.sub(r'<\|endoftext\|>', '', full_text)

    # Find chapters
    chapters = []
    skip_pos = int(min(15000, len(full_text) * 0.02))  # Skip cover only
    for pattern, ptype in CHAPTER_PATTERNS:
        if chapters: break  # Found with first pattern
        for m in re.finditer(pattern, full_text, re.MULTILINE):
            if m.start() > skip_pos:
                chapters.append(m.start())
        if len(chapters) >= 3: break  # Enough chapters found

    # Dedup
    deduped = []
    for pos in chapters:
        if not deduped or pos - deduped[-1] > 5000:
            deduped.append(pos)

    book_dir = os.path.join(STITCH_DIR, book_name)
    os.makedirs(book_dir, exist_ok=True)

    # Save full text (cleaned)
    with open(os.path.join(book_dir, '_full.md'), 'w') as f:
        f.write(full_text)

    if len(deduped) >= 2:
        # Split at chapter boundaries
        for i, pos in enumerate(deduped):
            end = deduped[i+1] if i+1 < len(deduped) else len(full_text)
            chunk = full_text[pos:end]
            if len(chunk) > 3000:
                fname = f'ch{i+1:02d}.md'
                with open(os.path.join(book_dir, fname), 'w') as f:
                    f.write(chunk)
    else:
        # No chapters found — split by size, ~80KB each
        chunk_size = 80000
        overlap = 3000
        start = int(max(0, skip_pos))
        i = 1
        while start < len(full_text):
            end = min(start + chunk_size, len(full_text))
            chunk = full_text[start:end]
            if len(chunk) > 5000:
                fname = f'ch{i:02d}.md'
                with open(os.path.join(book_dir, fname), 'w') as f:
                    f.write(chunk)
            start = end - overlap if end < len(full_text) else len(full_text)
            i += 1

    stitched += 1
    if stitched % 30 == 0:
        print(f'  {stitched} books...')

print(f'Stitched {stitched} books into {STITCH_DIR}')
