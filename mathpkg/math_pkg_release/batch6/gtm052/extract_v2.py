#!/usr/bin/env python3
"""
GTM052 (Hartshorne, Algebraic Geometry) Concept Extractor v8 — Improved.
Extracts ALL labeled definitions, theorems, propositions, lemmas, corollaries.
"""
import re, os, json, hashlib
from pathlib import Path
from datetime import datetime

BOOK_ID = "gtm052"
SECTIONS_DIR = Path("/home/a123/文档/mathpkg/pipeline_output/stitched_sections/(GTM052)Algebraic geometry (1977, Springer) - libgen.lc")
OUTPUT_DIR = Path("/home/a123/文档/mathpkg/pipeline_output/math_pkg_tmp/concepts_batch6/gtm052")
DONE_FILE = OUTPUT_DIR / ".done"
DATE = "2026-06-27"
AGENT = "v8-full-extract"

# Chapter mapping — will be refined by actual text analysis
CHAPTER_MAP = {
    1:("I","1"),2:("I","2"),3:("I","3"),4:("I","4"),5:("I","5"),6:("I","6"),
    7:("II","1"),8:("II","2"),9:("II","3"),10:("II","4"),11:("II","5"),12:("II","6"),13:("II","7"),
    14:("III","1"),15:("III","2"),16:("III","3"),17:("III","4"),18:("III","5"),
    19:("III","6"),20:("III","7"),21:("III","8"),22:("III","9"),23:("III","10"),
    24:("III","11"),25:("III","12"),
    26:("IV","1"),27:("IV","2"),28:("IV","3"),29:("IV","4"),30:("IV","5"),31:("IV","6"),
    32:("V","1"),33:("V","2"),34:("V","3"),35:("V","4"),36:("V","5"),37:("V","5"),38:("V","6"),
    39:("A","1"),40:("A","2"),41:("A","3"),42:("A","4"),43:("A","5"),44:("A","5"),45:("A","6"),
    46:("B","1"),47:("B","2"),48:("B","3"),49:("C","1"),
}

def content_hash(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()[:12]

def clean_latex(text):
    """Fix common OCR artifacts."""
    replacements = {
        '𝐀': '\\mathbf{A}', '𝒞': '\\mathcal{C}', '𝒪': '\\mathcal{O}',
        'ℱ': '\\mathcal{F}', 'ℐ': '\\mathcal{I}', '𝒢': '\\mathcal{G}',
        'ℋ': '\\mathcal{H}', '𝒦': '\\mathcal{K}', '𝒰': '\\mathcal{U}',
        '𝒱': '\\mathcal{V}', '𝒲': '\\mathcal{W}',
        '̂': '', '̃': '',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

def find_concept_markers(text):
    """
    Find ALL concept markers in the text.
    Returns sorted list of (position, type, label, raw_match).
    """
    markers = []

    # Pattern: **Definition.** or **Definition:**
    for m in re.finditer(r'\*\*Definition\*\*\s*[\.:]', text):
        markers.append((m.start(), 'definition', '', m.group()))

    # Pattern: **Theorem N.M.** or **Theorem N.MA.**
    for m in re.finditer(r'\*\*Theorem\s+([\d]+(?:\.[\d]+)?[A-Z]?)\*\*\s*[\.:]', text):
        markers.append((m.start(), 'theorem', m.group(1), m.group()))

    # Pattern: **Proposition N.M.** or **Proposition N.MA.**
    for m in re.finditer(r'\*\*Proposition\s+([\d]+(?:\.[\d]+)?[A-Z]?)\*\*\s*[\.:]', text):
        markers.append((m.start(), 'proposition', m.group(1), m.group()))

    # Pattern: **Lemma N.M.**
    for m in re.finditer(r'\*\*Lemma\s+([\d]+(?:\.[\d]+)?[A-Z]?)\*\*\s*[\.:]', text):
        markers.append((m.start(), 'lemma', m.group(1), m.group()))

    # Pattern: **Corollary N.M.**
    for m in re.finditer(r'\*\*Corollary\s+([\d]+(?:\.[\d]+)?[A-Z]?)\*\*\s*[\.:]', text):
        markers.append((m.start(), 'corollary', m.group(1), m.group()))

    # Now non-bold patterns
    # These should NOT overlap with bold patterns already found
    bold_positions = {m[0] for m in markers}

    # Definition. or Definition: (standalone, not bold)
    for m in re.finditer(r'(?:^|\n)Definition\s*[\.:]', text, re.MULTILINE):
        pos = m.start()
        if pos not in bold_positions and not text[max(0,pos-1):pos+len(m.group())].startswith('*'):
            markers.append((pos, 'definition', '', m.group()))

    # Theorem N.M. or Theorem N.MA. (non-bold)
    for m in re.finditer(r'(?:^|\n)Theorem\s+([\d]+(?:\.[\d]+)?[A-Z]?)\s*[\.:]', text, re.MULTILINE):
        pos = m.start()
        if pos not in bold_positions and not text[max(0,pos-1):pos+len(m.group())].startswith('*'):
            markers.append((pos, 'theorem', m.group(1), m.group()))

    # Proposition N.M. or N.MA. (non-bold)
    for m in re.finditer(r'(?:^|\n)Proposition\s+([\d]+(?:\.[\d]+)?[A-Z]?)\s*[\.:]', text, re.MULTILINE):
        pos = m.start()
        if pos not in bold_positions and not text[max(0,pos-1):pos+len(m.group())].startswith('*'):
            markers.append((pos, 'proposition', m.group(1), m.group()))

    # Lemma N.M. (non-bold)
    for m in re.finditer(r'(?:^|\n)Lemma\s+([\d]+(?:\.[\d]+)?[A-Z]?)\s*[\.:]', text, re.MULTILINE):
        pos = m.start()
        if pos not in bold_positions and not text[max(0,pos-1):pos+len(m.group())].startswith('*'):
            markers.append((pos, 'lemma', m.group(1), m.group()))

    # Corollary N.M. (non-bold)
    for m in re.finditer(r'(?:^|\n)Corollary\s+([\d]+(?:\.[\d]+)?[A-Z]?)\s*[\.:]', text, re.MULTILINE):
        pos = m.start()
        if pos not in bold_positions and not text[max(0,pos-1):pos+len(m.group())].startswith('*'):
            markers.append((pos, 'corollary', m.group(1), m.group()))

    # Sort by position, deduplicate by position
    markers.sort(key=lambda x: x[0])
    seen_pos = set()
    unique = []
    for pos, ctype, label, raw in markers:
        if pos not in seen_pos:
            seen_pos.add(pos)
            unique.append((pos, ctype, label, raw))

    return unique

def find_proof_boundary(text, start):
    """Find where the proof (if any) ends."""
    # Look for next concept marker or exercise block or chapter break
    stop_patterns = [
        r'\n\*\*(?:Definition|Theorem|Proposition|Lemma|Corollary)',
        r'\n(?:Definition|Theorem|Proposition|Lemma|Corollary)\s+(?:\d|\.)',
        r'\n(?:Definition|Theorem|Proposition|Lemma|Corollary)\s*[\.:]',
        r'\nEXERCISES?\s*\n',
        r'\nCHAPTER\s+[IVX]+',
        r'\nAppendix\s',
        r'\*\*(?:Definition|Theorem|Proposition|Lemma|Corollary)',
    ]
    best_end = len(text)
    for pat in stop_patterns:
        m = re.search(pat, text[start:])
        if m:
            end = start + m.start()
            if end < best_end:
                best_end = end
    return best_end

def extract_statement_and_proof(text, start, end, next_marker_pos):
    """
    Extract statement and proof from a concept region.
    start: position right after the concept label
    end: position of next marker (or end of text)
    """
    region = text[start:end]

    # Look for Proof. marker within region
    proof_patterns = [
        r'\n\*\*Proof\*\*\s*[\.:]?\s*',
        r'\nProof\s*[\.:]?\s*',
        r'\nPROOF\s*[\.:]?\s*',
    ]

    proof_start = len(region)  # default: no proof
    proof_marker_end = 0

    for pat in proof_patterns:
        m = re.search(pat, region)
        if m and m.start() < proof_start:
            proof_start = m.start()
            proof_marker_end = m.end()

    statement = region[:proof_start].strip()
    proof = region[proof_marker_end:].strip() if proof_start < len(region) else ''

    # Clean up statement — remove trailing artifacts
    statement = re.sub(r'\n\s*\n\s*\n+', '\n\n', statement)

    return statement, proof

def parse_concepts(text, section_num):
    """Parse ALL labeled concepts from section text."""
    ch, sec = CHAPTER_MAP.get(section_num, ("?", str(section_num)))
    markers = find_concept_markers(text)
    concepts = []

    for i, (pos, ctype, label, raw) in enumerate(markers):
        # Statement starts after the marker
        # Find the end of the marker line
        marker_end = pos + len(raw)

        # Find next concept boundary
        if i + 1 < len(markers):
            next_pos = markers[i + 1][0]
        else:
            # Find exercise block or end of text
            ex_match = re.search(r'\nEXERCISES?\s*\n', text[marker_end:])
            ch_match = re.search(r'\nCHAPTER\s+[IVX]+', text[marker_end:])
            next_pos = marker_end + min(
                ex_match.start() if ex_match else len(text) - marker_end,
                ch_match.start() if ch_match else len(text) - marker_end
            )

        statement, proof = extract_statement_and_proof(text, marker_end, next_pos, next_pos)

        if not statement.strip():
            continue

        concepts.append({
            'type': ctype,
            'label': label,
            'statement': clean_latex(statement.strip()),
            'proof': clean_latex(proof.strip()),
            'chapter': ch,
            'section': sec,
        })

    # Parse exercises
    exercises = []
    ex_match = re.search(r'\n(EXERCISES?)\s*\n', text)
    if ex_match:
        ex_text = text[ex_match.end():]
        # Split by exercise numbers like "1.1." or "2.1."
        ex_parts = re.split(r'\n(?=\d+\.\d+\.?\s)', ex_text)
        for part in ex_parts:
            part = part.strip()
            if part and re.match(r'^\d+\.\d+', part):
                m = re.match(r'^(\d+\.\d+)', part)
                ex_num = m.group(1)
                exercises.append({
                    'number': ex_num,
                    'text': clean_latex(part),
                    'chapter': ch,
                    'section': sec
                })

    return concepts, exercises

def generate_slug(concept):
    """Generate semantic lowercase-hyphen English slug."""
    ctype = concept['type']
    label = concept['label']
    statement = concept['statement']

    # Build meaningful slug from concept type and label
    if label:
        label_slug = label.replace('.', '-').lower()
        return f"{ctype}-{label_slug}"

    # Fallback: use first few words
    clean = re.sub(r'\$\$.*?\$\$', ' ', statement, flags=re.DOTALL)
    clean = re.sub(r'\$.*?\$', ' ', clean)
    clean = re.sub(r'\\[a-zA-Z]+(\{[^}]*\})*', ' ', clean)
    clean = re.sub(r'[^a-zA-Z\s]', ' ', clean.lower())
    words = [w for w in clean.split() if len(w) > 2][:6]
    return '-'.join(words) if words else f"{ctype}-unnamed"

def extract_title(concept):
    """Extract a clean English title from statement."""
    statement = concept['statement']
    ctype = concept['type'].title()
    label = concept['label']

    # Get first meaningful line
    first_line = statement.split('\n')[0].strip()
    # Clean math
    clean = re.sub(r'\$\$.*?\$\$', '', first_line, flags=re.DOTALL)
    clean = re.sub(r'\$.*?\$', '', clean)
    clean = re.sub(r'\\[a-zA-Z]+(\{[^}]*\})*', '', clean)
    clean = re.sub(r'\s+', ' ', clean).strip('.,;: ')
    clean = clean[:200]

    if label:
        return f"{ctype} {label}: {clean}" if clean else f"{ctype} {label}"
    return clean if clean else ctype

def write_concept(concept, output_dir, exercises):
    """Write 5-file format for a concept."""
    slug = concept['slug']
    cdir = output_dir / slug
    cdir.mkdir(parents=True, exist_ok=True)

    ctype = concept['type']
    label = concept['label']
    statement = concept['statement']
    proof = concept['proof']
    ch = concept['chapter']
    sec = concept['section']
    title = concept['title']

    # FILE 1: concept.yaml
    yaml = f"""id: {slug}
title_en: "{title}"
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
    (cdir / "concept.yaml").write_text(yaml, encoding='utf-8')

    # FILE 2: theorem.tex — the LaTeX statement
    (cdir / "theorem.tex").write_text(statement, encoding='utf-8')

    # FILE 3: introduce.en.md
    label_str = f" {label}" if label else ""
    if ctype == 'definition':
        intro_body = f"This is a Definition{label_str} from Chapter {ch}, Section §{sec} of Hartshorne's Algebraic Geometry. It introduces a fundamental concept in algebraic geometry, central to the development of the theory of varieties and schemes over an algebraically closed field."
    elif ctype == 'theorem':
        intro_body = f"This is Theorem{label_str} from Chapter {ch}, Section §{sec} of Hartshorne's Algebraic Geometry. It establishes an important result connecting algebraic properties of rings and ideals with geometric properties of varieties and schemes."
    elif ctype == 'proposition':
        intro_body = f"This is Proposition{label_str} from Chapter {ch}, Section §{sec} of Hartshorne's Algebraic Geometry. It is a fundamental structural result used throughout the development of modern algebraic geometry."
    elif ctype == 'lemma':
        intro_body = f"This is Lemma{label_str} from Chapter {ch}, Section §{sec} of Hartshorne's Algebraic Geometry. It provides a key technical step used in proving deeper theorems about sheaves, cohomology, and schemes."
    elif ctype == 'corollary':
        intro_body = f"This is Corollary{label_str} from Chapter {ch}, Section §{sec} of Hartshorne's Algebraic Geometry. It follows directly from the preceding result and provides an important consequence for the study of algebraic varieties."
    else:
        intro_body = f"This is a {ctype}{label_str} from Chapter {ch}, Section §{sec} of Hartshorne's Algebraic Geometry."

    intro_md = f"""---
role: introduce
locale: en
content_hash: "{content_hash(intro_body)}"
written_against: ""
---
{intro_body}
"""
    (cdir / "introduce.en.md").write_text(intro_md, encoding='utf-8')

    # FILE 4: proof file (for theorem/proposition/lemma/corollary only)
    if ctype in ('theorem', 'proposition', 'lemma', 'corollary') and proof.strip():
        safe_label = label.replace('.', '-').replace(' ', '_') if label else 'main'
        proof_filename = f"proof_{BOOK_ID}_{ch}_{sec}.en.md"
        proof_md = f"""---
role: proof
locale: en
of_concept: {slug}
source_book: {BOOK_ID}
source_chapter: "{ch}"
source_section: "§{sec}"
---
{proof}
"""
        (cdir / proof_filename).write_text(proof_md, encoding='utf-8')

    # FILE 5: exercise files (shared across concepts of same section)
    if exercises:
        ex_dir = cdir / "exercises"
        ex_dir.mkdir(exist_ok=True)
        for ex in exercises:
            ex_num = ex['number'].replace('.', '_')
            ex_filename = f"exercise_{BOOK_ID}_{ch}_{sec}_{ex_num}.en.md"
            ex_md = f"""---
role: exercise
locale: en
chapter: "{ch}"
section: "§{sec}"
exercise_number: {ex['number']}
---
{ex['text']}
"""
            (ex_dir / ex_filename).write_text(ex_md, encoding='utf-8')

def process_section(sec_index):
    """Process one section by its index number."""
    section_file = SECTIONS_DIR / f"s{sec_index:03d}_Section_{sec_index}.md"
    if not section_file.exists():
        # Try glob
        candidates = list(SECTIONS_DIR.glob(f"s{sec_index:03d}_*.md"))
        if candidates:
            section_file = candidates[0]
        else:
            return 0, 0

    text = section_file.read_text(encoding='utf-8')
    concepts, exercises = parse_concepts(text, sec_index)
    written = 0

    for c in concepts:
        c['slug'] = generate_slug(c)
        c['title'] = extract_title(c)
        try:
            write_concept(c, OUTPUT_DIR, exercises)
            written += 1
        except Exception as e:
            print(f"    ERROR: {c['slug']}: {e}")

    return len(concepts), written

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Find all section files
    section_indices = sorted(set(
        int(f.stem.split('_')[0][1:])
        for f in SECTIONS_DIR.glob("s[0-9]*.md")
        if f.stem.split('_')[0][1:].isdigit()
    ))

    print(f"Found {len(section_indices)} sections")
    total = 0
    total_written = 0

    for idx in section_indices:
        ch, sec = CHAPTER_MAP.get(idx, ("?", "?"))
        n, w = process_section(idx)
        print(f"  s{idx:03d} (Ch.{ch} §{sec}): {n} concepts, {w} written")
        total += n
        total_written += w

    print(f"\n{'='*60}")
    print(f"Total: {total} concepts found, {total_written} written")
    DONE_FILE.write_text(f"DONE {datetime.now().isoformat()}\n{total_written} concepts\n")

if __name__ == '__main__':
    main()
