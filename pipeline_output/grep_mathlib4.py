#!/usr/bin/env python3
"""多策略 grep Mathlib4，统计 10 本书 6,374 concepts 的覆盖率"""
import os, re, json, subprocess, yaml
from collections import defaultdict

CONCEPTS_DIR = '/home/a123/文档/mathpkg/pipeline_output/math_pkg_release/concepts_v7'
MATHLIB = os.path.expanduser('~/lean-demo/.lake/packages/mathlib/Mathlib')
OUTPUT = '/home/a123/文档/mathpkg/pipeline_output/data/mathlib4_grep_results.json'

def gen_search_terms(slug, title_en):
    """从 slug 和 title 生成多个搜索变体"""
    terms = set()

    # 1. slug 变体
    slug_underscore = slug.replace('-', '_')
    terms.add(slug_underscore)                      # lagrange_theorem

    # 2. PascalCase
    parts = slug.split('-')
    pascal = ''.join(p.capitalize() for p in parts)
    terms.add(pascal)                                # LagrangeTheorem
    camel = parts[0] + ''.join(p.capitalize() for p in parts[1:])
    terms.add(camel)                                 # lagrangeTheorem

    # 3. 从 title_en 提取关键词
    if title_en:
        # 去除所有格 's, 标点
        clean = re.sub(r"[''']s?", '', title_en)
        clean = re.sub(r'[^\w\s]', ' ', clean)
        words = clean.split()

        # 取前 3 个有意义的关键词（跳过冠词/介词）
        skip = {'the','a','an','of','in','on','for','to','and','is','are','be'}
        keywords = [w for w in words if w.lower() not in skip and len(w) > 2]

        if len(keywords) >= 2:
            # 关键词组合
            kw_snake = '_'.join(k.lower() for k in keywords[:3])
            terms.add(kw_snake)                      # subgroup_card_dvd
            kw_pascal = ''.join(k.capitalize() for k in keywords[:3])
            terms.add(kw_pascal)                     # SubgroupCardDvd

            # 关键名词单独搜
            for kw in keywords[:2]:
                if len(kw) > 4:
                    terms.add(kw.lower())

    # 4. 常见 Mathlib 命名模式
    if 'theorem' in slug:
        base = slug.replace('-theorem', '')
        terms.add(f'{base.replace("-","_")}_theorem')
    if 'lemma' in slug:
        base = slug.replace('-lemma', '')
        terms.add(f'{base.replace("-","_")}_lemma')
    if slug.startswith('definition-') or slug.endswith('-definition'):
        pass  # definitions 通常不直接对应 theorem

    return list(terms)[:10]  # 最多 10 个变体


def grep_mathlib(term):
    """在 Mathlib4 中搜索一个术语"""
    try:
        # -l: 只输出文件名, -i: 忽略大小写(仅针对字母变体), --include只搜.lean
        result = subprocess.run(
            ['grep', '-r', '-l', '--include=*.lean', term, MATHLIB],
            capture_output=True, text=True, timeout=10
        )
        files = result.stdout.strip().split('\n')
        return [f for f in files if f]
    except:
        return []


def main():
    # 收集所有概念
    concepts = []
    for book in sorted(os.listdir(CONCEPTS_DIR)):
        book_dir = os.path.join(CONCEPTS_DIR, book)
        if not os.path.isdir(book_dir): continue
        for section in os.listdir(book_dir):
            section_dir = os.path.join(book_dir, section)
            if not os.path.isdir(section_dir): continue
            for concept_name in os.listdir(section_dir):
                concept_dir = os.path.join(section_dir, concept_name)
                if not os.path.isdir(concept_dir): continue
                yf = os.path.join(concept_dir, 'concept.yaml')
                if not os.path.exists(yf): continue
                try:
                    d = yaml.safe_load(open(yf))
                    if d and d.get('id'):
                        concepts.append({
                            'id': d['id'],
                            'title_en': d.get('title_en', ''),
                            'type': d.get('type', ''),
                            'book': book,
                            'dir': concept_dir
                        })
                except:
                    pass

    print(f"总计: {len(concepts)} concepts")

    # 统计
    by_book = defaultdict(lambda: {'total': 0, 'hit': 0, 'hits': []})
    total_hit = 0
    results = []

    for i, c in enumerate(concepts):
        by_book[c['book']]['total'] += 1
        terms = gen_search_terms(c['id'], c['title_en'])

        found_files = []
        found_term = None
        for term in terms:
            files = grep_mathlib(term)
            if files:
                found_term = term
                found_files = files[:3]  # 最多保留3个文件
                break

        if found_files:
            total_hit += 1
            by_book[c['book']]['hit'] += 1
            results.append({
                'id': c['id'],
                'title_en': c['title_en'],
                'type': c['type'],
                'book': c['book'],
                'matched_term': found_term,
                'mathlib_files': [f.replace(MATHLIB + '/', '') for f in found_files]
            })

        if (i+1) % 500 == 0:
            print(f"  {i+1}/{len(concepts)}... {total_hit} hits ({total_hit/(i+1)*100:.1f}%)")

    print(f"\n命中: {total_hit}/{len(concepts)} ({total_hit/len(concepts)*100:.1f}%)")

    # 按书统计
    print(f"\n{'书':<12} {'总数':>5} {'命中':>5} {'命中率':>7}")
    print("-" * 35)
    for book in sorted(by_book.keys()):
        b = by_book[book]
        pct = b['hit'] / b['total'] * 100 if b['total'] > 0 else 0
        print(f"{book:<12} {b['total']:>5} {b['hit']:>5} {pct:>6.1f}%")

    # 按类型统计
    by_type = defaultdict(lambda: {'total': 0, 'hit': 0})
    for c in concepts:
        by_type[c['type']]['total'] += 1
    for r in results:
        by_type[r['type']]['hit'] += 1

    print(f"\n{'类型':<15} {'总数':>5} {'命中':>5} {'命中率':>7}")
    print("-" * 35)
    for t in sorted(by_type.keys()):
        b = by_type[t]
        pct = b['hit'] / b['total'] * 100 if b['total'] > 0 else 0
        print(f"{t:<15} {b['total']:>5} {b['hit']:>5} {pct:>6.1f}%")

    # 保存结果
    with open(OUTPUT, 'w') as f:
        json.dump({
            'total_concepts': len(concepts),
            'total_hits': total_hit,
            'hit_rate': total_hit / len(concepts),
            'by_book': {k: {'total': v['total'], 'hit': v['hit']} for k, v in by_book.items()},
            'by_type': {k: {'total': v['total'], 'hit': v['hit']} for k, v in by_type.items()},
            'results': results[:100]  # 前100个结果
        }, f, indent=2, ensure_ascii=False)

    print(f"\n详细结果保存到: {OUTPUT}")

    # 列出一些未命中的例子
    missed = [c for c in concepts if c['id'] not in {r['id'] for r in results}]
    print(f"\n未命中示例 ({len(missed)} total):")
    for c in missed[:15]:
        print(f"  [{c['type']}] {c['id']}: {c['title_en'][:60]}")


if __name__ == '__main__':
    main()
