#!/usr/bin/env python3
"""
V8 Concept Extractor v2 for GTM029 (Zariski-Samuel, Commutative Algebra Vol.II).
Improved: concept statement vs reference detection, semantic slug generation,
proper statement/proof boundary detection.
"""
import os, re, hashlib, yaml, json, sys
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
SECTION_MAP = {
    "s001": ("VI", "2", "Places"),
    "s002": ("VI", "4", "Existence of places"),
    "s003": ("VI", "7", "Algebraic field extension case"),
    "s004": ("VI", "9", "Places and valuations"),
    "s005": ("VI", "13", "Classical ideal theory and valuations"),
    "s006": ("VI", "16", "Composite centered valuations existence"),
    "s007": ("VI", "17", "Abstract Riemann surface of a field"),
    "s008": ("VII", "1-2", "Polynomial and power series rings"),
    "s009": ("VII", "3", "Algebraic varieties in affine space"),
    "s010": ("VII", "5", "Non-homogeneous and homogeneous ideals"),
    "s011": ("VII", "8", "Dimension theory of polynomial rings"),
    "s012": ("VII", "11", "Extension of the ground field"),
    "s013": ("VII", "13", "Chains of syzygies"),
    "s014": ("VIII", "1", "Associated graded rings"),
    "s015": ("VIII", "5", "Comparison of topologies"),
    "s016": ("VIII", "7", "Hensel's lemma and applications"),
    "s017": ("VIII", "9", "Dimension theory and systems of parameters"),
    "s018": ("VIII", "10", "Theory of multiplicities"),
    "s019": ("VIII", "11", "Regular local rings"),
    "s020": ("VIII", "12", "Complete local rings structure"),
    "s021": ("Appendix", "1", "Prime ideals in noetherian domains"),
    "s022": ("Appendix", "2", "Valuations in noetherian domains"),
    "s023": ("Appendix", "3", "Valuation ideals"),
    "s024": ("Appendix", "4", "Complete modules and ideals"),
    "s025": ("Appendix", "5", "Complete ideals in regular local rings dim 2"),
    "s026": ("Appendix", "5", "Complete ideals in regular local rings dim 2"),
    "s027": ("Appendix", "5", "Complete ideals in regular local rings dim 2"),
    "s028": ("Appendix", "7", "Unique factorization in regular local rings"),
}


# ─── CONCEPT TYPE PATTERNS ───
# Must match standalone concept STATEMENTS, not references
# Pattern: optional whitespace/line start + TYPE + optional number + period/colon
CONCEPT_STATEMENT_PATTERN = re.compile(
    r'(?:^|\n)((DEFINITION|THEOREM|LEMMA|PROPOSITION|COROLLARY|AXIOM)'
    r'\s+(\d+(?:\s*[′\'’](?:\s*[′\'’])?)?)'
    r'\.?(?:\s|$))',
    re.MULTILINE | re.IGNORECASE
)

# Also match unnumbered concepts
UNNUMBERED_CONCEPT = re.compile(
    r'(?:^|\n\s*\n)((DEFINITION|THEOREM|LEMMA|PROPOSITION|COROLLARY)'
    r'\.(?:\s|$))',
    re.MULTILINE
)

# Reference patterns (to exclude)
REFERENCE_PATTERNS = [
    re.compile(r'\b(?:by|from|see|using|to|of|in|and|,)\s+' + t, re.IGNORECASE)
    for t in ['Theorem', 'Definition', 'Lemma', 'Proposition', 'Corollary',
              'THEOREM', 'DEFINITION', 'LEMMA', 'PROPOSITION', 'COROLLARY']
]

# Proof markers
PROOF_START = re.compile(r'\bPROOF\b[.:]?\s*', re.MULTILINE)
PROOF_END = re.compile(r'\bQ\.?\s*E\.?\s*D\.?\b', re.MULTILINE)

# ─── MATH KEYWORD EXTRACTION FOR SLUGS ───
def extract_math_keywords(text, max_words=5):
    """Extract meaningful mathematical keywords from text for slug generation."""
    # Remove LaTeX math and commands for keyword extraction
    clean = text

    # Replace math with placeholder to identify key terms
    # Extract named concepts (X's theorem, Y's lemma)
    named_patterns = [
        r"(Hensel(?:'s)?)\s+(?:lemma|Lemma)",
        r"(Macaulay(?:'s)?)\s+(?:theorem|ring)",
        r"(Cohen(?:-Macaulay)?)\s+(?:ring|theorem)",
        r"(Zariski(?:'s)?)\s+(?:ring|lemma|theorem)",
        r"(Hilbert(?:'s)?)\s+(?:(?:basis|Nullstellensatz)\s+)?(?:theorem|function)",
        r"(Krull(?:'s)?)\s+(?:domain|theorem|intersection)",
        r"(Dedekind)\s+(?:domain|ring)",
        r"(Noether(?:ian)?)\s+(?:ring|domain|theorem)",
        r"(Artin(?:ian)?)\s+(?:ring|module)",
        r"(Auslander|Buchsbaum)",
        r"(Grothendieck)",
        r"(Serre)",
        r"(Rees)",
        r"(Jacobson)\s+(?:radical|ring)",
        r"(Nagata)",
        r"(Mori)",
    ]

    for pattern in named_patterns:
        m = re.search(pattern, clean, re.IGNORECASE)
        if m:
            return m.group(0).lower().replace("'s", "s").replace(" ", "-").replace("--", "-")

    # Extract key mathematical terms
    key_terms = []
    math_terms = [
        # Ring theory
        'regular local ring', 'local ring', 'noetherian ring', 'noetherian domain',
        'polynomial ring', 'power series ring', 'quotient ring', 'valuation ring',
        'integrally closed', 'integral domain', 'ufd', 'pid', 'dedekind domain',
        'krull domain', 'macaulay ring', 'cohen-macaulay', 'gorenstein',
        # Valuation theory
        'valuation', 'place', 'prime divisor', 'specialization',
        'value group', 'residue field', 'rank', 'dimension',
        # Ideal theory
        'prime ideal', 'maximal ideal', 'minimal prime', 'associated prime',
        'primary ideal', 'invertible ideal', 'complete ideal',
        # Module theory
        'free module', 'projective module', 'injective module', 'flat module',
        'graded module', 'complete module', 'syzygy', 'cohomological dimension',
        # Local algebra
        'completion', 'associated graded ring', 'system of parameters',
        'multiplicity', 'regular sequence', 'depth', 'hensels lemma',
        # Algebraic geometry
        'algebraic variety', 'affine variety', 'projective variety', 'function field',
        'birational', 'normal model', 'riemann surface',
        # General
        'homomorphism', 'isomorphism', 'exact sequence', 'transcendence degree',
        'characteristic', 'field extension', 'ground field',
    ]

    clean_lower = clean.lower()
    for term in math_terms:
        if term in clean_lower:
            key_terms.append(term.replace(' ', '-'))
            if len(key_terms) >= max_words:
                break

    if not key_terms:
        # Fall back to extracting non-LaTeX, non-stopword words
        no_math = re.sub(r'\$[^$]*\$', ' ', clean)
        no_math = re.sub(r'\\[a-zA-Z]+(\{[^}]*\})*', ' ', no_math)
        no_math = re.sub(r'[^a-zA-Z\s]', ' ', no_math)
        words = [w.lower() for w in no_math.split()
                if len(w) > 2 and w not in {'the', 'and', 'for', 'let', 'are', 'any',
                    'all', 'has', 'had', 'was', 'that', 'this', 'with', 'from', 'have',
                    'been', 'not', 'but', 'its', 'their', 'they', 'also', 'may', 'such',
                    'into', 'some', 'then', 'there', 'each', 'which', 'when', 'where',
                    'over', 'here', 'these', 'those', 'more', 'only', 'other', 'shall',
                    'every', 'does', 'being', 'assume', 'case', 'follows', 'will', 'can',
                    'must', 'need', 'prove', 'proof', 'show', 'hence', 'thus'}]
        key_terms = words[:max_words]

    return '-'.join(key_terms)


def is_concept_statement(text, match_start, match_end):
    """
    Determine if a concept marker is actually stating a concept (vs. referencing one).
    Checks context before AND after the match.
    """
    # Get context before the match
    context_start = max(0, match_start - 150)
    before = text[context_start:match_start]

    # Check preceding context for reference indicators
    before_clean = before.strip().split()[-5:] if before.strip().split() else []
    before_str = ' '.join(before_clean).lower()

    referrers = ['by', 'from', 'see', 'using', 'to', 'cf', 'cf.', 'e.g.', 'i.e.', 'viz.',
                 'remark', 'notice', 'note']
    for w in referrers:
        if before_str.rstrip(',.').endswith(w):
            return False

    # Check if preceded by concept number (e.g., "Corollary 2 to")
    if re.search(r'(?:Theorem|Definition|Lemma|Proposition|Corollary)\s+\d+\s*(?:to|of)\s*$',
                 before_str, re.IGNORECASE):
        return False

    # Check context AFTER the match (next ~30 chars)
    after = text[match_end:match_end + 50].strip()
    # If followed by "to Theorem X" or "of Theorem X", it's a reference
    if re.match(r'(?:to|of)\s+(?:Theorem|Definition|Lemma|Proposition|Corollary)\s+\d+',
                after, re.IGNORECASE):
        return False

    # Check if preceded by a section reference
    if re.search(r'§\d+.*$', before_str):
        return False

    return True


def extract_statement_and_proof(text, start_pos, concept_type, next_concept_start=None):
    """
    Extract statement and proof from concept text.
    Uses next concept start as hard boundary.
    Returns (statement, proof, end_pos).
    """
    remaining = text[start_pos:]

    # Determine hard boundary
    if next_concept_start:
        max_len = next_concept_start - start_pos
    else:
        max_len = len(remaining)

    if max_len <= 0:
        return "", "", start_pos

    remaining = remaining[:max_len]

    # Find proof marker
    proof_match = PROOF_START.search(remaining)

    if proof_match:
        statement = remaining[:proof_match.start()].strip()
        after_proof_start = proof_match.end()
        after_proof = remaining[after_proof_start:]

        # Find end of proof
        qed_match = PROOF_END.search(after_proof)
        proof_end = len(after_proof)
        if qed_match:
            proof_end = qed_match.end()

        proof = after_proof[:proof_end].strip()
        abs_end = start_pos + proof_match.start() + after_proof_start + proof_end
    else:
        # No proof marker - concept has no explicit proof (e.g., definition)
        # Statement is everything until next concept or other boundary
        statement = remaining.strip()
        proof = ""
        abs_end = start_pos + len(remaining)

    return statement, proof, abs_end


def generate_slug(concept_type, number, statement, chapter, section_num):
    """Generate a semantic English slug."""
    keywords = extract_math_keywords(statement, max_words=5)

    # Build slug
    parts = []
    if number:
        # Clean number for filename
        clean_num = re.sub(r'[^\w]', '', number.replace('′', '-prime').replace('\'', '-prime'))
        parts.append(f"{concept_type}-{clean_num}")
    else:
        parts.append(concept_type)

    if keywords:
        parts.append(keywords)

    slug = '-'.join(parts).lower()
    slug = re.sub(r'[^a-z0-9-]', '', slug)
    slug = re.sub(r'-+', '-', slug)
    return slug.strip('-')[:100]


def generate_title(concept_type, number, statement):
    """Generate canonical English title."""
    # Take first meaningful sentence
    clean = re.sub(r'\s+', ' ', statement[:200]).strip()
    first_part = clean.split('.')[0] if '.' in clean else clean[:150]

    if number:
        prefix = f"{concept_type.capitalize()} {number}"
    else:
        prefix = concept_type.capitalize()

    title = f"{prefix}: {first_part.strip()}"
    if len(title) > 250:
        title = title[:247] + "..."
    return title


def generate_intro(concept_type, title, statement, chapter):
    """Generate 2-4 sentence introduction."""
    domain_map = {
        "VI": "valuation theory",
        "VII": "polynomial and power series rings",
        "VIII": "local algebra",
        "Appendix": "commutative algebra",
    }
    domain = domain_map.get(chapter, "commutative algebra")

    intro = f"This {concept_type} is established in Zariski-Samuel's Commutative Algebra Volume II, "
    intro += f"within the context of {domain}. "

    # Brief description from statement
    clean_stmt = re.sub(r'\$[^$]*\$', '[...]', statement[:150])
    clean_stmt = re.sub(r'\s+', ' ', clean_stmt).strip()
    intro += f"It deals with {clean_stmt[:120]}..."

    if concept_type in ('theorem', 'lemma', 'proposition', 'corollary'):
        intro += " The result includes a detailed proof."
    elif concept_type == 'definition':
        intro += " This definition is fundamental for the subsequent development."

    return intro


def write_concept_files(slug, data):
    """Write all concept files."""
    slug_dir = os.path.join(OUTPUT_BASE, slug)
    os.makedirs(slug_dir, exist_ok=True)

    # FILE 1: concept.yaml
    yaml_data = {
        'id': slug,
        'title_en': data['title_en'],
        'title_zh': '',
        'type': data['type'],
        'domain': data['domain'],
        'subdomain': data['subdomain'],
        'difficulty': data['difficulty'],
        'tags': [],
        'depends_on': {'required': [], 'recommended': [], 'suggested': []},
        'source_books': [{
            'book_id': BOOK_ID,
            'author': AUTHORS,
            'title': BOOK_TITLE,
            'chapter': data['chapter'],
            'section': data['section_num'],
            'pages': '',
            'role_in_book': ''
        }],
        'content_hash': data['content_hash'],
        'extraction_date': EXTRACTION_DATE,
        'extraction_agent': EXTRACTION_AGENT
    }

    with open(os.path.join(slug_dir, 'concept.yaml'), 'w') as f:
        yaml.dump(yaml_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    # FILE 2: theorem.tex
    with open(os.path.join(slug_dir, 'theorem.tex'), 'w') as f:
        f.write(data['statement_tex'])

    # FILE 3: introduce.en.md
    intro_md = f"""---
role: introduce
locale: en
content_hash: "{data['content_hash']}"
written_against: ""
---

{data['introduction']}
"""
    with open(os.path.join(slug_dir, 'introduce.en.md'), 'w') as f:
        f.write(intro_md)

    # FILE 4: proof (if applicable)
    if data['type'] not in ('definition', 'axiom') and data.get('proof_text'):
        ch = data['chapter']
        sec = data['section_num']
        proof_md = f"""---
role: proof
locale: en
of_concept: {slug}
source_book: {BOOK_ID}
source_chapter: "{ch}"
source_section: "{sec}"
---

{data['proof_text']}
"""
        # Use clean filename
        sec_clean = sec.replace(' ', '-').replace('/', '-')
        proof_fn = f"proof_{BOOK_ID}_{ch}.{sec_clean}.en.md"
        with open(os.path.join(slug_dir, proof_fn), 'w') as f:
            f.write(proof_md)


def determine_difficulty(ctype, chapter):
    if chapter == "VI":
        return "advanced"
    if chapter == "VII" and ctype in ("theorem", "proposition"):
        return "intermediate"
    if chapter == "VIII":
        return "advanced"
    if chapter == "Appendix":
        return "advanced"
    return "intermediate"


def determine_domain_subdomain(chapter):
    domain_map = {
        "VI": ("algebra", "valuation-theory"),
        "VII": ("algebra", "polynomial-rings"),
        "VIII": ("algebra", "local-algebra"),
        "Appendix": ("algebra", "commutative-algebra"),
    }
    return domain_map.get(chapter, ("algebra", "commutative-algebra"))


def process_section(filepath, section_id):
    """Process a single section, extracting all concepts."""
    chapter, section_num, section_label = SECTION_MAP[section_id]

    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        text = f.read()

    # Find all concept STATEMENTS (not references)
    concepts = []

    for m in CONCEPT_STATEMENT_PATTERN.finditer(text):
        ctype = m.group(2).lower()
        number = m.group(3) if m.lastindex and m.lastindex >= 3 else ''
        start = m.start()

        match_end = m.end()
        if is_concept_statement(text, start, match_end):
            concepts.append({
                'type': ctype,
                'number': number,
                'start': start,
                'match_end': match_end,
                'match_length': len(m.group(1))
            })

    # Sort by position
    concepts.sort(key=lambda x: x['start'])

    # Remove overlapping concepts
    filtered = []
    last_end = 0
    for c in concepts:
        if c['start'] >= last_end:
            filtered.append(c)
            last_end = c['start'] + c['match_length']
    concepts = filtered

    domain, subdomain = determine_domain_subdomain(chapter)
    results = []
    seen_slugs = set()

    for i, c in enumerate(concepts):
        # Determine next concept start for boundary
        next_start = concepts[i+1]['start'] if i+1 < len(concepts) else None

        # Extract statement and proof (skip the concept label)
        statement, proof, end_pos = extract_statement_and_proof(
            text, c['start'] + c['match_length'], c['type'], next_start
        )

        if not statement.strip():
            continue

        # Generate metadata
        slug = generate_slug(c['type'], c['number'], statement, chapter, section_num)

        # Ensure unique slug
        base_slug = slug
        counter = 1
        while slug in seen_slugs:
            slug = f"{base_slug}-{counter}"
            counter += 1
        seen_slugs.add(slug)

        content_hash = hashlib.sha256(
            (statement + proof).encode('utf-8', errors='replace')
        ).hexdigest()[:16]

        title_en = generate_title(c['type'], c['number'], statement)
        introduction = generate_intro(c['type'], title_en, statement, chapter)
        difficulty = determine_difficulty(c['type'], chapter)

        data = {
            'title_en': title_en,
            'type': c['type'],
            'domain': domain,
            'subdomain': subdomain,
            'difficulty': difficulty,
            'chapter': chapter,
            'section_num': section_num,
            'content_hash': content_hash,
            'statement_tex': statement,
            'introduction': introduction,
            'proof_text': proof,
        }

        try:
            write_concept_files(slug, data)
            results.append({
                'slug': slug,
                'type': c['type'],
                'number': c['number'],
            })
        except Exception as e:
            print(f"    ERROR writing {slug}: {e}")

    return results


def main():
    os.makedirs(OUTPUT_BASE, exist_ok=True)

    all_files = sorted(os.listdir(SECTIONS_DIR))
    total_concepts = 0
    all_results = {}

    for sf in all_files:
        if not sf.endswith('.md'):
            continue
        if sf == '_manifest.json':
            continue

        # Extract section id
        section_id = sf[:4]
        if section_id == 's00_' or section_id == 's029':
            print(f"SKIP: {sf}")
            continue

        if section_id not in SECTION_MAP:
            print(f"SKIP (no mapping): {sf}")
            continue

        filepath = os.path.join(SECTIONS_DIR, sf)
        fsize = os.path.getsize(filepath)
        chapter, sec, label = SECTION_MAP[section_id]
        print(f"\nProcessing: [{section_id}] Ch.{chapter} §{sec} '{label}' ({fsize} bytes)")

        results = process_section(filepath, section_id)
        all_results[section_id] = results
        total_concepts += len(results)
        print(f"  -> Extracted {len(results)} concepts")

    # Summary
    summary = {
        'book_id': BOOK_ID,
        'total_concepts': total_concepts,
        'sections_processed': len(all_results),
        'extraction_date': EXTRACTION_DATE,
        'agent': EXTRACTION_AGENT,
        'per_section': {k: len(v) for k, v in all_results.items()}
    }

    with open(os.path.join(OUTPUT_BASE, '_extraction_summary.json'), 'w') as f:
        json.dump(summary, f, indent=2)

    # Write .done
    with open(os.path.join(OUTPUT_BASE, '.done'), 'w') as f:
        f.write(f"DONE - {total_concepts} concepts extracted on {EXTRACTION_DATE}\n")

    print(f"\n{'='*60}")
    print(f"TOTAL CONCEPTS: {total_concepts}")
    for k, v in sorted(all_results.items()):
        ch, sec, label = SECTION_MAP[k]
        print(f"  {k} (Ch.{ch} §{sec}): {len(v)} concepts")
    print(f"\nDone marker: {os.path.join(OUTPUT_BASE, '.done')}")


if __name__ == '__main__':
    main()
