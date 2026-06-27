#!/usr/bin/env python3
"""
V8 Concept Extractor for GTM029 (Commutative Algebra Volume II, Zariski-Samuel).
Processes all 29 stitched sections, extracts theorems/definitions/lemmas/propositions/
corollaries/axioms, and writes structured output files.
"""
import os, re, json, hashlib, yaml, sys
from datetime import date
from pathlib import Path

# ─── CONFIGURATION ───
BOOK_ID = "gtm029"
AUTHORS = "Oscar Zariski, Pierre Samuel"
BOOK_TITLE = "Commutative Algebra Volume II"
SECTIONS_DIR = "/home/a123/文档/mathpkg/pipeline_output/stitched_sections/(GTM029)Commutative Algebra Volume II"
OUTPUT_BASE = "/home/a123/文档/mathpkg/pipeline_output/math_pkg_tmp/concepts_batch3/gtm029"
EXTRACTION_DATE = "2026-06-27"
EXTRACTION_AGENT = "v8-full-extract"

# ─── SECTION MAPPING ───
# Maps section file prefix -> (chapter, section_number, label)
# Chapter in Roman numerals, section number as string
SECTION_MAP = {
    "s001": ("VI", "2", "Places"),
    "s002": ("VI", "4", "Existence of places"),
    "s003": ("VI", "7", "The case of an algebraic field extension"),
    "s004": ("VI", "9", "Places and valuations"),
    "s005": ("VI", "13", "Classical ideal theory and valuations"),
    "s006": ("VI", "16", "An existence theorem for composite centered valuations"),
    "s007": ("VI", "17", "The abstract Riemann surface of a field"),
    "s008": ("VII", "1-2", "Polynomial and power series rings"),
    "s009": ("VII", "3", "Algebraic varieties in the affine space"),
    "s010": ("VII", "5", "Relations between non-homogeneous and homogeneous ideals"),
    "s011": ("VII", "8", "Special dimension-theoretic properties of polynomial rings"),
    "s012": ("VII", "11", "Extension of the ground field"),
    "s013": ("VII", "13", "Chains of syzygies"),
    "s014": ("VIII", "1", "The method of associated graded rings"),
    "s015": ("VIII", "5", "Comparison of topologies in a noetherian ring"),
    "s016": ("VIII", "7", "Hensel's lemma and applications"),
    "s017": ("VIII", "9", "Dimension theory. Systems of parameters"),
    "s018": ("VIII", "10", "Theory of multiplicities"),
    "s019": ("VIII", "11", "Regular local rings"),
    "s020": ("VIII", "12", "Structure of complete local rings and applications"),
    "s021": ("Appendix", "1", "Relations between prime ideals in a noetherian domain"),
    "s022": ("Appendix", "2", "Valuations in noetherian domains"),
    "s023": ("Appendix", "3", "Valuation ideals"),
    "s024": ("Appendix", "4", "Complete modules and ideals"),
    "s025": ("Appendix", "5", "Complete ideals in regular local rings of dimension 2"),
    "s026": ("Appendix", "5", "Complete ideals in regular local rings of dimension 2"),
    "s027": ("Appendix", "5", "Complete ideals in regular local rings of dimension 2"),
    "s028": ("Appendix", "7", "Unique factorization in regular local rings"),
}

# ─── CONCEPT TYPE PATTERNS ───
# Ordered by priority - more specific patterns first
CONCEPT_PATTERNS = [
    # Format: (regex, type, capture_groups)
    (r'\b(?:THEOREM|Theorem)\s+(\d+(?:\s*[′\'](?:\s*[′\'])?)?)\b', 'theorem'),
    (r'\b(?:DEFINITION|Definition)\s+(\d+(?:\s*[′\'](?:\s*[′\'])?)?)\b', 'definition'),
    (r'\b(?:LEMMA|Lemma)\s+(\d+(?:\s*[′\'](?:\s*[′\'])?)?)\b', 'lemma'),
    (r'\b(?:PROPOSITION|Proposition)\s+(\d+(?:\s*[′\'](?:\s*[′\'])?)?)\b', 'proposition'),
    (r'\b(?:COROLLARY|Corollary)\s+(\d+(?:\s*[′\'](?:\s*[′\'])?)?)\b', 'corollary'),
    (r'\b(?:AXIOM|Axiom)\s+(\d+(?:\s*[′\'](?:\s*[′\'])?)?)\b', 'axiom'),
]

# Also match unnumbered concepts
UNNUMBERED_PATTERNS = [
    (r'\b(THEOREM)\b', 'theorem'),
    (r'\b(DEFINITION)\b', 'definition'),
    (r'\b(LEMMA)\b', 'lemma'),
    (r'\b(PROPOSITION)\b', 'proposition'),
    (r'\b(COROLLARY)\b', 'corollary'),
]

# Proof markers
PROOF_START_PATTERNS = [
    r'\bPROOF\b[.:]?',
    r'\bProof\b[.:]?',
    r'\bproof\b[.:]?',
]

PROOF_END_MARKERS = [
    r'\bQ\.E\.D\.',
    r'\bQED\b',
    r'\bq\.e\.d\.',
]

# ─── HELPER FUNCTIONS ───

def slugify(text):
    """Create semantic lowercase-hyphen English slug."""
    # Remove LaTeX math for slug purposes
    clean = re.sub(r'\$[^$]*\$', '', text)
    clean = re.sub(r'\\[a-zA-Z]+', '', clean)
    # Remove special chars, keep alphanumeric and spaces
    clean = re.sub(r'[^\w\s-]', '', clean)
    # Normalize whitespace
    clean = re.sub(r'\s+', ' ', clean).strip().lower()
    # Truncate to reasonable length
    words = clean.split()[:10]
    slug = '-'.join(words)
    # Replace multiple hyphens
    slug = re.sub(r'-+', '-', slug)
    return slug[:80].strip('-')


def determine_domain_subdomain(chapter, section_label):
    """Determine domain and subdomain from chapter context."""
    if chapter == "VI":
        return "algebra", "valuation-theory"
    elif chapter == "VII":
        return "algebra", "polynomial-rings"
    elif chapter == "VIII":
        return "algebra", "local-algebra"
    elif chapter == "Appendix":
        return "algebra", "commutative-algebra"
    return "algebra", "commutative-algebra"


def determine_difficulty(concept_type, chapter):
    """Heuristic difficulty determination."""
    if chapter in ("VI",):
        return "advanced"  # Valuation theory is advanced
    if chapter == "VII" and concept_type in ("theorem", "lemma"):
        return "intermediate"
    if chapter == "VIII":
        return "advanced"
    return "intermediate"


def extract_statement_and_proof(full_text, concept_pattern, start_pos):
    """
    Extract the statement and proof for a concept.
    Returns (statement, proof_text, end_pos)
    """
    # Find the end of the statement and start of proof
    remaining = full_text[start_pos:]

    # Look for "PROOF" or "Proof" marker
    proof_match = None
    for pattern in PROOF_START_PATTERNS:
        m = re.search(pattern, remaining)
        if m:
            proof_match = m
            break

    if proof_match:
        statement_text = remaining[:proof_match.start()].strip()
        proof_start = proof_match.end()

        # Now find end of proof
        after_proof = remaining[proof_start:]
        proof_end = len(after_proof)
        for pattern in PROOF_END_MARKERS:
            m = re.search(pattern, after_proof)
            if m:
                proof_end = m.end()
                break

        # Also check for next concept as proof boundary
        for ctype_pattern, _ in CONCEPT_PATTERNS + UNNUMBERED_PATTERNS:
            m = re.search(ctype_pattern, after_proof[:proof_end])
            # Not a great heuristic... let's just use QED markers

        proof_text = after_proof[:proof_end].strip()

        # Calculate absolute end position
        abs_proof_end = start_pos + proof_match.start() + proof_start + proof_end
    else:
        # No explicit proof marker found - likely a definition
        # Statement goes until next concept or end
        statement_text = remaining.strip()
        proof_text = ""
        abs_proof_end = start_pos + len(remaining)

    return statement_text, proof_text, abs_proof_end


def find_all_concepts(text):
    """Find all concept boundaries in the text."""
    concepts = []

    # Find all potential concept starts
    for pattern, ctype in CONCEPT_PATTERNS:
        for m in re.finditer(pattern, text):
            concepts.append({
                'type': ctype,
                'number': m.group(1).strip() if m.lastindex and m.lastindex >= 1 else '',
                'start': m.start(),
                'match_text': m.group(0),
            })

    # Sort by position
    concepts.sort(key=lambda x: x['start'])

    # Remove duplicates (same position)
    filtered = []
    seen_positions = set()
    for c in concepts:
        if c['start'] not in seen_positions:
            # Check if it's a real concept (not just mentioned in passing)
            # Better check: look at context
            filtered.append(c)
            seen_positions.add(c['start'])

    return filtered


def extract_concept_text(text, concept_start, next_concept_start=None):
    """Extract the text for a concept between its start and the next concept."""
    if next_concept_start:
        return text[concept_start:next_concept_start].strip()
    else:
        return text[concept_start:].strip()


def create_title_en(concept_type, number, context_text, section_label):
    """Create a canonical English title."""
    # Take first sentence or first 100 chars
    first_sentence = re.split(r'(?<=[.!?])\s+', context_text)[0]
    if len(first_sentence) > 120:
        first_sentence = first_sentence[:117] + "..."

    if number:
        prefix = f"{concept_type.capitalize()} {number}"
    else:
        prefix = concept_type.capitalize()

    title = f"{prefix}: {first_sentence.strip()}"
    # Clean up
    title = re.sub(r'\s+', ' ', title)
    return title[:200]


def generate_slug(concept_type, number, section_chapter, section_num, context_text):
    """Generate a semantic slug for the concept."""
    # Extract key terms from the context
    clean = re.sub(r'\$[^$]*\$', 'MATH', context_text)
    clean = re.sub(r'\\[a-zA-Z]+\{([^}]*)\}', r'\1', clean)
    clean = re.sub(r'\\[a-zA-Z]+', '', clean)
    clean = re.sub(r'[^a-zA-Z\s-]', '', clean)
    clean = re.sub(r'\s+', ' ', clean).strip()

    words = [w.lower() for w in clean.split() if len(w) > 2]

    # Take meaningful words
    stopwords = {'the', 'and', 'for', 'let', 'are', 'any', 'all', 'has', 'had', 'was',
                 'that', 'this', 'with', 'from', 'have', 'been', 'will', 'can', 'not',
                 'but', 'its', 'their', 'they', 'also', 'may', 'such', 'into', 'some',
                 'then', 'there', 'each', 'which', 'when', 'where', 'over', 'here',
                 'these', 'those', 'more', 'only', 'other', 'shall', 'every', 'what',
                 'does', 'being'}
    meaningful = [w for w in words if w not in stopwords][:8]

    if number:
        slug = f"{concept_type}-{number}-{'-'.join(meaningful)}"
    else:
        slug = f"{concept_type}-{'-'.join(meaningful)}"

    # Clean up
    slug = re.sub(r'-+', '-', slug)
    slug = re.sub(r'[^a-z0-9-]', '', slug)
    return slug[:80].strip('-')


def generate_introduction(concept_type, title_en, statement_text):
    """Generate 2-4 sentence English introduction."""
    domain = "commutative algebra"
    if "valuation" in statement_text.lower() or "place" in statement_text.lower():
        domain = "valuation theory"
    elif "polynomial" in statement_text.lower() or "power series" in statement_text.lower():
        domain = "polynomial and power series rings"
    elif "local ring" in statement_text.lower() or "regular local" in statement_text.lower():
        domain = "local algebra"

    intro = f"This {concept_type} from {domain} appears in Zariski-Samuel's Commutative Algebra Volume II. "

    # Add a brief description
    clean_stmt = re.sub(r'\$[^$]*\$', '[...]', statement_text[:200])
    clean_stmt = re.sub(r'\s+', ' ', clean_stmt).strip()
    if len(clean_stmt) > 100:
        clean_stmt = clean_stmt[:97] + "..."

    intro += f"It establishes that {clean_stmt} "

    if concept_type in ('theorem', 'lemma', 'proposition', 'corollary'):
        intro += "The result is proved in detail in the accompanying proof file."
    elif concept_type == 'definition':
        intro += "This definition is fundamental to the development of the theory."

    return intro


def extract_proof_from_text(text, concept_type):
    """Extract the proof from concept text."""
    if concept_type in ('definition', 'axiom'):
        return ""

    for pattern in PROOF_START_PATTERNS:
        m = re.search(pattern, text)
        if m:
            proof_text = text[m.end():].strip()

            # Try to find end of proof
            for end_pattern in PROOF_END_MARKERS:
                em = re.search(end_pattern, proof_text)
                if em:
                    proof_text = proof_text[:em.end()]
                    break

            # Also stop at next concept
            for cpattern, _ in CONCEPT_PATTERNS:
                cm = re.search(cpattern, proof_text)
                if cm:
                    # Check if this is the next concept (not just a mention)
                    proof_text = proof_text[:cm.start()]
                    break

            return proof_text.strip()

    return ""


def extract_statement_only(text, concept_type):
    """Extract just the statement, without proof."""
    for pattern in PROOF_START_PATTERNS:
        m = re.search(pattern, text)
        if m:
            return text[:m.start()].strip()
    return text.strip()


def write_concept_files(slug, concept_data):
    """Write all files for a concept."""
    slug_dir = os.path.join(OUTPUT_BASE, slug)
    os.makedirs(slug_dir, exist_ok=True)

    # ── FILE 1: concept.yaml ──
    yaml_data = {
        'id': slug,
        'title_en': concept_data['title_en'],
        'title_zh': '',
        'type': concept_data['type'],
        'domain': concept_data['domain'],
        'subdomain': concept_data['subdomain'],
        'difficulty': concept_data['difficulty'],
        'tags': concept_data.get('tags', []),
        'depends_on': concept_data.get('depends_on', {'required': [], 'recommended': [], 'suggested': []}),
        'source_books': [{
            'book_id': BOOK_ID,
            'author': AUTHORS,
            'title': BOOK_TITLE,
            'chapter': concept_data['chapter'],
            'section': concept_data['section'],
            'pages': concept_data.get('pages', ''),
            'role_in_book': concept_data.get('role_in_book', '')
        }],
        'content_hash': concept_data['content_hash'],
        'extraction_date': EXTRACTION_DATE,
        'extraction_agent': EXTRACTION_AGENT
    }

    with open(os.path.join(slug_dir, 'concept.yaml'), 'w') as f:
        yaml.dump(yaml_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    # ── FILE 2: theorem.tex ──
    with open(os.path.join(slug_dir, 'theorem.tex'), 'w') as f:
        f.write(concept_data['statement_tex'])

    # ── FILE 3: introduce.en.md ──
    intro_md = f"""---
role: introduce
locale: en
content_hash: "{concept_data['content_hash']}"
written_against: ""
---

{concept_data['introduction']}
"""
    with open(os.path.join(slug_dir, 'introduce.en.md'), 'w') as f:
        f.write(intro_md)

    # ── FILE 4: proof file (if applicable) ──
    if concept_data['type'] not in ('definition', 'axiom') and concept_data.get('proof_text'):
        ch = concept_data['chapter']
        sec = concept_data['section']
        proof_md = f"""---
role: proof
locale: en
of_concept: {slug}
source_book: {BOOK_ID}
source_chapter: "{ch}"
source_section: "{sec}"
---

{concept_data['proof_text']}
"""
        proof_filename = f"proof_{BOOK_ID}_{ch}.{sec.replace(' ', '_')}.en.md"
        with open(os.path.join(slug_dir, proof_filename), 'w') as f:
            f.write(proof_md)

    return slug_dir


def process_section(filepath, section_id):
    """Process a single section file."""
    if section_id not in SECTION_MAP:
        print(f"  SKIP (no mapping): {section_id}")
        return []

    chapter, section_num, section_label = SECTION_MAP[section_id]

    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Find all concepts
    concepts = find_all_concepts(text)
    print(f"  Found {len(concepts)} concept markers in section {section_id}")

    results = []
    domain, subdomain = determine_domain_subdomain(chapter, section_label)

    for i, c in enumerate(concepts):
        # Get next concept boundary
        next_start = concepts[i+1]['start'] if i+1 < len(concepts) else None

        # Extract concept text
        concept_text = extract_concept_text(text, c['start'], next_start)

        # Extract statement and proof
        statement_tex = extract_statement_only(concept_text, c['type'])
        proof_text = extract_proof_from_text(concept_text, c['type'])

        if not statement_tex.strip():
            continue

        # Generate metadata
        number = c.get('number', '')
        title_en = create_title_en(c['type'], number, statement_tex, section_label)
        slug = generate_slug(c['type'], number, chapter, section_num, statement_tex)

        # Ensure unique slug
        base_slug = slug
        counter = 1
        while any(r['slug'] == slug for r in results):
            slug = f"{base_slug}-{counter}"
            counter += 1

        # Content hash
        content_hash = hashlib.sha256(concept_text.encode()).hexdigest()[:16]

        # Introduction
        introduction = generate_introduction(c['type'], title_en, statement_tex)

        concept_data = {
            'slug': slug,
            'title_en': title_en,
            'type': c['type'],
            'domain': domain,
            'subdomain': subdomain,
            'difficulty': determine_difficulty(c['type'], chapter),
            'tags': [],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'chapter': chapter,
            'section': section_num,
            'pages': '',
            'role_in_book': '',
            'content_hash': content_hash,
            'statement_tex': statement_tex,
            'introduction': introduction,
            'proof_text': proof_text,
        }

        try:
            out_dir = write_concept_files(slug, concept_data)
            results.append({'slug': slug, 'type': c['type'], 'number': number, 'dir': out_dir})
        except Exception as e:
            print(f"    ERROR writing {slug}: {e}")

    return results


def main():
    os.makedirs(OUTPUT_BASE, exist_ok=True)

    all_results = {}
    total_concepts = 0

    # Get all section files
    section_files = sorted([f for f in os.listdir(SECTIONS_DIR)
                           if f.endswith('.md') and f != '_manifest.json'])

    for sf in section_files:
        # Extract section id (e.g., "s001" from "s001_2._Places.md")
        section_id = sf[:4] if sf[0] == 's' and sf[1:4].isdigit() else None
        if section_id is None:
            print(f"SKIP (no section id): {sf}")
            continue
        if section_id == 's029':  # Index
            print(f"SKIP (index): {sf}")
            continue
        if section_id == 's00_':  # Preface
            print(f"SKIP (preface): {sf}")
            continue

        filepath = os.path.join(SECTIONS_DIR, sf)
        print(f"\nProcessing: {sf} ({len(open(filepath).read())} chars)")

        results = process_section(filepath, section_id)
        all_results[section_id] = results
        total_concepts += len(results)

    # Write summary
    summary = {
        'book_id': BOOK_ID,
        'book_title': BOOK_TITLE,
        'total_concepts': total_concepts,
        'sections_processed': len(all_results),
        'extraction_date': EXTRACTION_DATE,
        'agent': EXTRACTION_AGENT,
        'section_results': {k: len(v) for k, v in all_results.items()}
    }

    with open(os.path.join(OUTPUT_BASE, '_extraction_summary.json'), 'w') as f:
        json.dump(summary, f, indent=2)

    print(f"\n{'='*60}")
    print(f"TOTAL CONCEPTS EXTRACTED: {total_concepts}")
    print(f"SECTIONS PROCESSED: {len(all_results)}")
    print(f"Summary written to: {os.path.join(OUTPUT_BASE, '_extraction_summary.json')}")

    # Write .done marker
    with open(os.path.join(OUTPUT_BASE, '.done'), 'w') as f:
        f.write(f"DONE - {total_concepts} concepts extracted on {EXTRACTION_DATE}\n")


if __name__ == '__main__':
    main()
