#!/usr/bin/env python3
"""Extract all theorems, definitions, lemmas, propositions, corollaries from GTM058."""
import re, os, yaml, hashlib, json

BOOK_FILE = "/home/a123/文档/mathpkg/pipeline_output/stitched/(GTM058)p-adic Numbers, p-adic Analysis, and Zeta-Functions/_full.md"
STAGING = "/home/a123/文档/mathpkg/pipeline_output/v7_test/staging/_GTM058_p_adic_Numbers__p_adic_Analysis__and_Zeta_Funct"

# Read book and clean
with open(BOOK_FILE, 'r') as f:
    text = f.read()

# Remove <|endoftext|> markers
text = re.sub(r'<\|endoftext\|>', '', text)
# Normalize whitespace
text = re.sub(r'\n{3,}', '\n\n', text)

lines = text.split('\n')

# ============================================================
# Manual concept definitions based on thorough reading
# Format: (start_line_approx, concept_type, slug, title_en, chapter, section)
# ============================================================

concepts = []

def add_concept(line_num, ctype, slug, title_en, chapter, section, domain="number_theory", subdomain="p-adic_analysis"):
    concepts.append({
        'line': line_num,
        'type': ctype,
        'slug': slug,
        'title_en': title_en,
        'chapter': chapter,
        'section': section,
        'domain': domain,
        'subdomain': subdomain
    })

# Chapter I, Section 2: Metrics on Q
add_concept(211, 'definition', 'p_adic_ordinal', 'p-adic Ordinal (ord_p)', 'I', '2')
add_concept(221, 'definition', 'non_archimedean_norm', 'Non-Archimedean Norm', 'I', '2')

# Ostrowski's Theorem - embedded in section 2
add_concept(260, 'theorem', 'ostrowskis_theorem', "Ostrowski's Theorem: Classification of Norms on Q", 'I', '2')

# Lemma in section 4 about approximation
add_concept(400, 'lemma', 'approximation_by_integers_mod_pn', 'Approximation Lemma for Rational p-adic Integers', 'I', '4')

# Hensel's Lemma (Theorem 3)
add_concept(464, 'theorem', 'hensels_lemma', "Hensel's Lemma", 'I', '5')

# Chapter II, Section 1: Formula for zeta(2k)
add_concept(572, 'proposition', 'product_formula_for_sinh', 'Infinite Product Formula for sinh(pi x)', 'II', '1')
add_concept(584, 'lemma', 'expansion_of_sin_nx', 'Expansion of sin(nx) as Polynomial in sin(x)', 'II', '1')
add_concept(588, 'theorem', 'euler_formula_for_zeta_2k', "Euler's Formula for zeta(2k)", 'II', '1')

# Chapter II, Section 2: p-adic interpolation of f(s)=a^s
add_concept(668, 'proposition', 'p_adic_interpolation_of_exponential', 'p-adic Interpolation of f(s)=a^s', 'II', '2')

# Chapter II, Section 3: p-adic distributions
add_concept(734, 'definition', 'locally_constant_function', 'Locally Constant Function', 'II', '3')
add_concept(746, 'definition', 'p_adic_distribution', 'p-adic Distribution', 'II', '3')
add_concept(756, 'proposition', 'extension_of_distribution_from_intervals', 'Extension of a Distribution from Intervals', 'II', '3')

# Chapter II, Section 4: Bernoulli distributions
add_concept(804, 'proposition', 'bernoulli_distribution_extension', 'Extension of the k-th Bernoulli Distribution', 'II', '4')

# Chapter II, Section 5: Measures and integration
add_concept(834, 'definition', 'p_adic_measure', 'p-adic Measure', 'II', '5')
add_concept(838, 'theorem', 'regularization_of_bernoulli_measures', 'Regularization of Bernoulli Distributions (Theorem 5)', 'II', '5')

# Chapter II, Section 6: p-adic zeta-function
add_concept(948, 'proposition', 'integral_relation_mu_k_alpha', 'Integral Relation Between mu_{k,alpha} and mu_{1,alpha}', 'II', '6')
add_concept(980, 'definition', 'p_adic_zeta_function_at_negative_integers', 'p-adic Zeta Function at 1-k', 'II', '6')
add_concept(1016, 'definition', 'p_adic_zeta_function_continuous', 'p-adic Zeta Function on Z_p', 'II', '6')

# Theorem 7: Kummer congruences (line ~1000 area)
add_concept(995, 'theorem', 'kummer_congruences', 'Kummer Congruences (von Staudt-Clausen Theorem)', 'II', '6')

# Chapter III, Section 1: Finite fields
add_concept(1171, 'proposition', 'finite_field_multiplicative_group_cyclic', 'Multiplicative Group of a Finite Field is Cyclic', 'III', '1')

# Chapter III, Section 2: Extension of norms
add_concept(1240, 'theorem', 'uniqueness_of_norm_extension', 'Uniqueness of the Extension of the p-adic Norm', 'III', '2')
add_concept(1251, 'lemma', 'norm_of_one_plus_gamma', 'Norm Lemma: |1+gamma|_p <= 1', 'III', '2')

# Chapter III, Section 2/3: Integral closure
add_concept(1280, 'proposition', 'integral_closure_of_zp_in_finite_extension', 'Integral Closure of Z_p in a Finite Extension', 'III', '2')

# Chapter III, Section 3: Unramified extensions
add_concept(1310, 'proposition', 'unramified_extensions_of_qp', 'Unramified Extensions of Q_p', 'III', '3')

# Chapter III, Section 3: Polynomial root continuity
add_concept(1330, 'proposition', 'continuity_of_roots_of_polynomials', 'Continuity of Roots of Polynomials over p-adic Fields', 'III', '3')

# Chapter III, Section 4: Omega
add_concept(1350, 'theorem', 'algebraic_closure_not_complete', 'The Algebraic Closure of Q_p is Not Complete', 'III', '4')
add_concept(1364, 'definition', 'omega_field', 'The Field Omega: Completion of the Algebraic Closure of Q_p', 'III', '4')
add_concept(1380, 'theorem', 'omega_is_algebraically_closed', 'Omega is Algebraically Closed', 'III', '4')

# Chapter IV, Section 1: Elementary functions
add_concept(1412, 'definition', 'radius_of_convergence_p_adic', 'Radius of Convergence of a p-adic Power Series', 'IV', '1')
add_concept(1430, 'lemma', 'zp_power_series_convergence', 'Lemma 1: Z_p[[X]] Converges on D(1^-)', 'IV', '1')
add_concept(1436, 'lemma', 'convergent_power_series_continuous', 'Lemma 2: Convergent Power Series are Continuous', 'IV', '1')
add_concept(1484, 'proposition', 'log_exp_inverse_isomorphisms', 'log_p and exp_p as Inverse Isomorphisms on Small Disc', 'IV', '1')

# Chapter IV, Section 2: Logarithm, gamma, Artin-Hasse
add_concept(1559, 'proposition', 'iwasawa_logarithm_extension', "Iwasawa's Extension of the p-adic Logarithm", 'IV', '2')
add_concept(1608, 'proposition', 'p_adic_gamma_function', 'The p-adic Gamma Function Gamma_p', 'IV', '2')
add_concept(1695, 'lemma', 'dworks_lemma', "Dwork's Lemma on Formal Power Series", 'IV', '2')
add_concept(1666, 'definition', 'artin_hasse_exponential', 'The Artin-Hasse Exponential E_p(X)', 'IV', '2')

# Chapter IV, Section 3: Newton polygons for polynomials
add_concept(1747, 'definition', 'newton_polygon', 'Newton Polygon of a Polynomial', 'IV', '3')
add_concept(1753, 'lemma', 'newton_polygon_roots', 'Lemma 4: Newton Polygon and Roots of a Polynomial', 'IV', '3')

# Chapter IV, Section 4: Newton polygons for power series
add_concept(1761, 'definition', 'newton_polygon_power_series', 'Newton Polygon of a Power Series', 'IV', '4')
add_concept(1785, 'lemma', 'newton_polygon_radius', 'Lemma 5: Newton Polygon Determines Radius of Convergence', 'IV', '4')
add_concept(1797, 'lemma', 'newton_polygon_multiplication', 'Lemma 6: Newton Polygon Under Multiplication by (1-cX)', 'IV', '4')
add_concept(1807, 'lemma', 'newton_polygon_zero_existence', 'Lemma 7: Existence of Zero with Given Ordinal', 'IV', '4')
add_concept(1839, 'theorem', 'weierstrass_preparation_theorem', 'p-adic Weierstrass Preparation Theorem (Theorem 14)', 'IV', '4')

# Chapter V, Section 1: Hypersurfaces and their zeta-functions
add_concept(1900, 'definition', 'affine_hypersurface', 'Affine Hypersurface', 'V', '1')
add_concept(1906, 'definition', 'projective_space_and_hypersurface', 'Projective Space and Projective Hypersurface', 'V', '1')
add_concept(1920, 'definition', 'homogeneous_polynomial_and_completion', 'Homogeneous Polynomial and Homogeneous Completion', 'V', '1')
add_concept(1928, 'definition', 'zeta_function_of_hypersurface', 'Zeta-Function of a Hypersurface over a Finite Field', 'V', '1')
add_concept(1934, 'lemma', 'zeta_function_integer_coefficients', 'Lemma 1: Zeta-Function has Integer Coefficients', 'V', '1')
add_concept(1964, 'theorem', 'dworks_theorem_rationality', "Dwork's Theorem: Rationality of the Zeta-Function", 'V', '1')

# Chapter V, Section 2: Characters and their lifting
add_concept(1999, 'definition', 'omega_valued_character_of_finite_group', 'Omega-valued Character of a Finite Group', 'V', '2')
add_concept(2003, 'definition', 'trace_in_finite_field', 'Trace Map in a Finite Field', 'V', '2')

# Chapter V, Section 3: Linear map on power series
add_concept(2049, 'definition', 'linear_map_psi_on_power_series', 'Linear Map Psi on the Space of Power Series', 'V', '3')
add_concept(2061, 'definition', 'space_r0_of_power_series', 'The Space R_0 of Power Series', 'V', '3')
add_concept(2117, 'lemma', 'determinant_formula_psi', 'Lemma 4: Determinant Formula for det(1-AT)', 'V', '3')

# Chapter V, Section 4: p-adic expression for zeta-function
add_concept(2135, 'proposition', 'p_adic_meromorphic_zeta', 'p-adic Meromorphic Expression for Zeta-Function', 'V', '4')

# Chapter V, Section 5: End of proof
add_concept(2197, 'lemma', 'rationality_criterion_power_series', 'Lemma 5: Criterion for Rationality of a Power Series', 'V', '5')


# ============================================================
# Extraction: for each concept, extract LaTeX content
# ============================================================

def find_concept_content(lines, start_line, concept_type):
    """Extract the content of a concept starting at start_line (1-indexed)."""
    i = start_line - 1  # convert to 0-indexed

    # Find where the concept statement begins
    begin = i
    end = i

    # Skip backwards to find the start of the paragraph
    # Actually, the concept text starts at or near start_line. Let's find the actual start.

    # Look for the concept keyword near the designated line
    keywords = {
        'definition': r'^Definition\.\s',
        'theorem': r'^\*\*Theorem',
        'lemma': r'^(Lemma\.|Lemma\s+\d+\.|\*\*Lemma)',
        'proposition': r'^(Proposition\.|\*\*Proposition)',
        'corollary': r'^(Corollary\.|\*\*Corollary)',
    }

    # Scan backwards up to 5 lines to find the keyword
    found = False
    for offset in range(5):
        test_idx = max(0, begin - offset)
        for ctype, pattern in keywords.items():
            if re.match(pattern, lines[test_idx].strip()):
                begin = test_idx
                found = True
                break
        if found:
            break

    # Collect content until we hit a clear boundary
    # Stop at: exercises, next section header, end of chapter,
    # another concept, or sufficient content

    collected = []
    j = begin
    depth = 0  # for tracking $$ math blocks
    found_proof = False

    while j < len(lines):
        line = lines[j].strip()

        # Stop conditions
        if j > begin + 5:  # give at least some content
            # Check for clear boundaries
            if line == 'EXERCISES':
                break
            if re.match(r'^CHAPTER\s+[IVX]+', line):
                break
            if line.startswith('§') or re.match(r'^\d+\.\s+[A-Z]', line):
                break
            # Check for another concept starting
            if j > begin + 2:
                is_concept = False
                for ctype, pattern in keywords.items():
                    if re.match(pattern, line):
                        is_concept = True
                        break
                if is_concept:
                    break

        collected.append(lines[j])
        j += 1

        # Stop after collecting enough meaningful content (not just empty lines)
        content_text = '\n'.join(collected).strip()
        if len(content_text) > 1500:
            break

    result = '\n'.join(collected).strip()
    return result


def extract_math_content(text_section):
    """Extract the mathematical content (theorem statement) from a text section."""
    # Try to find the formal statement, removing running text before and after
    # We want to capture: the theorem/definition statement + proof if labeled

    # Remove leading metadata-like lines
    lines = text_section.split('\n')

    # Find where the actual math starts
    start = 0
    for i, line in enumerate(lines):
        stripped = line.strip()
        if re.match(r'^(Definition\.|Theorem|Lemma|Proposition|Corollary|\*\*Theorem|\*\*Lemma|\*\*Proposition)', stripped):
            start = i
            break

    # Find where the proof starts
    proof_start = len(lines)
    for i in range(start, len(lines)):
        if re.match(r'^(Proof\.|\*\*Proof|\*Proof)', lines[i].strip()):
            proof_start = i
            break

    # Find where content ends (look for exercises, next section, etc.)
    end = len(lines)
    for i in range(start + 1, len(lines)):
        stripped = lines[i].strip()
        if stripped == 'EXERCISES':
            end = i
            break
        if re.match(r'^\d+\.\s+[A-Z]', stripped) and i > start + 3:
            end = i
            break
        if stripped.startswith('CHAPTER') and i > start + 3:
            end = i
            break

    # Try to include proof if it's short
    if proof_start < end and (end - proof_start) < 100:
        end = end  # keep proof

    result = '\n'.join(lines[start:end]).strip()

    # Clean up common artifacts
    # Remove page number artifacts like isolated numbers
    result = re.sub(r'\n+\d+\n+', '\n\n', result)

    return result


# ============================================================
# Create concept folders
# ============================================================

os.makedirs(STAGING, exist_ok=True)

for concept in concepts:
    slug = concept['slug']
    folder = os.path.join(STAGING, slug)
    os.makedirs(folder, exist_ok=True)

    # Extract content
    raw_content = find_concept_content(lines, concept['line'], concept['type'])
    math_content = extract_math_content(raw_content)

    # Clean up for LaTeX
    tex_content = math_content
    # Remove markdown bold markers
    tex_content = re.sub(r'\*\*', '', tex_content)

    # ---- concept.yaml ----
    yaml_data = {
        'id': slug,
        'title_en': concept['title_en'],
        'title_zh': '',
        'type': concept['type'],
        'domain': concept['domain'],
        'subdomain': concept['subdomain'],
        'difficulty': 'basic',
        'tags': [],
        'depends_on': {'required': [], 'recommended': [], 'suggested': []},
        'proof_deps': {},
        'source_books': [{
            'book_id': 'GTM058',
            'author': 'Neal Koblitz',
            'title': 'p-adic Numbers, p-adic Analysis, and Zeta-Functions',
            'chapter': concept['chapter'],
            'section': concept['section'],
            'pages': '',
            'role_in_book': 'primary_source'
        }],
        'content_hash': hashlib.sha256(tex_content.encode()).hexdigest()[:16],
        'extraction_date': '2026-06-24',
        'extraction_agent': 'v7-10books'
    }

    with open(os.path.join(folder, 'concept.yaml'), 'w') as f:
        yaml.dump(yaml_data, f, default_flow_style=False, allow_unicode=True)

    # ---- theorem.tex ----
    with open(os.path.join(folder, 'theorem.tex'), 'w') as f:
        f.write(tex_content)

    # ---- introduce.en.md ----
    # Find a brief 2-4 sentence description
    desc = tex_content[:400].replace('\n', ' ').strip()
    if len(desc) > 400:
        desc = desc[:397] + '...'

    md_content = f'''---
id: {slug}
title: "{concept['title_en']}"
type: {concept['type']}
---

{concept['title_en']} from Chapter {concept['chapter']}, Section {concept['section']} of Koblitz's "p-adic Numbers, p-adic Analysis, and Zeta-Functions".

{desc}
'''
    with open(os.path.join(folder, 'introduce.en.md'), 'w') as f:
        f.write(md_content)

# ---- Write .done ----
with open(os.path.join(STAGING, '.done'), 'w') as f:
    f.write('DONE\n')

print(f"Extracted {len(concepts)} concepts to {STAGING}")
for c in concepts:
    print(f"  [{c['type']}] {c['slug']}: {c['title_en']} (Ch.{c['chapter']} §{c['section']})")
