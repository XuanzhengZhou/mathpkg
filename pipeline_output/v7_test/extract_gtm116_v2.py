#!/usr/bin/env python3
"""V2: Extract all theorems, lemmas, propositions, corollaries from GTM116.
Better boundary detection, semantic slugs, handles named concepts.
"""

import re
import os
import yaml
import hashlib

BOOK_PATH = '/home/a123/文档/mathpkg/pipeline_output/stitched/(GTM116)Measure and Integral/_full.md'
STAGING = '/home/a123/文档/mathpkg/pipeline_output/v7_test/staging/_GTM116_Measure_and_Integral'
BOOK_ID = 'GTM116'
BOOK_TITLE = 'Measure and Integral'
AUTHORS = 'John L. Kelley, T.P. Srinivasan'
EXTRACTION_DATE = '2026-06-24'

# Clean staging
import shutil
if os.path.exists(STAGING):
    shutil.rmtree(STAGING)
os.makedirs(STAGING, exist_ok=True)

with open(BOOK_PATH, 'r', encoding='utf-8') as f:
    text = f.read()

text = re.sub(r'<\|endoftext\|>', '', text)
lines = text.split('\n')

# ============================
# Chapter/supplement boundaries
# ============================
chapter_starts = {}
for i, line in enumerate(lines):
    m = re.match(r'^Chapter (\d+)$', line.strip())
    if m:
        chapter_starts[i] = f'Chapter {m.group(1)}'

supplement_starts = {}
for i, line in enumerate(lines):
    if re.match(r'^SUPPLEMENT:', line.strip()):
        supplement_starts[i] = line.strip()

def get_chapter_for_line(line_num):
    ch = 'Chapter 0'
    for start in sorted(chapter_starts.keys()):
        if line_num >= start:
            ch = chapter_starts[start]
        else:
            break
    return ch

def get_supplement_for_line(line_num):
    sec = ''
    for start in sorted(supplement_starts.keys()):
        if line_num >= start:
            sec = supplement_starts[start]
        else:
            break
    return sec

def is_boundary(line):
    """Check if a line marks the start of a new concept, chapter, or supplement."""
    s = line.strip()
    if not s:
        return False
    if re.match(r'^Chapter \d+$', s):
        return True
    if re.match(r'^SUPPLEMENT:', s):
        return True
    # Numbered concept start
    if re.match(r'^\d+\s+(THEOREM|LEMMA|PROPOSITION|COROLLARY|Theorem|Lemma|Proposition|Corollary)\b', s):
        return True
    return False

def is_concept_start(line):
    """Check if a line starts a new labeled concept."""
    s = line.strip()
    return bool(re.match(r'^\d+\s+(THEOREM|LEMMA|PROPOSITION|COROLLARY|Theorem|Lemma|Proposition|Corollary)\b', s))


# ============================
# Detect concept label, extract name, number, type
# ============================
def parse_concept_header(line):
    """
    Parse a concept header line like:
    "8 Dini's Theorem ..."
    "5 THEOREM There is..."
    "4 PROPOSITION The unique normalized..."
    "6 THEOREM ON NORM COMPLETENESS If J..."
    "8 LEMMA (APPROXIMATION FROM ABOVE AND BELOW) If I..."
    "2 FUNDAMENTAL LEMMA If..."
    "9 FUBINI THEOREM Let..."
    "10 FATOU'S LEMMA Suppose..."
    Returns (number, ctype, name, statement_start) or None.
    """
    s = line.strip()

    # Pattern: N TYPE [optional ON/name] [optional (NAME)] rest_of_statement
    m = re.match(
        r'^(\d+)\s+'
        r'(THEOREM|LEMMA|PROPOSITION|COROLLARY|Theorem|Lemma|Proposition|Corollary)'
        r'(?:\s+(?:ON\s+)?(.*?))?$',
        s
    )
    if not m:
        return None

    num = m.group(1)
    ctype = m.group(2).lower()
    rest = m.group(3) or ''

    # Normalize type
    type_map = {
        'theorem': 'theorem', 'theorem': 'theorem',
        'lemma': 'lemma', 'lemma': 'lemma',
        'proposition': 'proposition', 'proposition': 'proposition',
        'corollary': 'corollary', 'corollary': 'corollary',
    }
    ctype = type_map.get(ctype, ctype)

    name = ''
    statement_start = rest

    # Check for parenthetical name e.g. "(APPROXIMATION FROM ABOVE AND BELOW)"
    paren_match = re.match(r'\(([^)]+)\)\s*(.*)', rest)
    if paren_match:
        name = paren_match.group(1).strip()
        statement_start = paren_match.group(2).strip()
        return (num, ctype, name, statement_start)

    # Check for name before the actual statement
    # Pattern: ALL_CAPS_WORDS followed by a lowercase letter or math
    # e.g. "ON NORM COMPLETENESS If J is..."
    # e.g. "ON GENERATED δ-RINGS Suppose..."
    # e.g. "ON CONTINUITY OF TRANSLATION If..."
    name_match = re.match(r'((?:ON\s+)?[A-Z][A-Z\s\'-]+(?:[A-Z][a-z])?)\s{2,}(.*)', rest)
    if name_match:
        potential_name = name_match.group(1).strip()
        statement_start = name_match.group(2).strip()
        # Verify it looks like a name (all caps mostly)
        caps_ratio = sum(1 for c in potential_name if c.isupper() or c in " '-") / max(len(potential_name), 1)
        if caps_ratio > 0.7:
            name = potential_name
            return (num, ctype, name, statement_start)

    # Check if the "rest" starts with a named concept like "Dini's Theorem"
    # e.g. "Dini's Theorem If a decreasing..."
    named_match = re.match(r"([A-Z][a-z]+'?s?\s+(?:Theorem|Lemma|Proposition|Corollary))\s+(.*)", rest)
    if named_match:
        name = named_match.group(1).strip()
        statement_start = named_match.group(2).strip()
        return (num, ctype, name, statement_start)

    # Check for ALL CAPS name followed by statement
    # e.g. "FUNDAMENTAL LEMMA If..."
    # e.g. "FATOU'S LEMMA Suppose..."
    # e.g. "FUBINI THEOREM Let..."
    caps_match = re.match(r'([A-Z][A-Z\s\'-]+(?:THEOREM|LEMMA|PROPOSITION|COROLLARY))\s+(.*)', rest)
    if caps_match:
        name = caps_match.group(1).strip()
        statement_start = caps_match.group(2).strip()
        return (num, ctype, name, statement_start)

    # If no explicit name found, use first few words as name hint
    if not name:
        # Use first sentence or first ~80 chars
        pass

    return (num, ctype, name, statement_start)


# ============================
# Main extraction
# ============================
concepts = []

i = 0
while i < len(lines):
    line = lines[i].strip()

    if not line:
        i += 1
        continue

    # Check if this line starts a concept
    result = parse_concept_header(line)
    if not result:
        i += 1
        continue

    num, ctype, name, statement_start = result
    header_line = i

    # If there's NO statement body on this line, read the next lines as statement
    # Otherwise, statement_start has the first part

    statement_parts = []
    if statement_start:
        statement_parts.append(statement_start)

    proof_parts = []
    in_proof = False
    j = i + 1

    while j < len(lines):
        next_line = lines[j].strip()

        # Check for proof start
        if re.match(r'^PROOF\b', next_line):
            in_proof = True
            proof_text = next_line
            if proof_text == 'PROOF':
                # PROOF is on its own line, rest follows
                pass
            else:
                # "PROOF actual proof text"
                proof_parts.append(proof_text[5:].strip())
            j += 1
            continue

        # Stop at boundaries
        if is_concept_start(next_line):
            break
        if re.match(r'^Chapter \d+$', next_line):
            break
        if re.match(r'^SUPPLEMENT:', next_line):
            break
        if re.match(r'^Graduate Texts in Mathematics', next_line):
            break

        if not in_proof:
            statement_parts.append(next_line)
        else:
            proof_parts.append(next_line)

        j += 1

    statement = ' '.join(statement_parts).strip()
    # Clean up multiple spaces
    statement = re.sub(r'\s+', ' ', statement)
    proof = ' '.join(proof_parts).strip()
    proof = re.sub(r'\s+', ' ', proof)

    chapter = get_chapter_for_line(i)
    supplement = get_supplement_for_line(i)
    chapter_num = chapter.split()[-1] if chapter else '0'

    # Generate slug
    if name:
        slug = name.lower()
        slug = re.sub(r'[^a-z0-9\s]+', '', slug)
        slug = re.sub(r'\s+', '_', slug)
        slug = slug.strip('_')
        # Add chapter prefix to avoid collisions
        slug = f'ch{chapter_num}_{slug}'
    else:
        # Use first words of statement for context
        first_words = statement[:60].strip()
        first_words = re.sub(r'[^a-zA-Z0-9\s]+', '', first_words)
        first_words = re.sub(r'\s+', '_', first_words.lower()).strip('_')
        slug = f'ch{chapter_num}_{ctype}_{num}'
        if first_words:
            slug += f'_{first_words[:40]}'

    # Ensure unique slug
    base_slug = slug
    counter = 1
    existing_slugs = {c['slug'] for c in concepts}
    while slug in existing_slugs:
        slug = f'{base_slug}_{counter}'
        counter += 1

    # Generate title
    if name:
        title = name.title()
    else:
        # Use first ~100 chars
        title = statement[:100].strip()
        if len(statement) > 100:
            title += '...'

    # Domain guesses based on chapter
    ch_int = int(chapter_num) if chapter_num.isdigit() else 0
    domain_map = {
        0: ('foundations', 'set_theory'),
        1: ('measure_theory', 'pre_measures'),
        2: ('measure_theory', 'pre_integrals'),
        3: ('measure_theory', 'integration'),
        4: ('measure_theory', 'measures'),
        5: ('measure_theory', 'measurability'),
        6: ('measure_theory', 'lebesgue_integral'),
        7: ('measure_theory', 'product_measures'),
        8: ('measure_theory', 'measure_transformations'),
        9: ('measure_theory', 'signed_measures'),
        10: ('functional_analysis', 'banach_spaces'),
    }
    domain, subdomain = domain_map.get(ch_int, ('measure_theory', 'integration'))

    concepts.append({
        'num': num,
        'type': ctype,
        'name': name,
        'title': title,
        'slug': slug,
        'statement': statement,
        'proof': proof,
        'chapter': chapter,
        'supplement': supplement,
        'chapter_num': chapter_num,
        'domain': domain,
        'subdomain': subdomain,
    })

    i = j

print(f"Found {len(concepts)} concepts")

# ============================
# Write files
# ============================
created = 0
for c in concepts:
    slug = c['slug']
    folder = os.path.join(STAGING, slug)
    os.makedirs(folder, exist_ok=True)

    # 1. concept.yaml
    concept_data = {
        'id': slug,
        'title_en': c['title'],
        'title_zh': '',
        'type': c['type'],
        'domain': c['domain'],
        'subdomain': c['subdomain'],
        'difficulty': 'basic',
        'tags': [],
        'depends_on': {
            'required': [],
            'recommended': [],
            'suggested': []
        },
        'proof_deps': {},
        'source_books': [{
            'book_id': BOOK_ID,
            'author': AUTHORS,
            'title': BOOK_TITLE,
            'chapter': c['chapter'],
            'section': c['supplement'] if c['supplement'] else 'main',
            'pages': '',
            'role_in_book': 'primary'
        }],
        'content_hash': hashlib.md5(c['statement'].encode()).hexdigest(),
        'extraction_date': EXTRACTION_DATE,
        'extraction_agent': 'v7-10books'
    }

    with open(os.path.join(folder, 'concept.yaml'), 'w', encoding='utf-8') as f:
        yaml.dump(concept_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    # 2. theorem.tex - pure LaTeX
    env_map = {
        'theorem': 'theorem',
        'lemma': 'lemma',
        'proposition': 'proposition',
        'corollary': 'corollary'
    }
    env = env_map.get(c['type'], 'theorem')
    title_tex = c['title'].replace('_', r'\_')

    tex_lines = [f"% {c['type'].title()}: {title_tex}"]
    tex_lines.append(f"\\begin{{{env}}}")
    tex_lines.append(c['statement'])
    if c['proof']:
        tex_lines.append('')
        tex_lines.append('\\begin{proof}')
        tex_lines.append(c['proof'])
        tex_lines.append('\\end{proof}')
    tex_lines.append(f"\\end{{{env}}}")

    with open(os.path.join(folder, 'theorem.tex'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(tex_lines) + '\n')

    # 3. introduce.en.md
    type_desc = {
        'theorem': 'provides a key result',
        'lemma': 'serves as a technical lemma',
        'proposition': 'establishes an important intermediate result',
        'corollary': 'follows directly from a preceding theorem or proposition'
    }.get(c['type'], 'presents a mathematical statement')

    intro = f"""---
id: {slug}
title: "{c['title']}"
type: {c['type']}
domain: {c['domain']}
source_book: "{BOOK_TITLE}" by {AUTHORS}
chapter: {c['chapter']}
---

## {c['title']}

{c['statement'][:400]}

This {c['type']} {type_desc} in the theory of measure and integration, from {c['chapter']} of "{BOOK_TITLE}" by {AUTHORS}.
"""

    with open(os.path.join(folder, 'introduce.en.md'), 'w', encoding='utf-8') as f:
        f.write(intro)

    created += 1

print(f"\nCreated {created} concept folders")
print(f"Output in: {STAGING}")

# Write .done
done_file = os.path.join(STAGING, '.done')
with open(done_file, 'w') as f:
    f.write(f"DONE\n{created} concepts extracted from GTM116 Measure and Integral\n")
print(f"Done: {done_file}")

# Summary
type_counts = {}
for c in concepts:
    t = c['type']
    type_counts[t] = type_counts.get(t, 0) + 1
print(f"\nBreakdown: {type_counts}")
