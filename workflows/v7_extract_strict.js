export const meta = {
  name: 'v7-extract-strict',
  description: 'Strict V7 extraction with enforced semantic slugs, no proofs in theorem.tex',
  phases: [{ title: 'Extract', detail: '10 agents parallel with strict prompt template' }]
}

var BOOKS = args.books
var STITCHED = '/home/a123/文档/mathpkg/pipeline_output/stitched'
var STAGING = '/home/a123/文档/mathpkg/pipeline_output/v7_test/staging_v2'

phase('Extract')

var tasks = BOOKS.map(function(bookDir, i) {
  return async function() {
    var fullPath = STITCHED + '/' + bookDir + '/_full.md'
    var bookSlug = bookDir.replace(/[^a-zA-Z0-9]/g, '_').substring(0, 50)
    var destDir = STAGING + '/' + bookSlug
    var prompt = [
      '=== CONCEPT EXTRACTOR (V7, Strict Mode) ===',
      '',
      'READ the book: ' + fullPath,
      '',
      'YOU MUST extract ALL theorems, definitions, lemmas, propositions, and corollaries.',
      'For each concept, create a folder under: ' + destDir + '/{SLUG}/',
      '',
      '═══ SLUG RULES ═══',
      'Slug = lowercase-hyphen semantic English describing the concept.',
      '',
      '✅ GOOD slugs:',
      '  kummers-theorem-for-regular-primes',
      '  first-isomorphism-theorem-for-groups',
      '  subgroup-criterion',
      '  compactness-in-metric-spaces',
      '  class-number-formula-for-cyclotomic-fields',
      '',
      '❌ BAD slugs (DO NOT USE):',
      '  gtm006-theorem-4-6       ← book reference, not semantic',
      '  chii-defn-1-1             ← abbreviated chapter ref',
      '  theorem.tex               ← not a slug',
      '  def_gtm073_1              ← encoded book info',
      '',
      '═══ theorem.tex RULES ═══',
      'theorem.tex contains ONLY the theorem STATEMENT in LaTeX.',
      'NOT a proof. NOT a definition. NOT natural language.',
      '',
      '✅ CORRECT theorem.tex:',
      '  Let $G$ be a finite group and $H \\\\leq G$. Then $|H| \\\\mid |G|$.',
      '',
      '❌ WRONG theorem.tex:',
      '  \\\\textbf{Proof.} Let $a,b \\\\in G$...     ← NO PROOF',
      '  A group is a set with a binary operation...  ← use definition.tex',
      '  We shall prove that...                        ← NO natural language',
      '',
      '═══ FILE STRUCTURE (per concept) ═══',
      destDir + '/{slug}/',
      '',
      '1. concept.yaml:',
      'id: <SAME AS SLUG>',
      'title_en: "<Full English Name>"',
      'title_zh: ""',
      'type: theorem        ← theorem|definition|lemma|proposition|corollary|axiom',
      'domain: <best guess from: algebra|analysis|topology|geometry|number-theory|logic-foundations|probability-statistics|combinatorics|applied-math|algebraic-geometry>',
      'subdomain: <lowercase-hyphen>',
      'difficulty: basic    ← basic|intermediate|advanced',
      'tags: []',
      'depends_on: { required: [], recommended: [], suggested: [] }',
      'proof_deps: {}',
      'source_books:',
      '  - book_id: "<guess>"',
      '    author: ""',
      '    title: ""',
      '    chapter: ""',
      '    section: ""',
      '    pages: ""',
      '    role_in_book: ""',
      'content_hash: ""',
      'extraction_date: "2026-06-24"',
      'extraction_agent: "v7-strict"',
      '',
      '2. theorem.tex (or definition.tex/lemma.tex/proposition.tex/corollary.tex):',
      'PURE LaTeX STATEMENT ONLY. No proof. No English words outside \\\\text{}.',
      '',
      '3. introduce.en.md:',
      '---',
      'role: introduce',
      'locale: en',
      'content_hash: ""',
      'written_against: ""',
      '---',
      '<2-4 sentence natural language description>',
      '',
      '═══ FINAL CHECK ═══',
      'Before marking done, verify:',
      '- [ ] Every slug is SEMANTIC (not gtm006-theorem-4-6)',
      '- [ ] Every theorem.tex has NO proof text',
      '- [ ] Every concept.yaml has source_books as array of OBJECTS',
      '- [ ] Every folder has concept.yaml + theorem.tex + introduce.en.md',
      '',
      'Write .done when DONE: echo DONE > ' + destDir + '/.done'
    ].join('\n')

    try { await agent(prompt, { label: 'bk-' + i, phase: 'Extract' }) } catch(e) {}

    var cnt = 0
    try {
      var r = await agent('bash -c "find ' + destDir + ' -name concept.yaml 2>/dev/null | wc -l"', { label: 'cnt-' + i, phase: 'Extract' })
      cnt = r ? parseInt(r.trim()) || 0 : 0
    } catch(e) {}
    log(bookDir.substring(0,35) + ': ' + cnt + ' concepts')
    return { book: bookDir.substring(0,30), concepts: cnt }
  }
})

var results = await parallel(tasks)
var total = results.filter(Boolean).reduce(function(s,r){return s+r.concepts},0)
var ok = results.filter(Boolean).length
log('TOTAL: ' + total + ' concepts from ' + ok + '/10 books')
return { total_concepts: total, books: ok, details: results.filter(Boolean) }
