#!/usr/bin/env python3
"""Extract all theorems, definitions, lemmas, propositions, corollaries from GTM065."""

import re
import os
import hashlib
import yaml
import textwrap

BOOK_PATH = '/home/a123/文档/mathpkg/pipeline_output/stitched/(GTM065)Differential Analysis on Complex Manifolds/_full.md'
OUTPUT_DIR = '/home/a123/文档/mathpkg/pipeline_output/v7_test/staging/_GTM065_Differential_Analysis_on_Complex_Manifolds'

# Chapter mapping: roman numeral to chapter name
CHAPTER_MAP = {
    'I': 'Manifolds and Vector Bundles',
    'II': 'Sheaf Theory',
    'III': 'Differential Geometry',
    'IV': 'Elliptic Operator Theory',
    'V': 'Compact Complex Manifolds',
    'VI': "Kodaira's Projective Embedding Theorem",
    'APP': 'Moduli Spaces and Geometric Structures',
}

# Section names per chapter (rough)
CHAPTER_SECTIONS = {
    'I': {1: 'Manifolds', 2: 'Vector Bundles', 3: 'Almost Complex Manifolds and the ∂-Operator'},
    'II': {1: 'Presheaves and Sheaves', 2: 'Resolutions of Sheaves', 3: 'Cohomology Theory', 4: 'Čech Cohomology with Coefficients in a Sheaf'},
    'III': {1: 'Hermitian Differential Geometry', 2: 'The Canonical Connection and Curvature of a Hermitian Holomorphic Vector Bundle', 3: 'Chern Classes of Differentiable Vector Bundles', 4: 'Complex Line Bundles'},
    'IV': {1: 'Sobolev Spaces', 2: 'Differential Operators', 3: 'Pseudodifferential Operators', 4: 'A Parametrix for Elliptic Differential Operators', 5: 'Elliptic Complexes'},
    'V': {1: 'Hermitian Exterior Algebra on a Hermitian Vector Space', 2: 'Harmonic Theory on Compact Manifolds', 3: 'Representations of sl(2,C) on Hermitian Exterior Algebras', 4: 'Differential Operators on a Kähler Manifold', 5: 'The Hodge Decomposition Theorem on Compact Kähler Manifolds', 6: 'The Hodge-Riemann Bilinear Relations on a Kähler Manifold'},
    'VI': {1: 'Hodge Manifolds', 2: "Kodaira's Vanishing Theorem", 3: 'Quadratic Transformations', 4: "Kodaira's Embedding Theorem"},
}

# Type normalization
TYPE_MAP = {
    'definition': 'definition',
    'theorem': 'theorem',
    'lemma': 'lemma',
    'proposition': 'proposition',
    'corollary': 'corollary',
}

# Domain guesses based on chapter
CHAPTER_DOMAIN = {
    'I': 'differential_geometry',
    'II': 'sheaf_theory',
    'III': 'differential_geometry',
    'IV': 'partial_differential_equations',
    'V': 'complex_geometry',
    'VI': 'complex_geometry',
    'APP': 'moduli_theory',
}

def clean_text(text):
    """Remove <|endoftext|> markers and clean up."""
    text = re.sub(r'<\|endoftext\|>', '', text)
    # Remove excessive newlines
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    return text.strip()

def slugify(name):
    """Create a semantic English slug from a concept name."""
    # Remove LaTeX markup
    slug = name.lower()
    slug = re.sub(r'\$[^$]+\$', '', slug)
    slug = re.sub(r'\\[a-zA-Z]+(\{[^}]*\})*', '', slug)
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'\s+', '_', slug.strip())
    slug = re.sub(r'_+', '_', slug)
    slug = slug.strip('_')
    if len(slug) > 80:
        slug = slug[:80].rstrip('_')
    return slug

def extract_latex(text):
    """Extract LaTeX content from text, cleaning up."""
    # Remove markdown bold markers
    text = re.sub(r'\*\*', '', text)
    # Clean up
    text = text.strip()
    return text

def find_chapter(line_num):
    """Determine which chapter a line number is in."""
    chapters = [
        (211, 'I'), (946, 'II'), (1608, 'III'), (2732, 'IV'),
        (3757, 'V'), (5251, 'VI'),
    ]
    current = 'I'
    for start, ch in chapters:
        if line_num >= start:
            current = ch
    return current

def find_section(chapter, concept_num):
    """Guess the section number from the concept number."""
    # Concept numbers are like 1.13, 2.1, 3.5 etc.
    # The integer part before the decimal is the section number
    if '.' in str(concept_num):
        section = int(str(concept_num).split('.')[0])
        return section
    return 1

def extract_concepts():
    """Extract all concepts from the book."""
    with open(BOOK_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # Clean the content
    content = clean_text(content)
    lines = content.split('\n')

    # Pattern for concept labels
    # Matches: "Definition 2.1:", "**Definition 2.2:**", "Theorem 1.10 (Whitney [1]):", etc.
    concept_pattern = re.compile(
        r'^\*{0,2}\s*(Definition|Theorem|Lemma|Proposition|Corollary)\s+'
        r'([IVX]+\.)?(\d+\.\d+|\d+)\s*'
        r'(\([^)]*\))?\s*[:\*]?\*{0,2}\s*',
        re.IGNORECASE
    )

    # Find all concept line numbers
    concept_candidates = []
    for i, line in enumerate(lines):
        m = concept_pattern.match(line.strip())
        if m:
            ctype = m.group(1).lower()
            roman = m.group(2)
            cnum = m.group(3)
            note = m.group(4)

            # Get full label
            label_start = m.start()
            label_end = m.end()

            concept_candidates.append({
                'line_num': i,
                'type': ctype,
                'number': cnum,
                'roman': roman,
                'note': note,
                'full_label': line.strip()[label_start:label_end].strip(),
            })

    print(f"Found {len(concept_candidates)} concept candidates")

    # Deduplicate: remove references that aren't actual definitions
    # A concept is valid if the line starts with the label (possibly with **)
    valid_concepts = []
    for c in concept_candidates:
        line = lines[c['line_num']].strip()
        # Check that the line starts with the concept type (possibly with **)
        if re.match(r'^\*{0,2}\s*(Definition|Theorem|Lemma|Proposition|Corollary)\s', line, re.IGNORECASE):
            valid_concepts.append(c)

    print(f"Valid concepts: {len(valid_concepts)}")

    # Extract content for each concept
    results = []
    for idx, c in enumerate(valid_concepts):
        start_line = c['line_num']
        ctype = c['type']
        cnum = c['number']

        # Find end: next concept or chapter boundary or empty line gap
        end_line = min(start_line + 100, len(lines))  # default max 100 lines

        for j in range(start_line + 1, min(start_line + 100, len(lines))):
            line_j = lines[j].strip()
            # Check if next concept starts
            m = concept_pattern.match(line_j)
            if m:
                end_line = j
                break
            # Check for section break (e.g., "3. Almost Complex Manifolds")
            if re.match(r'^\d+\.\s+[A-Z]', line_j):
                # Only break if this is a new section, not just a numbered equation
                # Check that the previous line is empty or this is clearly a section header
                if j > 0 and lines[j-1].strip() == '':
                    end_line = j
                    break
            # Check for Q.E.D. or proof end markers
            if line_j in ['Q.E.D.', 'Q.E.D'] and j - start_line > 5:
                end_line = j + 1
                break

        concept_text = '\n'.join(lines[start_line:end_line])

        # Get the first line (the label + statement beginning)
        first_line = lines[start_line].strip()

        # Extract statement text (everything after the label on the first line, plus subsequent lines)
        m = concept_pattern.match(first_line)
        if m:
            statement_start = m.end()
            statement_first = first_line[statement_start:].strip()
        else:
            statement_first = first_line

        # Build the full statement
        full_statement_lines = [statement_first]
        for j in range(start_line + 1, end_line):
            full_statement_lines.append(lines[j])

        full_statement = '\n'.join(full_statement_lines).strip()

        # Determine chapter
        chapter = find_chapter(start_line)
        section_num = find_section(chapter, cnum)

        # Generate a title
        title = f"{ctype.capitalize()} {cnum}"
        if c['note']:
            title = f"{ctype.capitalize()} {cnum} {c['note']}"

        # Try to extract a better name from the statement
        # For definitions, use the first key term
        better_name = title
        if ctype == 'definition' or ctype == 'theorem':
            # Look for common patterns like "A ... is called a ..."
            stmt_clean = re.sub(r'\$[^$]+\$', 'X', full_statement[:200])
            stmt_clean = re.sub(r'\\[a-zA-Z]+(\{[^}]*\})*', '', stmt_clean)
            # Just use the type + number as name

        results.append({
            'line_num': start_line,
            'type': ctype,
            'number': cnum,
            'chapter': chapter,
            'section': section_num,
            'chapter_name': CHAPTER_MAP.get(chapter, ''),
            'title': title,
            'note': c.get('note', ''),
            'statement_first': statement_first,
            'full_statement': full_statement,
            'concept_text': concept_text,
            'roman': c.get('roman', ''),
        })

    return results, lines

def create_slug(concept):
    """Create a meaningful unique slug including chapter number."""
    ctype = concept['type']
    cnum = concept['number']
    chapter = concept['chapter']

    # Base slug with chapter prefix: e.g., ch1_def_1_13, ch2_thm_3_20
    roman_to_num = {'I': '1', 'II': '2', 'III': '3', 'IV': '4', 'V': '5', 'VI': '6', 'APP': 'A'}
    ch_num = roman_to_num.get(chapter, '0')
    num_clean = cnum.replace('.', '_')
    slug = f"ch{ch_num}_{ctype[:3]}_{num_clean}"

    # Try to make more semantic based on the statement
    stmt = concept['statement_first'][:150].lower()

    semantic = None
    # Try patterns specific to definitions first
    if ctype == 'definition':
        patterns = [
            (r'is called a[n]?\s+(\w[\w\s]*)', 1),
            (r'is said to be a[n]?\s+(\w[\w\s]*)', 1),
            (r'defines?\s+(?:a\s+)?(\w[\w\s]*)', 1),
            (r'let\s+(\w[\w\s]+)\s+be\s+(?:a\s+)?(\w[\w\s]*)', 2),
        ]
    else:
        patterns = [
            (r'let\s+(\w[\w\s]+)\s+be', 1),
            (r'suppose\s+that\s+(\w[\w\s]+)\s+(?:is|are|be)', 1),
            (r'if\s+(\w[\w\s]+)\s+(?:is|are)', 1),
            (r'the\s+(\w[\w\s]+)\s+(?:group|space|manifold|bundle|sheaf)', 1),
        ]

    for pat, group in patterns:
        m = re.search(pat, stmt)
        if m:
            try:
                name = m.group(group).strip()
            except IndexError:
                continue
            # Clean up LaTeX
            name = re.sub(r'\$[^$]+\$', '', name)
            name = re.sub(r'\\[a-zA-Z]+(\{[^}]*\})*', '', name)
            name = re.sub(r'[^a-z0-9\s]', '', name)
            name = re.sub(r'\s+', '_', name.strip())
            name = name.strip('_')
            if len(name) >= 5 and len(name) <= 40 and not name.startswith('ch') and name not in ('there', 'exists', 'follows', 'suppose', 'which', 'where', 'then', 'that', 'this', 'have', 'such', 'each', 'some', 'every', 'these', 'those', 'their', 'about', 'other', 'also', 'over', 'into', 'more', 'from', 'with', 'both', 'well', 'only', 'most', 'very', 'been', 'does', 'much', 'they', 'will', 'when', 'what', 'many', 'being', 'case'):
                semantic = name
                break

    if semantic:
        slug = f"{semantic}_{slug}"

    # Clean up
    slug = re.sub(r'_+', '_', slug)
    slug = slug.strip('_').lower()
    if len(slug) > 100:
        slug = slug[:100].rstrip('_')

    return slug

def write_concept_files(concept, output_dir, slug_counts=None):
    """Write the three files for a concept. Uses slug_counts to handle collisions."""
    slug = create_slug(concept)

    # Handle collisions
    if slug_counts is not None:
        if slug in slug_counts:
            slug_counts[slug] += 1
            slug = f"{slug}_{slug_counts[slug]}"
        else:
            slug_counts[slug] = 0

    concept_dir = os.path.join(output_dir, slug)
    os.makedirs(concept_dir, exist_ok=True)

    ctype = concept['type']
    title = concept['title']
    chapter = concept['chapter']
    chapter_name = concept['chapter_name']
    section = concept['section']
    domain = CHAPTER_DOMAIN.get(chapter, 'mathematics')

    # Clean the statement for LaTeX
    tex_content = extract_latex(concept['full_statement'])

    # Generate content hash
    content_hash = hashlib.sha256(tex_content.encode()).hexdigest()[:16]

    # Write concept.yaml
    yaml_data = {
        'id': slug,
        'title_en': title,
        'title_zh': '',
        'type': ctype,
        'domain': domain,
        'subdomain': chapter_name.lower().replace(' ', '_').replace("'", "")[:50],
        'difficulty': 'basic',
        'tags': [],
        'depends_on': {'required': [], 'recommended': [], 'suggested': []},
        'proof_deps': {},
        'source_books': [{
            'book_id': 'GTM065',
            'author': 'Raymond O. Wells, Jr.',
            'title': 'Differential Analysis on Complex Manifolds',
            'chapter': f'Chapter {chapter}',
            'section': str(section),
            'pages': '',
            'role_in_book': f'{ctype.capitalize()} in Chapter {chapter}, Section {section}',
        }],
        'content_hash': content_hash,
        'extraction_date': '2026-06-24',
        'extraction_agent': 'v7-10books',
    }

    yaml_path = os.path.join(concept_dir, 'concept.yaml')
    with open(yaml_path, 'w', encoding='utf-8') as f:
        yaml.dump(yaml_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    # Write theorem.tex
    tex_path = os.path.join(concept_dir, 'theorem.tex')
    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(tex_content)
        if not tex_content.endswith('\n'):
            f.write('\n')

    # Write introduce.en.md
    # Create a 2-4 sentence description
    first_line = concept['statement_first'][:200]
    type_name = ctype.capitalize()

    md_content = f"""---
id: {slug}
title: "{title}"
type: {ctype}
---

## Description

This {ctype} from Wells' "Differential Analysis on Complex Manifolds" (Chapter {chapter}: {chapter_name}, Section {section}) states:

{first_line}

This is a {ctype} in the theory of {chapter_name.lower()}, providing foundational results for the study of compact complex manifolds and related geometric structures.
"""

    md_path = os.path.join(concept_dir, 'introduce.en.md')
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)

    return slug

def main():
    print("Extracting concepts from GTM065...")
    concepts, lines = extract_concepts()

    print(f"\nTotal valid concepts: {len(concepts)}")

    # Print summary by type
    from collections import Counter
    type_counts = Counter(c['type'] for c in concepts)
    print(f"By type: {dict(type_counts)}")

    # Write all concepts
    written = 0
    slug_counts = {}
    for i, concept in enumerate(concepts):
        try:
            slug = write_concept_files(concept, OUTPUT_DIR, slug_counts)
            written += 1
            if (i+1) % 50 == 0:
                print(f"  Written {i+1}/{len(concepts)} concepts...")
        except Exception as e:
            print(f"  ERROR writing concept {concept['title']}: {e}")

    print(f"\nTotal written: {written}/{len(concepts)} concepts")

    # Write .done marker
    done_path = os.path.join(OUTPUT_DIR, '.done')
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(done_path, 'w') as f:
        f.write('DONE\n')

    print(f"\nDone marker written to {done_path}")

    # Print a few examples
    print("\n=== Sample concepts ===")
    for c in concepts[:5]:
        slug = create_slug(c)
        print(f"  {c['type'].upper()} {c['number']} -> {slug}")

if __name__ == '__main__':
    main()
