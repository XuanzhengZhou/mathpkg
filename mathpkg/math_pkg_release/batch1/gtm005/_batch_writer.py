#!/usr/bin/env python3
"""Batch writer for GTM005 concept extraction. Reads concepts as JSON, writes all files."""
import json, os, sys

BASE = "/home/a123/文档/mathpkg/pipeline_output/math_pkg_tmp/concepts_batch1/gtm005"

def write_concept(slug, concept):
    """Write all files for one concept. concept is a dict with keys:
    concept.yaml data: id, title_en, title_zh, type, domain, subdomain, difficulty, tags, depends_on, source_books
    theorem.tex: raw LaTeX statement
    introduce.en.md: frontmatter + intro text
    proof: optional proof text
    exercises: optional list of {number, statement}
    """
    d = os.path.join(BASE, slug)
    os.makedirs(d, exist_ok=True)

    # concept.yaml
    cy = {
        'id': slug,
        'title_en': concept.get('title_en', slug.replace('-', ' ').title()),
        'title_zh': '',
        'type': concept['type'],
        'domain': concept.get('domain', 'foundations'),
        'subdomain': concept.get('subdomain', 'category-theory'),
        'difficulty': concept.get('difficulty', 'basic'),
        'tags': concept.get('tags', []),
        'depends_on': concept.get('depends_on', {'required': [], 'recommended': [], 'suggested': []}),
        'source_books': concept.get('source_books', []),
        'content_hash': '',
        'extraction_date': '2026-06-27',
        'extraction_agent': 'v8-full-extract',
    }
    with open(os.path.join(d, 'concept.yaml'), 'w') as f:
        f.write(json.dumps(cy, indent=2, ensure_ascii=False))

    # theorem.tex
    with open(os.path.join(d, 'theorem.tex'), 'w') as f:
        f.write(concept.get('statement', '% No statement'))

    # introduce.en.md
    intro_fm = {
        'role': 'introduce',
        'locale': 'en',
        'content_hash': '',
        'written_against': '',
    }
    intro_text = concept.get('intro', f"{concept.get('title_en', slug)} — {concept['type']} from Mac Lane's Categories for the Working Mathematician.")
    with open(os.path.join(d, 'introduce.en.md'), 'w') as f:
        f.write('---\n')
        for k, v in intro_fm.items():
            f.write(f'{k}: {json.dumps(v)}\n')
        f.write('---\n')
        f.write(intro_text + '\n')

    # proof file (for theorem/proposition/lemma/corollary only)
    if concept['type'] in ('theorem', 'proposition', 'lemma', 'corollary') and 'proof' in concept and concept['proof']:
        proof_fm = {
            'role': 'proof',
            'locale': 'en',
            'of_concept': slug,
            'source_book': 'gtm005',
            'source_chapter': concept.get('source_books', [{}])[0].get('chapter', '') if concept.get('source_books') else '',
            'source_section': concept.get('source_books', [{}])[0].get('section', '') if concept.get('source_books') else '',
        }
        ch = proof_fm['source_chapter']
        sec = proof_fm['source_section']
        pfname = f'proof_gtm005_{ch}.{sec}.en.md'
        with open(os.path.join(d, pfname), 'w') as f:
            f.write('---\n')
            for k, v in proof_fm.items():
                f.write(f'{k}: {json.dumps(v)}\n')
            f.write('---\n')
            f.write(concept['proof'] + '\n')

    # exercise files
    if 'exercises' in concept and concept['exercises']:
        for ex in concept['exercises']:
            ch = concept.get('source_books', [{}])[0].get('chapter', '') if concept.get('source_books') else ''
            sec = concept.get('source_books', [{}])[0].get('section', '') if concept.get('source_books') else ''
            ex_fm = {
                'role': 'exercise',
                'locale': 'en',
                'chapter': ch,
                'section': sec,
                'exercise_number': ex['number'],
            }
            exname = f'exercise_gtm005_{ch}.{sec}.{ex["number"]}.en.md'
            with open(os.path.join(d, exname), 'w') as f:
                f.write('---\n')
                for k, v in ex_fm.items():
                    f.write(f'{k}: {json.dumps(v)}\n')
                f.write('---\n')
                f.write(ex['statement'] + '\n')

    print(f"  Wrote: {slug} ({concept['type']})")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 _batch_writer.py <concepts.json>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        data = json.load(f)

    for slug, concept in data.items():
        write_concept(slug, concept)

    print(f"\nTotal: {len(data)} concepts written")
