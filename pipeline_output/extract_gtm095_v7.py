#!/usr/bin/env python3
"""
GTM095 (Probability-1, Shiryaev 3ed) V7 Concept Extractor v3.
Strips bold markers first, supports period-less headers, better slugs.
"""
import re, os, hashlib
from pathlib import Path
from datetime import date
from collections import Counter

SRC = "/home/a123/文档/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)"
DST = "/home/a123/文档/mathpkg/pipeline_output/concepts_v7/gtm095"

CHAPTER_MAP = {
    "s001":1,"s002":1,"s003":1,"s004":1,"s005":1,"s006":1,"s007":1,"s008":1,"s009":1,
    "s010":1,"s011":1,"s012":1,"s013":1,"s014":1,"s015":1,"s016":1,"s017":1,"s018":1,
    "s019":2,"s020":2,"s021":2,"s022":2,"s023":2,"s024":2,"s025":2,"s026":2,"s027":2,
    "s028":2,"s029":2,"s030":2,
    "s031":3,"s032":3,"s033":3,"s034":3,"s035":3,"s036":3,"s037":3,"s038":3,"s039":3,
    "s040":3,"s041":3,"s042":3,
}

SECTION_NAMES = {
    "s001":"§2. Sample space and events",
    "s002":"§3-5. Probabilistic model, classical probability",
    "s003":"§2-6. Conditional probability, independence, random variables",
    "s004":"§7. Variance, covariance, Chebyshev inequality",
    "s005":"§4. Law of large numbers, de Moivre-Laplace, Macmillan theorem",
    "s006":"§1. Local limit theorem, de Moivre-Laplace integral theorem",
    "s007":"§3. Integral theorem, applications",
    "s008":"§7. Normal distribution, error function",
    "s009":"§2. Parameter estimation, Fisher information",
    "s010":"§3. Random walk, arcsine law, ruin problem",
    "s011":"§3. Martingales, ballot theorem",
    "s012":"§3. Stopping times, Doob decomposition, Markov chains",
    "s013":"§3. Ergodic theorem for Markov chains",
    "s014":"§6. Strong Markov property, optimal stopping",
    "s015":"§5. Generating functions",
    "s016":"§8. Branching processes",
    "s017":"§1. Inclusion-exclusion, derangements",
    "s018":"§4. Inclusion-exclusion, derangements, generating functions",
    "s019":"Ch2 §1. Axioms of probability theory",
    "s020":"§2. σ-algebras, measures, monotone class theorem",
    "s021":"§5. Distribution functions, Lebesgue-Stieltjes measures on R^n",
    "s022":"§4. Kolmogorov extension theorem, random variables",
    "s023":"§3. Expectation, dominated convergence, change of variables",
    "s024":"§11. Lebesgue vs Riemann, integration by parts, cond. expectation",
    "s025":"§4. Conditional expectations, regular conditional probabilities",
    "s026":"§10. Generalized Bayes theorem, sufficient σ-algebras",
    "s027":"§2. Optimal estimation, normal correlation theorem",
    "s028":"§3. Distribution of functions of random variables",
    "s029":"§2. Kolmogorov extension, Ionescu Tulcea, convergence modes",
    "s030":"§2. L² theory, characteristic functions, uniqueness",
    "s031":"§5. Inversion formula, moments and semi-invariants",
    "s032":"§4. Gaussian vectors, covariance matrix",
    "s033":"§6. Gaussian systems, weak convergence, tightness",
    "s034":"§2. Continuity theorem, tightness, Helly theorem",
    "s035":"§3. Khinchin LLN, CLT for i.i.d., Poisson theorem",
    "s036":"§2. Lindeberg condition, Lyapunov condition",
    "s037":"§2. Nonclassical CLT conditions",
    "s038":"§1. Infinitely divisible distributions",
    "s039":"§2. Kolmogorov-Levy-Khinchin, stable distributions",
    "s040":"§1-5. Levy-Prokhorov metric, convergence in distribution",
    "s041":"§3. Continuous mapping theorem, variation distance",
    "s042":"§2. Kakutani-Hellinger distance, contiguity",
}

def strip_bold(text):
    return re.sub(r'\*{1,2}', '', text)

def find_concept_starts(filepath):
    """
    Find concept starts. Works by stripping bold markers then matching:
    (Definition|Theorem|...) (optional number) (optional (Name)) [. or end-of-header]
    Also handles multi-line headers like "Theorem 1\n(a) ..."
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    starts = []  # (line_idx, concept_type, number, name, title_text)

    for i, line in enumerate(lines):
        clean = strip_bold(line).strip()

        # Pattern 1: "Type N. Statement..." or "Type N (Name). Statement..." (all on one line with period)
        m1 = re.match(
            r'^(Definition|Theorem|Lemma|Proposition|Corollary|Axiom|Fundamental\s+Definition)'
            r'(?:\s+([0-9]+[a-z]?))?'
            r'(?:\s*\(([^)]+)\))?'
            r'\s*\.'
            r'\s*',
            clean, re.IGNORECASE
        )
        if m1:
            ctype_raw = m1.group(1).strip().lower()
            cnum = m1.group(2)
            cname = m1.group(3)
            if 'fundamental definition' in ctype_raw:
                ctype = 'definition'
            elif 'definition' in ctype_raw: ctype = 'definition'
            elif 'theorem' in ctype_raw: ctype = 'theorem'
            elif 'lemma' in ctype_raw: ctype = 'lemma'
            elif 'proposition' in ctype_raw: ctype = 'proposition'
            elif 'corollary' in ctype_raw: ctype = 'corollary'
            elif 'axiom' in ctype_raw: ctype = 'axiom'
            else: ctype = ctype_raw
            starts.append((i, ctype, cnum, cname, clean))
            continue

        # Pattern 2: "Type N" on its own line (no period, no name; statement follows on next lines)
        m2 = re.match(
            r'^(Definition|Theorem|Lemma|Proposition|Corollary|Axiom)'
            r'(?:\s+([0-9]+[a-z]?))?'
            r'\s*$',
            clean, re.IGNORECASE
        )
        if m2:
            ctype_raw = m2.group(1).strip().lower()
            cnum = m2.group(2)
            if 'definition' in ctype_raw: ctype = 'definition'
            elif 'theorem' in ctype_raw: ctype = 'theorem'
            elif 'lemma' in ctype_raw: ctype = 'lemma'
            elif 'proposition' in ctype_raw: ctype = 'proposition'
            elif 'corollary' in ctype_raw: ctype = 'corollary'
            elif 'axiom' in ctype_raw: ctype = 'axiom'
            else: ctype = ctype_raw
            # Title will be "Type N" if we can't find a better description
            starts.append((i, ctype, cnum, None, clean))
            continue

        # Pattern 3: "Type (Name)." — name in parens right after type keyword
        m3 = re.match(
            r'^(Definition|Theorem|Lemma|Proposition|Corollary|Axiom|Fundamental\s+Definition)'
            r'\s*\(([^)]+)\)'
            r'\s*\.?\s*',
            clean, re.IGNORECASE
        )
        if m3:
            ctype_raw = m3.group(1).strip().lower()
            cname = m3.group(2)
            if 'fundamental definition' in ctype_raw:
                ctype = 'definition'
            elif 'definition' in ctype_raw: ctype = 'definition'
            elif 'theorem' in ctype_raw: ctype = 'theorem'
            elif 'lemma' in ctype_raw: ctype = 'lemma'
            elif 'proposition' in ctype_raw: ctype = 'proposition'
            elif 'corollary' in ctype_raw: ctype = 'corollary'
            elif 'axiom' in ctype_raw: ctype = 'axiom'
            else: ctype = ctype_raw
            starts.append((i, ctype, None, cname, clean))
            continue

    return starts, lines

PROOF_RE = re.compile(r'^\*{0,2}Proof\.?\*{0,2}\s', re.IGNORECASE)

def extract_statement(lines, start_idx, end_idx):
    result_lines = []
    for i in range(start_idx, end_idx):
        result_lines.append(lines[i].rstrip('\n'))
    return '\n'.join(result_lines).strip()

def make_tex_statement(lines, start_idx, end_idx, header_is_solo=False):
    """
    Extract PURE LaTeX statement.
    If header_is_solo, the header line is standalone (like 'Theorem 1'),
    so the statement starts from start_idx+1.
    Otherwise, the header line also contains statement text.
    """
    if header_is_solo:
        stmt_start = start_idx + 1
    else:
        stmt_start = start_idx + 1  # always skip header line, content after it

    stmt_lines = []
    for i in range(stmt_start, end_idx):
        raw = lines[i].strip()
        # Stop at proof marker
        if PROOF_RE.match(raw):
            break
        # Keep the original line
        stmt_lines.append(lines[i].rstrip('\n'))

    tex = '\n'.join(stmt_lines).strip()
    tex = re.sub(r'\*{2}', '', tex)
    # Remove trailing proof fragments
    tex = re.sub(r'\n\*{0,2}Proof\.?\*{0,2}.*$', '', tex, flags=re.IGNORECASE)
    return tex

# ── Slug generation ──

def make_slug(ctype, cnum, cname, tex_stmt, full_stmt):
    """Generate semantic English slug from concept metadata and content."""

    # Priority 1: Explicit parenthetical name
    if cname:
        name = cname.strip().lower()
        name = re.sub(r'[^a-z0-9\s-]', '', name)
        name = re.sub(r'\s+', '-', name).strip('-')
        if len(name) > 3:
            return name[:80]

    # Priority 2: Check statement text for well-known theorem/lemma names
    tex_lower = (tex_stmt + ' ' + full_stmt).lower()[:600]

    # Extensive known concept patterns
    known = [
        # ── Named theorems ──
        ("central limit theorem for independent identically distributed", "central-limit-theorem-iid"),
        ("central limit theorem", "central-limit-theorem"),
        ("law of large numbers", "law-of-large-numbers"),
        ("khinchin's law of large numbers", "khinchin-law-of-large-numbers"),
        ("khinchin", "khinchin-law-of-large-numbers"),
        ("ergodic theorem", "ergodic-theorem"),
        ("ballot theorem", "ballot-theorem"),
        ("arcsine law", "arcsine-law"),
        ("continuity theorem", "continuity-theorem"),
        ("dominated convergence", "dominated-convergence-theorem"),
        ("monotone convergence", "monotone-convergence-theorem"),
        ("change of variables in a lebesgue integral", "change-of-variables-theorem"),
        ("change of variables", "change-of-variables-theorem"),
        ("inversion formula", "inversion-formula"),
        ("bayes theorem", "bayes-theorem"),
        ("generalized bayes", "generalized-bayes-theorem"),
        ("rao-blackwell", "rao-blackwell-theorem"),
        ("normal correlation", "normal-correlation-theorem"),
        ("kolmogorov's theorem on the extension", "kolmogorov-extension-theorem"),
        ("kolmogorov extension", "kolmogorov-extension-theorem"),
        ("ionescu tulcea's theorem", "ionescu-tulcea-theorem"),
        ("ionescu tulcea", "ionescu-tulcea-theorem"),
        ("macmillan", "macmillan-theorem"),
        ("poisson's theorem", "poisson-limit-theorem"),
        ("lindeberg condition", "lindeberg-condition"),
        ("lyapunov condition", "lyapunov-condition"),
        ("lyapounov", "lyapunov-condition"),
        ("levy-prokhorov metric", "levy-prokhorov-metric"),
        ("lévy-prokhorov", "levy-prokhorov-metric"),
        ("levy distance", "levy-distance"),
        ("kakutani-hellinger", "kakutani-hellinger-distance"),
        ("hellinger integral", "hellinger-integral"),
        ("hellinger distance", "hellinger-distance"),
        ("kolmogorov-levy-khinchin representation", "kolmogorov-levy-khinchin-representation"),
        ("lévy-khinchin representation", "levy-khinchin-representation"),
        ("kolmogorov–lévy–khinchin", "kolmogorov-levy-khinchin-representation"),
        ("infinitely divisible", "infinitely-divisible-distribution"),
        ("stable distribution", "stable-distribution"),
        ("stable if", "stable-distribution"),
        ("kolmogorov-smirnov", "kolmogorov-smirnov-test"),
        ("essen's inequality", "essens-inequality"),
        ("cauchy test for convergence", "cauchy-criterion-convergence"),
        ("cauchy criterion", "cauchy-criterion"),
        ("borel-cantelli", "borel-cantelli-lemma"),
        ("radon-nikodym", "radon-nikodym-theorem"),
        ("slutsky", "slutsky-theorem"),
        ("continuous mapping", "continuous-mapping-theorem"),
        ("prokhorov's theorem", "prokhorov-theorem"),
        ("helly's theorem", "helly-theorem"),
        ("helly theorem", "helly-theorem"),
        ("de moivre-laplace integral theorem", "de-moivre-laplace-integral-theorem"),
        ("de moivre-laplace local", "local-limit-theorem"),
        ("local limit theorem", "local-limit-theorem"),
        ("cramér", "cramer-rao-inequality"),
        ("rao-cramér", "cramer-rao-inequality"),
        ("fisher information", "fisher-information"),
        ("chebyshev inequality", "chebyshev-inequality"),
        ("bonferroni", "bonferroni-inequalities"),
        ("gumbel's inequalities", "gumbel-inequalities"),
        ("frechét's inequalities", "frechet-inequalities"),
        ("de morgan's laws", "de-morgan-laws"),

        # ── Named lemmas ──
        ("fatou's lemma", "fatou-lemma"),
        ("borel-cantelli lemma", "borel-cantelli-lemma"),
        ("lemma on taking limits", "limit-under-conditional-expectation"),

        # ── Named definitions/concepts ──
        ("bernoulli scheme", "bernoulli-scheme"),
        ("binomial distribution", "binomial-distribution"),
        ("conditional probability", "conditional-probability"),
        ("conditional expectation of the random variable", "conditional-expectation-given-random-variable"),
        ("conditional expectation under the condition", "conditional-expectation-given-random-variable"),
        ("conditional expectation", "conditional-expectation"),
        ("conditional probability of the event", "conditional-probability-wrt-sigma-algebra"),
        ("regular conditional probability", "regular-conditional-probability"),
        ("regular conditional distribution of", "regular-conditional-distribution"),
        ("regular conditional distribution", "regular-conditional-distribution"),
        ("regular distribution function for", "regular-distribution-function"),
        ("regular distribution function", "regular-distribution-function"),
        ("borel space", "borel-space"),
        ("total probability", "total-probability-formula"),
        ("multiplication formula for probabilities", "multiplication-formula"),
        ("multiplication formula", "multiplication-formula"),
        ("probability space", "probability-space"),
        ("finitely additive probability measure", "finitely-additive-probability-measure"),
        ("finitely additive measure", "finitely-additive-measure"),
        ("countably additive measure", "countably-additive-measure"),
        ("sigma-algebra", "sigma-algebra"),
        ("σ-algebra", "sigma-algebra"),
        ("monotone class", "monotone-class"),
        ("monotonic class", "monotone-class"),
        ("measurable space", "measurable-space"),
        ("measurable function", "measurable-function"),
        ("random variable", "random-variable"),
        ("simple random variable", "simple-random-variable"),
        ("n-dimensional random vector", "random-vector"),
        ("random process with time", "random-process"),
        ("random process", "random-process"),
        ("trajectory of the process", "trajectory"),
        ("realization", "realization"),
        ("characteristic function of the random vector", "characteristic-function-vector"),
        ("characteristic function of the random variable", "characteristic-function"),
        ("characteristic function is", "characteristic-function"),
        ("characteristic function", "characteristic-function"),
        ("uniformly integrable", "uniform-integrability"),
        ("sufficient σ-algebra", "sufficient-sigma-algebra"),
        ("sufficient sigma-algebra", "sufficient-sigma-algebra"),
        ("converges with probability one", "almost-sure-convergence"),
        ("almost surely", "almost-sure-convergence"),
        ("converges in the mean of order", "convergence-in-mean"),
        ("converges in distribution", "convergence-in-distribution"),
        ("converges in probability", "convergence-in-probability"),
        ("converge in distribution", "convergence-in-distribution"),
        ("events are called independent", "independence-of-events"),
        ("algebras of events are called independent", "independence-of-algebras"),
        ("random variables are said to be independent", "independence-of-random-variables"),
        ("mutually independent", "mutual-independence"),
        ("variance of the random variable", "variance"),
        ("covariance", "covariance"),
        ("covariance matrix", "covariance-matrix"),
        ("gaussian system", "gaussian-system"),
        ("gaussian vector", "gaussian-vector"),
        ("gaussian distribution", "gaussian-distribution"),
        ("brownian motion", "brownian-motion"),
        ("standard brownian motion", "brownian-motion"),
        ("expectation of the random variable", "expectation"),
        ("expectation of", "expectation"),
        ("lebesgue integral of the nonnegative", "lebesgue-integral"),
        ("lebesgue integral", "lebesgue-integral"),
        ("lebesgue-stieltjes", "lebesgue-stieltjes-measure"),
        ("distribution function on", "distribution-function"),
        ("distribution function", "distribution-function"),
        ("n-dimensional distribution function", "multivariate-distribution-function"),
        ("stopping time", "stopping-time"),
        ("markov chain", "markov-chain"),
        ("martingale", "martingale"),
        ("generating function", "generating-function"),
        ("branching process", "branching-process"),
        ("galton-watson", "branching-process"),
        ("inclusion-exclusion", "inclusion-exclusion-formula"),
        ("derangements", "derangements"),
        ("λ-system", "lambda-system"),
        ("lambda-system", "lambda-system"),
        ("π-system", "pi-system"),
        ("pi-system", "pi-system"),
        ("dynkin", "dynkin-system"),
        ("d-system", "dynkin-system"),
        ("distance in variation", "distance-in-variation"),
        ("orthogonal", "orthogonal-random-variables"),
        ("optimal estimator", "optimal-estimator"),
        ("mean-square", "optimal-estimator"),
        ("semi-invariants", "semi-invariants"),
        ("cumulants", "semi-invariants"),
        ("lebesgue vs riemann", "lebesgue-vs-riemann-integral"),
        ("integration by parts", "integration-by-parts"),
        ("efficient estimator", "efficient-estimator"),
        ("unbiased estimator", "unbiased-estimator"),
        ("fundamental definition", "probability-space-kolmogorov-axioms"),
        ("kolmogorov's axiom", "probability-space-kolmogorov-axioms"),
        ("probabilistic model", "probabilistic-model"),
        ("bernoulli random walk", "bernoulli-random-walk"),
        ("ruin problem", "ruin-problem"),
        ("optimal stopping", "optimal-stopping"),
        ("strong markov property", "strong-markov-property"),
        ("factorial moments", "factorial-moments"),
        ("bell's number", "bell-number"),
        ("algebra of events", "algebra-of-events"),
        ("decomposition of", "decomposition"),
        ("atoms of the", "decomposition-atoms"),
        ("ordered triple", "probabilistic-model"),
        ("tight family", "tight-family"),
        ("tight if", "tight-family"),
        ("relatively compact if", "relatively-compact-family"),
        ("relatively compact", "relatively-compact-family"),
        ("weakly convergent", "weak-convergence"),
        ("weak convergence", "weak-convergence"),
        ("converges weakly", "weak-convergence"),
        ("converges in general", "weak-convergence"),
        ("lindeberg condition", "lindeberg-condition"),
        ("contiguous", "contiguity"),
        ("independent with respect to", "independence-of-measurable-functions"),
        ("independence of collections", "independence-of-systems"),
        ("independence of random variables", "independence-of-random-variables"),
        ("independence of events", "independence-of-events"),
        ("statistically independent", "independence"),
        ("bernoulli random variables", "bernoulli-random-variable"),
        ("indicator of an event", "indicator-function"),
        ("lebesgue dominated convergence", "dominated-convergence-theorem"),
        ("jensen's inequality", "jensen-inequality"),
        ("hoelder's inequality", "holder-inequality"),
        ("holder inequality", "holder-inequality"),
        ("minkowski inequality", "minkowski-inequality"),
        ("distribution function satisfying", "distribution-function"),
        ("probability measure on", "probability-measure"),
        ("probability distribution", "probability-distribution"),
        ("binomial coefficient", "binomial-coefficient"),
        ("sample space", "sample-space"),
        ("elementary event", "elementary-event"),
        ("event consisting", "event-definition"),
        ("event is", "event-definition"),
    ]

    for pattern, slug_pattern in known:
        if pattern in tex_lower:
            return slug_pattern[:80]

    # Priority 3: Type abbreviation + number
    abbrevs = {'definition':'def','theorem':'thm','lemma':'lem',
               'proposition':'prop','corollary':'cor','axiom':'ax'}
    abbr = abbrevs.get(ctype, ctype[:3])
    if cnum:
        return f"{abbr}-{cnum}"

    # Priority 4: Extract from first meaningful words in statement
    words = re.findall(r'[a-zA-Z]+', tex_stmt + ' ' + full_stmt)
    stopwords = {'the','and','for','let','all','that','with','then','this','from',
                 'are','have','has','its','any','each','every','some','such','into',
                 'also','not','but','can','may','will','shall','does','which','been',
                 'was','were','had','said','called','denoted','defined','given'}
    meaningful = [w.lower() for w in words if len(w) > 3 and w.lower() not in stopwords]
    slug = '-'.join(meaningful[:4]) if meaningful else f"{abbr}-unnamed"
    return slug[:80]

def write_concept_files(concept, slug, dest_parent):
    out_dir = dest_parent / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    ctype = concept['type']
    title = concept['title']
    tex_stmt = concept['tex_statement']
    statement = concept['statement']
    chapter_num = concept['chapter_num']
    section_name = concept['section_name']

    content_hash = hashlib.md5(statement.encode()).hexdigest()[:12]

    # Difficulty
    diff = {'1': 'basic', '2': 'intermediate', '3': 'advanced'}.get(str(chapter_num), 'intermediate')

    # ── concept.yaml ──
    yaml_lines = [
        f"id: {slug}",
        f'title_en: "{title}"',
        'title_zh: ""',
        f'type: {ctype}',
        'domain: probability',
        'subdomain: probability-theory',
        f'difficulty: {diff}',
        'tags: []',
        'depends_on: {required: [], recommended: [], suggested: []}',
        f'source_books: [{{book_id: "gtm095", author: "Albert N. Shiryaev", title: "Probability-1 (3ed, 2016)", chapter: "Chapter {chapter_num}", section: "{section_name}", pages: "", role_in_book: ""}}]',
        f'content_hash: "{content_hash}"',
        'extraction_date: "2026-06-25"',
        'extraction_agent: "v7-section-test"',
    ]
    with open(out_dir / 'concept.yaml', 'w', encoding='utf-8') as f:
        f.write('\n'.join(yaml_lines) + '\n')

    # ── theorem.tex ──
    tex_clean = tex_stmt.strip()
    # Remove leading concept header text
    tex_clean = re.sub(r'^(Definition|Theorem|Lemma|Proposition|Corollary|Axiom)\s+\d+\.?\s*', '', tex_clean)
    tex_clean = re.sub(r'^Fundamental\s+Definition\.\s*', '', tex_clean)
    # Remove parenthetical name from start (it's in the header)
    tex_clean = re.sub(r'^\s*\([^)]+\)\.\s*', '', tex_clean)

    with open(out_dir / 'theorem.tex', 'w', encoding='utf-8') as f:
        f.write(tex_clean)
        if not tex_clean.endswith('\n'):
            f.write('\n')

    # ── introduce.en.md ──
    type_descs = {
        'definition': 'This definition introduces a fundamental concept in probability theory.',
        'theorem': 'This theorem establishes an important result in probability theory.',
        'lemma': 'This lemma provides a key technical result used in proving theorems.',
        'corollary': 'This corollary follows directly from a preceding result.',
        'proposition': 'This proposition states an important intermediate result.',
        'axiom': 'This axiom forms part of the foundational assumptions.',
    }
    intro = f"""---
role: introduce
locale: en
content_hash: "{content_hash}"
written_against: "{content_hash}"
---
{title}. {type_descs.get(ctype, '')}"""
    with open(out_dir / 'introduce.en.md', 'w', encoding='utf-8') as f:
        f.write(intro.strip() + '\n')

    return out_dir

def main():
    src_dir = Path(SRC)
    dest_dir = Path(DST)
    dest_dir.mkdir(parents=True, exist_ok=True)

    section_files = sorted(src_dir.glob('s*.md'))
    print(f"Processing {len(section_files)} section files...")

    slug_set = set()
    all_entries = []

    for sf in section_files:
        starts, lines = find_concept_starts(sf)
        if not starts:
            print(f"  {sf.name}: 0")
            continue

        section_id = sf.stem[:4]
        chapter_num = CHAPTER_MAP.get(section_id, 1)
        section_name = SECTION_NAMES.get(section_id, sf.stem)
        section_dir_name = sf.stem

        concepts_in_file = 0
        for idx, (start_line, ctype, cnum, cname, clean_header) in enumerate(starts):
            end_line = starts[idx + 1][0] if idx + 1 < len(starts) else len(lines)

            # Check if header is on its own line (solo) or part of a paragraph
            header_line = strip_bold(lines[start_line]).strip()
            # If the header line has only the concept marker (no statement following on same line)
            header_is_solo = bool(re.match(
                r'^(Definition|Theorem|Lemma|Proposition|Corollary|Axiom)\s*\d*\s*$',
                header_line, re.IGNORECASE))

            raw_stmt = extract_statement(lines, start_line, end_line)
            tex_stmt = make_tex_statement(lines, start_line, end_line, header_is_solo)

            title = clean_header.strip().rstrip('.').strip()

            slug = make_slug(ctype, cnum, cname, tex_stmt, raw_stmt[:400])
            unique_slug = slug
            counter = 1
            while unique_slug in slug_set:
                unique_slug = f"{slug}-{counter}"
                counter += 1
            slug_set.add(unique_slug)

            concept = {
                'type': ctype, 'number': cnum, 'name': cname,
                'title': title, 'statement': raw_stmt,
                'tex_statement': tex_stmt,
                'section_id': section_id,
                'chapter_num': chapter_num,
                'section_name': section_name,
            }
            all_entries.append((concept, unique_slug, section_dir_name))
            concepts_in_file += 1

        print(f"  {sf.name}: {concepts_in_file}")

    print(f"\nTotal concepts: {len(all_entries)}")
    print("Writing output files...")

    written = 0
    for concept, slug, section_dir in all_entries:
        try:
            dest_parent = dest_dir / section_dir
            write_concept_files(concept, slug, dest_parent)
            written += 1
        except Exception as e:
            print(f"  ERROR [{slug}]: {e}")

    print(f"Successfully wrote {written}/{len(all_entries)} concepts")

    # .done marker
    done_file = dest_dir / '.done'
    with open(done_file, 'w') as f:
        f.write(f"DONE\nExtracted {written} concepts from GTM095 on {date.today()}\n")
    print(f"Done marker: {done_file}")

    type_counts = Counter(c['type'] for c, _, _ in all_entries)
    print(f"Concepts by type: {dict(type_counts)}")

if __name__ == '__main__':
    main()
