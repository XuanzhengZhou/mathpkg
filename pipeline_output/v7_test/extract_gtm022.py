#!/usr/bin/env python3
"""Extract all theorems, definitions, lemmas, propositions, corollaries from GTM022."""
import os, re, yaml, hashlib, json

BASE = "/home/a123/文档/mathpkg/pipeline_output/v7_test/staging/_GTM022_An_Algebraic_Introduction_to_Mathematical_Logic"
SRC = "/home/a123/文档/mathpkg/pipeline_output/stitched/(GTM022)An Algebraic Introduction to Mathematical Logic/_full.md"

with open(SRC, 'r', encoding='utf-8') as f:
    text = f.read()

# Clean up excessive <|endoftext|> tokens
text = re.sub(r'<\|endoftext\|>+', ' ', text)
# Clean up multiple blank lines
text = re.sub(r'\n{3,}', '\n\n', text)

lines = text.split('\n')

# Identify chapter and section info
chapters = {}
current_chapter = None
current_section = None
section_items = {}  # (ch, sec) -> []

# Items found
items = []

# Patterns
chap_pat = re.compile(r'^Chapter\s+([IVX]+)$')
sec_pat = re.compile(r'^§(\d+)\s+(.+)$')
# Numbered item patterns: Definition/Theorem/Lemma/Proposition/Corollary X.Y
item_pat = re.compile(r'^(\*\*)?\s*(Definition|Theorem|Lemma|Proposition|Corollary)\s+(\d+)\.(\d+)\.?\s*(\*\*)?\s*(.*)$')
# Exercise pattern to skip
exercise_pat = re.compile(r'^Exercises?\s*$')

# Also match bold **Definition X.Y.** at start of paragraph
bold_item_pat = re.compile(r'^\*\*(Definition|Theorem|Lemma|Proposition|Corollary)\s+(\d+)\.(\d+)\.\*\*\s*(.*)$')

chapter_map = {'I':1,'II':2,'III':3,'IV':4,'V':5,'VI':6,'VII':7,'VIII':8,'IX':9,'X':10}
# Reverse map
chapter_names = {1:'Universal Algebra',2:'Propositional Calculus',3:'Properties of the Propositional Calculus',
    4:'Predicate Calculus',5:'First-Order Mathematics',6:'Zermelo-Fraenkel Set Theory',
    7:'Ultraproducts',8:'Non-Standard Models',9:'Turing Machines and Gödel Numbers',
    10:"Hilbert's Tenth Problem, Word Problems"}

# State tracking
in_exercises = False
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

for i, line in enumerate(lines):
    # Check for chapter
    m = chap_pat.match(line.strip())
    if m:
        flush_item()
        current_chapter = chapter_map.get(m.group(1), 0)
        current_section = None
        in_exercises = False
        continue

    # Check for section
    m = sec_pat.match(line.strip())
    if m:
        flush_item()
        current_section = int(m.group(1))
        in_exercises = False
        continue

    # Check for Exercises marker (line containing only Exercises)
    if exercise_pat.match(line.strip()):
        flush_item()
        in_exercises = True
        continue

    # Skip exercises content
    if in_exercises or 'Exercise' in line.strip()[:20] or 'Exercises' in line.strip()[:20]:
        # But check if next section starts
        if sec_pat.match(line.strip()) or chap_pat.match(line.strip()):
            in_exercises = False
        if current_item:
            flush_item()
        continue

    # Check for numbered item start
    m = item_pat.match(line.strip())
    if not m:
        m = bold_item_pat.match(line.strip())

    if m:
        flush_item()
        item_type = m.group(2).lower()
        sec_num = int(m.group(3))
        item_num = int(m.group(4))
        rest = m.group(6) if m.group(6) is not None else ''

        current_item = {
            'type': item_type,
            'chapter': current_chapter,
            'section': current_section,
            'sec_num': sec_num,
            'item_num': item_num,
            'label': f"{sec_num}.{item_num}",
            'first_line': rest
        }
        item_lines = [rest] if rest else []
        continue

    # Also check for items that start on a new line after the label
    # e.g. "Definition 4.1. A T-algebra R..."
    m2 = re.match(r'^(Definition|Theorem|Lemma|Proposition|Corollary)\s+(\d+)\.(\d+)\.\s+(.+)', line.strip())
    if m2:
        flush_item()
        current_item = {
            'type': m2.group(1).lower(),
            'chapter': current_chapter,
            'section': current_section,
            'sec_num': int(m2.group(2)),
            'item_num': int(m2.group(3)),
            'label': f"{m2.group(2)}.{m2.group(3)}",
            'first_line': m2.group(4)
        }
        item_lines = [m2.group(4)]
        continue

    # Accumulate lines for current item
    if current_item:
        # Stop conditions: new numbered item, empty line after content, exercises
        if line.strip() == '':
            if item_lines:
                item_lines.append(line)
        else:
            item_lines.append(line)

flush_item()

print(f"Found {len(items)} concepts total")

# Group by chapter
by_chapter = {}
for it in items:
    ch = it['chapter']
    if ch not in by_chapter:
        by_chapter[ch] = []
    by_chapter[ch].append(it)

for ch, its in sorted(by_chapter.items()):
    print(f"  Chapter {ch} ({chapter_names.get(ch, 'Unknown')}): {len(its)} concepts")
    for it in its:
        print(f"    {it['label']} [{it['type']}]: {it['first_line'][:80]}")

# Now write the files
os.makedirs(BASE, exist_ok=True)

def make_slug(it):
    """Create a semantic English slug from the concept."""
    first_line = it.get('first_line', '')
    content = it.get('content', '')
    typ = it['type']
    ch = it['chapter']
    sec = it['section']
    label = it['label']

    # Extract key terms from first line and content
    # For definitions: use the term being defined
    # For theorems: use key topic
    clean_first = re.sub(r'[^\w\s-]', '', first_line.lower())[:80]

    # Build chapter prefix
    ch_prefix = f"ch{ch}"
    sec_prefix = f"s{sec}"

    # Type abbreviation
    t_abbr = {'definition': 'def', 'theorem': 'thm', 'lemma': 'lem',
              'proposition': 'prop', 'corollary': 'cor'}[typ]

    # Try to extract key term
    if typ == 'definition':
        # Often "Definition X.Y. A T-algebra is..." or "Definition X.Y. Let X be..."
        term_match = re.match(r'(?:A|An|The)\s+([\w\s-]+?)\s+(?:is|are|be)\b', first_line)
        if not term_match:
            term_match = re.match(r'Let\s+([\w\s-]+?)\s+be\b', first_line)
        if not term_match:
            term_match = re.match(r'([\w\s-]+?)\s+(?:is|are)\b', first_line)
        if term_match:
            term = term_match.group(1).strip().lower().replace(' ', '_')[:50]
        else:
            term = clean_first.replace(' ', '_')[:50]
    else:
        term = clean_first.replace(' ', '_')[:50]

    # Clean up term
    term = re.sub(r'[^\w]', '_', term)
    term = re.sub(r'_+', '_', term).strip('_')

    return f"{ch_prefix}_{sec_prefix}_{t_abbr}_{label.replace('.', '_')}_{term}"

def infer_domain_type(it):
    """Infer domain and subdomain from content."""
    ch = it['chapter']
    typ = it['type']
    content = it.get('content', '')[:500].lower()

    if ch == 1:
        domain = 'universal_algebra'
        subdomain = 'algebraic_structures'
    elif ch == 2:
        domain = 'propositional_calculus'
        subdomain = 'logic'
    elif ch == 3:
        domain = 'propositional_calculus'
        subdomain = 'metalogic'
    elif ch == 4:
        domain = 'first_order_logic'
        subdomain = 'predicate_calculus'
    elif ch == 5:
        domain = 'first_order_theories'
        subdomain = 'model_theory'
    elif ch == 6:
        domain = 'set_theory'
        subdomain = 'zermelo_fraenkel'
    elif ch == 7:
        domain = 'ultraproducts'
        subdomain = 'model_theory'
    elif ch == 8:
        domain = 'non_standard_analysis'
        subdomain = 'model_theory'
    elif ch == 9:
        domain = 'computability_theory'
        subdomain = 'turing_machines'
    elif ch == 10:
        domain = 'computability_theory'
        subdomain = 'decision_problems'
    else:
        domain = 'mathematical_logic'
        subdomain = 'general'

    return domain, subdomain

def extract_latex(content):
    """Extract the main LaTeX content."""
    # Keep math, clean up text
    lines = content.split('\n')
    result = []
    for line in lines:
        stripped = line.strip()
        # Skip exercise references and Proof headers
        if stripped.startswith('Proof') or stripped.startswith('Proof:'):
            continue
        if stripped.startswith('Exercises') or stripped.startswith('Exercise'):
            continue
        result.append(line)
    return '\n'.join(result).strip()

def write_concept(it):
    slug = make_slug(it)
    dirpath = os.path.join(BASE, slug)
    os.makedirs(dirpath, exist_ok=True)

    # concept.yaml
    domain, subdomain = infer_domain_type(it)
    label = it['label']
    typ = it['type']
    ch = it['chapter']
    sec = it['section']
    ch_name = chapter_names.get(ch, 'Unknown')

    # Build title from first line
    first_line = it.get('first_line', '')
    title_en = f"{typ.title()} {label}: {first_line[:120]}"

    concept = {
        'id': slug,
        'title_en': title_en,
        'title_zh': '',
        'type': typ,
        'domain': domain,
        'subdomain': subdomain,
        'difficulty': 'basic',
        'tags': [],
        'depends_on': {'required': [], 'recommended': [], 'suggested': []},
        'proof_deps': {},
        'source_books': [{
            'book_id': 'GTM022',
            'author': 'Donald W. Barnes, John M. Mack',
            'title': 'An Algebraic Introduction to Mathematical Logic',
            'chapter': f'Chapter {list(chapter_map.keys())[list(chapter_map.values()).index(ch)]} - {ch_name}',
            'section': f'§{sec}',
            'pages': '',
            'role_in_book': f'{typ} {label}'
        }],
        'content_hash': hashlib.md5(it['content'].encode()).hexdigest(),
        'extraction_date': '2026-06-24',
        'extraction_agent': 'v7-10books'
    }

    with open(os.path.join(dirpath, 'concept.yaml'), 'w', encoding='utf-8') as f:
        yaml.dump(concept, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    # theorem.tex - pure LaTeX
    latex_content = extract_latex(it['content'])
    # If no good LaTeX, use the first line
    if not latex_content or len(latex_content) < 10:
        latex_content = first_line

    with open(os.path.join(dirpath, 'theorem.tex'), 'w', encoding='utf-8') as f:
        f.write(latex_content)

    # introduce.en.md
    lines_summary = it['content'][:300].strip()
    intro = f"""---
id: {slug}
title_en: "{title_en}"
type: {typ}
---

{first_line}

{lines_summary[:200] if len(lines_summary) > len(first_line) else ''}
"""
    with open(os.path.join(dirpath, 'introduce.en.md'), 'w', encoding='utf-8') as f:
        f.write(intro)

# Write all concepts
for it in items:
    try:
        write_concept(it)
    except Exception as e:
        print(f"Error writing {it['label']}: {e}")

# Write .done
with open(os.path.join(BASE, '.done'), 'w') as f:
    f.write(f"DONE - {len(items)} concepts extracted\n")

print(f"\nTotal: {len(items)} concepts written to {BASE}")
print("Concepts by type:")
type_counts = {}
for it in items:
    t = it['type']
    type_counts[t] = type_counts.get(t, 0) + 1
for t, c in sorted(type_counts.items()):
    print(f"  {t}: {c}")

# Also print all items with their labels for verification
print("\n=== FULL LIST ===")
for it in items:
    print(f"  Ch{it['chapter']}§{it['section']} {it['label']} [{it['type']}] {it['first_line'][:100]}")
