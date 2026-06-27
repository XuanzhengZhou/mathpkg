export const meta = {
  name: 'v7-section-extract-v2',
  description: 'One book: per-section concept extraction. Sections passed as args.',
  phases: [{ title: 'Extract', detail: 'One agent per section, parallel via pipeline' }]
}

// args.sections = array of absolute paths to section .md files
// args.staging = output directory
// args.book_slug = short book identifier

var SECTIONS = args.sections
var STAGING = args.staging
var BOOK_SLUG = args.book_slug

phase('Extract')

log(BOOK_SLUG + ': ' + SECTIONS.length + ' sections, launching agents...')

var results = await pipeline(SECTIONS, function(sectionPath, item, idx) {
  return async function() {
    var sName = sectionPath.split('/').pop().replace('.md','')
    var destDir = STAGING + '/' + sName

    var prompt = [
      '=== V7 CONCEPT EXTRACTOR (Per-Section) ===',
      '',
      'READ this section file: ' + sectionPath,
      '',
      'Extract EVERY theorem, definition, lemma, proposition, corollary, and axiom.',
      'For EACH concept, write these 3 files in: ' + destDir + '/{SLUG}/',
      '',
      'FILE 1 — concept.yaml:',
      '  id: <semantic-english-slug>',
      '  title_en: "<Full name>"',
      '  title_zh: ""',
      '  type: theorem|definition|lemma|proposition|corollary|axiom',
      '  domain: <best-guess>',
      '  subdomain: <best-guess>',
      '  difficulty: basic|intermediate|advanced',
      '  tags: []',
      '  depends_on: {required:[], recommended:[], suggested:[]}',
      '  source_books: [{book_id:"' + BOOK_SLUG + '",author:"",title:"",chapter:"",section:"",pages:"",role_in_book:""}]',
      '  content_hash: ""',
      '  extraction_date: "2026-06-25"',
      '  extraction_agent: "v7-section-test"',
      '',
      'FILE 2 — theorem.tex: PURE LaTeX statement. NO proof. NO natural language outside \\text{}.',
      '',
      'FILE 3 — introduce.en.md:',
      '  YAML frontmatter: role:introduce, locale:en, content_hash:"", written_against:""',
      '  Then 2-4 English sentences explaining the concept.',
      '',
      'CRITICAL RULES:',
      '1. Slug = lowercase-hyphen semantic English (kummers-theorem, NOT gtm004-thm-3-2)',
      '2. theorem.tex = STATEMENT ONLY',
      '3. source_books = array of OBJECTS',
      '4. Extract ALL concepts, even small lemmas',
      '5. Fix OCR artifacts using mathematical reasoning',
      '',
      'Write .done when complete: echo "DONE" > ' + destDir + '/.done'
    ].join('\n')

    try { await agent(prompt, { label: sName.substring(0,40), phase: 'Extract' }) } catch(e) {}

    // Count disk output
    var cnt = 0
    try {
      var cr = await agent(
        'python3 -c "import os; d=\'' + destDir + '\'; print(len([x for x in os.listdir(d) if os.path.isdir(os.path.join(d,x))]) if os.path.exists(d) else 0)"',
        { label: 'cnt-' + sName.substring(0,30), phase: 'Extract' }
      )
      cnt = cr ? parseInt(cr.trim()) || 0 : 0
    } catch(e) {}

    return { section: sName.substring(0,50), concepts: cnt }
  }
})

var totalConcepts = results.filter(function(r) { return r !== null }).reduce(function(s, r) { return s + (r.concepts || 0) }, 0)
var failed = results.filter(function(r) { return r === null || (r.concepts === 0) }).length

log(BOOK_SLUG + ': ' + totalConcepts + ' concepts from ' + (SECTIONS.length - failed) + '/' + SECTIONS.length + ' sections')

return { book: BOOK_SLUG, sections: SECTIONS.length, concepts: totalConcepts, failed: failed }
