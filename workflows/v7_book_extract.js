export const meta = {
  name: 'v7-book-extract',
  description: 'One book: per-chapter concept extraction in V7 strict format',
  phases: [{ title: 'Extract', detail: 'One agent per chapter, parallel within book' }]
}

var BOOK_DIR = args.book_dir
var STAGING = args.staging
var BOOK_SLUG = args.book_slug

phase('Extract')

// Read chapter list
var chList = []
try {
  var r = await agent(
    'bash -c "ls ' + BOOK_DIR + '/ch*.md 2>/dev/null"',
    { label: 'list-chapters', phase: 'Extract' }
  )
  if (r) chList = r.trim().split('\n').filter(function(x) { return x.length > 0 })
} catch(e) {}
if (chList.length === 0) { log('No chapters found in ' + BOOK_DIR); return { chapters: 0, concepts: 0 } }

log(BOOK_SLUG + ': ' + chList.length + ' chapters')

var tasks = chList.map(function(chPath, i) {
  return async function() {
    var chName = chPath.split('/').pop().replace('.md','')
    var destDir = STAGING + '/' + chName

    var prompt = [
      '=== V7 CONCEPT EXTRACTOR (Strict, per-chapter) ===',
      '',
      'READ the chapter: ' + chPath,
      '',
      'Extract ALL theorems, definitions, lemmas, propositions, corollaries.',
      'For EACH concept, create folder: ' + destDir + '/{SLUG}/',
      'Then write: concept.yaml + theorem.tex + introduce.en.md',
      '',
      '═══ SLUG RULES ═══',
      'Slug = lowercase-hyphen semantic English.',
      'GOOD: kummers-theorem-for-regular-primes, subgroup-criterion',
      'BAD: gtm006-theorem-4-6, chii-defn-1-1, theorem.tex',
      '',
      '═══ theorem.tex ═══',
      'PURE LaTeX STATEMENT only. NO proof. NO English words outside \\text{}.',
      '',
      '═══ concept.yaml ═══',
      'id: <SLUG>',
      'title_en: "<Full Name>"',
      'title_zh: ""',
      'type: theorem|definition|lemma|proposition|corollary',
      'domain: <best-guess>',
      'subdomain: <best-guess>',
      'difficulty: basic|intermediate|advanced',
      'tags: []',
      'depends_on: {required:[], recommended:[], suggested:[]}',
      'source_books: [{book_id:"",author:"",title:"",chapter:"",section:"",pages:"",role_in_book:""}]',
      'content_hash: ""',
      'extraction_date: "2026-06-24"',
      'extraction_agent: "v7-per-chapter"',
      '',
      '═══ introduce.en.md ═══',
      'YAML frontmatter (role:introduce, locale:en, content_hash:"", written_against:"") + 2-4 sentences.',
      '',
      'Write .done when ALL concepts extracted: echo DONE > ' + destDir + '/.done'
    ].join('\n')

    try { await agent(prompt, { label: chName, phase: 'Extract' }) } catch(e) {}

    var cnt = 0
    try {
      var cr = await agent('bash -c "find ' + destDir + ' -name concept.yaml 2>/dev/null | wc -l"', { label: 'cnt-' + chName, phase: 'Extract' })
      cnt = cr ? parseInt(cr.trim()) || 0 : 0
    } catch(e) {}
    return { chapter: chName, concepts: cnt }
  }
})

var results = await parallel(tasks)
var total = results.filter(Boolean).reduce(function(s,r){return s+(r.concepts||0)},0)
log(BOOK_SLUG + ': ' + total + ' concepts from ' + chList.length + ' chapters')
return { book: BOOK_SLUG, chapters: chList.length, concepts: total, details: results.filter(Boolean) }
