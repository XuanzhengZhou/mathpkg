#!/usr/bin/env python3
"""
GTM052 (Hartshorne) Concept Extractor v3 — Fixed regex patterns.
The OCR text has bold markers wrapping the ENTIRE label including period:
  **Definition.**  **Theorem 3.2.**  **Lemma 3.1.**
"""
import re, os, hashlib
from pathlib import Path
from datetime import datetime

BOOK_ID = "gtm052"
SECTIONS_DIR = Path("/home/a123/文档/mathpkg/pipeline_output/stitched_sections/(GTM052)Algebraic geometry (1977, Springer) - libgen.lc")
OUTPUT_DIR = Path("/home/a123/文档/mathpkg/pipeline_output/math_pkg_tmp/concepts_batch6/gtm052")
DONE_FILE = OUTPUT_DIR / ".done"
DATE = "2026-06-27"
AGENT = "v8-full-extract"

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
    replacements = {
        '𝐀': '\\mathbf{A}', '𝒞': '\\mathcal{C}', '𝒪': '\\mathcal{O}',
        'ℱ': '\\mathcal{F}', 'ℐ': '\\mathcal{I}', '𝒢': '\\mathcal{G}',
        'ℋ': '\\mathcal{H}', '𝒦': '\\mathcal{K}', '𝒰': '\\mathcal{U}',
        '𝒱': '\\mathcal{V}', '𝒲': '\\mathcal{W}', 'ℒ': '\\mathcal{L}',
        '𝒩': '\\mathcal{N}', '𝒫': '\\mathcal{P}',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

def find_concept_markers(text):
    """
    Find ALL concept markers. Returns sorted list of (position, type, label).
    Strategy: search for keyword patterns, then deduplicate by position.
    """
    markers = []

    # ── KEY PATTERNS ──
    # The text uses **Bold Label.** format where period is inside bold markers.
    # Also plain text "Theorem N.M." without bold.

    patterns = [
        # Bold definitions: **Definition.** or **Definition:**
        (r'\*\*Definition[\.:]?\*\*', 'definition', ''),
        # Bold Theorem N.M. or N.MA.: **Theorem 3.2.** or **Theorem 1.3A.**
        (r'\*\*Theorem\s+(\d+(?:\.\d+)?[A-Z]?)[\.:]?\*\*', 'theorem', 1),
        # Bold Proposition N.M. or N.MA.: **Proposition 1.1.**
        (r'\*\*Proposition\s+(\d+(?:\.\d+)?[A-Z]?)[\.:]?\*\*', 'proposition', 1),
        # Bold Lemma N.M.: **Lemma 3.1.**
        (r'\*\*Lemma\s+(\d+(?:\.\d+)?[A-Z]?)[\.:]?\*\*', 'lemma', 1),
        # Bold Corollary N.M.: **Corollary 3.7.**
        (r'\*\*Corollary\s+(\d+(?:\.\d+)?[A-Z]?)[\.:]?\*\*', 'corollary', 1),
        # Plain Definition. or Definition: (line start)
        (r'(?:^|\n)Definition[\.:]\s', 'definition', ''),
        # Plain Theorem N.M. or N.MA. (line start)
        (r'(?:^|\n)Theorem\s+(\d+(?:\.\d+)?[A-Z]?)[\.:]', 'theorem', 1),
        # Plain Proposition N.M. or N.MA. (line start)
        (r'(?:^|\n)Proposition\s+(\d+(?:\.\d+)?[A-Z]?)[\.:]', 'proposition', 1),
        # Plain Lemma N.M. (line start)
        (r'(?:^|\n)Lemma\s+(\d+(?:\.\d+)?[A-Z]?)[\.:]', 'lemma', 1),
        # Plain Corollary N.M. (line start)
        (r'(?:^|\n)Corollary\s+(\d+(?:\.\d+)?[A-Z]?)[\.:]', 'corollary', 1),
    ]

    for pat, ctype, label_group in patterns:
        for m in re.finditer(pat, text):
            pos = m.start()
            label = m.group(label_group) if label_group else ''
            markers.append((pos, ctype, label))

    # Sort by position
    markers.sort(key=lambda x: x[0])

    # Deduplicate (keep first occurrence at each position)
    seen = set()
    unique = []
    for pos, ctype, label in markers:
        if pos not in seen:
            seen.add(pos)
            unique.append((pos, ctype, label))

    return unique

def extract_statement_and_proof(text, start, end):
    """Extract statement (before Proof.) and proof from a text region."""
    region = text[start:end]
    # Normalize — strip leading whitespace/newlines
    region = region.strip()

    # Find Proof. marker
    proof_marker = None
    for pat in [r'\n\*\*Proof[\.:]?\*\*', r'\nProof[\.:]', r'\nPROOF[\.:]']:
        m = re.search(pat, region)
        if m:
            proof_marker = m
            break

    if proof_marker:
        statement = region[:proof_marker.start()].strip()
        proof = region[proof_marker.end():].strip()
    else:
        statement = region
        proof = ''

    return statement, proof

def parse_concepts(text, section_num):
    """Parse all labeled concepts from section text."""
    ch, sec = CHAPTER_MAP.get(section_num, ("?", str(section_num)))
    markers = find_concept_markers(text)

    # Find exercise block boundary
    ex_match = re.search(r'\n(EXERCISES?)\s*\n', text)
    ex_start = ex_match.start() if ex_match else len(text)

    concepts = []

    for i, (pos, ctype, label) in enumerate(markers):
        # Determine where this concept's text region ends
        # End at: next concept marker, or exercise block, or chapter break
        if i + 1 < len(markers):
            next_pos = markers[i + 1][0]
        else:
            next_pos = ex_start

        # Start of statement = end of the marker text
        # Find the actual end of the marker line in the original text
        marker_line_end = text.index('\n', pos) if '\n' in text[pos:] else len(text)
        # The actual marker might span across the matched pattern — find where the label ends
        # For bold patterns: **Theorem 3.2.** -> content ends after the last **.
        # For plain: "Theorem 3.4." -> content ends after the period.
        # We search for the end of the marker including any trailing space
        marker_region = text[pos:pos+200]
        # Find where the concept keyword + label + punctuation ends
        # Simple approach: find the first newline after the matched pattern
        m_end = re.search(r'\*\*', marker_region)
        if m_end and ctype != 'definition':
            # Bold with label — find second **
            m2 = re.search(r'\*\*', marker_region[m_end.end():])
            if m2:
                statement_start = pos + m_end.end() + m2.end()
            else:
                statement_start = pos + len(m.group(0)) if 'm' in dir() else pos + 50
        else:
            # Plain or bold definition — find end of marker
            statement_start = pos
            for j in range(pos, min(pos+100, len(text))):
                if text[j] == '\n':
                    statement_start = j + 1
                    break
                # Also handle the case where concept text starts right after the marker
                if j > pos + 10 and text[j] not in ' *.0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
                    pass

        # Actually, simpler approach: find position right after the FULL marker
        # For **Theorem N.M.**: the full marker is up to and including the closing ** and period
        # Let's find the actual end by looking for the pattern in the original text
        full_marker_end = pos
        remaining = text[pos:]
        # Find where the concept label ends and the actual math content begins
        # Marker ends at: the period/colon followed by space, or newline
        m = re.match(r'.*?[\.:]\s', remaining)
        if m:
            full_marker_end = pos + m.end()
        else:
            # Fallback: next newline
            nl = remaining.find('\n')
            full_marker_end = pos + (nl + 1 if nl >= 0 else len(remaining))

        statement, proof = extract_statement_and_proof(text, full_marker_end, next_pos)

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
    if ex_match:
        ex_text = text[ex_match.end():]
        # Split by exercise numbers
        ex_parts = re.split(r'\n(?=\d+\.\d+[\.\s])', ex_text)
        for part in ex_parts:
            part = part.strip()
            if part and re.match(r'^\d+\.\d+', part):
                m = re.match(r'^(\d+\.\d+)', part)
                ex_num = m.group(1)
                ex_body = part[len(ex_num):].strip().lstrip('.').strip()
                exercises.append({
                    'number': ex_num,
                    'text': clean_latex(f"{ex_num}. {ex_body}"),
                    'chapter': ch,
                    'section': sec
                })

    return concepts, exercises

def generate_slug(concept):
    ctype = concept['type']
    label = concept['label']
    if label:
        return f"{ctype}-{label.replace('.', '-').replace(' ', '-').lower()}"
    statement = concept['statement']
    clean = re.sub(r'\$\$.*?\$\$', ' ', statement, flags=re.DOTALL)
    clean = re.sub(r'\$.*?\$', ' ', clean)
    clean = re.sub(r'\\[a-zA-Z]+(\{[^}]*\})*', ' ', clean)
    clean = re.sub(r'[^a-zA-Z\s]', ' ', clean.lower())
    words = [w for w in clean.split() if len(w) > 2][:5]
    return f"{ctype}-{'-'.join(words)}" if words else f"{ctype}-unnamed"

def extract_title(concept):
    ctype = concept['type'].title()
    label = concept['label']
    statement = concept['statement']
    first_line = statement.split('\n')[0].strip()[:200]
    clean = re.sub(r'\$\$.*?\$\$', '', first_line, flags=re.DOTALL)
    clean = re.sub(r'\$.*?\$', '', clean)
    clean = re.sub(r'\\[a-zA-Z]+(\{[^}]*\})*', '', clean)
    clean = re.sub(r'\s+', ' ', clean).strip('.,;: ')
    if label:
        return f"{ctype} {label}: {clean}" if clean else f"{ctype} {label}"
    return clean if clean else ctype

def write_concept(concept, output_dir, exercises):
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

    # FILE 2: theorem.tex
    (cdir / "theorem.tex").write_text(statement, encoding='utf-8')

    # FILE 3: introduce.en.md
    label_str = f" {label}" if label else ""
    if ctype == 'definition':
        intro_body = f"Definition{label_str} from Chapter {ch}, Section §{sec} of Hartshorne's Algebraic Geometry. Introduces a fundamental concept in the theory of algebraic varieties and schemes over an algebraically closed field."
    elif ctype == 'theorem':
        intro_body = f"Theorem{label_str} from Chapter {ch}, Section §{sec} of Hartshorne's Algebraic Geometry. Establishes an important result connecting algebraic and geometric properties."
    elif ctype == 'proposition':
        intro_body = f"Proposition{label_str} from Chapter {ch}, Section §{sec} of Hartshorne's Algebraic Geometry. A fundamental structural result in modern algebraic geometry."
    elif ctype == 'lemma':
        intro_body = f"Lemma{label_str} from Chapter {ch}, Section §{sec} of Hartshorne's Algebraic Geometry. A key technical step for proving deeper theorems about sheaves, cohomology, and schemes."
    elif ctype == 'corollary':
        intro_body = f"Corollary{label_str} from Chapter {ch}, Section §{sec} of Hartshorne's Algebraic Geometry. Follows directly from a preceding result with important consequences for algebraic varieties."
    else:
        intro_body = f"{ctype.title()}{label_str} from Chapter {ch}, Section §{sec} of Hartshorne's Algebraic Geometry."

    intro_md = f"""---
role: introduce
locale: en
content_hash: "{content_hash(intro_body)}"
written_against: ""
---
{intro_body}
"""
    (cdir / "introduce.en.md").write_text(intro_md, encoding='utf-8')

    # FILE 4: proof
    if ctype in ('theorem', 'proposition', 'lemma', 'corollary') and proof.strip():
        safe_label = label.replace('.', '-') if label else 'main'
        pf = f"""---
role: proof
locale: en
of_concept: {slug}
source_book: {BOOK_ID}
source_chapter: "{ch}"
source_section: "§{sec}"
---
{proof}
"""
        (cdir / f"proof_{BOOK_ID}_{ch}_{sec}.en.md").write_text(pf, encoding='utf-8')

    # FILE 5: exercises
    if exercises:
        ex_dir = cdir / "exercises"
        ex_dir.mkdir(exist_ok=True)
        for ex in exercises:
            en = ex['number'].replace('.', '_')
            em = f"""---
role: exercise
locale: en
chapter: "{ch}"
section: "§{sec}"
exercise_number: {ex['number']}
---
{ex['text']}
"""
            (ex_dir / f"exercise_{BOOK_ID}_{ch}_{sec}_{en}.en.md").write_text(em, encoding='utf-8')

def process_section(idx):
    section_file = SECTIONS_DIR / f"s{idx:03d}_Section_{idx}.md"
    if not section_file.exists():
        candidates = list(SECTIONS_DIR.glob(f"s{idx:03d}_*.md"))
        if candidates:
            section_file = candidates[0]
        else:
            return 0, 0

    text = section_file.read_text(encoding='utf-8')
    concepts, exercises = parse_concepts(text, idx)
    written = 0
    for c in concepts:
        c['slug'] = generate_slug(c)
        c['title'] = extract_title(c)
        try:
            write_concept(c, OUTPUT_DIR, exercises)
            written += 1
        except Exception as e:
            print(f"    ERR {c['slug']}: {e}")
    return len(concepts), written

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    indices = sorted(set(
        int(f.stem.split('_')[0][1:])
        for f in SECTIONS_DIR.glob("s[0-9]*.md")
        if f.stem.split('_')[0][1:].isdigit()
    ))
    total = total_w = 0
    for idx in indices:
        ch, sec = CHAPTER_MAP.get(idx, ("?","?"))
        n, w = process_section(idx)
        print(f"s{idx:03d} Ch.{ch} §{sec}: {n} concepts, {w} written")
        total += n; total_w += w
    print(f"\n{'='*60}")
    print(f"TOTAL: {total} concepts, {total_w} written")
    DONE_FILE.write_text(f"DONE {datetime.now().isoformat()}\n{total_w} concepts\n")

if __name__ == '__main__':
    main()
