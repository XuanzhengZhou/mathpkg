export const meta = {
  name: 'v7-10books-test',
  description: '10 books concurrent concept extraction test',
  phases: [{ title: 'Extract', detail: '10 agents parallel, one per book' }]
}

var BOOKS = args.books
var STITCHED = '/home/a123/文档/mathpkg/pipeline_output/stitched'
var STAGING = '/home/a123/文档/mathpkg/pipeline_output/v7_test/staging'

phase('Extract')

var tasks = BOOKS.map(function(bookDir, i) {
  return async function() {
    var fullPath = STITCHED + '/' + bookDir + '/_full.md'
    var stagingDir = STAGING + '/' + bookDir.replace(/[^a-zA-Z0-9]/g, '_')
    try {
      await agent([
        '=== V7 CONCEPT EXTRACTOR ===',
        'Read the book: ' + fullPath,
        'This book is ~' + Math.round(100) + 'KB. Extract ALL theorems, definitions, lemmas, propositions, corollaries.',
        '',
        'For EACH concept, create folder: ' + stagingDir + '/{slug}/',
        'Write these files with EXACT format:',
        '',
        '1. concept.yaml:',
        'id: <semantic-english-slug>',
        'title_en: "<Full Name>"',
        'title_zh: ""',
        'type: theorem',
        'domain: <best-guess>',
        'subdomain: <best-guess>',
        'difficulty: basic',
        'tags: []',
        'depends_on: { required: [], recommended: [], suggested: [] }',
        'proof_deps: {}',
        'source_books: [{ book_id: "<guess>", author: "", title: "", chapter: "", section: "", pages: "", role_in_book: "" }]',
        'content_hash: ""',
        'extraction_date: "2026-06-24"',
        'extraction_agent: "v7-10books"',
        '',
        '2. theorem.tex: PURE LaTeX. ZERO YAML. ZERO markdown.',
        '',
        '3. introduce.en.md: YAML frontmatter + 2-4 sentence description.',
        '',
        'CRITICAL: Slug = semantic English. source_books = array of OBJECTS. theorem.tex = pure LaTeX.',
        'If the book is large, process it in sections.',
        'Write .done when complete: echo DONE > ' + stagingDir + '/.done'
      ].join('\n'), { label: 'book-' + i, phase: 'Extract' })
    } catch(e) {}

    var cnt = 0
    try {
      var r = await agent(
        'python3 -c "import os; d=\'' + stagingDir + '\'; print(len([x for x in os.listdir(d) if os.path.isdir(os.path.join(d,x))]))"',
        { label: 'cnt-' + i, phase: 'Extract' }
      )
      cnt = r ? parseInt(r.trim()) || 0 : 0
    } catch(e) {}
    log(bookDir.substring(0,40) + ': ' + cnt + ' concepts')
    return { book: bookDir.substring(0,30), concepts: cnt }
  }
})

var results = await parallel(tasks)
var total = results.filter(Boolean).reduce(function(s,r){return s+r.concepts},0)
var attempted = results.filter(Boolean).length
log('TOTAL: ' + total + ' concepts from ' + attempted + '/10 books')
return { total_concepts: total, books_processed: attempted, details: results.filter(Boolean) }
