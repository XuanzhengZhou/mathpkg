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
// This avoids JSON parse issues with agent output formatting
var prepResult = ''
try {
  prepResult = await agent(
    'python3 << ' + "'PYEOF'\n" +
    'import os, json, glob\n' +
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
    '# Build section→group mapping\n' +
    'mapping = []\n' +
    'for sf in sec_files:\n' +
    '    sName = sf.replace(".md", "")\n' +
    '    matched_group = None\n' +
    '    # Try direct match first\n' +
    '    if sName in groups:\n' +
    '        matched_group = sName\n' +
    '    else:\n' +
    '        # Try prefix match on first 5 chars (s001_, s002_, etc.)\n' +
    '        prefix = sName[:5]\n' +
    '        for g in groups:\n' +
    '            if g.startswith(prefix):\n' +
    '                matched_group = g\n' +
    '                break\n' +
    '    if matched_group:\n' +
    '        mapping.append({"section_file": sf, "group": matched_group, "slugs": groups[matched_group]})\n' +
    '    else:\n' +
    '        mapping.append({"section_file": sf, "group": None, "slugs": []})\n' +
    '\n' +
    '# Write mapping to temp file\n' +
    'out = {"sections_dir": sections_dir, "staging": staging, "book": book, "mapping": mapping}\n' +
    'with open("/tmp/proofs_map_" + book + ".json", "w") as f:\n' +
    '    json.dump(out, f)\n' +
    '\n' +
    '# Print summary (agent-safe, no JSON)\n' +
    'matched = sum(1 for m in mapping if m["group"])\n' +
    'total_slugs = sum(len(m["slugs"]) for m in mapping)\n' +
    'print("OK: " + str(len(sec_files)) + " sections, " + str(matched) + " matched, " + str(total_slugs) + " concepts")\n' +
    'PYEOF',
    { label: 'prep-mapping', phase: 'Prep' }
  )
} catch(e) {}
log(BOOK_SLUG + ' prep: ' + (prepResult || '?'))

// Step 2: Verify prep file exists, get section count
var sectionCount = 0
try {
  var verify = await agent(
    'python3 -c "import json; d=json.load(open(\'/tmp/proofs_map_' + BOOK_SLUG + '.json\')); print(len(d[\'mapping\']))"',
    { label: 'verify-prep', phase: 'Prep' }
  )
  sectionCount = parseInt((verify || '0').trim()) || 0
} catch(e) {}
log(BOOK_SLUG + ': ' + sectionCount + ' sections to process')

if (sectionCount === 0) {
  log('No sections to process')
  return { book: BOOK_SLUG, sections: 0, proofs: 0 }
}

phase('Extract')

// Step 3: Process each section index (0, 1, 2, ... sectionCount-1)
// Instead of passing data through JS, each agent call reads from the JSON file
var thunks = []
for (var i = 0; i < sectionCount; i++) {
  thunks.push((function(idx) {
    return async function() {
      // This agent reads the JSON file, processes one section, and writes proof files
      var prompt = [
        '=== PROOF EXTRACTOR ===',
        '',
        'Execute this Python script to extract proofs+exercises for section index ' + idx + ' of book ' + BOOK_SLUG + ':',
        '',
        '```python',
        'import os, json, yaml, glob',
        '',
        '# Load mapping',
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
        'print(f"Concepts: {slugs}")',
        '',
        'if not group or not slugs:',
        '    print("No matched concepts — skipping")',
        '    exit(0)',
        '',
        '# Check if already done',
        'dest_dir = os.path.join(staging, group)',
        'done_marker = os.path.join(dest_dir, ".proofs.done")',
        'if os.path.exists(done_marker):',
        '    existing = len(glob.glob(dest_dir + "/**/proof_*.md", recursive=True))',
        '    print(f"Already done: {existing} existing proofs")',
        '    exit(0)',
        '',
        '# Read section file (prefix match)',
        'prefix = sf[:5]  # s001_',
        'sec_files = [f for f in os.listdir(sections_dir) if f.startswith(prefix) and f.endswith(".md")]',
        'if not sec_files:',
        '    print("Section file not found")',
        '    exit(1)',
        'section_path = os.path.join(sections_dir, sec_files[0])',
        'with open(section_path) as f:',
        '    section_text = f.read()[:40000]',
        '',
        'print(f"Read {len(section_text)} chars from section")',
        '',
        '# Process each concept',
        'proof_count = 0',
        'ex_count = 0',
        '',
        'for slug in slugs:',
        '    concept_dir = os.path.join(dest_dir, slug)',
        '    yaml_path = os.path.join(concept_dir, "concept.yaml")',
        '    if not os.path.exists(yaml_path):',
        '        continue',
        '    ',
        '    with open(yaml_path) as f:',
        '        cy = yaml.safe_load(f)',
        '    ctype = cy.get("type", "")',
        '    title = cy.get("title_en", slug)',
        '    chapter = cy.get("source_books", [{}])[0].get("chapter", "X")',
        '    section = cy.get("source_books", [{}])[0].get("section", "X")',
        '',
        '    print(f"  {slug}: type={ctype}, ch={chapter}, sec={section}")',
        '',
        '    # Check if proof already exists',
        '    existing_proofs = glob.glob(concept_dir + "/proof_*.md")',
        '    if existing_proofs:',
        '        print(f"    proof already exists, skipping")',
        '        continue',
        '',
        '    # For theorem/proposition/lemma/corollary: look for proof in section text',
        '    if ctype in ("theorem", "proposition", "lemma", "corollary"):',
        '        # Search for the concept title or slug in the section text',
        '        # The agent should find the proof and write it',
        '        print(f"    needs proof extraction")',
        '        # The actual extraction is done by the Agent reading this Python output',
        '        # and then writing the file. The Python script maps the location.',
        '    else:',
        '        print(f"    type={ctype}, no proof needed")',
        '',
        'print(f"Concepts to process: {len(slugs)}")',
        'print("READY_FOR_EXTRACTION")',
        '```',
        '',
        '═══ YOUR TASK ═══',
        'Run the Python script above. It will output concept info.',
        'Then for EACH concept listed as "needs proof extraction":',
        '1. Read the section text',
        '2. Find the concept\'s proof in the text',
        '3. Read the concept.yaml to get chapter/section numbers',
        '4. Write proof_' + BOOK_SLUG + '_{chapter}_{section}.en.md into the concept directory',
        '5. Find related exercises and write exercise_' + BOOK_SLUG + '_{chapter}_{section}.{N}.en.md',
        '',
        '═══ PROOF FILE FORMAT ═══',
        'Filename: proof_' + BOOK_SLUG + '_Ch.Sec.en.md  (e.g. proof_gtm004_II.2.en.md)',
        'Content:',
        '---',
        'role: proof',
        'locale: en',
        'of_concept: <slug>',
        'source_book: ' + BOOK_SLUG,
        'source_chapter: "<chapter>"',
        'source_section: "<section>"',
        '---',
        '',
        '# Proof of <concept title>',
        '',
        'Full proof with LaTeX math.',
        '',
        '═══ EXERCISE FILE FORMAT ═══',
        'Filename: exercise_' + BOOK_SLUG + '_Ch.Sec.N.en.md',
        'Content:',
        '---',
        'role: exercise',
        'locale: en',
        'chapter: "<X>"',
        'section: "<X>"',
        'exercise_number: N',
        '---',
        '',
        '# Exercise N',
        '',
        'Exercise statement with LaTeX math.',
        '',
        '═══ CRITICAL ═══',
        '1. For EACH theorem/proposition/lemma/corollary: extract proof from section text',
        '2. For definitions: skip proof but check for exercises',
        '3. Fix OCR artifacts using mathematical reasoning',
        '4. After ALL concepts in this section are done, create the .proofs.done marker in the section group directory',
        '5. Use Bash tool to mkdir -p and write files'
      ].join('\n')

      try {
        await agent(prompt, { label: 'sec-' + idx, phase: 'Extract' })
      } catch(e) {
        log('Error section ' + idx + ': ' + (e.message || '').toString().substring(0, 80))
      }

      // Count results via Python
      var count = 0
      try {
        var c = await agent(
          'python3 -c "import json, os, glob; d=json.load(open(\'/tmp/proofs_map_' + BOOK_SLUG + '.json\')); m=d[\'mapping\'][' + idx + ']; g=m[\'group\']; dest=os.path.join(d[\'staging\'],g) if g else \'\'; proofs=len(glob.glob(dest+\'/**/proof_*.md\',recursive=True)) if dest else 0; exs=len(glob.glob(dest+\'/**/exercise_*.md\',recursive=True)) if dest else 0; print(str(proofs)+\' \'+str(exs))"',
          { label: 'count-' + idx, phase: 'Extract' }
        )
        if (c) { var parts = c.trim().split(' '); count = parseInt(parts[0]) || 0 }
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
