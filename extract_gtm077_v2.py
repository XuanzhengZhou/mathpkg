#!/usr/bin/env python3
"""
V2: Comprehensive concept extraction for GTM077.
Handles all formatting variations found in the 31 sections.
"""

import os, re, yaml, hashlib, json
from pathlib import Path
from collections import Counter

SECTION_DIR = "/home/a123/文档/mathpkg/pipeline_output/stitched_sections/(GTM077)Lectures on the Theory of Algebraic Numbers"
OUTPUT_BASE = "/home/a123/文档/mathpkg/pipeline_output/concepts_v7/gtm077"
BOOK_ID = "gtm077"
BOOK_AUTHOR = "Erich Hecke"
BOOK_TITLE = "Lectures on the Theory of Algebraic Numbers"

def clean_md(text):
    """Remove markdown artifacts and clean up text."""
    # Remove page markers
    text = re.sub(r'\{page_\d+\}', '', text)
    # Normalize whitespace
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()

def extract_section_label(filepath):
    """Extract section label from filename."""
    fn = os.path.basename(filepath)
    m = re.match(r's\d+_(\d+)\.md$', fn)
    if m:
        return m.group(1)
    m = re.match(r's(\d+)_(\d+)', fn)
    if m:
        return f"§{m.group(2)}"
    return fn.replace('.md','')

def make_slug(concept_type, number=None, text_hint=''):
    """Create semantic slug."""
    if concept_type == 'theorem' and number is not None:
        # For named theorems, use a cleaner slug
        name_map = {
            1: 'gcd-linear-combination', 2: 'module-characterization',
            3: 'linear-form-module', 4: 'gcd-multiplicative-property',
            5: 'fundamental-theorem-of-arithmetic', 6: 'congruence-cancellation',
            7: 'residue-system-translation', 8: 'crt-residue-system',
            9: 'fermat-euler-theorem', 10: 'root-implies-linear-factor-mod',
            11: 'root-of-factor-mod-p', 12: 'polynomial-root-bound-mod-p',
            13: 'gauss-lemma-polynomials', 14: 'linear-congruence-solvability',
            15: 'crt-for-congruences', 16: 'associative-law-group',
            17: 'group-unit-element', 18: 'group-inverse-element',
            19: 'lagrange-theorem-group', 20: 'element-order-properties',
            21: 'element-order-powers', 22: 'existence-of-element-of-order-p',
            23: 'decomposition-by-coprime-orders', 24: 'basis-theorem-abelian-group',
            25: 'fundamental-theorem-finite-abelian-groups',
            26: 'basis-theorem-prime-power', 27: 'basis-number-theorem',
            28: 'cyclic-group-characterization', 29: 'factor-group-order',
            30: 'character-count-theorem', 31: 'character-orthogonality-relations',
            32: 'character-values-and-order', 33: 'subgroup-characterization',
            34: 'subgroup-basis-theorem', 35: 'torsion-free-subgroup-basis',
            36: 'subgroup-index-theorem', 37: 'maximal-independent-elements',
            38: 'basis-transition-theorem', 39: 'subgroup-index-determinant',
            40: 'finite-index-criterion', 41: 'group-of-rational-numbers',
            42: 'decomposition-of-residue-class-group',
            43: 'cyclic-group-of-residues-mod-p',
            44: 'cyclicity-of-residue-group-mod-p-alpha',
            45: 'structure-of-residue-group-mod-2-alpha',
            46: 'binomial-congruence-solvability',
            47: 'binomial-congruence-mod-2-alpha',
            48: 'gcd-of-polynomials-over-field',
            49: 'irreducible-polynomial-divisor',
            50: 'algebraic-operations-closure',
            51: 'polynomial-with-algebraic-coefficients',
            52: 'primitive-element-theorem',
            53: 'representation-of-field-elements',
            54: 'conjugates-as-polynomial-values',
            55: 'conjugate-operations-preservation',
            56: 'generating-element-characterization',
            57: 'fundamental-system-determinant',
            58: 'linear-independence-criterion',
            59: 'tower-degree-theorem',
            60: 'integer-criterion-by-monic-polynomial',
            61: 'closure-of-algebraic-integers',
            62: 'integral-equation-integer-root',
            63: 'integer-by-multiplication',
            64: 'basis-and-discriminant',
            65: 'ideal-basis-theorem',
            66: 'ideal-to-principal-ideal',
            67: 'gauss-lemma-algebraic-integers',
            68: 'ideal-cancellation-law',
            69: 'ideal-divisibility-equivalence',
            70: 'gcd-of-two-ideals',
            71: 'prime-ideal-divisor-property',
            72: 'fundamental-theorem-of-ideal-theory',
            73: 'norm-multiplicativity',
            74: 'principal-ideal-relative-prime',
            75: 'norm-of-ideal-finite',
            76: 'residue-class-count',
            77: 'generating-class-mod-p',
            78: 'linear-congruence-mod-ideal',
            79: 'norm-multiplicative-property',
            80: 'euler-phi-for-ideals',
            81: 'fermat-theorem-for-ideals',
            82: 'polynomial-congruence-mod-prime-ideal',
            83: 'cyclic-group-for-prime-ideals-degree-1',
            84: 'residue-class-group-multiplication',
            85: 'polynomial-content-mod-p',
            86: 'zero-divisor-property-mod-prime-ideal',
            87: 'content-of-product-of-polynomials',
            88: 'norm-of-conjugate-ideals',
            89: 'decomposition-in-quadratic-fields',
            90: 'ramification-and-discriminant',
            91: 'squarefree-prime-ideal-in-cyclotomic',
            92: 'decomposition-law-cyclotomic-field',
            93: 'fractional-ideal-representation',
            94: 'minkowski-linear-forms-theorem',
            95: 'minkowski-theorem-algebraic-numbers',
            96: 'finiteness-of-class-number',
            97: 'hth-power-principal-ideal',
            98: 'ideal-number-representation',
            99: 'finiteness-of-roots-of-unity',
            100: 'bound-for-fundamental-units',
            101: 'different-and-discriminant-properties',
            102: 'different-divisibility-criterion',
            103: 'discriminant-prime-factors',
            104: 'relative-different-properties',
            105: 'discriminant-and-different-summary',
            106: 'ideal-correspondence-relative-fields',
            107: 'relative-norm-multiplicative',
            108: 'relative-norm-of-ideal',
            109: 'relative-different-properties-2',
            110: 'relative-different-prime-factors',
            111: 'relative-different-composition',
            112: 'relative-discriminant-decomposition',
            113: 'relative-norm-of-different',
            114: 'relative-discriminant-prime-factors',
            115: 'dedekind-theorem-relative-discriminant',
            116: 'decomposition-in-relative-quadratic-I',
            117: 'decomposition-in-relative-quadratic-II',
            118: 'relative-different-of-quadratic-extension',
            119: 'quadratic-symbol-law',
            120: 'relative-discriminant-one-characterization',
            121: 'ideal-density-in-class',
            122: 'ideal-count-with-norm',
            123: 'dedekind-zeta-function',
            124: 'zeta-function-analytic-continuation',
            125: 'class-number-formula-zeta',
            126: 'prime-ideal-distribution',
            127: 'dirichlet-l-series-properties',
            128: 'dirichlet-series-with-residue-characters',
            129: 'prime-ideals-in-progressions',
            130: 'cyclotomic-field-degree',
            131: 'dirichlet-theorem-arithmetic-progressions',
            132: 'quadratic-field-summary-ideals',
            133: 'ideal-classes-quadratic-field',
            134: 'genus-theory-intro',
            135: 'quadratic-form-correspondence',
            136: 'class-number-formula-quadratic',
            137: 'quadratic-residue-character-mod-d',
            138: 'class-number-formula-real-quadratic',
            139: 'class-number-formula-imaginary-quadratic',
            140: 'sum-of-residue-character',
            141: 'class-number-by-density',
            142: 'class-number-zeta-quadratic',
            143: 'gauss-sum-definition-quadratic',
            144: 'gauss-sum-factorization',
            145: 'gauss-sum-evaluation-odd',
            146: 'gauss-sum-evaluation-even',
            147: 'class-number-final-formula',
            148: 'class-number-without-zeta',
            149: 'unit-from-series',
            150: 'gauss-sum-quadratic-reciprocity',
            151: 'gauss-sum-sign-determination',
            152: 'final-class-number-formula',
            153: 'ideal-quadratic-form-correspondence',
            154: 'quadratic-form-class-number',
            155: 'quadratic-residue-symbol-arbitrary-field',
            156: 'gauss-sum-square-denominator',
            157: 'theta-function-convergence',
            158: 'theta-function-transformation',
            159: 'reciprocity-gauss-sums-totally-real',
            160: 'gauss-sum-value-totally-real',
            161: 'quadratic-reciprocity-totally-real',
            162: 'reciprocity-gauss-sums-general',
            163: 'gauss-sum-value-general',
            164: 'gauss-sum-sign-rational-field',
            165: 'quadratic-reciprocity-law-general',
            166: 'supplementary-theorem-odd',
            167: 'supplementary-theorem-general',
            168: 'existence-of-prime-ideals-residue',
            169: 'prime-ideals-prescribed-residues',
            170: 'singular-primary-numbers-existence',
            171: 'first-supplementary-theorem',
            172: 'singular-primary-number-characterization',
            173: 'odd-ideal-primary-condition',
            174: 'hyperprimary-characterization',
            175: 'singular-primary-mod-4l',
            176: 'class-field-existence-degree-2',
            177: 'relative-different-square-equivalence',
        }
        return name_map.get(number, f'theorem-{number}')

    # For others, use hash
    h = hashlib.md5(text_hint.encode()).hexdigest()[:10]
    return f'{concept_type}-{h}'

def find_concepts(text, section_label, section_file):
    """Find all concepts in text using comprehensive patterns."""
    concepts = []
    found_numbers = set()  # track which theorem numbers are found

    # =========== BOLD-FORMAT CONCEPTS ===========
    # Pattern: **Theorem N.** or **Theorem N:**
    for m in re.finditer(r'\*\*Theorem\s+(\d+)[\.\:\s](?:[^(*]|\*(?!\*))*?\*\*', text):
        number = int(m.group(1))
        if number in found_numbers:
            continue
        found_numbers.add(number)

        # Extract text from after the bold marker
        post_marker = text[m.end():]
        # Find end of statement
        end_patterns = [
            r'\n\s*\*\*Theorem\s+\d+', r'\n\s*\*\*Definition', r'\n\s*\*\*Lemma',
            r'\n\s*\*\*Proposition', r'\n\s*\*\*Corollary',
            r'\n\s*Proof[\.\s]', r'\n\s*\n\s*§\d+', r'\n\s*\n\s*CHAPTER',
            r'\n\s*Theorem\s+\d+[\.\:]', r'\n\s*Definition[\.\:]',
        ]
        end_idx = len(post_marker)
        for pat in end_patterns:
            em = re.search(pat, post_marker)
            if em:
                end_idx = min(end_idx, em.start())

        statement = post_marker[:end_idx].strip()
        if len(statement) > 20:
            concepts.append(('theorem', number, statement, section_label))

    # Pattern: **Definition.**
    def_idx = 0
    for m in re.finditer(r'\*\*Definition[\.\:]\s*\*\*', text):
        post_marker = text[m.end():]
        end_patterns = [
            r'\n\s*\*\*Theorem', r'\n\s*\*\*Definition', r'\n\s*\*\*Lemma',
            r'\n\s*\*\*Proposition', r'\n\s*\*\*Corollary',
            r'\n\s*§\d+', r'\n\s*CHAPTER',
            r'\n\s*Theorem\s+\d+', r'\n\s*Definition[\.\:]',
        ]
        end_idx = len(post_marker)
        for pat in end_patterns:
            em = re.search(pat, post_marker)
            if em:
                end_idx = min(end_idx, em.start())
        statement = post_marker[:end_idx].strip()
        if len(statement) > 20:
            concepts.append(('definition', None, statement, section_label))
            def_idx += 1

    # Pattern: **Lemma.** or **Lemma (a).**
    for m in re.finditer(r'\*\*Lemma\s*(?:\([a-z]\))?[\.\:]\s*\*\*', text):
        post_marker = text[m.end():]
        end_patterns = [
            r'\n\s*\*\*Theorem', r'\n\s*\*\*Definition', r'\n\s*\*\*Lemma',
            r'\n\s*\*\*Proposition', r'\n\s*\*\*Corollary',
            r'\n\s*§\d+', r'\n\s*CHAPTER',
        ]
        end_idx = len(post_marker)
        for pat in end_patterns:
            em = re.search(pat, post_marker)
            if em:
                end_idx = min(end_idx, em.start())
        statement = post_marker[:end_idx].strip()
        if len(statement) > 20:
            concepts.append(('lemma', None, statement, section_label))

    # Pattern: **Proposition.** or **Corollary.**
    for ct in ['proposition', 'corollary']:
        for m in re.finditer(rf'\*\*{ct.title()}[\.\:]\s*\*\*', text):
            post_marker = text[m.end():]
            end_patterns = [
                r'\n\s*\*\*Theorem', r'\n\s*\*\*Definition', r'\n\s*\*\*Lemma',
                r'\n\s*\*\*Proposition', r'\n\s*\*\*Corollary',
                r'\n\s*§\d+', r'\n\s*CHAPTER',
            ]
            end_idx = len(post_marker)
            for pat in end_patterns:
                em = re.search(pat, post_marker)
                if em:
                    end_idx = min(end_idx, em.start())
            statement = post_marker[:end_idx].strip()
            if len(statement) > 20:
                concepts.append((ct, None, statement, section_label))

    # =========== PLAIN-TEXT CONCEPTS ===========
    # Pattern: plain "Theorem N." or "Theorem N:"
    for m in re.finditer(r'(?<!\*)Theorem\s+(\d+)[\.\:]\s', text):
        number = int(m.group(1))
        if number in found_numbers:
            continue
        # Skip if this is within a bold marker range
        prefix = text[max(0,m.start()-10):m.start()]
        if '**' in prefix:
            continue
        found_numbers.add(number)

        post_marker = text[m.end():]
        end_patterns = [
            r'\n\s*Theorem\s+\d+[\.\:]', r'\n\s*Definition[\.\:]', r'\n\s*Lemma[\.\s]',
            r'\n\s*\n\s*§\d+', r'\n\s*\n\s*CHAPTER',
        ]
        end_idx = len(post_marker)
        for pat in end_patterns:
            em = re.search(pat, post_marker)
            if em:
                end_idx = min(end_idx, em.start())
        # Also stop at "Proof" that starts a new paragraph
        em = re.search(r'\n\s*\n\s*Proof[\.\s]', post_marker)
        if em:
            end_idx = min(end_idx, em.start())

        statement = post_marker[:end_idx].strip()
        if len(statement) > 20:
            concepts.append(('theorem', number, statement, section_label))

    # Pattern: plain "Definition."
    for m in re.finditer(r'(?<!\*)Definition[\.\:]\s', text):
        # Skip if within bold marker
        prefix = text[max(0,m.start()-10):m.start()]
        if '**' in prefix:
            continue
        post_marker = text[m.end():]
        end_patterns = [
            r'\n\s*Theorem\s+\d+[\.\:]', r'\n\s*Definition[\.\:]',
            r'\n\s*Lemma[\.\s]', r'\n\s*§\d+', r'\n\s*CHAPTER',
        ]
        end_idx = len(post_marker)
        for pat in end_patterns:
            em = re.search(pat, post_marker)
            if em:
                end_idx = min(end_idx, em.start())
        statement = post_marker[:end_idx].strip()
        if len(statement) > 20:
            concepts.append(('definition', None, statement, section_label))

    # Pattern: plain "Lemma." or "Lemma (a)."
    for m in re.finditer(r'(?<!\*)Lemma\s*(?:\([a-z]\))?[\.\:]\s', text):
        prefix = text[max(0,m.start()-10):m.start()]
        if '**' in prefix:
            continue
        post_marker = text[m.end():]
        end_patterns = [
            r'\n\s*Theorem\s+\d+', r'\n\s*Definition[\.\:]', r'\n\s*Lemma[\.\s]',
            r'\n\s*§\d+', r'\n\s*CHAPTER',
        ]
        end_idx = len(post_marker)
        for pat in end_patterns:
            em = re.search(pat, post_marker)
            if em:
                end_idx = min(end_idx, em.start())
        statement = post_marker[:end_idx].strip()
        if len(statement) > 20:
            concepts.append(('lemma', None, statement, section_label))

    # =========== DEDUPLICATE ===========
    seen = set()
    unique = []
    for ct, num, stmt, sl in concepts:
        key = (ct, num, stmt[:80])
        if key not in seen:
            seen.add(key)
            unique.append((ct, num, stmt, sl))

    return unique

def classify_domain(text):
    tl = text.lower()
    nt = 0; alg = 0
    for kw in ['prime','divisor','gcd','congruence','residue','quadratic','reciprocity',
               'zeta','class-number','gauss','legendre','euler','fermat','modulus','coprime',
               'cyclotomic','minkowski']:
        if kw in tl: nt += 1
    for kw in ['group','field','ring','module','ideal','polynomial','basis','cyclic',
               'abelian','character','subgroup','irreducible','discriminant','norm',
               'unit','conjugate','integer','algebraic','extension','galois']:
        if kw in tl: alg += 1
    return 'number-theory' if nt >= alg else 'algebra'

def classify_subdomain(text):
    tl = text.lower()
    if 'reciprocity' in tl: return 'quadratic-reciprocity'
    if 'gauss' in tl and 'sum' in tl: return 'gauss-sums'
    if 'theta' in tl: return 'theta-functions'
    if 'zeta' in tl: return 'zeta-functions'
    if 'class' in tl and ('number' in tl or 'group' in tl): return 'class-number'
    if 'ideal' in tl:
        if 'prime' in tl: return 'prime-ideals'
        return 'ideal-theory'
    if 'quadratic' in tl:
        if 'field' in tl: return 'quadratic-fields'
        return 'quadratic-residues'
    if 'cyclotomic' in tl: return 'cyclotomic-fields'
    if 'character' in tl: return 'group-characters'
    if 'abelian' in tl or 'basis' in tl: return 'abelian-groups'
    if 'group' in tl: return 'group-theory'
    if 'decomposition' in tl: return 'decomposition-laws'
    if 'unit' in tl: return 'units'
    if 'discriminant' in tl or 'different' in tl: return 'discriminants'
    if 'norm' in tl: return 'norms'
    if 'congruence' in tl: return 'congruences'
    if 'polynomial' in tl: return 'polynomials'
    if 'field' in tl or 'algebraic' in tl: return 'algebraic-number-fields'
    if 'prime' in tl: return 'prime-numbers'
    if 'density' in tl: return 'density-theorems'
    return 'general'

def classify_difficulty(text):
    tl = text.lower()
    if any(k in tl for k in ['reciprocity','gauss sum','class field','theta function',
                              'zeta-function','singular primary']):
        return 'advanced'
    if any(k in tl for k in ['ideal','galois','discriminant','relative','decomposition',
                              'character','fundamental unit','cyclotomic']):
        return 'intermediate'
    return 'basic'

def write_concept(ct, num, stmt, section_label, output_base):
    """Write 3-file output for a concept."""
    slug = make_slug(ct, num, stmt)
    slug_dir = os.path.join(output_base, slug)
    os.makedirs(slug_dir, exist_ok=True)

    domain = classify_domain(stmt)
    subdomain = classify_subdomain(stmt)
    difficulty = classify_difficulty(stmt)
    content_hash = hashlib.md5(stmt.encode()).hexdigest()[:12]

    # Title
    if ct == 'theorem' and num is not None:
        title_en = f'Theorem {num}'
    else:
        first_line = stmt.split('.')[0].strip()[:100]
        title_en = first_line

    # FILE 1: concept.yaml
    yaml_data = {
        'id': slug,
        'title_en': title_en,
        'title_zh': '',
        'type': ct,
        'domain': domain,
        'subdomain': subdomain,
        'difficulty': difficulty,
        'tags': [],
        'depends_on': {'required': [], 'recommended': [], 'suggested': []},
        'source_books': [{
            'book_id': BOOK_ID, 'author': BOOK_AUTHOR, 'title': BOOK_TITLE,
            'chapter': '', 'section': section_label, 'pages': '', 'role_in_book': ''
        }],
        'content_hash': content_hash,
        'extraction_date': '2026-06-25',
        'extraction_agent': 'v7-section-test'
    }
    with open(os.path.join(slug_dir, 'concept.yaml'), 'w') as f:
        yaml.dump(yaml_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    # FILE 2: theorem.tex
    tex = re.sub(r'\n\s*Proof[\.\s].*$', '', stmt, flags=re.DOTALL)
    tex = tex.strip()
    with open(os.path.join(slug_dir, 'theorem.tex'), 'w') as f:
        f.write(tex + '\n')

    # FILE 3: introduce.en.md
    preview = stmt[:200].replace('\n', ' ').strip()
    intro = f"""---
role: introduce
locale: en
content_hash: "{content_hash}"
written_against: ""
---

This is {ct.title()} {num or ''} from {BOOK_TITLE} by {BOOK_AUTHOR}. {preview}... This {'result' if ct=='theorem' else 'concept'} appears in the section {section_label} of the book and is part of the foundational development of algebraic number theory.
"""
    with open(os.path.join(slug_dir, 'introduce.en.md'), 'w') as f:
        f.write(intro)

    return slug

def main():
    section_files = sorted([
        f for f in os.listdir(SECTION_DIR)
        if f.startswith('s') and f.endswith('.md')
    ])

    print(f"Processing {len(section_files)} section files...")

    all_concepts = []
    for sf in section_files:
        fp = os.path.join(SECTION_DIR, sf)
        with open(fp, 'r') as f:
            text = f.read()
        text = clean_md(text)
        section_label = extract_section_label(fp)
        concepts = find_concepts(text, section_label, sf)
        print(f"  {sf}: {len(concepts)} concepts")
        all_concepts.extend(concepts)

    print(f"\nTotal: {len(all_concepts)} concepts")

    # Count types
    type_counts = Counter(ct for ct, _, _, _ in all_concepts)
    for t, c in type_counts.most_common():
        print(f"  {t}: {c}")

    # Write all
    written = 0
    for ct, num, stmt, sl in all_concepts:
        try:
            write_concept(ct, num, stmt, sl, OUTPUT_BASE)
            written += 1
        except Exception as e:
            print(f"  ERROR writing {ct} {num}: {e}")

    print(f"\nWrote {written} concept triples to {OUTPUT_BASE}")

if __name__ == '__main__':
    main()
