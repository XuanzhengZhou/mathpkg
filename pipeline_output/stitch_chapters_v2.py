#!/usr/bin/env python3
"""
stitch_chapters_v2.py — 从 OCR 逐页 JSON 检测章首页，按章组装 .md

策略 (按优先级):
  1. 显式章标题: CHAPTER X, Chapter X, Kapitel X, Chapitre X, 第X章
  2. 罗马数字标题: I. Title, II. Title (用于 GTM006, GTM005 等)
  3. 内容感知回退: 每 ~60KB 切分，优选空白/短页

TOC 排除: 一页上出现 ≥3 个 chapter 引用 → 判定为目录页
章首页验证: 后续页必须有足够内容 (≥300字)，且不是纯空白

用法:
  python3 stitch_chapters_v2.py                    # 处理全部书
  python3 stitch_chapters_v2.py --dry-run           # 只报告检测结果
  python3 stitch_chapters_v2.py --book "GTM006"     # 只处理匹配的书
"""

import json, os, re, sys, argparse
from dataclasses import dataclass, field
from typing import List, Tuple, Optional

OCR_DIR = '/home/a123/文档/mathpkg/pipeline_output/ocr_output'
STITCH_DIR = '/home/a123/文档/mathpkg/pipeline_output/stitched_v2'

os.makedirs(STITCH_DIR, exist_ok=True)

# ─── 章首页检测 ───────────────────────────────────────────────

@dataclass
class PageInfo:
    filename: str
    page_num: int
    text_raw: str
    text_clean: str          # 去除了 <|endoftext|>
    n_chars: int
    n_lines: int
    first_300: str
    lines: List[str]

def load_book_pages(book_dir: str) -> List[PageInfo]:
    """加载一本书的全部 OCR 页面"""
    pages = []
    for f in sorted(os.listdir(book_dir)):
        if not f.startswith('page_'):
            continue
        try:
            data = json.load(open(os.path.join(book_dir, f)))
        except (json.JSONDecodeError, IOError):
            continue
        text = data.get('text', '')
        text_clean = re.sub(r'<\|endoftext\|>', '', text).strip()
        lines = [l.strip() for l in text_clean.split('\n') if l.strip()]
        pages.append(PageInfo(
            filename=f,
            page_num=int(re.search(r'(\d+)', f).group(1)),
            text_raw=text,
            text_clean=text_clean,
            n_chars=len(text_clean),
            n_lines=len(lines),
            first_300=text_clean[:300],
            lines=lines,
        ))
    return pages


def find_toc_pages(pages: List[PageInfo]) -> set:
    """标记目录页: 一页上出现 ≥3 个不同 chapter 编号引用"""
    toc_indices = set()
    for i, p in enumerate(pages):
        refs = set()
        for m in re.finditer(r'(?i)\bchapter\s+([IVX\d]+)', p.text_clean):
            refs.add(m.group(1).upper())
        if len(refs) >= 3:
            # TOC 页及其前后各 2 页都标记
            for j in range(max(0, i-2), min(len(pages), i+3)):
                toc_indices.add(j)
    return toc_indices


def detect_chapter_starts(pages: List[PageInfo], toc_indices: set) -> List[Tuple[int, str, str]]:
    """
    检测章首页。
    返回: [(page_index, chapter_label, method), ...]
    """
    results = []

    for i, p in enumerate(pages):
        if i in toc_indices:
            continue
        if p.n_chars < 30:  # 太短，空白页或纯插图
            continue

        matched = None
        method = None

        # ── 策略1: 显式章标题标记 (页首 300 字符内) ──
        for pat, label_fmt in [
            (r'(?i)^\s*(CHAPTER)\s+([IVX\d]+)', 'heading_en'),
            (r'(?i)^\s*(Chapter)\s+(\d+)', 'heading_en_lc'),
            (r'(?i)^\s*(Kapitel)\s+(\d+)', 'heading_de'),
            (r'(?i)^\s*(Chapitre)\s+(\d+)', 'heading_fr'),
        ]:
            m = re.search(pat, p.first_300)
            if m:
                matched = f"{m.group(1)} {m.group(2)}"
                method = label_fmt
                break

        # 中文 "第X章"
        if not matched:
            m = re.search(r'第\s*([一二三四五六七八九十\d]+)\s*章', p.first_300)
            if m:
                matched = f"第{m.group(1)}章"
                method = 'heading_zh'

        # ── 策略2: 罗马数字标题 (如 "I. Review of Basic Algebra") ──
        if not matched:
            # 页首附近: 罗马数字 + 句号 + 大写字母开头的长标题
            m = re.search(r'(?:^|\n)\s*([IVX]{1,5})\.\s+([A-Z][A-Za-z\s]{10,80})', p.first_300)
            if m:
                roman = m.group(1)
                title = m.group(2).strip()
                # 过滤: 不能是常见短词 (I., V. 容易误匹配)
                if roman not in ('I', 'V', 'X', 'II', 'III', 'IV', 'VI', 'VII', 'VIII', 'IX', 'XI', 'XII'):
                    pass  # 不太可能是章节号
                elif len(roman) <= 4 and len(title) >= 15:
                    # 验证: 这是一页的开头或前一行很短
                    before_title = p.first_300[:m.start()]
                    if len(before_title.strip()) < 30:
                        matched = f"{roman}. {title[:50]}"
                        method = 'roman_heading'

        # ── 策略2b: 短页 + 全大写单行标题 ──
        if not matched and p.n_lines <= 6 and 50 <= p.n_chars <= 400:
            for line in p.lines[:2]:
                line = line.strip()
                if len(line) > 10 and line == line.upper() and not re.match(r'^[\d\s\.\,\-]+$', line):
                    matched = line[:60]
                    method = 'short_upper'
                    break

        # ── 验证: 章首页后面必须有内容 ──
        if matched:
            next_content = 0
            for j in range(i+1, min(len(pages), i+4)):
                if pages[j].n_chars > 50:
                    next_content += pages[j].n_chars
            if next_content >= 200:
                results.append((i, matched, method))

    return results


def deduplicate_chapters(chapters: List[Tuple[int, str, str]], pages: List[PageInfo]) -> List[Tuple[int, str, str]]:
    """去重: 同一个章标记连续多页只保留第一页"""
    if not chapters:
        return chapters
    deduped = [chapters[0]]
    for i in range(1, len(chapters)):
        prev_idx, prev_label, prev_method = deduped[-1]
        curr_idx, curr_label, curr_method = chapters[i]
        # 提取章编号
        prev_num = re.search(r'([IVX\d]+)', prev_label.split()[-1] if ' ' in prev_label else prev_label)
        curr_num = re.search(r'([IVX\d]+)', curr_label.split()[-1] if ' ' in curr_label else curr_label)
        # 如果间距 < 5 页且编号相同或连续 → 合并
        if curr_idx - prev_idx < 5:
            if prev_num and curr_num:
                # 保留 method 更可靠的那个
                if prev_method == 'heading_en' or prev_method == 'heading_zh':
                    continue  # 保留前一个
                elif curr_method == 'heading_en' or curr_method == 'heading_zh':
                    deduped[-1] = (curr_idx, curr_label, curr_method)  # 替换
                # 否则跳过
                continue
        deduped.append((curr_idx, curr_label, curr_method))
    return deduped


def validate_chapters(chapters: List[Tuple[int, str, str]], pages: List[PageInfo]) -> List[Tuple[int, str, str]]:
    """验证: 移除异常的章首页 (间距过大或过小)"""
    if len(chapters) < 2:
        return chapters

    # 计算章节间距分布
    gaps = []
    for i in range(1, len(chapters)):
        gaps.append(chapters[i][0] - chapters[i-1][0])

    if not gaps:
        return chapters

    avg_gap = sum(gaps) / len(gaps)
    # 过滤: 间距 < 5 页的可能不是真正的章首页(如 section 标题被误识别)
    # 或者间距 > avg_gap * 2.5 的可能缺失了中间的章
    valid = [chapters[0]]
    for i in range(1, len(chapters)):
        gap = chapters[i][0] - chapters[i-1][0]
        if gap < 3:
            # 太近了，保留 method 更可靠的
            prev_method = valid[-1][2]
            curr_method = chapters[i][2]
            if curr_method in ('heading_en', 'heading_zh') and prev_method not in ('heading_en', 'heading_zh'):
                valid[-1] = chapters[i]  # 替换
            # 否则跳过
        else:
            valid.append(chapters[i])

    return valid


# ─── 组装章节 ─────────────────────────────────────────────────

def assemble_chapters(
    pages: List[PageInfo],
    chapter_starts: List[Tuple[int, str, str]],
    book_dir: str,
    book_name: str,
):
    """将页面按章首页分组，写出 .md 文件"""
    book_out = os.path.join(STITCH_DIR, book_name)
    os.makedirs(book_out, exist_ok=True)

    # 确定章节边界
    boundaries = [c[0] for c in chapter_starts]  # 章首页索引

    # 处理前言 (第一章之前的内容)
    if boundaries and boundaries[0] > 0:
        preface_pages = pages[:boundaries[0]]
        preface_text = '\n\n'.join(p.text_clean for p in preface_pages if p.n_chars > 20)
        if len(preface_text) > 500:
            fname = 'ch00_preface.md'
            with open(os.path.join(book_out, fname), 'w') as f:
                f.write(preface_text)
            print(f"    → {fname} ({len(preface_text)} chars, front matter)")

    # 过滤: 去除太早出现且太短的伪章 (TOC 残留)
    # 规则: 如果第一个"章"在前 10% 页且 < 15KB, 合并到 preface
    filtered_starts = []
    n_pages = len(pages)
    for idx, (start_pos, label, method) in enumerate(chapter_starts):
        end_pos = chapter_starts[idx+1][0] if idx+1 < len(chapter_starts) else n_pages
        ch_size = sum(p.n_chars for p in pages[start_pos:end_pos] if p.n_chars > 20)
        if start_pos < n_pages * 0.08 and ch_size < 15000:
            print(f"    ⊘ 跳过疑似TOC伪章: {label} @ {pages[start_pos].filename} ({ch_size}字)")
            continue
        filtered_starts.append((start_pos, label, method))
    chapter_starts = filtered_starts

    # 组装每个章节
    chapter_files = []
    for idx, (start_pos, label, method) in enumerate(chapter_starts):
        end_pos = chapter_starts[idx+1][0] if idx+1 < len(chapter_starts) else len(pages)
        ch_pages = pages[start_pos:end_pos]
        ch_text = '\n\n'.join(p.text_clean for p in ch_pages if p.n_chars > 20)

        if len(ch_text) < 3000:
            continue  # 太短的忽略

        # 提取章编号 (按页面顺序编号,不按 Roman numeral)
        num_str = f"{idx+1:02d}"

        # 安全文件名: 去除非法字符
        safe_label = re.sub(r'[^\w\s\-]', '', label)[:50].strip()
        fname = f'ch{num_str}_{safe_label}.md' if safe_label else f'ch{num_str}.md'
        fpath = os.path.join(book_out, fname)

        with open(fpath, 'w') as f:
            f.write(ch_text)

        chapter_files.append({
            'file': fname,
            'label': label,
            'method': method,
            'pages': f"{pages[start_pos].filename}–{pages[end_pos-1].filename}",
            'chars': len(ch_text),
        })

    # 写 _manifest.json
    manifest = {
        'book_name': book_name,
        'total_pages': len(pages),
        'chapters_detected': len(chapter_starts),
        'chapters_written': len(chapter_files),
        'detection_methods': list(set(c['method'] for c in chapter_files)),
        'chapter_files': chapter_files,
    }
    with open(os.path.join(book_out, '_manifest.json'), 'w') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    return manifest


# ─── 主流程 ───────────────────────────────────────────────────

def process_book(book_name: str, dry_run: bool = False) -> Optional[dict]:
    book_dir = os.path.join(OCR_DIR, book_name)
    if not os.path.isdir(book_dir):
        return None

    pages = load_book_pages(book_dir)
    if len(pages) < 20:
        return None

    toc_indices = find_toc_pages(pages)
    raw_chapters = detect_chapter_starts(pages, toc_indices)
    deduped = deduplicate_chapters(raw_chapters, pages)
    validated = validate_chapters(deduped, pages)

    # 如果检测到的章数太少 (< 3)，尝试回退策略
    if len(validated) < 3:
        # 回退1: 去掉 TOC 过滤再试
        raw2 = detect_chapter_starts(pages, set())
        deduped2 = deduplicate_chapters(raw2, pages)
        validated2 = validate_chapters(deduped2, pages)
        if len(validated2) > len(validated):
            validated = validated2
            print(f"    ⚠ 回退: 放宽 TOC 过滤 → {len(validated2)} 章")

    # 回退2: 如果还是太少，降低 roman_heading 的阈值
    if len(validated) < 3:
        # 放宽策略: 允许更多 roman_heading 匹配
        extra = []
        for i, p in enumerate(pages):
            if i in toc_indices or p.n_chars < 20:
                continue
            if any(i == v[0] for v in validated):
                continue
            m = re.search(r'(?:^|\n)\s*([IVX]{1,5})\.\s+([A-Z][A-Za-z\s]{8,})', p.first_300)
            if m:
                extra.append((i, f"{m.group(1)}. {m.group(2).strip()[:50]}", 'roman_loose'))
        if len(validated) + len(extra) >= 3:
            validated = sorted(validated + extra, key=lambda x: x[0])

    # 仍然太少 → 按大小切分
    if len(validated) < 3:
        # 按 ~60KB 切分，边界选在短页处
        print(f"    ⚠ 未检测到足够的章标记，使用大小回退切分")
        validated = fallback_split(pages)

    if dry_run:
        print(f"\n{'='*60}")
        print(f"书: {book_name}")
        print(f"总页: {len(pages)}, TOC页: {len(toc_indices)}")
        print(f"检测方法: {[m for _,_,m in validated]}")
        print(f"检测到 {len(validated)} 章:")
        for idx, label, method in validated:
            p = pages[idx]
            print(f"  {p.filename} [{method}] {label} ({p.n_chars}字)")
        if len(validated) < 2:
            print(f"  ⚠ 章节数过少，可能需要人工检查")
        return {'chapters': len(validated), 'methods': [m for _,_,m in validated]}

    manifest = assemble_chapters(pages, validated, book_dir, book_name)
    print(f"  {book_name}: {manifest['chapters_written']} 章 → {book_dir.replace(OCR_DIR, STITCH_DIR)}")
    return manifest


def fallback_split(pages: List[PageInfo]) -> List[Tuple[int, str, str]]:
    """内容感知切分: 每 ~60KB 一块，优先在短页处切"""
    target_size = 60000
    chapters = []
    cum_size = 0
    last_cut = 0

    for i, p in enumerate(pages):
        cum_size += p.n_chars
        if cum_size >= target_size and i > last_cut + 5:
            # 在最近的短页处切 (前 5 页内找最短的)
            best_cut = i
            best_score = 999999
            for j in range(i-5, i+1):
                if j > last_cut and pages[j].n_chars < best_score:
                    best_score = pages[j].n_chars
                    best_cut = j
            chapters.append((best_cut, f"Part {len(chapters)+1}", 'size_fallback'))
            last_cut = best_cut
            cum_size = 0

    if len(chapters) < 2 and pages:
        # 至少切 2 块
        mid = len(pages) // 2
        chapters = [
            (10, "Part 1", 'size_fallback'),
            (mid, "Part 2", 'size_fallback'),
        ]

    return chapters


def main():
    parser = argparse.ArgumentParser(description='从 OCR 逐页产物按章组装 .md')
    parser.add_argument('--dry-run', action='store_true', help='只报告检测结果，不写文件')
    parser.add_argument('--book', type=str, help='只处理书名包含此字符串的书')
    parser.add_argument('--limit', type=int, default=0, help='最多处理 N 本')
    args = parser.parse_args()

    books = sorted(os.listdir(OCR_DIR))
    processed = 0
    stats = []

    for book_name in books:
        if args.book and args.book.lower() not in book_name.lower():
            continue

        book_dir = os.path.join(OCR_DIR, book_name)
        if not os.path.isdir(book_dir):
            continue
        pages_files = [f for f in os.listdir(book_dir) if f.startswith('page_')]
        if len(pages_files) < 20:
            continue

        result = process_book(book_name, dry_run=args.dry_run)
        if result:
            stats.append({'book': book_name, **result})
        processed += 1
        if args.limit and processed >= args.limit:
            break

    # 汇总
    if stats:
        total_ch = sum(s['chapters'] for s in stats)
        methods_used = set()
        for s in stats:
            for m in s.get('methods', []):
                methods_used.add(m)
        print(f"\n{'='*60}")
        print(f"汇总: {len(stats)} 本书, {total_ch} 章")
        print(f"检测方法: {methods_used}")
        low_ch_books = [s for s in stats if s['chapters'] < 2]
        if low_ch_books:
            print(f"⚠ 章节数 <2 的书 ({len(low_ch_books)}):")
            for s in low_ch_books:
                print(f"  {s['book'][:60]}: {s['chapters']} 章 [{', '.join(s.get('methods',[]))}]")


if __name__ == '__main__':
    main()
