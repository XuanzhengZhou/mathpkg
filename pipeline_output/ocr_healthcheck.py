#!/usr/bin/env python3
"""OCR 健康检查 — 每小时运行，检测 OOM 漏页、进度、失败书"""
import json, os, re, sys
from datetime import datetime
from pathlib import Path

OCR_DIR = Path('/home/a123/文档/mathpkg/pipeline_output/ocr_output')
CHECKPOINT = OCR_DIR / 'ocr_checkpoint.json'
LOG_FILE = Path('/home/a123/文档/mathpkg/pipeline_output/ocr_healthcheck.log')
MIN_CHARS_PER_PAGE = 50  # 低于此值视为空页

def log(msg):
    ts = datetime.now().strftime('%m-%d %H:%M')
    line = f"[{ts}] {msg}"
    print(line, flush=True)
    with open(LOG_FILE, 'a') as f:
        f.write(line + '\n')

def check():
    if not CHECKPOINT.exists():
        log("❌ checkpoint 文件不存在")
        return

    cp = json.loads(CHECKPOINT.read_text())
    total_books = len(cp)
    total_done_pages = sum(len(v) for v in cp.values())

    log(f"═══ 健康检查 ═══")
    log(f"  Checkpoint: {total_books} 本书, {total_done_pages} 页")

    # ── 1. 扫描所有已标记完成的书，找 OOM 漏页 ──
    oom_books = []
    empty_page_books = []

    for book_name in sorted(cp.keys()):
        book_dir = OCR_DIR / book_name.replace('.pdf', '')
        if not book_dir.exists():
            continue

        page_files = sorted(book_dir.glob('page_*.json'))
        if not page_files:
            continue

        done_pages = set(cp.get(book_name, []))
        total_oom = 0
        total_empty = 0
        max_page = 0

        for pf in page_files:
            try:
                data = json.loads(pf.read_text())
            except:
                continue
            pg = data.get('page', 0)
            max_page = max(max_page, pg)
            text = data.get('text', '')
            error = data.get('error', '')
            chars = len(re.sub(r'<\|endoftext\|>', '', text).strip())

            if 'oom' in error.lower() or 'out of memory' in error.lower():
                total_oom += 1
            if chars < MIN_CHARS_PER_PAGE and not error:
                total_empty += 1

        # 检查是否 checkpoint 认为完成但实际有大量空页/OOM
        if total_oom > 0:
            oom_books.append((book_name, total_oom, len(done_pages), max_page))
        elif total_empty > max_page * 0.3:  # >30% 空页
            empty_page_books.append((book_name, total_empty, len(done_pages), max_page))

    # ── 2. 报告 OOM 书 + 自动修复 ──
    if oom_books:
        log(f"  🔴 OOM 漏页书 ({len(oom_books)}本) — 自动清理并加入重跑队列:")
        for name, oom_count, done, max_pg in oom_books:
            short = name[:50]
            log(f"     {short}: {oom_count} OOM页")
            # 从 checkpoint 删除
            if name in cp:
                del cp[name]
            # 删除 OCR 目录
            book_dir = OCR_DIR / name.replace('.pdf', '')
            if book_dir.exists():
                import shutil
                shutil.rmtree(book_dir)
                log(f"       → 已清理，等待重新OCR")
        CHECKPOINT.write_text(json.dumps(cp, indent=2))
    else:
        log(f"  ✅ 无 OOM 漏页")

    # ── 3. 报告空页书 ──
    if empty_page_books:
        log(f"  🟡 大量空页书 ({len(empty_page_books)}本):")
        for name, empty_count, done, max_pg in empty_page_books:
            short = name[:50]
            pct = empty_count / max(max_pg, 1) * 100
            log(f"     {short}: {empty_count}/{max_pg} 空页 ({pct:.0f}%)")

    # ── 4. 进度统计 ──
    # 看最近完成的（字符数 > 0 的）
    recent_ok = 0
    recent_total_chars = 0
    for book_name in sorted(cp.keys()):
        book_dir = OCR_DIR / book_name.replace('.pdf', '')
        if not book_dir.exists():
            continue
        page_files = sorted(book_dir.glob('page_*.json'))
        if not page_files:
            continue
        total_chars = 0
        for pf in page_files:
            try:
                data = json.loads(pf.read_text())
                text = re.sub(r'<\|endoftext\|>', '', data.get('text', '')).strip()
                total_chars += len(text)
            except:
                pass
        if total_chars > 10000:
            recent_ok += 1
            recent_total_chars += total_chars

    # 总 OCR 页数
    total_ocr_pages = 0
    total_ocr_chars = 0
    for book_name in sorted(cp.keys()):
        book_dir = OCR_DIR / book_name.replace('.pdf', '')
        if not book_dir.exists():
            continue
        page_files = list(book_dir.glob('page_*.json'))
        for pf in page_files:
            try:
                data = json.loads(pf.read_text())
                text = re.sub(r'<\|endoftext\|>', '', data.get('text', '')).strip()
                total_ocr_chars += len(text)
            except:
                pass
        total_ocr_pages += len(page_files)

    avg_cpp = total_ocr_chars // max(total_ocr_pages, 1)
    # UTM 单独统计
    utm_books = [k for k in cp if 'UTM' in k]
    utm_pages = sum(len(cp[k]) for k in utm_books)
    gtm_books = [k for k in cp if 'GTM' in k]
    gtm_pages = sum(len(cp[k]) for k in gtm_books)
    log(f"  📊 进度: {recent_ok}本合格, {total_ocr_pages}页已OCR, 平均{avg_cpp}字/页")
    log(f"     GTM={len(gtm_books)}本/{gtm_pages}页, UTM={len(utm_books)}本/{utm_pages}页")

    # ── 5. 列出最近完成的5本的字符统计 ──
    recent = []
    for book_name in sorted(cp.keys()):
        book_dir = OCR_DIR / book_name.replace('.pdf', '')
        if not book_dir.exists(): continue
        page_files = sorted(book_dir.glob('page_*.json'))
        chars = 0
        for pf in page_files:
            try:
                data = json.loads(pf.read_text())
                text = re.sub(r'<\|endoftext\|>', '', data.get('text', '')).strip()
                chars += len(text)
            except: pass
        recent.append((book_name, chars, len(page_files)))
    recent.sort(key=lambda x: -x[1])  # sort by chars
    log(f"  📝 最近完成 (按字符数TOP5):")
    for name, chars, pages in recent[:5]:
        cpp = chars // max(pages, 1)
        log(f"     {name[:55]}: {chars//1000}K字, {cpp}字/p, {pages}p")

    log(f"═══ 检查完成 ═══\n")


if __name__ == '__main__':
    check()
