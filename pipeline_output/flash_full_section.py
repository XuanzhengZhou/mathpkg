#!/usr/bin/env python3
"""用 DeepSeek Flash 分析完整 OCR 文本，识别 section 边界。全量文本，约 ¥12/28本。"""
import json, os, re, time, requests

API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
API_URL = "https://api.deepseek.com/v1/chat/completions"
OCR_DIR = "/home/a123/文档/mathpkg/pipeline_output/ocr_output"
RESULT_DIR = "/home/a123/文档/mathpkg/pipeline_output/section_indexes/_flash_full"
os.makedirs(RESULT_DIR, exist_ok=True)

# 用之前 stitch_by_section 的 dry-run 结果筛选出 size_fallback 的 28 本
REMAINING = [
    'GTM025','GTM035','GTM043','GTM046','GTM047','GTM052','GTM054',
    'GTM055','GTM056','GTM060','GTM061','GTM071','GTM074','GTM078',
    'GTM079','GTM080','GTM082','GTM101','GTM102','GTM106','GTM107',
    'GTM108','GTM115','GTM116','GTM118','GTM119','GTM124','GTM127'
]

total_cost = 0

for book_key in REMAINING:
    # 查找 OCR 目录
    bd = None
    for b in sorted(os.listdir(OCR_DIR)):
        if book_key in b and os.path.isdir(os.path.join(OCR_DIR, b)):
            bd = os.path.join(OCR_DIR, b)
            break
    if not bd:
        print(f"  {book_key}: OCR 目录未找到")
        continue

    result_path = os.path.join(RESULT_DIR, f"{book_key}.json")
    if os.path.exists(result_path):
        existing = json.load(open(result_path))
        print(f"  {book_key[:30]}: 已有 {existing['sections']} sections (跳过)")
        continue

    files = sorted([f for f in os.listdir(bd) if f.startswith('page_')])
    n_pages = len(files)

    # 组装全量文本
    pages_text = []
    for i, f in enumerate(files):
        data = json.load(open(os.path.join(bd, f)))
        text = data.get('text', '')
        text = re.sub(r'<\|endoftext\|>', '', text).strip()
        if text:
            pages_text.append(f"<!-- PAGE {i+1} -->\n{text}")

    full_text = '\n\n'.join(pages_text)
    n_chars = len(full_text)

    # 太小的跳过（OCR 质量太差）
    if n_chars < 5000:
        print(f"  {book_key[:30]}: OCR 仅 {n_chars} 字符，跳过（OCR 太差）")
        continue

    # 目标 section 数
    target_sections = max(10, min(50, n_pages // 8))

    prompt = f"""Given the FULL OCR text of a {n_pages}-page math textbook (pages marked <!-- PAGE N -->), identify ALL section boundaries.

A section is a sub-chapter unit, typically 5-20 pages. Look for:
- Numbered headings like "1. Title", "2. Basic Properties" at page start
- ALL-CAPS standalone lines that look like section titles
- CHAPTER headers
- § symbol sections
- Logical topic breaks (new major topic starts)

Target: around {target_sections} sections.
Do NOT split at individual theorem/lemma/definition/exercise numbers — those are too fine.

Output ONLY a JSON array of section-start page numbers: [12, 35, 68, ...]

TEXTBOOK:

{full_text}"""

    payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 8192,
        "temperature": 0.0,
        "stream": False
    }
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

    try:
        print(f"  {book_key[:30]}: {n_pages}p, {n_chars/1000:.0f}K chars → Flash...", end=' ', flush=True)
        resp = requests.post(API_URL, json=payload, headers=headers, timeout=600)
        data = resp.json()

        if "choices" not in data:
            print(f"API Error: {data.get('error',{}).get('message','?')[:80]}")
            continue

        reply = data["choices"][0]["message"]["content"]
        m = re.search(r'\[[\d,\s\n]+\]', reply)

        if m:
            pages = sorted(set(int(p) for p in json.loads(m.group(0)) if 1 <= p <= n_pages))
            if len(pages) >= 3:
                gaps = [pages[i+1]-pages[i] for i in range(len(pages)-1)] if len(pages) > 1 else [0]
                avg_gap = sum(gaps) / len(gaps) if gaps else 0
                print(f"{len(pages)} sections, avg {avg_gap:.0f}p")

                result = {"book": book_key, "pages": n_pages, "sections": len(pages),
                          "avg_pages_per_section": avg_gap, "boundaries": pages}
                with open(result_path, "w") as f:
                    json.dump(result, f, indent=2)
            else:
                print(f"仅 {len(pages)} sections → 回退 size split")
        else:
            print(f"解析失败: {reply[:80]}")

        usage = data.get("usage", {})
        cost = (usage.get("prompt_tokens", 0) * 1 + usage.get("completion_tokens", 0) * 2) / 1_000_000
        total_cost += cost

    except Exception as e:
        print(f"Exception: {e}")

    time.sleep(1)  # rate limit

print(f"\n总成本: ¥{total_cost:.4f}")
