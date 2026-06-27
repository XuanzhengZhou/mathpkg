#!/usr/bin/env python3
"""
GTM052 (Hartshorne, Algebraic Geometry) Concept Extractor v8.
Extracts ALL theorems, definitions, lemmas, propositions, corollaries, axioms
from 49 stitched section files, writing 5-file format per concept.
"""
import re, os, json, hashlib, textwrap
from pathlib import Path
from datetime import datetime

# ── Configuration ──────────────────────────────────────────────
BOOK_ID = "gtm052"
SECTIONS_DIR = Path("/home/a123/文档/mathpkg/pipeline_output/stitched_sections/(GTM052)Algebraic geometry (1977, Springer) - libgen.lc")
OUTPUT_DIR = Path("/home/a123/文档/mathpkg/pipeline_output/math_pkg_tmp/concepts_batch6/gtm052")
DONE_FILE = OUTPUT_DIR / ".done"
DATE = "2026-06-27"
AGENT = "v8-full-extract"

# ── Section file → Chapter.Section mapping ──────────────────────
# The section files correspond to sequentially numbered sections in the book:
# s001-s005 = Ch.I  §1-§5 (but s005 contains both §5 end + §6 start)
# s006-s013 = Ch.II §1-§8
# s014-s025 = Ch.III §1-§12
# s026-s031 = Ch.IV §1-§6
# s032-s040 = Ch.V  §1-§5 (+ App A start)
# s041-s045 = App A (Intersection Theory)
# s046-s048 = App B (Transcendental Methods)
# s049     = App C (Weil Conjectures)

# We need to figure out the mapping from the text content.
# From reading the text, we can identify chapter headers.
# Let's build a mapping dynamically from section content analysis.

CHAPTER_MAP = {
    # Section file index → (Chapter, Section in book)
    # Ch.I: Varieties (§1-§5)
    1: ("I", "1"),   # §1 Affine Varieties
    2: ("I", "2"),   # §2 Projective Varieties
    3: ("I", "3"),   # §3 Morphisms
    4: ("I", "4"),   # §4 Rational Maps
    5: ("I", "5"),   # §5 Nonsingular Varieties
    6: ("I", "6"),   # §6 Nonsingular Curves
    # Ch.II: Schemes
    7: ("II", "1"),  # §1 Sheaves
    8: ("II", "2"),  # §2 Schemes
    9: ("II", "3"),  # §3 First Properties of Schemes
    10: ("II", "4"), # §4 Separated and Proper Morphisms
    11: ("II", "5"), # §5 Sheaves of Modules
    12: ("II", "6"), # §6 Divisors
    13: ("II", "7"), # §7 Projective Morphisms
    # Ch.III: Cohomology
    14: ("III", "1"),  # §1 Derived Functors
    15: ("III", "2"),  # §2 Cohomology of Sheaves
    16: ("III", "3"),  # §3 Cohomology of Affine Schemes
    17: ("III", "4"),  # §4 Cech Cohomology
    18: ("III", "5"),  # §5 Cohomology of Projective Space
    19: ("III", "6"),  # §6 Ext Groups and Sheaves
    20: ("III", "7"),  # §7 Serre Duality
    21: ("III", "8"),  # §8 Higher Direct Images
    22: ("III", "9"),  # §9 Flat Morphisms
    23: ("III", "10"), # §10 Smooth Morphisms
    24: ("III", "11"), # §11 Formal Functions
    25: ("III", "12"), # §12 Semicontinuity
    # Ch.IV: Curves
    26: ("IV", "1"),   # §1 Riemann-Roch Theorem
    27: ("IV", "2"),   # §2 Hurwitz's Theorem
    28: ("IV", "3"),   # §3 Embeddings in Projective Space
    29: ("IV", "4"),   # §4 Elliptic Curves
    30: ("IV", "5"),   # §5 Canonical Embedding
    31: ("IV", "6"),   # §6 Classification of Curves in P^3
    # Ch.V: Surfaces
    32: ("V", "1"),    # §1 Geometry on a Surface
    33: ("V", "2"),    # §2 Ruled Surfaces
    34: ("V", "3"),    # §3 Monoidal Transformations
    35: ("V", "4"),    # §4 The Cubic Surface in P^3
    36: ("V", "5"),    # §5 Birational Transformations
    37: ("V", "5"),    # §5 continued (Castelnuovo)
    38: ("V", "6"),    # §6 Classification of Surfaces
    # App A: Intersection Theory
    39: ("A", "1"),    # §1 Intersection Theory
    40: ("A", "2"),    # §2 Properties of Chow Ring
    41: ("A", "3"),    # §3 Chern Classes
    42: ("A", "4"),    # §4 Riemann-Roch Theorem
    43: ("A", "5"),    # §5 Supplementary
    44: ("A", "5"),    # §5 continued
    45: ("A", "6"),    # §6 Algebraic Equivalence
    # App B: Transcendental Methods
    46: ("B", "1"),    # §1 Associated Complex Analytic Space
    47: ("B", "2"),    # §2 Comparison of Categories
    48: ("B", "3"),    # §3 When is a Compact Complex Manifold Algebraic?
    # App C: The Weil Conjectures
    49: ("C", "1"),    # §1-4 Weil Conjectures
}

# ── Helper Functions ────────────────────────────────────────────

def slugify(text):
    """Generate semantic lowercase-hyphen English slug."""
    # Remove LaTeX, special chars
    text = re.sub(r'\$\$.*?\$\$', '', text, flags=re.DOTALL)
    text = re.sub(r'\$.*?\$', '', text)
    text = re.sub(r'\\[a-zA-Z]+(\{[^}]*\})*', '', text)
    text = re.sub(r'[^a-zA-Z0-9\s-]', '', text.lower())
    text = re.sub(r'\s+', '-', text.strip())
    # Truncate to reasonable length
    if len(text) > 80:
        words = text.split('-')
        text = '-'.join(words[:8])
    return text[:100].strip('-')

def content_hash(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()[:12]

def demarkdown_title(title):
    """Clean up markdown formatting to get plain text title."""
    title = re.sub(r'\*\*', '', title)
    title = re.sub(r'#+\s*', '', title)
    title = re.sub(r'\n+', ' ', title)
    title = re.sub(r'\s+', ' ', title).strip()
    return title

def clean_latex(text):
    """Basic cleanup of OCR LaTeX artifacts."""
    text = re.sub(r'\\mathbf\{A\}', r'\\mathbf{A}', text)
    text = re.sub(r'𝐀', r'\\mathbf{A}', text)
    text = re.sub(r'\\mathfrak\{a\}', r'\\mathfrak{a}', text)
    # Fix common OCR errors
    text = text.replace('𝒞', '\\mathcal{C}')
    text = text.replace('𝒪', '\\mathcal{O}')
    text = text.replace('ℱ', '\\mathcal{F}')
    text = text.replace('ℐ', '\\mathcal{I}')
    text = text.replace('𝒢', '\\mathcal{G}')
    text = text.replace('ℋ', '\\mathcal{H}')
    return text

# ── Main Extraction Logic ──────────────────────────────────────

def parse_concepts_from_section(text, section_num):
    """
    Parse a section file and extract all formal concepts.
    Returns list of dicts with keys:
      type, label, statement, proof, chapter, section, exercises
    """
    ch, sec = CHAPTER_MAP.get(section_num, ("?", str(section_num)))
    concepts = []

    lines = text.split('\n')

    # First, try to identify chapter/section from text content
    # Look for patterns like "1 Affine Varieties", "2 Projective Varieties", etc.
    for i, line in enumerate(lines[:20]):
        m = re.match(r'^(\d+)\s+([A-Z][A-Za-z\s,]+)$', line.strip())
        if m:
            sec_num = m.group(1)
            sec_name = m.group(2).strip()
            # This is a section header within a chapter

    # Find exercise blocks
    exercise_blocks = []
    in_exercises = False
    ex_start = -1
    for i, line in enumerate(lines):
        if re.match(r'^EXERCISES?\s*$', line.strip(), re.IGNORECASE):
            in_exercises = True
            ex_start = i
        elif in_exercises and re.match(r'^\d+\s+(January|February|March|April|May|June|July|August|September|October|November|December)', line.strip()):
            # Probably a new chapter/section header - end of exercises
            in_exercises = False
            exercise_blocks.append((ex_start, i))
        elif in_exercises and re.match(r'^CHAPTER\s', line.strip(), re.IGNORECASE):
            in_exercises = False
            exercise_blocks.append((ex_start, i))
        elif in_exercises and re.match(r'^Appendix\s', line.strip(), re.IGNORECASE):
            in_exercises = False
            exercise_blocks.append((ex_start, i))
    if in_exercises:
        exercise_blocks.append((ex_start, len(lines)))

    # Parse exercises from blocks
    exercises = []
    for start, end in exercise_blocks:
        ex_text = '\n'.join(lines[start+1:end])
        # Split into individual exercises
        ex_parts = re.split(r'\n(?=\d+\.\d*\.?\s)', ex_text)
        for part in ex_parts:
            part = part.strip()
            if part and re.match(r'^\d+\.\d*', part):
                m = re.match(r'^(\d+\.\d*)', part)
                ex_num = m.group(1)
                exercises.append({'number': ex_num, 'text': part, 'chapter': ch, 'section': sec})

    # Now find concepts by scanning for patterns
    # Join lines back for multi-line pattern matching
    full_text = text

    # Patterns for concept identification
    # Order matters: check Theorem before Definition (to avoid matching "Definition" inside theorem statements)
    concept_patterns = [
        # Theorem
        (r'\*\*Theorem\s+([\d.A-Za-z]+)\*\*\s*[\.:]?\s*', 'theorem'),
        # Proposition
        (r'\*\*Proposition\s+([\d.A-Za-z]+)\*\*\s*[\.:]?\s*', 'proposition'),
        # Lemma
        (r'\*\*Lemma\s+([\d.A-Za-z]+)\*\*\s*[\.:]?\s*', 'lemma'),
        # Corollary
        (r'\*\*Corollary\s+([\d.A-Za-z]+)\*\*\s*[\.:]?\s*', 'corollary'),
        # Definition
        (r'\*\*Definition\*\*\s*[\.:]?\s*', 'definition'),
    ]

    # Also handle non-bold patterns
    loose_patterns = [
        (r'(?:^|\n)Theorem\s+([\d.A-Za-z]+)\s*[\.:]\s*', 'theorem'),
        (r'(?:^|\n)Proposition\s+([\d.A-Za-z]+)\s*[\.:]\s*', 'proposition'),
        (r'(?:^|\n)Lemma\s+([\d.A-Za-z]+)\s*[\.:]\s*', 'lemma'),
        (r'(?:^|\n)Corollary\s+([\d.A-Za-z]+)\s*[\.:]\s*', 'corollary'),
        (r'(?:^|\n)Definition\s*[\.:]\s*', 'definition'),
    ]

    # Process bold patterns first
    for pattern, ctype in concept_patterns:
        for m in re.finditer(pattern, full_text):
            label = m.group(1) if m.lastindex else ''
            start_pos = m.end()
            # Find end of statement (before Proof. or next concept)
            end_pos = find_statement_end(full_text, start_pos)
            statement = full_text[start_pos:end_pos].strip()
            # Find proof
            proof = find_proof(full_text, end_pos)

            if statement:
                concepts.append({
                    'type': ctype,
                    'label': label.strip(),
                    'statement': clean_latex(statement),
                    'proof': clean_latex(proof) if proof else '',
                    'chapter': ch,
                    'section': sec,
                    'source_file': section_num
                })

    # Process loose patterns (only if no bold match at same position)
    bold_positions = set()
    for pattern, _ in concept_patterns:
        for m in re.finditer(pattern, full_text):
            bold_positions.add(m.start())

    for pattern, ctype in loose_patterns:
        for m in re.finditer(pattern, full_text):
            if m.start() in bold_positions:
                continue  # Already captured by bold pattern
            label = m.group(1) if m.lastindex else ''
            start_pos = m.end()
            end_pos = find_statement_end(full_text, start_pos)
            statement = full_text[start_pos:end_pos].strip()
            proof = find_proof(full_text, end_pos)

            if statement:
                concepts.append({
                    'type': ctype,
                    'label': label.strip(),
                    'statement': clean_latex(statement),
                    'proof': clean_latex(proof) if proof else '',
                    'chapter': ch,
                    'section': sec,
                    'source_file': section_num
                })

    # Deduplicate concepts that are very close in position
    concepts = deduplicate_concepts(concepts)

    # Attach exercises
    for c in concepts:
        c['exercises'] = exercises if exercises else []

    return concepts

def find_statement_end(text, start):
    """Find where a concept statement ends (before 'Proof.' or next concept)."""
    # Look for the next concept marker or Proof.
    end_markers = [
        (r'\n\*\*Proof', start + 1),
        (r'\nProof\s*[\.:]', start + 1),
        (r'\n\*\*Theorem', start + 1),
        (r'\n\*\*Proposition', start + 1),
        (r'\n\*\*Lemma', start + 1),
        (r'\n\*\*Corollary', start + 1),
        (r'\n\*\*Definition', start + 1),
        (r'\nTheorem\s+[\d]', start + 1),
        (r'\nProposition\s+[\d]', start + 1),
        (r'\nLemma\s+[\d]', start + 1),
        (r'\nCorollary\s+[\d]', start + 1),
        (r'\nDefinition\s*[\.:]', start + 1),
        (r'\nEXERCISES?\s*\n', start + 1),
        (r'\nCHAPTER\s', start + 1),
    ]

    best_end = len(text)
    for pattern, min_pos in end_markers:
        m = re.search(pattern, text[min_pos:])
        if m:
            end = min_pos + m.start()
            if end < best_end:
                best_end = end

    return best_end

def find_proof(text, start):
    """Extract proof text if present."""
    # Look for "Proof." marker
    proof_patterns = [
        r'\n\*\*Proof\*\*\s*[\.:]?\s*',
        r'\nProof\s*[\.:]\s*',
        r'\nPROOF\s*[\.:]?\s*',
    ]

    proof_start = None
    for pattern in proof_patterns:
        m = re.search(pattern, text[start:])
        if m:
            proof_start = start + m.start() + len(m.group(0))
            break

    if proof_start is None:
        return ''

    # Find end of proof (next concept or exercise block)
    proof_end = find_statement_end(text, proof_start)

    proof_text = text[proof_start:proof_end].strip()

    # Remove trailing QED markers
    proof_text = re.sub(r'\s*[□■∎]\s*$', '', proof_text)

    return proof_text

def deduplicate_concepts(concepts):
    """Remove duplicate concepts based on position proximity."""
    # Sort by appearance (use statement hash as proxy)
    seen_hashes = set()
    unique = []
    for c in concepts:
        h = content_hash(c['statement'][:200])
        if h not in seen_hashes:
            seen_hashes.add(h)
            unique.append(c)
    return unique

def generate_slug(concept):
    """Generate semantic English slug for a concept."""
    ctype = concept['type']
    label = concept['label']
    statement = concept['statement']

    # Try to extract meaningful words from statement
    # Clean the statement for slug generation
    clean = re.sub(r'\$\$.*?\$\$', ' ', statement, flags=re.DOTALL)
    clean = re.sub(r'\$.*?\$', ' ', clean)
    clean = re.sub(r'\\[a-zA-Z]+(\{[^}]*\})*', ' ', clean)
    clean = re.sub(r'[^a-zA-Z\s]', ' ', clean.lower())
    clean = re.sub(r'\s+', ' ', clean).strip()

    words = clean.split()[:10]  # First 10 words
    slug = '-'.join(words)

    # Add label number for uniqueness
    if label:
        label_part = label.replace('.', '-').replace(' ', '-').lower()
        slug = f"{label_part}-{slug}" if slug else label_part

    slug = slug[:120].strip('-')

    # Ensure uniqueness with hash if needed
    if len(slug) < 5:
        slug = f"{ctype}-{label.replace('.', '-')}" if label else f"{ctype}-unnamed"

    return slug

def write_concept_files(concept, output_base):
    """Write the 5-file format for a concept."""
    slug = concept['slug']
    concept_dir = output_base / slug
    concept_dir.mkdir(parents=True, exist_ok=True)

    ctype = concept['type']
    label = concept['label']
    statement = concept['statement']
    proof = concept['proof']
    ch = concept['chapter']
    sec = concept['section']

    # Build title from statement
    title_en = demarkdown_title(concept.get('title_en', ''))
    if not title_en:
        # Use first line of statement as title
        first_line = statement.split('\n')[0].strip()
        first_line = re.sub(r'\$\$.*?\$\$', '', first_line)
        first_line = re.sub(r'\$.*?\$', '', first_line)
        first_line = re.sub(r'\\[a-zA-Z]+(\{[^}]*\})*', '', first_line)
        first_line = first_line.strip('.,;: ')
        if label:
            title_en = f"{ctype.title()} {label}: {first_line}" if first_line else f"{ctype.title()} {label}"
        else:
            title_en = first_line if first_line else f"{ctype.title()}"

    # ── FILE 1: concept.yaml ──
    yaml_content = f"""id: {slug}
title_en: "{title_en}"
title_zh: ""
type: {ctype}
domain: geometry
subdomain: algebraic-geometry
difficulty: advanced
tags: []
depends_on:
  required: []
  recommended: []
  suggested: []
source_books:
  - book_id: "{BOOK_ID}"
    author: "Robin Hartshorne"
    title: "Algebraic Geometry"
    chapter: "{ch}"
    section: "§{sec}"
    pages: ""
    role_in_book: ""
content_hash: "{content_hash(statement)}"
extraction_date: "{DATE}"
extraction_agent: "{AGENT}"
"""
    (concept_dir / "concept.yaml").write_text(yaml_content, encoding='utf-8')

    # ── FILE 2: theorem.tex ──
    # Extract pure LaTeX statement (no proof, no natural language)
    tex_statement = extract_pure_latex_statement(statement)
    (concept_dir / "theorem.tex").write_text(tex_statement, encoding='utf-8')

    # ── FILE 3: introduce.en.md ──
    intro_text = generate_intro(concept)
    intro = f"""---
role: introduce
locale: en
content_hash: "{content_hash(intro_text)}"
written_against: ""
---
{intro_text}
"""
    (concept_dir / "introduce.en.md").write_text(intro, encoding='utf-8')

    # ── FILE 4: proof file (for theorems/propositions/lemmas/corollaries) ──
    if ctype in ('theorem', 'proposition', 'lemma', 'corollary') and proof:
        proof_filename = f"proof_{BOOK_ID}_{ch}_{sec}.en.md"
        # Make label safe for filename
        safe_label = label.replace('.', '-').replace(' ', '-')
        proof_text = f"""---
role: proof
locale: en
of_concept: {slug}
source_book: {BOOK_ID}
source_chapter: "{ch}"
source_section: "§{sec}"
---
{proof}
"""
        (concept_dir / proof_filename).write_text(proof_text, encoding='utf-8')

    # ── FILE 5: exercise files ──
    for ex in concept.get('exercises', []):
        ex_num = ex['number'].replace('.', '-')
        ex_filename = f"exercise_{BOOK_ID}_{ch}_{sec}_{ex_num}.en.md"
        ex_text = f"""---
role: exercise
locale: en
chapter: "{ch}"
section: "§{sec}"
exercise_number: {ex['number']}
---
{ex['text']}
"""
        ex_dir = concept_dir / "exercises"
        ex_dir.mkdir(exist_ok=True)
        (ex_dir / ex_filename).write_text(ex_text, encoding='utf-8')

    return concept_dir

def extract_pure_latex_statement(statement):
    """Extract only the LaTeX mathematical content of a statement."""
    # Remove natural language wrapper but keep math
    # The statement will have mixed text and math
    # For theorem.tex we want the statement with LaTeX math preserved
    # but with minimal natural language

    # Wrap display math properly
    lines = statement.split('\n')
    tex_lines = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Preserve lines with math
        tex_lines.append(line)

    return '\n'.join(tex_lines)

def generate_intro(concept):
    """Generate 2-4 English sentences introducing the concept."""
    ctype = concept['type']
    label = concept['label']
    statement = concept['statement']
    ch = concept['chapter']
    sec = concept['section']

    # Extract first sentence of statement for context
    first_sent = statement.split('.')[0].strip() if statement else ''
    first_sent = re.sub(r'\$\$.*?\$\$', '', first_sent)
    first_sent = re.sub(r'\$.*?\$', '', first_sent)
    first_sent = re.sub(r'\\[a-zA-Z]+(\{[^}]*\})*', '', first_sent)
    first_sent = first_sent.strip()

    label_str = f" {label}" if label else ""

    if ctype == 'definition':
        return f"This is a definition{label_str} from Chapter {ch}, Section §{sec} of Hartshorne's Algebraic Geometry. It introduces a key concept in the theory of algebraic geometry over an algebraically closed field."
    elif ctype == 'theorem':
        return f"This is Theorem{label_str} from Chapter {ch}, Section §{sec} of Hartshorne's Algebraic Geometry. It establishes an important result relating algebraic and geometric properties of varieties and schemes."
    elif ctype == 'proposition':
        return f"This is Proposition{label_str} from Chapter {ch}, Section §{sec} of Hartshorne's Algebraic Geometry. It is a fundamental building block used throughout the development of scheme theory and cohomology."
    elif ctype == 'lemma':
        return f"This is Lemma{label_str} from Chapter {ch}, Section §{sec} of Hartshorne's Algebraic Geometry. It provides a technical result used in the proof of larger theorems."
    elif ctype == 'corollary':
        return f"This is Corollary{label_str} from Chapter {ch}, Section §{sec} of Hartshorne's Algebraic Geometry. It follows directly from the preceding theorem or proposition."
    else:
        return f"This is a {ctype}{label_str} from Chapter {ch}, Section §{sec} of Hartshorne's Algebraic Geometry."

def process_section(section_num):
    """Process one section file and extract all concepts."""
    section_file = SECTIONS_DIR / f"s{section_num:03d}_Section_{section_num}.md"

    # Handle non-contiguous numbering (section files skip some numbers)
    # The actual mapping between file index and section number is in the filenames
    # s028_Section_29.md → section_num=28 but book section is 29

    if not section_file.exists():
        # Try to find the actual file
        import glob
        pattern = str(SECTIONS_DIR / f"s{section_num:03d}_*.md")
        matches = list(Path(SECTIONS_DIR).glob(f"s{section_num:03d}_*.md"))
        if matches:
            section_file = matches[0]
        else:
            print(f"  Section file not found for index {section_num}")
            return []

    text = section_file.read_text(encoding='utf-8')
    concepts = parse_concepts_from_section(text, section_num)

    print(f"  Found {len(concepts)} concepts in s{section_num:03d}")
    return concepts

# ── Main ────────────────────────────────────────────────────────

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    all_sections = sorted([
        int(f.stem.split('_')[0][1:])
        for f in SECTIONS_DIR.glob("s[0-9]*.md")
        if f.stem.split('_')[0][1:].isdigit()
    ])

    print(f"Processing {len(all_sections)} sections: {all_sections}")

    total_concepts = 0

    for sec_num in all_sections:
        print(f"\nSection s{sec_num:03d} (Ch.{CHAPTER_MAP.get(sec_num, ('?','?'))[0]} §{CHAPTER_MAP.get(sec_num, ('?','?'))[1]}):")
        concepts = process_section(sec_num)

        for i, c in enumerate(concepts):
            slug = generate_slug(c)
            c['slug'] = slug
            c['title_en'] = demarkdown_title(c['statement'][:200])

            try:
                write_concept_files(c, OUTPUT_DIR)
            except Exception as e:
                print(f"    ERROR writing {slug}: {e}")
                continue

        total_concepts += len(concepts)
        print(f"  Wrote {len(concepts)} concepts")

    print(f"\n{'='*60}")
    print(f"Total: {total_concepts} concepts extracted from {len(all_sections)} sections")

    # Write .done marker
    DONE_FILE.write_text(f"DONE at {datetime.now().isoformat()}\n{total_concepts} concepts extracted\n")

if __name__ == '__main__':
    main()
