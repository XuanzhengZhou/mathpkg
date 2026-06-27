export const meta = {
  name: 'v8-book-extract',
  description: 'One book: per-section concept extraction with proofs+exercises (5 files per concept)',
  phases: [{ title: 'List' }, { title: 'Extract' }]
}

// args: { book_dir, staging, book_slug }
var BOOK_DIR = args.book_dir
var STAGING = args.staging
var BOOK_SLUG = args.book_slug

phase('List')

// Write section file list to /tmp/v8_sections_{book}.json (avoids embedded-newline issues)
var sectionFiles = []
var sectionCount = 0
try {
  // Write section list + metadata to temp file
  await agent(
    'python3 -c "import os, json; files=sorted(f for f in os.listdir(\'' + BOOK_DIR + '\') if f.startswith(\'s\') and f.endswith(\'.md\')); json.dump({\'files\':files,\'dir\':\'' + BOOK_DIR + '\',\'staging\':\'' + STAGING + '\'}, open(\'/tmp/v8_sections_' + BOOK_SLUG + '.json\',\'w\')); print(\'OK:\'+str(len(files)))"',
    { label: 'list-write', phase: 'List' }
  )
  // Get count by parsing agent output for "OK:N"
  var prepOut = ''
  try {
    var r3 = await agent(
      'python3 -c "import json; d=json.load(open(\'/tmp/v8_sections_' + BOOK_SLUG + '.json\')); print(len(d[\'files\']))"',
      { label: 'count', phase: 'List' }
    )
    prepOut = r3 || ''
  } catch(e2) {}
  var m = prepOut.match(/\d+/)
  sectionCount = m ? parseInt(m[0]) || 0 : 0
  // Also try direct Python approach
  if (sectionCount === 0) {
    var r4 = await agent(
      'python3 -c "import json; print(len(json.load(open(\'/tmp/v8_sections_' + BOOK_SLUG + '.json\'))[\'files\']))"',
      { label: 'count2', phase: 'List' }
    )
    var m2 = (r4 || '0').match(/\d+/)
    sectionCount = m2 ? parseInt(m2[0]) || 0 : 0
  }
  log(BOOK_SLUG + ': ' + sectionCount + ' sections')
  // Build sectionFiles from count (used for loop iteration only)
  for (var k = 0; k < sectionCount; k++) sectionFiles.push('idx-' + k)
} catch(e) { log('List error: ' + (e.message || '')) }
log(BOOK_SLUG + ': ' + sectionFiles.length + ' sections found')

if (sectionFiles.length === 0) {
  log('ERROR: no sections in ' + BOOK_DIR)
  return { book: BOOK_SLUG, concepts: 0, sections: 0 }
}

phase('Extract')

var thunks = sectionFiles.map(function(sf, i) {
  return async function() {
    var sName = sf.replace('.md','')
    var sectionPath = BOOK_DIR + '/' + sf
    var destDir = STAGING + '/' + sName

    // Skip if already done
    var alreadyDone = false
    try {
      var check = await agent(
        'python3 -c "import os; print(1 if os.path.exists(\'' + destDir + '/.done\') else 0)"',
        { label: 'skip-'+sName.substring(0,20), phase: 'Extract' }
      )
      alreadyDone = check && check.trim() === '1'
    } catch(e) {}

    if (alreadyDone) {
      var existingCnt = 0
      try {
        var ec = await agent(
          'python3 -c "import os; d=\'' + destDir + '\'; print(len([x for x in os.listdir(d) if os.path.isdir(os.path.join(d,x))]))"',
          { label: 'exist-'+sName.substring(0,20), phase: 'Extract' }
        )
        existingCnt = ec ? parseInt(ec.trim()) || 0 : 0
      } catch(e) {}
      return { section: sName.substring(0,40), concepts: existingCnt, cached: true }
    }

    var prompt = [
      '=== V8 CONCEPT EXTRACTOR (Per-Section, with Proofs+Exercises) ===',
      '',
      'READ this section file: ' + sectionPath,
      '',
      'Extract EVERY theorem, definition, lemma, proposition, corollary, axiom.',
      'For EACH concept, write files in: ' + destDir + '/{SLUG}/',
      '',
      '═══ FILE 1: concept.yaml ═══',
      'id: <semantic-english-slug>',
      'title_en: "<Full canonical name>"',
      'title_zh: ""',
      'type: theorem|definition|lemma|proposition|corollary|axiom',
      'domain: algebra|analysis|topology|geometry|number-theory|logic|combinatorics|probability|applied-math|foundations',
      'subdomain: <lowercase-hyphen>',
      'difficulty: basic|intermediate|advanced',
      'tags: []',
      'depends_on: {required:[], recommended:[], suggested:[]}',
      'source_books: [{book_id:"' + BOOK_SLUG + '",author:"",title:"",chapter:"",section:"",pages:"",role_in_book:""}]',
      'content_hash: ""',
      'extraction_date: "2026-06-27"',
      'extraction_agent: "v8-full-extract"',
      '',
      '═══ FILE 2: theorem.tex ═══',
      'PURE LaTeX STATEMENT only. NO proof. NO natural language outside \\text{}.',
      'Use $$ for display math, $ for inline.',
      '',
      '═══ FILE 3: introduce.en.md ═══',
      'YAML frontmatter: role: introduce, locale: en, content_hash: "", written_against: ""',
      'Then 2-4 English sentences explaining the concept.',
      '',
      '═══ FILE 4: proof_' + BOOK_SLUG + '_Ch.Sec.en.md (for theorem/proposition/lemma/corollary ONLY) ═══',
      'YAML frontmatter:',
      '  role: proof',
      '  locale: en',
      '  of_concept: <slug>',
      '  source_book: ' + BOOK_SLUG,
      '  source_chapter: "<from concept.yaml>"',
      '  source_section: "<from concept.yaml>"',
      'Then: Full proof text with LaTeX math. Fix OCR artifacts using mathematical reasoning.',
      'Skip if the concept is a definition or axiom (no proof).',
      '',
      '═══ FILE 5: exercise_' + BOOK_SLUG + '_Ch.Sec.N.en.md (if section has exercises) ═══',
      'YAML frontmatter:',
      '  role: exercise',
      '  locale: en',
      '  chapter: "<X>"',
      '  section: "<X>"',
      '  exercise_number: N',
      'Then: Exercise statement with LaTeX math.',
      '',
      '═══ CRITICAL RULES ═══',
      '1. Slug = semantic lowercase-hyphen English (GOOD: kummers-theorem, BAD: gtm012-thm-3-2)',
      '2. theorem.tex = STATEMENT ONLY. NO proof, NO "Proof.", NO natural language',
      '3. proof_*.md = FULL PROOF extracted from section text, preserve LaTeX math',
      '4. For definitions and axioms: skip proof file (no proof needed)',
      '5. For exercises at end of section: write one exercise_*.md per exercise',
      '6. source_books = array of OBJECTS, NOT strings',
      '7. Extract ALL concepts, including lemmas and corollaries',
      '8. Fix OCR artifacts using mathematical reasoning',
      '9. Write .done when complete: echo DONE > ' + destDir + '/.done'
    ].join('\n')

    try { await agent(prompt, { label: sName.substring(0,35), phase: 'Extract' }) } catch(e) {}

    var cnt = 0
    try {
      var cr = await agent(
        'python3 -c "import os; d=\'' + destDir + '\'; print(len([x for x in os.listdir(d) if os.path.isdir(os.path.join(d,x))]) if os.path.exists(d) else 0)"',
        { label: 'cnt-'+sName.substring(0,20), phase: 'Extract' }
      )
      cnt = cr ? parseInt(cr.trim()) || 0 : 0
    } catch(e) {}

    return { section: sName.substring(0,40), concepts: cnt }
  }
})

var results = await parallel(thunks)
var valid = results.filter(function(r) { return r !== null && r !== undefined })
var totalConcepts = valid.reduce(function(s, r) { return s + (r.concepts || 0) }, 0)
var cached = valid.filter(function(r) { return r.cached }).length

log(BOOK_SLUG + ': ' + totalConcepts + ' concepts from ' + valid.length + '/' + sectionFiles.length + ' sections')
return { book: BOOK_SLUG, sections: sectionFiles.length, done: valid.length, concepts: totalConcepts, cached: cached }
