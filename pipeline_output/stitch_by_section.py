#!/usr/bin/env python3
"""
stitch_by_section.py — 从 OCR 逐页 JSON 检测 section 标记，按 section 组装 .md

与 stitch_chapters_v2.py 的区别:
  - 检测粒度更细: §1, 1.1, 2.3.1 等 section/subsection 标记
  - 每 section 通常 5-20 页，适合单 Agent 处理
  - 保留原书的 section 编号结构

用法:
  python3 stitch_by_section.py --dry-run --book "GTM006"
  python3 stitch_by_section.py --dry-run --test10
"""

import json, os, re, sys, argparse

OCR_DIR = '/home/a123/文档/mathpkg/pipeline_output/ocr_output'
STITCH_DIR = '/home/a123/文档/mathpkg/pipeline_output/stitched_sections'

os.makedirs(STITCH_DIR, exist_ok=True)

TEST_10 = ['GTM002','GTM006','GTM022','GTM046','GTM050',
           'GTM058','GTM065','GTM099','GTM116','GTM124']

# ─── Section 检测 ────────────────────────────────────────────

SECTION_PATTERNS = [
    # 优先级从高到低
    (r'(?:^|\n)\s*Part\s+([IVX\d]+)[\.:]\s*([A-Z].*)', 'part_label'),            # "Part 2: Elements"
    (r'(?:^|\n)\s*(\d+\.\d+\.\d+)\s+([A-Z].*)', 'subsubsection'),
    (r'(?:^|\n)\s*(\d+\.\d+)\s+([A-Z][A-Za-z\s]{8,})', 'subsection'),
    (r'(?:^|\n)\s*(\d+)\.[ \t]+([A-Z][A-Za-z\s]{12,})', 'numbered_section'),
    (r'(?:^|\n)\s*§\s*(\d+\.?\d*)\s*\.?\s+([A-Z].*)', 'section_symbol'),
    (r'(?:^|\n)\s*§\s*(\d+)\s*$', 'section_symbol_bare'),
    (r'(?:^|\n)\s*([IVX]{2,8})\.\s+([A-Z][A-Za-z\s]{8,})', 'bare_roman'),        # "IX. Designs"
    (r'(?:^|\n)\s*([A-Z][A-Z\s]{15,70})\s*\n', 'allcaps_title'),                  # "RADON-RIESZ THEOREM"
]

def load_pages(book_dir: str):
    """加载 OCR 页面"""
    pages = []
    for f in sorted(os.listdir(book_dir)):
        if not f.startswith('page_'):
            continue
        try:
            data = json.load(open(os.path.join(book_dir, f)))
        except:
            continue
        text = data.get('text', '')
        text_clean = re.sub(r'<\|endoftext\|>', '', text).strip()
        lines = [l.strip() for l in text_clean.split('\n') if l.strip()]
        pages.append({
            'filename': f,
            'page_num': int(re.search(r'(\d+)', f).group(1)),
            'text': text_clean,
            'n_chars': len(text_clean),
            'n_lines': len(lines),
            'first_300': text_clean[:300],
            'lines': lines,
        })
    return pages


def find_toc_sections(pages):
    """标记目录页: 一页上出现 ≥3 个 numbered section 引用"""
    toc_indices = set()
    for i, p in enumerate(pages):
        refs = 0
        for m in re.finditer(r'(?:^|\n)\s*(\d+\.\d+|\d+\.)\s', p['text']):
            refs += 1
        if refs >= 5:
            for j in range(max(0, i-2), min(len(pages), i+3)):
                toc_indices.add(j)
    return toc_indices


def detect_sections(pages, toc_indices, min_chars=2000):
    """检测 section 首页。返回 [(page_index, section_id, method), ...]"""
    results = []

    for i, p in enumerate(pages):
        if i in toc_indices:
            continue
        if p['n_chars'] < 30:
            continue

        matched = None
        method = None

        for pat, pname in SECTION_PATTERNS:
            m = re.search(pat, p['first_300'])
            if m:
                if len(m.groups()) >= 2:
                    matched = f"{m.group(1)} {m.group(2).strip()[:60]}"
                else:
                    matched = m.group(0).strip()[:60]
                method = pname
                break

        # 也检查全页文本(前 1000 字符), 因为有些 section 标记不在页首
        if not matched:
            for pat, pname in SECTION_PATTERNS:
                m = re.search(pat, p['text'][:1000])
                if m:
                    if len(m.groups()) >= 2:
                        matched = f"{m.group(1)} {m.group(2).strip()[:60]}"
                    else:
                        matched = m.group(0).strip()[:60]
                    method = pname + '_body'
                    break

        if matched:
            # 验证: 后面有足够内容
            next_chars = sum(pages[j]['n_chars'] for j in range(i+1, min(len(pages), i+5)) if pages[j]['n_chars'] > 30)
            if next_chars >= min_chars:
                results.append((i, matched, method))

    return results


def dedup_sections(sections, pages):
    """去重: 相同 section 号的多页只保留第一页"""
    if not sections:
        return sections
    deduped = [sections[0]]
    for i in range(1, len(sections)):
        prev_idx, prev_label, prev_method = deduped[-1]
        curr_idx, curr_label, curr_method = sections[i]
        # 提取 section 编号
        prev_num = prev_label.split()[0] if prev_label.split() else ''
        curr_num = curr_label.split()[0] if curr_label.split() else ''
        # 如果间距 < 3 页且编号前缀相同 → 合并
        if curr_idx - prev_idx < 3 and prev_num and curr_num:
            prev_prefix = re.match(r'(\d+)', prev_num)
            curr_prefix = re.match(r'(\d+)', curr_num)
            if prev_prefix and curr_prefix and prev_prefix.group(1) == curr_prefix.group(1):
                if prev_method.startswith('section_symbol') and not curr_method.startswith('section_symbol'):
                    continue  # 保留 section_symbol
                elif not prev_method.startswith('section_symbol') and curr_method.startswith('section_symbol'):
                    deduped[-1] = (curr_idx, curr_label, curr_method)
                continue
        deduped.append((curr_idx, curr_label, curr_method))

    return deduped


def assemble_sections(pages, sections, book_dir, book_name):
    """按 section 边界写出 .md"""
    book_out = os.path.join(STITCH_DIR, book_name)
    os.makedirs(book_out, exist_ok=True)

    # 过滤太短的 section
    valid = []
    for idx, (start_pos, label, method) in enumerate(sections):
        end_pos = sections[idx+1][0] if idx+1 < len(sections) else len(pages)
        ch_size = sum(p['n_chars'] for p in pages[start_pos:end_pos] if p['n_chars'] > 20)
        if ch_size >= 2000:
            valid.append((start_pos, label, method))

    # 前言
    if valid and valid[0][0] > 5:
        preface_pages = pages[:valid[0][0]]
        preface_text = '\n\n'.join(p['text'] for p in preface_pages if p['n_chars'] > 20)
        if len(preface_text) > 500:
            with open(os.path.join(book_out, 's00_preface.md'), 'w') as f:
                f.write(preface_text)

    # 组装
    files = []
    for idx, (start_pos, label, method) in enumerate(valid):
        end_pos = valid[idx+1][0] if idx+1 < len(valid) else len(pages)
        ch_pages = pages[start_pos:end_pos]
        ch_text = '\n\n'.join(p['text'] for p in ch_pages if p['n_chars'] > 20)

        if len(ch_text) < 2000:
            continue

        num_str = f"{idx+1:03d}"
        safe = re.sub(r'[^\w\s\.\-]', '', label)[:60].strip().replace(' ', '_')
        fname = f's{num_str}_{safe}.md'
        fpath = os.path.join(book_out, fname)

        with open(fpath, 'w') as f:
            f.write(ch_text)

        files.append({
            'file': fname,
            'label': label,
            'method': method,
            'pages': f"{pages[start_pos]['filename']}–{pages[end_pos-1]['filename']}",
            'chars': len(ch_text),
        })

    # manifest
    manifest = {
        'book_name': book_name,
        'total_pages': len(pages),
        'sections_detected': len(valid),
        'sections_written': len(files),
        'method': 'section',
        'files': files,
    }
    with open(os.path.join(book_out, '_manifest.json'), 'w') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    return manifest


def process_book(book_name, dry_run=False):
    book_dir = os.path.join(OCR_DIR, book_name)
    if not os.path.isdir(book_dir):
        return None

    pages = load_pages(book_dir)
    if len(pages) < 20:
        return None

    toc = find_toc_sections(pages)
    sections = detect_sections(pages, toc)
    deduped = dedup_sections(sections, pages)

    # ── 回退策略: 用 页/10 规律判断 section 数是否合理 ──
    expected = max(3, len(pages) // 10)
    min_acceptable = max(3, expected // 2)

    method_used = 'section'
    if len(deduped) < min_acceptable:
        # 先尝试 Chapter 检测
        chapters = _detect_chapters_fallback(pages, book_dir)
        if chapters is not None and len(chapters) > len(deduped):
            deduped = chapters
            method_used = 'chapter_fallback'

    # ── 回退策略 2: 尝试 Flash 全量文本分析 ──
    # Flash 语义边界远优于 size fallback，接受标准放宽
    flash_min = max(3, len(pages) // 30)
    if len(deduped) < min_acceptable:
        flash_boundaries = _try_flash_fallback(book_dir, book_name, len(pages))
        if flash_boundaries and len(flash_boundaries) >= flash_min:
            deduped = [(p-1, f"Section {i+1}", 'flash_full') for i, p in enumerate(flash_boundaries) if 1 <= p <= len(pages)]
            method_used = 'flash_full'
            qualifier = '⚠ 章级' if len(deduped) < min_acceptable else ''
            print(f"    ✅ Flash 全量分析: {len(deduped)} sections {qualifier}")
            # Flash 成功则跳过后续 size fallback
            min_acceptable = 0  # 不再触发 size fallback

    # ── 回退策略 3: 仍不够 → 大小切分 ──
    if len(deduped) < min_acceptable:
        ocr_chars = sum(p['n_chars'] for p in pages)
        print(f"    ⚠ 所有策略均失败 (regex/chapter/flash)，OCR {ocr_chars/1000:.0f}K 字符，使用大小回退...")
        deduped = _size_fallback(pages)
        method_used = 'size_fallback'

    if dry_run:
        print(f"\n{'='*60}")
        print(f"书: {book_name}")
        print(f"总页: {len(pages)}, 策略: {method_used}")
        if method_used != 'section':
            print(f"  ⚠ 使用了回退: {method_used}")
        methods = set(m for _,_,m in deduped)
        print(f"检测方法: {methods}")
        print(f"最终 {len(deduped)} 个 chunks:")
        for idx, label, method in deduped[:15]:
            print(f"  {pages[idx]['filename']} [{method}] {label} ({pages[idx]['n_chars']}字)")
        if len(deduped) > 15:
            print(f"  ... 还有 {len(deduped)-15} 个")
        return {'sections': len(deduped), 'methods': list(methods), 'strategy': method_used}

    manifest = assemble_sections(pages, deduped, book_dir, book_name)
    manifest['method'] = method_used
    # rewrite manifest with updated method
    with open(os.path.join(STITCH_DIR, book_name, '_manifest.json'), 'w') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"  {book_name[:50]}: {manifest['sections_written']} chunks [{method_used}]")
    return manifest


def _detect_chapters_fallback(pages, book_dir):
    """复用 stitch_chapters_v2 的 Chapter 检测逻辑作为回退"""
    try:
        # 使用 stitch_chapters_v2 中的检测函数
        import importlib.util, sys
        spec = importlib.util.spec_from_file_location(
            'stitch_v2',
            os.path.join(os.path.dirname(__file__), 'stitch_chapters_v2.py')
        )
        v2 = importlib.util.module_from_spec(spec)
        sys.modules['stitch_v2'] = v2
        spec.loader.exec_module(v2)

        # 构建 PageInfo 对象（v2 需要的格式）
        PageInfo = v2.PageInfo
        v2_pages = []
        for p in pages:
            v2_pages.append(PageInfo(
                filename=p['filename'],
                page_num=p['page_num'],
                text_raw=p['text'],
                text_clean=p['text'],
                n_chars=p['n_chars'],
                n_lines=p['n_lines'],
                first_300=p['first_300'],
                lines=p['lines'],
            ))

        toc = v2.find_toc_pages(v2_pages)
        raw = v2.detect_chapter_starts(v2_pages, toc)
        deduped = v2.deduplicate_chapters(raw, v2_pages)
        validated = v2.validate_chapters(deduped, v2_pages)

        # 放宽条件重试
        if len(validated) < 3:
            raw2 = v2.detect_chapter_starts(v2_pages, set())
            deduped2 = v2.deduplicate_chapters(raw2, v2_pages)
            validated2 = v2.validate_chapters(deduped2, v2_pages)
            if len(validated2) > len(validated):
                validated = validated2

        return validated
    except Exception as e:
        print(f"    Chapter fallback failed: {e}")
        return None


def _size_fallback(pages, target_size=60000):
    """按 ~60KB 切分，边界选在短页处"""
    chunks = []
    cum_size = 0
    last_cut = 0

    for i, p in enumerate(pages):
        cum_size += p['n_chars']
        if cum_size >= target_size and i > last_cut + 5:
            best_cut = i
            best_score = 999999
            for j in range(max(last_cut+1, i-5), min(len(pages), i+1)):
                if pages[j]['n_chars'] < best_score:
                    best_score = pages[j]['n_chars']
                    best_cut = j
            chunks.append((best_cut, f"Part {len(chunks)+1}", 'size_fallback'))
            last_cut = best_cut
            cum_size = 0

    if len(chunks) < 2 and len(pages) > 10:
        mid = len(pages) // 2
        chunks = [
            (max(5, mid-20), "Part 1", 'size_fallback'),
            (mid, "Part 2", 'size_fallback'),
        ]

    return chunks


def _try_flash_fallback(book_dir, book_name, n_pages):
    """尝试读取 Flash 全量分析结果"""
    import json
    # 从 OCR 目录名提取 book_key
    book_key = None
    for key in ['GTM025','GTM035','GTM043','GTM046','GTM047','GTM052','GTM054',
                'GTM055','GTM056','GTM060','GTM061','GTM071','GTM074','GTM078',
                'GTM079','GTM080','GTM082','GTM101','GTM102','GTM106','GTM107',
                'GTM108','GTM115','GTM116','GTM118','GTM119','GTM124','GTM127']:
        if key in book_name:
            book_key = key
            break
    if not book_key:
        return None

    result_path = f"/home/a123/文档/mathpkg/pipeline_output/section_indexes/_flash_full/{book_key}.json"
    if os.path.exists(result_path):
        try:
            data = json.load(open(result_path))
            boundaries = data.get('boundaries', [])
            if len(boundaries) >= 3:
                return boundaries
        except:
            pass
    return None


def main():
    parser = argparse.ArgumentParser(description='从 OCR 逐页产物按 section 组装 .md')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--test10', action='store_true', help='只处理 10 本测试书')
    parser.add_argument('--book', type=str)
    args = parser.parse_args()

    books = sorted(os.listdir(OCR_DIR))

    if args.test10:
        books = [b for b in books if any(tb in b for tb in TEST_10)]
        print(f"=== Section 级拆分: 10 本测试书 ===\n")

    if args.book:
        books = [b for b in books if args.book.lower() in b.lower()]

    stats = []
    for book_name in books:
        book_dir = os.path.join(OCR_DIR, book_name)
        if not os.path.isdir(book_dir):
            continue
        if len([f for f in os.listdir(book_dir) if f.startswith('page_')]) < 20:
            continue

        result = process_book(book_name, dry_run=args.dry_run)
        if result:
            stats.append({'book': book_name[:60], **result})

    if stats:
        total = sum(s['sections'] for s in stats)
        print(f"\n汇总: {len(stats)} 本书, {total} sections, 平均 {total/len(stats):.1f}/书")


if __name__ == '__main__':
    main()
