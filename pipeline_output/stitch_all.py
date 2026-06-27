#!/usr/bin/env python3
"""Batch stitch all OCR-complete books into chapter markdown."""
import json, os, re

OCR_DIR = '/home/a123/文档/mathpkg/pipeline_output/ocr_output'
STITCH_DIR = '/home/a123/文档/mathpkg/pipeline_output/stitched'

checkpoint = json.load(open(os.path.join(OCR_DIR, 'ocr_checkpoint.json')))
os.makedirs(STITCH_DIR, exist_ok=True)

stitched = 0

for book_name in sorted(os.listdir(OCR_DIR)):
    book_path = os.path.join(OCR_DIR, book_name)
    if not os.path.isdir(book_path): continue

    # Collect all pages
    pages = []
    for f in sorted(os.listdir(book_path)):
        if f.startswith('page_') and f.endswith('.json'):
            data = json.load(open(os.path.join(book_path, f)))
            pages.append(data.get('text', ''))

    if not pages:
        continue

    full_text = '\n\n'.join(pages)

    # Find CHAPTER markers (uppercase, after position 50000 to skip TOC)
    chapters = []
    for m in re.finditer(r'(?:^|\n)(CHAPTER\s+[IVX\d]+)\b', full_text, re.MULTILINE):
        if m.start() > max(50000, len(full_text) * 0.05):  # Skip TOC
            chapters.append((m.start(), m.group(1)))

    # If no chapters found (no TOC skip needed), try all uppercase CHAPTER markers
    if not chapters:
        for m in re.finditer(r'(?:^|\n)(CHAPTER\s+[IVX\d]+)\b', full_text, re.MULTILINE):
            chapters.append((m.start(), m.group(1)))

    # Dedup
    deduped = []
    for pos, title in chapters:
        if not deduped or pos - deduped[-1][0] > 2000:
            deduped.append((pos, title))

    # Save full text
    book_dir = os.path.join(STITCH_DIR, book_name)
    os.makedirs(book_dir, exist_ok=True)

    with open(os.path.join(book_dir, '_full.md'), 'w') as f:
        f.write(full_text)

    # Save chapters (skip tiny ones)
    valid_chapters = 0
    for i, (pos, title) in enumerate(deduped):
        end = deduped[i+1][0] if i+1 < len(deduped) else len(full_text)
        ch_text = full_text[pos:end]
        if len(ch_text) < 5000:  # Skip TOC/small sections
            continue
        fname = f'{valid_chapters+1:02d}_{title.replace(" ", "_")}.md'
        with open(os.path.join(book_dir, fname), 'w') as f:
            f.write(ch_text)
        valid_chapters += 1

    stitched += 1
    if stitched % 20 == 0:
        print(f'  {stitched} books...')

print(f'Stitched {stitched} books into {STITCH_DIR}')
