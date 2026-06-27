export const meta = {
  name: 'section-test',
  description: 'Test: extract concepts from one section of a book',
  phases: [{ title: 'Extract', detail: 'One agent per section' }]
}

// args: { section: "/absolute/path/to/section.md", staging: "/path/to/output", book_slug: "gtm004" }
var SECTION = args.section
var STAGING = args.staging
var BOOK = args.book_slug
var sName = SECTION.split('/').pop().replace('.md','')
var destDir = STAGING + '/' + sName

phase('Extract')

var prompt = [
  '=== V7 CONCEPT EXTRACTOR ===',
  '',
  'READ this section: ' + SECTION,
  '',
  'Extract EVERY theorem, definition, lemma, proposition, corollary, axiom.',
  'For EACH concept, write 3 files in: ' + destDir + '/{SLUG}/',
  '',
  'FILE 1 — concept.yaml:',
  '  id: <semantic-english-slug>',
  '  title_en: "<Full name>"',
  '  title_zh: ""',
  '  type: theorem|definition|lemma|proposition|corollary|axiom',
  '  domain: algebra|analysis|topology|geometry|number-theory|logic|combinatorics|probability|applied-math|foundations',
  '  subdomain: <best-guess>',
  '  difficulty: basic|intermediate|advanced',
  '  depends_on: {required:[], recommended:[], suggested:[]}',
  '  source_books: [{book_id:"' + BOOK + '",author:"",title:"",chapter:"",section:"",pages:"",role_in_book:""}]',
  '  content_hash: ""',
  '  extraction_date: "2026-06-25"',
  '  extraction_agent: "v7-section-test"',
  '',
  'FILE 2 — theorem.tex: PURE LaTeX statement. NO proof.',
  '',
  'FILE 3 — introduce.en.md: YAML frontmatter(role:introduce,locale:en,content_hash:"",written_against:"") + 2-4 English sentences.',
  '',
  'RULES:',
  '- slug = lowercase-hyphen semantic English (e.g., kummers-theorem)',
  '- source_books = array of OBJECTS, not strings',
  '- theorem.tex = zero natural language outside \\text{}',
  '- Extract ALL concepts including small lemmas',
  '- Fix OCR artifacts using math reasoning',
  '',
  'Write .done: echo DONE > ' + destDir + '/.done'
].join('\n')

try {
  await agent(prompt, { label: sName.substring(0,35), phase: 'Extract' })
} catch(e) {}

// Count
var cnt = 0
try {
  var cr = await agent(
    'python3 -c "import os; d=\'' + destDir + '\'; print(len([x for x in os.listdir(d) if os.path.isdir(os.path.join(d,x))]))"',
    { label: 'cnt', phase: 'Extract' }
  )
  cnt = cr ? parseInt(cr.trim()) || 0 : 0
} catch(e) {}

log(sName + ': ' + cnt + ' concepts')
return { section: sName, concepts: cnt }
