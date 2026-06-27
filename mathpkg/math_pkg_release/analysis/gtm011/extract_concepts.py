#!/usr/bin/env python3
"""
GTM011 Concept Extractor V8
Extracts all definitions, theorems, propositions, corollaries, lemmas
from stitched section files and writes 5-file concept format.
"""
import os, re, json, hashlib, sys
from pathlib import Path
from datetime import date

SECTION_DIR = "/home/a123/文档/mathpkg/pipeline_output/stitched_sections/(GTM011)Functions of One Complex Variable I"
OUTPUT_DIR = "/home/a123/文档/mathpkg/pipeline_output/math_pkg_tmp/concepts_batch2/gtm011"

TODAY = "2026-06-27"

# Chapter/section structure from GTM011 table of contents
CHAPTER_MAP = {
    "I": {"title": "The Complex Number System", "sections": {
        "1": "The real numbers", "2": "The field of complex numbers",
        "3": "The complex plane", "4": "Polar representation and roots of complex numbers",
        "5": "Lines and half planes in the complex plane",
        "6": "The extended plane and its spherical representation"}},
    "II": {"title": "Metric Spaces and the Topology of C", "sections": {
        "1": "Definition and examples of metric spaces",
        "2": "Connectedness", "3": "Sequences and completeness",
        "4": "Compactness", "5": "Continuity", "6": "Uniform convergence"}},
    "III": {"title": "Elementary Properties and Examples of Analytic Functions", "sections": {
        "1": "Power series", "2": "Analytic functions",
        "3": "Analytic functions as mapping, Möbius transformations"}},
    "IV": {"title": "Complex Integration", "sections": {
        "1": "Riemann-Stieltjes integrals",
        "2": "Power series representation of analytic functions",
        "3": "Zeros of an analytic function",
        "4": "The index of a closed curve",
        "5": "Cauchy's Theorem and Integral Formula",
        "6": "The homotopic version of Cauchy's Theorem and simple connectivity",
        "7": "Counting zeros; the Open Mapping Theorem",
        "8": "Goursat's Theorem"}},
    "V": {"title": "Singularities", "sections": {
        "1": "Classification of singularities",
        "2": "Residues", "3": "The Argument Principle"}},
    "VI": {"title": "The Maximum Modulus Theorem", "sections": {
        "1": "The Maximum Principle", "2": "Schwarz's Lemma",
        "3": "The Phragmén-Lindelöf Theorem"}},
    "VII": {"title": "Compactness and Convergence in the Space of Analytic Functions", "sections": {
        "1": "The space of continuous functions C(G,Ω)",
        "2": "Spaces of analytic functions",
        "3": "Spaces of meromorphic functions",
        "4": "The Riemann Mapping Theorem",
        "5": "Weierstrass Factorization Theorem",
        "6": "Factorization of the sine function",
        "7": "The gamma function", "8": "The Riemann zeta function"}},
    "VIII": {"title": "Runge's Theorem", "sections": {
        "1": "Runge's Theorem", "2": "Simple connectedness and rational approximation"}},
    "IX": {"title": "Analytic Continuation and Riemann Surfaces", "sections": {
        "1": "Schwarz Reflection Principle",
        "2": "Analytic Continuation Along a Path",
        "3": "Monodromy Theorem",
        "4": "Topological Spaces and Neighborhood Systems",
        "5": "The Sheaf of Germs of Analytic Functions on an Open Set",
        "6": "Analytic Manifolds",
        "7": "Covering Spaces"}},
    "X": {"title": "Harmonic Functions", "sections": {
        "1": "Basic properties of harmonic functions",
        "2": "Harmonic functions on a disk",
        "3": "Subharmonic functions",
        "4": "The Dirichlet Problem",
        "5": "Green's Function"}},
    "XI": {"title": "Entire Functions", "sections": {
        "1": "Jensen's Formula",
        "2": "The genus and order of an entire function",
        "3": "Hadamard Factorization Theorem"}},
    "XII": {"title": "The Range of an Analytic Function", "sections": {
        "1": "Bloch's Theorem",
        "2": "The Little Picard Theorem",
        "3": "Schottky's Theorem",
        "4": "The Great Picard Theorem"}},
}

def find_chapter_section(label):
    """Try to determine chapter and section from concept label like '3.5 Definition'"""
    # The section files already have chapter context from their content
    # We'll map by looking at surrounding context
    return None, None

def slugify(text):
    """Create semantic English slug from concept title."""
    # Remove LaTeX, keep only meaningful words
    text = re.sub(r'\$[^$]+\$', '', text)
    text = re.sub(r'\\[a-zA-Z]+', '', text)
    text = re.sub(r'[^a-zA-Z0-9\s-]', '', text)
    text = text.lower().strip()
    words = text.split()
    # Take up to 6 meaningful words
    meaningful = [w for w in words if len(w) > 2 and w not in
                  {'the', 'and', 'for', 'all', 'has', 'are', 'was', 'its',
                   'not', 'but', 'can', 'that', 'this', 'with', 'from', 'let',
                   'each', 'any', 'set', 'also', 'then', 'such', 'some', 'have'}]
    slug = '-'.join(meaningful[:6])
    return slug if slug else 'unnamed-concept'

def extract_concepts_from_file(filepath):
    """Extract all numbered concepts from a section file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    concepts = []
    # Pattern: number.number ConceptType.
    # Also match single numbers for Chapter-level concepts
    pattern = r'(?:(?:^|\n)\s*)(\d+\.\d+)\s+(Definition|Theorem|Proposition|Corollary|Lemma)\.\s+'
    # Also match Orientation Principle, etc.
    pattern2 = r'(?:(?:^|\n)\s*)(\d+\.\d+)\s+(Orientation\s+Principle)\.'

    for match in re.finditer(pattern, content):
        num = match.group(1)
        ctype = match.group(2).lower()
        start = match.end()

        # Find the statement text - go until next numbered concept or section break
        # Find next occurrence of a numbered concept or chapter header
        next_pattern = r'(?:\n\s*\d+\.\d+\s+(?:Definition|Theorem|Proposition|Corollary|Lemma|Orientation Principle)\.|Chapter\s+[IVX]+|\$\d+\.\s+)'
        next_match = re.search(next_pattern, content[start:])
        if next_match:
            stmt_end = start + next_match.start()
        else:
            stmt_end = min(start + 3000, len(content))

        statement = content[start:stmt_end].strip()

        # Clean up - remove proof text if present
        proof_idx = statement.find('\nProof.')
        if proof_idx > 0:
            statement = statement[:proof_idx].strip()

        # Truncate at reasonable length
        if len(statement) > 2000:
            # Try to find a natural break
            break_point = statement[:2000].rfind('\n\n')
            if break_point > 200:
                statement = statement[:break_point].strip()
            else:
                statement = statement[:2000].strip()

        # Build a title
        title = f"{num} {ctype.capitalize()}"
        slug = f"{ctype}-{num.replace('.', '-')}"

        concepts.append({
            'num': num,
            'type': ctype,
            'title': title,
            'statement': statement,
            'slug': slug,
            'has_proof': ctype in ('theorem', 'proposition', 'corollary', 'lemma'),
            'start_pos': match.start()
        })

    return concepts

def determine_chapter_section(content_before, concept_num):
    """Determine chapter and section from content before the concept."""
    # Look for Chapter headers
    ch_match = re.search(r'Chapter\s+([IVX]+)', content_before)
    if ch_match:
        ch_roman = ch_match.group(1)
        ch_num = roman_to_int(ch_roman)
        ch_key = ch_roman
        if ch_key in CHAPTER_MAP:
            ch_title = CHAPTER_MAP[ch_key]['title']
            # Try to find section
            sec_match = re.search(r'§(\d+)\.', content_before[-2000:])
            if sec_match:
                sec_num = sec_match.group(1)
                if sec_num in CHAPTER_MAP[ch_key]['sections']:
                    sec_title = CHAPTER_MAP[ch_key]['sections'][sec_num]
                    return f"{ch_title}", f"{sec_num}. {sec_title}"
            # Fallback: determine section from concept number
            parts = concept_num.split('.')
            if len(parts) == 2 and parts[0] in CHAPTER_MAP[ch_key]['sections']:
                sec_title = CHAPTER_MAP[ch_key]['sections'][parts[0]]
                return f"{ch_title}", f"{parts[0]}. {sec_title}"
            return f"{ch_title}", ""
    return "", ""

def roman_to_int(roman):
    vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
    result = 0
    prev = 0
    for c in reversed(roman):
        v = vals.get(c, 0)
        if v >= prev:
            result += v
        else:
            result -= v
        prev = v
    return result

def write_concept_files(concept, output_dir, filepath, content, concept_idx):
    """Write concept.yaml, theorem.tex, introduce.en.md, and optionally proof/exercise files."""
    slug = concept['slug']
    concept_dir = os.path.join(output_dir, slug)
    os.makedirs(concept_dir, exist_ok=True)

    # Get chapter/section context
    content_before = content[:concept['start_pos']] if concept['start_pos'] < len(content) else content
    chapter, section = determine_chapter_section(content_before, concept['num'])

    # Determine domain/subdomain
    stmt_lower = concept['statement'].lower()
    if any(w in stmt_lower for w in ['analytic', 'complex', 'holomorphic', 'entire', 'harmonic', 'meromorphic',
                                       'möbius', 'cauchy', 'power series', 'laurent', 'residue', 'pole',
                                       'singularity', 'branch', 'logarithm', 'conformal', 'riemann']):
        domain = "analysis"
        subdomain = "complex-analysis"
    elif any(w in stmt_lower for w in ['metric', 'topology', 'compact', 'connected', 'continuous',
                                         'open set', 'closed', 'limit', 'converge', 'dense', 'hausdorff']):
        domain = "topology"
        subdomain = "general-topology"
    else:
        domain = "analysis"
        subdomain = "complex-analysis"

    # Difficulty heuristic
    if concept['type'] in ('definition', 'lemma'):
        difficulty = "basic"
    elif concept['type'] == 'proposition':
        difficulty = "intermediate"
    else:
        difficulty = "intermediate"

    # 1. concept.yaml
    yaml_content = f"""id: {slug}
title_en: "{concept['title']}"
title_zh: ""
type: {concept['type']}
domain: {domain}
subdomain: {subdomain}
difficulty: {difficulty}
tags: []
depends_on:
  required: []
  recommended: []
  suggested: []
source_books:
  - book_id: "gtm011"
    author: "John B. Conway"
    title: "Functions of One Complex Variable I"
    chapter: "{chapter}"
    section: "{section}"
    pages: ""
    role_in_book: ""
content_hash: ""
extraction_date: "{TODAY}"
extraction_agent: "v8-full-extract"
"""
    with open(os.path.join(concept_dir, 'concept.yaml'), 'w', encoding='utf-8') as f:
        f.write(yaml_content)

    # 2. theorem.tex - pure statement
    tex_content = concept['statement']
    with open(os.path.join(concept_dir, 'theorem.tex'), 'w', encoding='utf-8') as f:
        f.write(tex_content)

    # 3. introduce.en.md
    intro = f"""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

{concept['title']} from Conway's "Functions of One Complex Variable I."
{concept['statement'][:300].strip()}...
"""
    with open(os.path.join(concept_dir, 'introduce.en.md'), 'w', encoding='utf-8') as f:
        f.write(intro)

    # 4. proof file for non-definition/axiom types
    if concept['has_proof']:
        # Look for proof in original content
        after_stmt = content[concept['start_pos']:]
        proof_match = re.search(r'\nProof\.\s+', after_stmt)
        proof_text = ""
        if proof_match:
            proof_start = proof_match.start()
            # Find end of proof (next numbered concept or next Proof. or Chapter)
            after_proof_start = after_stmt[proof_start + len(proof_match.group()):]
            end_match = re.search(r'\n\s*\d+\.\d+\s+(?:Definition|Theorem|Proposition|Corollary|Lemma)\.', after_proof_start)
            if end_match:
                proof_text = after_stmt[proof_start:proof_start + len(proof_match.group()) + end_match.start()].strip()
            else:
                proof_text = after_stmt[proof_start:proof_start + len(proof_match.group()) + min(len(after_proof_start), 3000)].strip()

        # Build chapter.section for filename
        ch_sec = section.replace('. ', '_').replace('.', '_') if section else "Ch_Sec"

        proof_fn = f"proof_gtm011_{ch_sec}.en.md"
        proof_yaml = f"""---
role: proof
locale: en
of_concept: {slug}
source_book: gtm011
source_chapter: "{chapter}"
source_section: "{section}"
---

{proof_text if proof_text else '(Proof to be extracted from source text.)'}
"""
        with open(os.path.join(concept_dir, proof_fn), 'w', encoding='utf-8') as f:
            f.write(proof_yaml)

    return concept_dir

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    section_files = sorted(Path(SECTION_DIR).glob('s*.md'))
    section_files = [f for f in section_files if f.name != '_manifest.json']

    print(f"Processing {len(section_files)} section files...")

    all_concepts = []
    for sf in section_files:
        concepts = extract_concepts_from_file(str(sf))
        if concepts:
            print(f"  {sf.name}: {len(concepts)} concepts")

        with open(sf, 'r', encoding='utf-8') as f:
            content = f.read()

        for i, concept in enumerate(concepts):
            try:
                write_concept_files(concept, OUTPUT_DIR, str(sf), content, i)
                all_concepts.append(concept['slug'])
            except Exception as e:
                print(f"    ERROR writing {concept['slug']}: {e}")

    print(f"\nTotal concepts extracted: {len(all_concepts)}")

    # Write done marker
    done_file = os.path.join(OUTPUT_DIR, '.done')
    with open(done_file, 'w') as f:
        f.write(f"DONE - {TODAY} - {len(all_concepts)} concepts extracted\n")
    print(f"Done marker written to {done_file}")

if __name__ == '__main__':
    main()
