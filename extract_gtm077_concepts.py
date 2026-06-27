#!/usr/bin/env python3
"""
Extract ALL theorems, definitions, lemmas, propositions, corollaries, axioms
from GTM077 (Lectures on the Theory of Algebraic Numbers by Erich Hecke).

Reads all 31 stitched section files, identifies formal concepts,
and writes 3-file output (concept.yaml, theorem.tex, introduce.en.md)
for each concept.
"""

import os
import re
import yaml
import hashlib
from pathlib import Path

SECTION_DIR = "/home/a123/文档/mathpkg/pipeline_output/stitched_sections/(GTM077)Lectures on the Theory of Algebraic Numbers"
OUTPUT_BASE = "/home/a123/文档/mathpkg/pipeline_output/concepts_v7/gtm077"

# Book metadata
BOOK_ID = "gtm077"
BOOK_AUTHOR = "Erich Hecke"
BOOK_TITLE = "Lectures on the Theory of Algebraic Numbers"
EXTRACTION_DATE = "2026-06-25"
EXTRACTION_AGENT = "v7-section-test"

# Domain mapping
DOMAIN_MAP = {
    "algebra": ["group", "field", "ring", "module", "ideal", "polynomial", "basis",
                 "cyclic", "abelian", "character", "subgroup", "factor", "quotient",
                 "irreducible", "primitive", "discriminant", "norm", "unit", "conjugate",
                 "integer", "algebraic", "extension", "galois", "fundamental"],
    "number-theory": ["prime", "divisor", "gcd", "congruence", "residue", "quadratic",
                      "reciprocity", "zeta", "class-number", "power-residue", "gauss-sum",
                      "legendre", "jacobi", "euler", "fermat", "minkowski", "dirichlet",
                      "cyclotomic", "rational", "modulus", "coprime", "relatively-prime"],
    "analysis": ["theta-function", "fourier", "density", "limit", "infinite-series",
                 "logarithm", "absolute-value", "converge"],
}

def classify_domain(text):
    """Classify the mathematical domain based on text content."""
    text_lower = text.lower()
    nt_score = sum(1 for kw in DOMAIN_MAP["number-theory"] if kw in text_lower)
    alg_score = sum(1 for kw in DOMAIN_MAP["algebra"] if kw in text_lower)
    ana_score = sum(1 for kw in DOMAIN_MAP["analysis"] if kw in text_lower)

    if nt_score >= alg_score and nt_score >= ana_score:
        return "number-theory"
    elif alg_score >= ana_score:
        return "algebra"
    else:
        return "analysis"

def classify_subdomain(text):
    """Determine subdomain based on text."""
    text_lower = text.lower()
    if "group" in text_lower:
        if "character" in text_lower:
            return "group-characters"
        if "abelian" in text_lower:
            return "abelian-groups"
        return "group-theory"
    if "ideal" in text_lower:
        if "class" in text_lower:
            return "ideal-class-group"
        if "prime" in text_lower:
            return "prime-ideals"
        return "ideal-theory"
    if "reciprocity" in text_lower:
        return "quadratic-reciprocity"
    if "gauss" in text_lower and "sum" in text_lower:
        return "gauss-sums"
    if "quadratic" in text_lower:
        if "field" in text_lower:
            return "quadratic-fields"
        return "quadratic-residues"
    if "congruence" in text_lower:
        return "congruences"
    if "prime" in text_lower:
        return "prime-numbers"
    if "field" in text_lower or "algebraic" in text_lower:
        return "algebraic-number-fields"
    if "unit" in text_lower:
        return "units"
    if "discriminant" in text_lower:
        return "discriminants"
    if "norm" in text_lower:
        return "norms"
    if "polynomial" in text_lower:
        return "polynomials"
    if "theta" in text_lower or "zeta" in text_lower:
        return "transcendental-methods"
    if "density" in text_lower:
        return "density-theorems"
    if "decomposition" in text_lower:
        return "decomposition-laws"
    return "general"

def classify_difficulty(text):
    """Estimate difficulty level."""
    if any(kw in text.lower() for kw in ["reciprocity", "gauss sum", "class field",
                                           "theta function", "zeta-function"]):
        return "advanced"
    if any(kw in text.lower() for kw in ["ideal", "galois", "discriminant", "relative",
                                           "decomposition", "character", "fundamental unit"]):
        return "intermediate"
    return "basic"

def make_slug(text, concept_type, number=None):
    """Create a semantic English slug."""
    text_lower = text.lower()

    # Try to extract a meaningful name from the text
    # Pattern-based slug generation
    name_map = {
        "group": "group-definition",
        "number field": "number-field-definition",
        "module": "module-definition",
        "basis": "basis-of-abelian-group",
        "character": "group-character-definition",
        "coset": "coset-definition",
        "prime ideal": "prime-ideal-definition",
        "discriminant": "discriminant-definition",
        "norm": "norm-definition",
        "unit": "unit-definition",
        "integer": "algebraic-integer-definition",
        "primitive polynomial": "primitive-polynomial-definition",
        "residue character": "residue-character-definition",
        "conjugate": "conjugate-definition",
        "ideal": "ideal-definition",
        "fundamental system": "fundamental-system-definition",
        "subgroup": "subgroup-definition",
        "irreducible": "irreducible-definition",
    }

    for key, slug in name_map.items():
        if key in text_lower and concept_type == "definition":
            return slug

    # For theorems, use numbered naming
    if number:
        return f"theorem-{number}"

    # Fallback: hash-based
    hash_val = hashlib.md5(text.encode()).hexdigest()[:8]
    return f"{concept_type}-{hash_val}"

def clean_latex(text):
    """Clean up LaTeX artifacts."""
    # Fix common OCR issues
    text = text.replace('$$', '$$')  # normalize display math
    # Remove excess whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def extract_statement_from_text(full_text, marker_start, next_marker=None):
    """Extract the statement part of a concept.

    The statement is the text from the marker until either:
    - The next formal concept marker
    - The end of a proof-like section
    - The end of the text
    """
    # Find where the actual statement begins (after the marker label)
    # Look for the first substantive mathematical content

    # Try to find the end of the statement - typically marked by "Proof",
    # "proof", or the next theorem/definition marker
    end_markers = [
        r'\n\s*Proof[\.\s]',
        r'\n\s*proof[\.\s]',
        r'\n\s*\*\*Theorem',
        r'\n\s*\*\*Definition',
        r'\n\s*\*\*Lemma',
        r'\n\s*\*\*Proposition',
        r'\n\s*\*\*Corollary',
        r'\n\s*Theorem \d+',
        r'\n\s*Definition[\.\s]',
        r'\n\s*Lemma[\.\s]',
        r'\n\s*§\d+',
    ]

    end_pos = len(full_text)
    for marker in end_markers:
        m = re.search(marker, full_text)
        if m and m.start() < end_pos:
            end_pos = m.start()

    statement = full_text[:end_pos].strip()
    return statement

def parse_section(filepath):
    """Parse a section file and extract all concepts."""
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    section_filename = os.path.basename(filepath)
    # Extract section label from filename
    section_match = re.match(r's(\d+)_(\d+)_(.+)\.md', section_filename)
    if section_match:
        section_num = section_match.group(1)
        section_label = section_match.group(3).replace('_', ' ')
    else:
        section_num = "??"
        section_label = section_filename

    concepts = []

    # Pattern 1: **Theorem N.** or **Theorem N:**
    # Match formal, numbered theorems
    for m in re.finditer(r'\*\*Theorem\s+(\d+)[\.\:]\s*\*\*\s*(.*?)(?=\n\s*\*\*Theorem|\n\s*\*\*Definition|\n\s*\*\*Lemma|\n\s*§|$)', text, re.DOTALL):
        number = m.group(1)
        rest = m.group(2).strip()

        # Extract the statement portion
        # Try to stop before "Proof" or next concept
        proof_match = re.search(r'\n\s*Proof[\.\s]', rest)
        next_concept = re.search(r'\n\s*\*\*(?:Theorem|Definition|Lemma|Proposition|Corollary)', rest)

        end_idx = len(rest)
        if proof_match:
            end_idx = min(end_idx, proof_match.start())
        if next_concept:
            end_idx = min(end_idx, next_concept.start())

        statement = rest[:end_idx].strip()

        concepts.append({
            'type': 'theorem',
            'number': int(number),
            'slug': f'theorem-{number}',
            'title_en': f'Theorem {number}',
            'statement': statement,
            'section': section_label,
            'section_file': section_filename,
        })

    # Pattern 2: **Definition.** (unnumbered definitions)
    for m in re.finditer(r'\*\*Definition[\.\:]\s*\*\*\s*(.*?)(?=\n\s*\*\*Theorem|\n\s*\*\*Definition|\n\s*\*\*Lemma|\n\s*§|$)', text, re.DOTALL):
        rest = m.group(1).strip()

        # Clean up
        end_idx = len(rest)
        next_concept = re.search(r'\n\s*\*\*(?:Theorem|Definition|Lemma|Proposition|Corollary)', rest)
        if next_concept:
            end_idx = min(end_idx, next_concept.start())

        statement = rest[:end_idx].strip()

        slug = make_slug(statement, 'definition')

        concepts.append({
            'type': 'definition',
            'number': None,
            'slug': slug,
            'title_en': statement.split('.')[0].strip() if '.' in statement[:80] else statement[:80].strip(),
            'statement': statement,
            'section': section_label,
            'section_file': section_filename,
        })

    # Pattern 3: **Lemma.** or **Lemma (a).**
    for m in re.finditer(r'\*\*Lemma\s*(?:\([a-z]\))?[\.\:]\s*\*\*\s*(.*?)(?=\n\s*\*\*Theorem|\n\s*\*\*Definition|\n\s*\*\*Lemma|\n\s*§|$)', text, re.DOTALL):
        rest = m.group(1).strip()

        end_idx = len(rest)
        next_concept = re.search(r'\n\s*\*\*(?:Theorem|Definition|Lemma|Proposition|Corollary)', rest)
        if next_concept:
            end_idx = min(end_idx, next_concept.start())

        statement = rest[:end_idx].strip()

        # Determine lemma label
        lemma_label = m.group(0).split('**')[1] if '**' in m.group(0) else ''

        concepts.append({
            'type': 'lemma',
            'number': None,
            'slug': f"lemma-{hashlib.md5(statement.encode()).hexdigest()[:8]}",
            'title_en': statement.split('.')[0].strip()[:80] if '.' in statement[:80] else statement[:80].strip(),
            'statement': statement,
            'section': section_label,
            'section_file': section_filename,
        })

    # Pattern 4: **Proposition** or **Corollary**
    for concept_type in ['proposition', 'corollary']:
        for m in re.finditer(rf'\*\*{concept_type.title()}\s*[\.\:]\s*\*\*\s*(.*?)(?=\n\s*\*\*Theorem|\n\s*\*\*Definition|\n\s*\*\*Lemma|\n\s*\*\*Proposition|\n\s*\*\*Corollary|\n\s*§|$)', text, re.DOTALL):
            rest = m.group(1).strip()

            end_idx = len(rest)
            next_concept = re.search(r'\n\s*\*\*(?:Theorem|Definition|Lemma|Proposition|Corollary)', rest)
            if next_concept:
                end_idx = min(end_idx, next_concept.start())

            statement = rest[:end_idx].strip()

            concepts.append({
                'type': concept_type,
                'number': None,
                'slug': f"{concept_type}-{hashlib.md5(statement.encode()).hexdigest()[:8]}",
                'title_en': statement.split('.')[0].strip()[:80] if '.' in statement[:80] else statement[:80].strip(),
                'statement': statement,
                'section': section_label,
                'section_file': section_filename,
            })

    # Pattern 5: Plain "Theorem N." (not bold) - common in this book
    for m in re.finditer(r'(?<!\*)Theorem\s+(\d+)[\.\:]\s+(.*?)(?=\n(?:Theorem\s+\d+|Definition[\.\s]|Lemma[\.\s]|§\d+|Proof[\.\s]))', text, re.DOTALL):
        number = m.group(1)
        rest = m.group(2).strip()

        # Skip if already captured as bold
        full_match = m.group(0)
        bold_pattern = f"**Theorem {number}"
        if bold_pattern in text[max(0, m.start()-20):m.end()]:
            continue

        end_idx = len(rest)
        proof_match = re.search(r'\n\s*Proof[\.\s]', rest)
        if proof_match:
            end_idx = min(end_idx, proof_match.start())

        statement = rest[:end_idx].strip()

        concepts.append({
            'type': 'theorem',
            'number': int(number),
            'slug': f'theorem-{number}',
            'title_en': f'Theorem {number}',
            'statement': statement,
            'section': section_label,
            'section_file': section_filename,
        })

    # Pattern 6: Plain "Definition." (not bold)
    for m in re.finditer(r'(?<!\*)Definition[\.\:]\s+(.*?)(?=\n(?:Theorem\s+\d+|Definition[\.\s]|Lemma[\.\s]|§\d+|Proof[\.\s]))', text, re.DOTALL):
        rest = m.group(1).strip()

        # Skip if already bold
        if "**Definition" in text[max(0, m.start()-5):m.start()+15]:
            continue

        # Skip very short matches (false positives)
        if len(rest) < 20:
            continue

        end_idx = len(rest)
        next_pattern = re.search(r'\n(?:Theorem\s+\d+|Definition[\.\s]|Lemma[\.\s])', rest)
        if next_pattern:
            end_idx = min(end_idx, next_pattern.start())

        statement = rest[:end_idx].strip()

        concepts.append({
            'type': 'definition',
            'number': None,
            'slug': f"definition-{hashlib.md5(statement.encode()).hexdigest()[:8]}",
            'title_en': statement.split('.')[0].strip()[:80],
            'statement': statement,
            'section': section_label,
            'section_file': section_filename,
        })

    # Deduplicate
    seen = set()
    unique = []
    for c in concepts:
        key = (c['type'], c.get('number'), c['statement'][:100])
        if key not in seen:
            seen.add(key)
            unique.append(c)

    return unique

def write_concept_files(concept, output_dir):
    """Write the 3 files for a concept."""
    slug = concept['slug']
    slug_dir = os.path.join(output_dir, slug)
    os.makedirs(slug_dir, exist_ok=True)

    statement = concept['statement']
    domain = classify_domain(statement)
    subdomain = classify_subdomain(statement)
    difficulty = classify_difficulty(statement)
    content_hash = hashlib.md5(statement.encode()).hexdigest()[:12]

    # FILE 1: concept.yaml
    yaml_data = {
        'id': slug,
        'title_en': concept['title_en'],
        'title_zh': '',
        'type': concept['type'],
        'domain': domain,
        'subdomain': subdomain,
        'difficulty': difficulty,
        'tags': [],
        'depends_on': {
            'required': [],
            'recommended': [],
            'suggested': []
        },
        'source_books': [{
            'book_id': BOOK_ID,
            'author': BOOK_AUTHOR,
            'title': BOOK_TITLE,
            'chapter': '',
            'section': concept['section'],
            'pages': '',
            'role_in_book': ''
        }],
        'content_hash': content_hash,
        'extraction_date': EXTRACTION_DATE,
        'extraction_agent': EXTRACTION_AGENT
    }

    yaml_path = os.path.join(slug_dir, 'concept.yaml')
    with open(yaml_path, 'w', encoding='utf-8') as f:
        yaml.dump(yaml_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    # FILE 2: theorem.tex
    # Clean up the statement for LaTeX
    tex_statement = statement
    # Fix display math
    tex_statement = re.sub(r'(?<!\$)\$\$(?!\$)', r'$$', tex_statement)
    # Remove any "Proof" remnants
    tex_statement = re.sub(r'\n\s*Proof[\.\s].*$', '', tex_statement, flags=re.DOTALL)

    tex_path = os.path.join(slug_dir, 'theorem.tex')
    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(tex_statement + '\n')

    # FILE 3: introduce.en.md
    intro_text = f"""---
role: introduce
locale: en
content_hash: "{content_hash}"
written_against: ""
---

This is {concept['type'].title()} {concept.get('number', '')} from {BOOK_TITLE} by {BOOK_AUTHOR}.

{statement[:300]}

This {'result' if concept['type'] == 'theorem' else 'concept'} is part of the foundational material in algebraic number theory, appearing in the section on {concept['section']}.
"""

    intro_path = os.path.join(slug_dir, 'introduce.en.md')
    with open(intro_path, 'w', encoding='utf-8') as f:
        f.write(intro_text)

    return slug_dir

def main():
    # List all section files
    section_files = sorted([
        f for f in os.listdir(SECTION_DIR)
        if f.startswith('s') and f.endswith('.md') and f != '_manifest.json'
    ])

    print(f"Found {len(section_files)} section files")

    all_concepts = []
    for sf in section_files:
        filepath = os.path.join(SECTION_DIR, sf)
        print(f"Parsing {sf}...")
        concepts = parse_section(filepath)
        print(f"  Found {len(concepts)} concepts")
        all_concepts.extend(concepts)

    print(f"\nTotal concepts found: {len(all_concepts)}")

    # Count by type
    from collections import Counter
    type_counts = Counter(c['type'] for c in all_concepts)
    for t, count in type_counts.most_common():
        print(f"  {t}: {count}")

    # Write all concept files
    written = 0
    for concept in all_concepts:
        try:
            slug_dir = write_concept_files(concept, OUTPUT_BASE)
            written += 1
        except Exception as e:
            print(f"Error writing concept {concept.get('slug', 'unknown')}: {e}")

    print(f"\nWrote {written} concept triples to {OUTPUT_BASE}")

    # Write .done marker (but note the exact path from the instructions)
    done_dir = os.path.join(OUTPUT_BASE)
    os.makedirs(done_dir, exist_ok=True)

    return all_concepts

if __name__ == '__main__':
    main()
