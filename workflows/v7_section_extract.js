export const meta = {
  name: 'v7-section-extract',
  description: 'One book: per-section concept extraction in V7 format',
  phases: [
    { title: 'Scan', detail: 'Read manifest, list sections' },
    { title: 'Extract', detail: 'One agent per section, parallel' },
  ]
}

// args: { book_dir: "stitched_sections/(GTM012)...", staging: "pipeline_output/concepts_v7/gtm-012" }
var BOOK_DIR = args.book_dir
var STAGING = args.staging
var BOOK_SLUG = args.book_slug

phase('Scan')

// Read manifest
var manifest = null
try {
  var r = await agent(
    'python3 -c "import json; m=json.load(open(\'' + BOOK_DIR + '/_manifest.json\')); print(len(m[\'files\']))"',
    { label: 'read-manifest', phase: 'Scan' }
  )
  if (r) {
    var count = parseInt(r.trim()) || 0
    log(BOOK_SLUG + ': ' + count + ' sections')
  }
} catch(e) {}

// List section files
var sectionFiles = []
try {
  var r2 = await agent(
    'bash -c "ls ' + BOOK_DIR + '/s*.md 2>/dev/null"',
    { label: 'list-sections', phase: 'Scan' }
  )
  if (r2) {
    sectionFiles = r2.trim().split('\n').filter(function(x) { return x.length > 0 })
  }
} catch(e) {}

if (sectionFiles.length === 0) {
  log(BOOK_SLUG + ': No sections found!')
  return { book: BOOK_SLUG, concepts: 0, error: 'no_sections' }
}

log(BOOK_SLUG + ': ' + sectionFiles.length + ' sections to process')

phase('Extract')

var results = await pipeline(sectionFiles, function(sectionPath, item, idx) {
  return async function() {
    var sName = sectionPath.split('/').pop().replace('.md','')
    var destDir = STAGING + '/' + sName

    var prompt = [
      '=== V7 CONCEPT EXTRACTOR (Section-level) ===',
      '',
      'You are extracting mathematical concepts from a SINGLE SECTION of a math textbook.',
      'This section is about 10 pages long — small enough to process completely.',
      '',
      'READ the section file: ' + sectionPath,
      '',
      'Extract EVERY theorem, definition, lemma, proposition, corollary, and axiom.',
      'For EACH concept, create: ' + destDir + '/{SLUG}/',
      'Then write these 3 files per concept:',
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
      'depends_on: {required: [], recommended: [], suggested: []}',
      'source_books: [{book_id: "<guess>", author: "", title: "", chapter: "", section: "", pages: "", role_in_book: ""}]',
      'content_hash: ""',
      'extraction_date: "2026-06-25"',
      'extraction_agent: "v7-section-test"',
      '',
      '═══ FILE 2: theorem.tex ═══',
      'PURE LaTeX STATEMENT only. NO proof. NO English words outside \\text{}.',
      'If the concept is a definition, write the formal definition.',
      'Use $$ for display math, $ for inline.',
      '',
      '═══ FILE 3: introduce.en.md ═══',
      'YAML frontmatter:',
      '  role: introduce',
      '  locale: en',
      '  content_hash: ""',
      '  written_against: ""',
      'Then 2-4 sentences in plain English explaining what this concept means and why it matters.',
      '',
      '═══ CRITICAL RULES ═══',
      '1. Slug = semantic lowercase-hyphen English (e.g. kummers-theorem, subgroup-criterion)',
      '   BAD slugs: gtm006-theorem-4-6, thm3.2, ch1-def1',
      '2. theorem.tex = STATEMENT ONLY. NO proof. NO "Proof." text.',
      '3. source_books = array of OBJECTS, not strings: [{book_id:"", author:"", ...}]',
      '4. depends_on: list concept SLUGS this concept uses (can be empty if no deps found in this section)',
      '5. Extract ALL concepts, even "obvious" lemmas',
      '6. OCR may have artifacts — use mathematical reasoning to fix garbled formulas',
      '7. If a formula is unreadable, mark with % OCR-ARTIFACT: <best guess>',
      '',
      'Write .done when ALL concepts in this section are extracted:',
      '  echo "DONE" > ' + destDir + '/.done',
      '',
      'If stuck or the section is unreadable, write .fail:',
      '  echo "FAIL: <reason>" > ' + destDir + '/.fail'
    ].join('\n')

    try {
      await agent(prompt, { label: sName, phase: 'Extract' })
    } catch(e) {
      // API error — mark for retry
    }

    // Count concepts written to disk
    var cnt = 0
    try {
      var cr = await agent(
        'bash -c "find ' + destDir + ' -name concept.yaml 2>/dev/null | wc -l"',
        { label: 'cnt-' + sName, phase: 'Extract' }
      )
      cnt = cr ? parseInt(cr.trim()) || 0 : 0
    } catch(e) {}

    // Check .done marker
    var done = false
    try {
      var dr = await agent(
        'bash -c "test -f ' + destDir + '/.done && echo YES || echo NO"',
        { label: 'check-' + sName, phase: 'Extract' }
      )
      done = dr && dr.trim() === 'YES'
    } catch(e) {}

    return { section: sName, concepts: cnt, done: done }
  }
})

var totalConcepts = results.filter(Boolean).reduce(function(s, r) { return s + (r.concepts || 0) }, 0)
var doneCount = results.filter(Boolean).filter(function(r) { return r.done }).length
var failCount = results.filter(Boolean).filter(function(r) { return !r.done }).length

log(BOOK_SLUG + ': ' + totalConcepts + ' concepts from ' + doneCount + '/' + results.filter(Boolean).length + ' sections (' + failCount + ' failed)')

return {
  book: BOOK_SLUG,
  sections_total: sectionFiles.length,
  sections_done: doneCount,
  sections_failed: failCount,
  total_concepts: totalConcepts,
  details: results.filter(Boolean)
}
