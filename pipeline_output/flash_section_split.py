#!/usr/bin/env python3
"""用 DeepSeek Flash 分析页面索引，识别 section 边界。每本约 ¥0.01-0.03。"""
import json, os, re, time, requests

API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
API_URL = "https://api.deepseek.com/v1/chat/completions"

INDEX_DIR = "/home/a123/文档/mathpkg/pipeline_output/section_indexes"
RESULT_DIR = os.path.join(INDEX_DIR, "_results")
os.makedirs(RESULT_DIR, exist_ok=True)

PROMPT_TEMPLATE = """You are analyzing a math textbook page index. Each line is "pNNNN: first 150 chars".

Identify ALL section boundaries at the sub-chapter level.
- A section typically starts with a numbered heading, ALL-CAPS title, or structural marker
- Target: roughly 10-40 sections per book, each 5-15 pages
- Output ONLY a JSON array of page numbers: [12, 30, 48, ...]"""

total_cost = 0
processed = 0

for fname in sorted(os.listdir(INDEX_DIR)):
    if not fname.endswith('.txt') or fname.startswith('_results'):
        continue

    fpath = os.path.join(INDEX_DIR, fname)
    book_key = fname.replace('.txt', '')

    # 跳过已处理的
    result_path = os.path.join(RESULT_DIR, f"{book_key}.json")
    if os.path.exists(result_path):
        with open(result_path) as f:
            existing = json.load(f)
        print(f"  {book_key[:40]}: 已有 {len(existing.get('boundaries',[]))} sections (跳过)")
        continue

    with open(fpath) as f:
        content = f.read()

    prompt = PROMPT_TEMPLATE + f"\n\nTarget: ~{len(content)//200} sections for this {len(content)//150}-page book.\n\nThe page index:\n\n{content}"

    payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 8192,
        "temperature": 0.0,
        "stream": False
    }
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

    try:
        resp = requests.post(API_URL, json=payload, headers=headers, timeout=300)
        data = resp.json()

        if "choices" not in data:
            print(f"  {book_key[:40]}: API Error {data.get('error',{}).get('message','?')[:80]}")
            continue

        reply = data["choices"][0]["message"]["content"]
        m = re.search(r'\[[\d,\s\n]+\]', reply)

        if m:
            pages = sorted(set(int(p) for p in json.loads(m.group(0))))
            # 过滤: 去掉太靠前(封面)或超出范围的
            pages = [p for p in pages if 5 <= p <= len(content.split('\n'))]

            if len(pages) >= 3:
                result = {
                    "book": book_key,
                    "pages_est": len(content.split('\n')),
                    "sections": len(pages),
                    "boundaries": pages
                }
                with open(result_path, "w") as f:
                    json.dump(result, f, indent=2)

                gaps = [pages[i+1]-pages[i] for i in range(len(pages)-1)]
                print(f"  {book_key[:40]}: {len(pages)} sections, {min(gaps)}-{max(gaps)}p avg{sum(gaps)//len(gaps)}p [{len(pages)} chunks]")
            else:
                print(f"  {book_key[:40]}: 仅 {len(pages)} sections, 回退到 size split")
        else:
            print(f"  {book_key[:40]}: 解析失败 → {reply[:80]}")

        usage = data.get("usage", {})
        cost = (usage.get("prompt_tokens",0)*1 + usage.get("completion_tokens",0)*2) / 1_000_000
        total_cost += cost
        processed += 1

        # 避免触发 rate limit
        time.sleep(0.5)

    except Exception as e:
        print(f"  {book_key[:40]}: Exception {e}")

print(f"\n处理 {processed} 本, 总成本 ¥{total_cost:.4f}")
