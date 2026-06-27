#!/usr/bin/env python3
"""Extract all concepts from GTM022 v2 - fixes exercise detection bug."""
import os, re, yaml, hashlib

BASE = "/home/a123/文档/mathpkg/pipeline_output/v7_test/staging/_GTM022_An_Algebraic_Introduction_to_Mathematical_Logic"
SRC = "/home/a123/文档/mathpkg/pipeline_output/stitched/(GTM022)An Algebraic Introduction to Mathematical Logic/_full.md"

with open(SRC, 'r', encoding='utf-8') as f:
    text = f.read()

text = re.sub(r'<\|endoftext\|>+', ' ', text)
text = re.sub(r'\n{3,}', '\n\n', text)
lines = text.split('\n')

chapter_names = {
    1:'Universal Algebra', 2:'Propositional Calculus',
    3:'Properties of the Propositional Calculus', 4:'Predicate Calculus',
    5:'First-Order Mathematics', 6:'Zermelo-Fraenkel Set Theory',
    7:'Ultraproducts', 8:'Non-Standard Models',
    9:'Turing Machines and Godel Numbers', 10:'Hilberts Tenth Problem, Word Problems'
}
chapter_roman = {1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X'}
roman_to_int = {'I':1,'II':2,'III':3,'IV':4,'V':5,'VI':6,'VII':7,'VIII':8,'IX':9,'X':10}

items = []
current_chapter = None
current_section = None
current_section_title = ""
current_item = None
item_lines = []

def flush_item():
    global current_item, item_lines
    if current_item and item_lines:
        content = '\n'.join(item_lines).strip()
        if content:
            items.append(dict(current_item, content=content))
    current_item = None
    item_lines = []

def is_concept_line(ls):
    for prefix in ['Definition', 'Theorem', 'Lemma', 'Proposition', 'Corollary']:
        if re.match(rf'^\*\*\s*{prefix}\s+\d+\.\d+', ls): return True
        if re.match(rf'^\s*{prefix}\s+\d+\.\d+\.?\s', ls): return True
    return False

def is_exercise_start(ls):
    if re.match(r'^Exercises?\s*$', ls): return True
    if re.match(r'^\d+\.\d+\.\s+', ls): return True
    if re.match(r'^Exercise\s+\d+\.\d+', ls): return True
    return False

i = 0
while i < len(lines):
    line = lines[i]
    ls = line.strip()

    # Chapter
    ch_m = re.match(r'^Chapter\s+([IVX]+)\s*$', ls)
    if ch_m:
        flush_item()
        current_chapter = roman_to_int.get(ch_m.group(1))
        current_section = None
        current_section_title = ""
        i += 1
        continue

    # Section
    sec_m = re.match(r'^§(\d+)\s+(.+)', ls)
    if sec_m:
        flush_item()
        current_section = int(sec_m.group(1))
        current_section_title = sec_m.group(2).strip()
        i += 1
        continue

    # CONCEPT DETECTION - MUST come before exercise skip
    ctype = None; c_sec = None; c_item = None; c_rest = ""

    # Plain: "Definition 1.4. text..."
    m = re.match(r'^(Definition|Theorem|Lemma|Proposition|Corollary)\s+(\d+)\.(\d+)\.\s*(.*)', ls)
    if m:
        ctype = m.group(1).lower(); c_sec = int(m.group(2)); c_item = int(m.group(3)); c_rest = m.group(4).strip()

    # Bold: "**Definition 2.1.** text..."
    if not ctype:
        m = re.match(r'^\*\*\s*(Definition|Theorem|Lemma|Proposition|Corollary)\s+(\d+)\.(\d+)\.?\s*\*\*\s*(.*)', ls)
        if m:
            ctype = m.group(1).lower(); c_sec = int(m.group(2)); c_item = int(m.group(3)); c_rest = m.group(4).strip()

    # Bold with name "**Theorem 2.13. (The Adequacy Theorem)**"
    if not ctype:
        m = re.match(r'^\*\*\s*(Definition|Theorem|Lemma|Proposition|Corollary)\s+(\d+)\.(\d+)\b', ls)
        if m:
            # Try to extract rest from the full line
            ctype = m.group(1).lower(); c_sec = int(m.group(2)); c_item = int(m.group(3))
            # Get everything after the number
            rest_start = m.end()
            rest = ls[rest_start:].strip()
            # Remove trailing ** if present
            rest = re.sub(r'\*\*\s*$', '', rest).strip()
            c_rest = rest

    if ctype:
        flush_item()
        current_item = {
            'type': ctype, 'chapter': current_chapter, 'section': current_section,
            'section_title': current_section_title,
            'sec_num': c_sec, 'item_num': c_item, 'label': f"{c_sec}.{c_item}",
            'first_line': c_rest
        }
        item_lines = [c_rest] if c_rest else []
        i += 1
        continue

    # Exercise detection (after concept check)
    if is_exercise_start(ls):
        # Only skip if NOT currently building a concept
        if not current_item:
            i += 1
            continue
        # If we're in a concept, this might be a reference - keep accumulating
        item_lines.append(line)
        i += 1
        continue

    # Accumulate body
    if current_item:
        item_lines.append(line)
    i += 1

flush_item()

print(f"Found {len(items)} concepts total\n")
by_chapter = {}
for it in items:
    ch = it['chapter'] or 0
    by_chapter.setdefault(ch, []).append(it)
for ch in sorted(by_chapter.keys()):
    its = by_chapter[ch]
    print(f"  Chapter {ch} ({chapter_names.get(ch, 'Unknown')}): {len(its)} concepts")
    for it in its:
        print(f"    {it['label']} [{it['type']}]: {it['first_line'][:80]}")

type_counts = {}
for it in items: type_counts[it['type']] = type_counts.get(it['type'], 0) + 1
print(f"\nBy type:"); [print(f"  {t}: {c}") for t,c in sorted(type_counts.items())]

# === WRITE ===
os.makedirs(BASE, exist_ok=True)

def make_slug(it):
    first = it.get('first_line', '')
    typ = it['type']; ch = it['chapter'] or 0; sec = it['section'] or 0; label = it['label']
    t_abbr = {'definition':'def','theorem':'thm','lemma':'lem','proposition':'prop','corollary':'cor'}[typ]
    clean = re.sub(r'[^a-zA-Z0-9\s]', ' ', first.lower())
    words = [w for w in clean.split() if len(w) > 2][:6]
    term = '_'.join(words)[:60] if words else label.replace('.','_')
    return f"ch{ch}_s{sec}_{t_abbr}_{label.replace('.','_')}_{term}"

def infer_domain(it):
    ch = it['chapter'] or 0
    if ch == 1: return 'universal_algebra', 'algebraic_structures'
    elif ch == 2: return 'mathematical_logic', 'propositional_calculus'
    elif ch == 3: return 'mathematical_logic', 'metalogic'
    elif ch == 4: return 'mathematical_logic', 'predicate_calculus'
    elif ch == 5: return 'mathematical_logic', 'first_order_theories'
    elif ch == 6: return 'mathematical_logic', 'set_theory'
    elif ch == 7: return 'mathematical_logic', 'model_theory'
    elif ch == 8: return 'mathematical_logic', 'nonstandard_analysis'
    elif ch == 9: return 'mathematical_logic', 'computability'
    elif ch == 10: return 'mathematical_logic', 'decision_problems'
    return 'mathematical_logic', 'general'

def extract_title(it):
    first = it.get('first_line', '')
    typ = it['type'].title(); label = it['label']
    clean = first.strip()
    clean = re.sub(r'\$[^$]*\$', '', clean)
    clean = re.sub(r'[{}]', '', clean)
    clean = re.sub(r'\s+', ' ', clean).strip()
    return f"{typ} {label}: {clean[:150]}" if clean else f"{typ} {label}"

def write_concept(it):
    slug = make_slug(it)
    dirpath = os.path.join(BASE, slug)
    os.makedirs(dirpath, exist_ok=True)
    domain, subdomain = infer_domain(it)
    label = it['label']; typ = it['type']
    ch = it['chapter'] or 0; sec = it['section'] or 0
    ch_name = chapter_names.get(ch, 'Unknown')
    ch_roman_str = chapter_roman.get(ch, str(ch))
    title_en = extract_title(it)
    content = it.get('content', it.get('first_line', ''))

    concept = {
        'id': slug, 'title_en': title_en, 'title_zh': '', 'type': typ,
        'domain': domain, 'subdomain': subdomain, 'difficulty': 'basic',
        'tags': [], 'depends_on': {'required':[],'recommended':[],'suggested':[]},
        'proof_deps': {},
        'source_books': [{
            'book_id':'GTM022','author':'Donald W. Barnes, John M. Mack',
            'title':'An Algebraic Introduction to Mathematical Logic',
            'chapter':f'Chapter {ch_roman_str}: {ch_name}',
            'section':f'§{sec}' if sec else '','pages':'','role_in_book':f'{typ} {label}'
        }],
        'content_hash':hashlib.md5(content.encode()).hexdigest()[:16],
        'extraction_date':'2026-06-24','extraction_agent':'v7-10books'
    }
    with open(os.path.join(dirpath, 'concept.yaml'), 'w', encoding='utf-8') as f:
        yaml.dump(concept, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    tex = re.sub(r'\*\*', '', content)
    tex = re.sub(r'<\|endoftext\|>+', '', tex).strip()
    if not tex: tex = it.get('first_line', '')
    with open(os.path.join(dirpath, 'theorem.tex'), 'w', encoding='utf-8') as f:
        f.write(tex)

    raw = content[:400].strip()
    sents = re.split(r'(?<=[.!?])\s+', raw)
    desc = ' '.join(sents[:3])
    if len(desc) > 400: desc = desc[:400] + '...'
    intro = f"""---
id: {slug}
title_en: "{title_en}"
type: {typ}
domain: {domain}
subdomain: {subdomain}
source_book: GTM022
---

{desc}
"""
    with open(os.path.join(dirpath, 'introduce.en.md'), 'w', encoding='utf-8') as f:
        f.write(intro)

written = 0
for it in items:
    try:
        write_concept(it); written += 1
    except Exception as e:
        print(f"ERROR {it['label']}: {e}")

with open(os.path.join(BASE, '.done'), 'w') as f:
    f.write(f"DONE - {written} concepts extracted on 2026-06-24\n")
print(f"\nWrote {written} concepts to {BASE}")
