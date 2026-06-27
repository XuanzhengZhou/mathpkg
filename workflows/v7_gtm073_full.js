export const meta = {
  name: 'v7-gtm073-full',
  description: 'GTM073 Algebra: extract all 9 chapters in parallel, count concepts + cost',
  phases: [{ title: 'Extract', detail: '9 agents in parallel, one per chapter' }]
}

var STAGING = '/home/a123/文档/mathpkg/pipeline_output/v7_test/staging/gtm-0073'
var CHAPTERS = [
  { file: '01_CHAPTER I.md',   name: 'Ch1_Groups',     n: 1 },
  { file: '02_CHAPTER II.md',  name: 'Ch2_Structure',  n: 2 },
  { file: '03_CHAPTER IV.md',  name: 'Ch4_Modules',    n: 3 },
  { file: '04_CHAPTER V.md',   name: 'Ch5_Fields',     n: 4 },
  { file: '05_CHAPTER VI.md',  name: 'Ch6_Structure',  n: 5 },
  { file: '06_CHAPTER VII.md', name: 'Ch7_Linear',     n: 6 },
  { file: '07_CHAPTER VIII.md',name: 'Ch8_CommRings',  n: 7 },
  { file: '08_CHAPTER IX.md',  name: 'Ch9_Rings',      n: 8 },
  { file: '09_CHAPTER X.md',   name: 'Ch10_Categories',n: 9 },
]
var BASE = '/home/a123/文档/mathpkg/pipeline_output/stitched/(GTM073)Algebra'

phase('Extract')

function chapterPrompt(ch) {
  var chapter_file = BASE + '/' + ch.file
  var chap_staging = STAGING + '/gtm-0073_ch' + String(ch.n).padStart(2,'0') + '_concepts'
  return [
    '=== CONCEPT EXTRACTOR (V7) — GTM073 ' + ch.name + ' ===',
    '',
    'Read: ' + chapter_file,
    '',
    'Extract ALL theorems, definitions, lemmas, propositions, corollaries.',
    'For EACH concept, create a folder under ' + chap_staging + '/{slug}/',
    '',
    'FILE FORMATS (exact):',
    '',
    '--- concept.yaml ---',
    'id: <semantic-english-slug>',
    'title_en: "<Full Name>"',
    'title_zh: ""',
    'type: theorem',
    'domain: algebra',
    'subdomain: <appropriate>',
    'difficulty: basic',
    'tags: []',
    'depends_on:',
    '  required: []',
    '  recommended: []',
    '  suggested: []',
    'proof_deps: {}',
    'source_books:',
    '  - book_id: gtm-0073',
    '    author: "Hungerford, Thomas W."',
    '    title: "Algebra"',
    '    chapter: I',
    '    section: "<I.X>"',
    '    pages: ""',
    '    role_in_book: "<Theorem X.X>"',
    'content_hash: ""',
    'extraction_date: "2026-06-24"',
    'extraction_agent: "v7-gtm073"',
    '',
    '--- theorem.tex ---',
    'PURE LaTeX only. ZERO YAML, ZERO markdown, ZERO English.',
    '',
    '--- introduce.en.md ---',
    '---',
    'role: introduce',
    'locale: en',
    'content_hash: ""',
    'written_against: ""',
    '---',
    '<2-4 sentence natural language description>',
    '',
    '--- proof_gtm-0073_I_SECTION_TECHNIQUE.en.md ---',
    '---',
    'role: proof',
    'source_book: gtm-0073',
    'chapter: I',
    'section: "<I.X>"',
    'proof_technique: <one-word>',
    'locale: en',
    'content_hash: ""',
    'written_against: ""',
    '---',
    '<proof>',
    '',
    'CRITICAL:',
    '- Slug = SEMANTIC English (e.g., "first-isomorphism-theorem")',
    '- source_books = array of OBJECTS, not strings',
    '- theorem.tex = PURE LaTeX. English goes in introduce.en.md',
    '- Extract ALL concepts, no limit',
    '- Write .done when complete'
  ].join('\n')
}

var tasks = CHAPTERS.map(function(ch) {
  return async function() {
    var chap_staging = STAGING + '/gtm-0073_ch' + String(ch.n).padStart(2,'0') + '_concepts'
    try {
      await agent(chapterPrompt(ch), { label: ch.name, phase: 'Extract' })
    } catch(e) {}
    // Count concepts
    try {
      var countResult = await agent(
        'python3 -c "import os; d=\'' + chap_staging + '\'; dirs=[x for x in os.listdir(d) if os.path.isdir(os.path.join(d,x))] if os.path.exists(d) else []; print(len(dirs))"',
        { label: 'count-' + ch.name, phase: 'Extract' }
      )
      var count = countResult ? parseInt(countResult.trim()) || 0 : 0
      log(ch.name + ': ' + count + ' concepts')
      return { chapter: ch.name, concepts: count }
    } catch(e) {
      return { chapter: ch.name, concepts: 0 }
    }
  }
})

var results = await parallel(tasks)
var total = results.filter(Boolean).reduce(function(sum, r) { return sum + r.concepts }, 0)
log('TOTAL: ' + total + ' concepts from GTM073')
return { total_concepts: total, chapters: results.filter(Boolean) }
