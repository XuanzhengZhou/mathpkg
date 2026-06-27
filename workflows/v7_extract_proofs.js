export const meta = {
  name: 'v7-extract-proofs',
  description: 'Per-section incremental proof+exercise extraction for existing concepts',
  phases: [{ title: 'Prep' }, { title: 'Extract' }]
}

// args: { book_slug, sections_dir, staging_dir }
var BOOK_SLUG = args.book_slug
var SECTIONS_DIR = args.sections_dir
var STAGING = args.staging_dir

phase('Prep')

// Step 1: Python writes the section→concept mapping to a temp JSON file
var prepResult = ''
try {
  prepResult = await agent(
    'python3 << ' + "'PYEOF'\n" +
    'import os, json, glob, re\n' +
    '\n' +
    'sections_dir = """' + SECTIONS_DIR + '"""\n' +
    'staging = """' + STAGING + '"""\n' +
    'book = """' + BOOK_SLUG + '"""\n' +
    '\n' +
    '# List section .md files\n' +
    'sec_files = sorted(f for f in os.listdir(sections_dir) if f.startswith("s") and f.endswith(".md"))\n' +
    '\n' +
    '# List concept groups and their slugs\n' +
    'groups = {}\n' +
    'for d in os.listdir(staging):\n' +
    '    dpath = os.path.join(staging, d)\n' +
    '    if os.path.isdir(dpath):\n' +
    '        slugs = [c for c in os.listdir(dpath) if os.path.isdir(os.path.join(dpath, c))]\n' +
    '        if slugs:\n' +
    '            groups[d] = slugs\n' +
    '\n' +
    '# Build section→group mapping (improved: regex number extraction)\n' +
    'mapping = []\n' +
    'for sf in sec_files:\n' +
    '    sName = sf.replace(".md", "")\n' +
    '    matched_group = None\n' +
    '    # Try direct match first\n' +
    '    if sName in groups:\n' +
    '        matched_group = sName\n' +
    '    else:\n' +
    '        # Extract section number via regex (s001, s002, ...)\n' +
    '        m = re.match(r"s(\\d+)", sName)\n' +
    '        if m:\n' +
    '            sec_num = m.group(1)\n' +
    '            # Match: group starts with "sNNN_" or "sNNN"\n' +
    '            sec_key = "s" + sec_num\n' +
    '            for g in groups:\n' +
    '                if g == sec_key or g.startswith(sec_key + "_") or g.startswith(sec_key):\n' +
    '                    matched_group = g\n' +
    '                    break\n' +
    '        # Fallback: try common prefix match\n' +
    '        if not matched_group:\n' +
    '            prefix = sName[:6]\n' +
    '            for g in groups:\n' +
    '                if g.startswith(prefix):\n' +
    '                    matched_group = g\n' +
    '                    break\n' +
    '    if matched_group:\n' +
    '        mapping.append({"section_file": sf, "group": matched_group, "slugs": groups[matched_group]})\n' +
    '    else:\n' +
    '        mapping.append({"section_file": sf, "group": None, "slugs": []})\n' +
    '\n' +
    '# Write mapping\n' +
    'out = {"sections_dir": sections_dir, "staging": staging, "book": book, "mapping": mapping}\n' +
    'with open("/tmp/proofs_map_" + book + ".json", "w") as f:\n' +
    '    json.dump(out, f)\n' +
    '\n' +
    'matched = sum(1 for m in mapping if m["group"])\n' +
    'total_slugs = sum(len(m["slugs"]) for m in mapping)\n' +
    'print("OK: " + str(len(sec_files)) + " sections, " + str(matched) + " matched, " + str(total_slugs) + " concepts")\n' +
    'PYEOF',
    { label: 'prep-mapping', phase: 'Prep' }
  )
} catch(e) {}
log(BOOK_SLUG + ' prep: ' + (prepResult || '?'))

// Step 2: Parse section count from prep summary
var sectionCount = 0
try {
  var match = (prepResult || '').match(/OK:\s*(\d+)\s+sections/)
  if (match) sectionCount = parseInt(match[1]) || 0
} catch(e) {}
log(BOOK_SLUG + ': ' + sectionCount + ' sections to process')

if (sectionCount === 0) {
  // Fallback: regex scan prep output for any number
  try {
    var numMatch = (prepResult || '').match(/\d+/)
    sectionCount = numMatch ? parseInt(numMatch[0]) || 0 : 0
    log(BOOK_SLUG + ' fallback: ' + sectionCount + ' sections')
  } catch(e2) {}
}

if (sectionCount === 0) {
  log('No sections to process')
  return { book: BOOK_SLUG, sections: 0, proofs: 0 }
}

phase('Extract')

// Step 3: Process each section in parallel
var thunks = []
for (var i = 0; i < sectionCount; i++) {
  thunks.push((function(idx) {
    return async function() {
      var prompt = [
        '=== PROOF EXTRACTOR ===',
        '',
        'Execute this Python script to extract proofs+exercises for section index ' + idx + ' of book ' + BOOK_SLUG + ':',
        '',
        '```python',
        'import os, json, yaml, glob',
        '',
        'data = json.load(open("/tmp/proofs_map_' + BOOK_SLUG + '.json"))',
        'm = data["mapping"][' + idx + ']',
        'sections_dir = data["sections_dir"]',
        'staging = data["staging"]',
        'book = data["book"]',
        '',
        'sf = m["section_file"]',
        'group = m["group"]',
        'slugs = m["slugs"]',
        '',
        'print(f"Section: {sf}")',
        'print(f"Group: {group}")',
        'print(f"Concepts: {len(slugs)} slugs")',
        '',
        'if not group or not slugs:',
        '    print("No matched concepts — skipping")',
        '    exit(0)',
        '',
        'dest_dir = os.path.join(staging, group)',
        'done_marker = os.path.join(dest_dir, ".proofs.done")',
        'if os.path.exists(done_marker):',
        '    existing = len(glob.glob(dest_dir + "/**/proof_*.md", recursive=True))',
        '    print(f"Already done: {existing} existing proofs")',
        '    exit(0)',
        '',
        '# Read section file (prefix match)',
        'import re',
        'sec_match = re.match(r"s(\\d+)", sf)',
        'if sec_match:',
        '    sec_num = sec_match.group(1)',
        '    sec_files = [f for f in os.listdir(sections_dir) if f.startswith("s" + sec_num) and f.endswith(".md")]',
        'else:',
        '    sec_files = [f for f in os.listdir(sections_dir) if f.startswith(sf[:5]) and f.endswith(".md")]',
        'if not sec_files:',
        '    print("Section file not found")',
        '    exit(1)',
        'section_path = os.path.join(sections_dir, sec_files[0])',
        'with open(section_path) as f:',
        '    section_text = f.read()[:40000]',
        '',
        'print(f"Read {len(section_text)} chars from section")',
        '',
        'for slug in slugs:',
        '    concept_dir = os.path.join(dest_dir, slug)',
        '    yaml_path = os.path.join(concept_dir, "concept.yaml")',
        '    if not os.path.exists(yaml_path):',
        '        continue',
        '    with open(yaml_path) as f:',
        '        cy = yaml.safe_load(f)',
        '    ctype = cy.get("type", "")',
        '    title = cy.get("title_en", slug)',
        '    chapter = cy.get("source_books", [{}])[0].get("chapter", "X")',
        '    section = cy.get("source_books", [{}])[0].get("section", "X")',
        '    print(f"  {slug}: type={ctype}, ch={chapter}, sec={section}")',
        '    existing_proofs = glob.glob(concept_dir + "/proof_*.md")',
        '    if existing_proofs:',
        '        print(f"    proof already exists, skipping")',
        '        continue',
        '    if ctype in ("theorem", "proposition", "lemma", "corollary"):',
        '        print(f"    needs proof extraction")',
        '    else:',
        '        print(f"    type={ctype}, no proof needed")',
        '',
        'print(f"Concepts to process: {len(slugs)}")',
        'print("READY_FOR_EXTRACTION")',
        '```',
        '',
        '═══ YOUR TASK ═══',
        'Run the Python script above. Then for EACH concept listed as "needs proof extraction":',
        '1. Find the concept\'s proof in the section text',
        '2. Read the concept.yaml to get chapter/section numbers',
        '3. Write proof_' + BOOK_SLUG + '_{chapter}_{section}.en.md into the concept directory',
        '4. Find related exercises and write exercise_' + BOOK_SLUG + '_{chapter}_{section}.{N}.en.md',
        '',
        '═══ PROOF FILE FORMAT ═══',
        '---',
        'role: proof',
        'locale: en',
        'of_concept: <slug>',
        'source_book: ' + BOOK_SLUG,
        'source_chapter: "<chapter>"',
        'source_section: "<section>"',
        '---',
        '# Proof of <concept title>',
        'Full proof with LaTeX math.',
        '',
        '═══ EXERCISE FILE FORMAT ═══',
        '---',
        'role: exercise',
        'locale: en',
        'chapter: "<X>"',
        'section: "<X>"',
        'exercise_number: N',
        '---',
        '# Exercise N',
        'Exercise statement with LaTeX math.',
        '',
        '═══ CRITICAL ═══',
        '1. For EACH theorem/proposition/lemma/corollary: extract proof from section text',
        '2. Fix OCR artifacts using mathematical reasoning',
        '3. After ALL concepts done, write .proofs.done marker in the group directory',
        '4. Use Bash tool to mkdir -p and write files'
      ].join('\n')

      try {
        await agent(prompt, { label: 'sec-' + idx, phase: 'Extract' })
      } catch(e) {
        log('Error sec ' + idx + ': ' + (e.message || '').toString().substring(0, 80))
      }

      var count = 0
      try {
        var c = await agent(
          'python3 -c "import json, os, glob; d=json.load(open(\'/tmp/proofs_map_' + BOOK_SLUG + '.json\')); m=d[\'mapping\'][' + idx + ']; g=m[\'group\']; dest=os.path.join(d[\'staging\'],g) if g else \'\'; proofs=len(glob.glob(dest+\'/**/proof_*.md\',recursive=True)) if dest else 0; print(str(proofs))"',
          { label: 'count-' + idx, phase: 'Extract' }
        )
        if (c) count = parseInt((c.trim().match(/\d+/) || ['0'])[0]) || 0
      } catch(e) {}
      return { idx: idx, proofs: count }
    }
  })(i))
}

var results = await parallel(thunks)
var valid = results.filter(function(r) { return r !== null && r !== undefined })
var totalProofs = valid.reduce(function(s, r) { return s + (r.proofs || 0) }, 0)

log(BOOK_SLUG + ': DONE — ' + totalProofs + ' proofs from ' + valid.length + ' sections')
return { book: BOOK_SLUG, sections: sectionCount, proofs: totalProofs }
