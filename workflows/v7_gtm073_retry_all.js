export const meta = {
  name: 'v7-gtm073-full-retry',
  description: 'Re-run ALL chapters that reported 0 concepts',
  phases: [{ title: 'Extract', detail: '5 agents re-extract failed chapters' }]
}

var STAGING = '/home/a123/文档/mathpkg/pipeline_output/v7_test/staging/gtm-0073'
var CHAPTERS = [
  { file: '02_CHAPTER II.md',  n: 2 },
  { file: '03_CHAPTER IV.md',  n: 3 },
  { file: '05_CHAPTER VI.md',  n: 5 },
  { file: '07_CHAPTER VIII.md',n: 7 },
  { file: '09_CHAPTER X.md',   n: 9 },
]
var BASE = '/home/a123/文档/mathpkg/pipeline_output/stitched/(GTM073)Algebra'

phase('Extract')

function prompt(ch) {
  var chap_file = BASE + '/' + ch.file
  var chap_staging = STAGING + '/gtm-0073_ch' + String(ch.n).padStart(2,'0') + '_concepts'
  return [
    '=== RETRY: Extract remaining concepts from this chapter. ===',
    'Read and process: ' + chap_file,
    '',
    'STEP 0: List existing concepts:',
    'find ' + chap_staging + ' -name concept.yaml 2>/dev/null | while read f; do dirname "$f" | xargs basename; done',
    '',
    'Extract ALL concepts NOT already extracted.',
    'Format: concept.yaml + theorem.tex + introduce.en.md + proof files.',
    'Slug = semantic English. source_books = array of objects.',
    'theorem.tex = pure LaTeX. English goes in introduce.en.md.',
    '',
    'Write .done when complete: echo DONE > ' + chap_staging + '/.done'
  ].join('\n')
}

var tasks = CHAPTERS.map(function(ch) {
  return async function() {
    var chap_staging = STAGING + '/gtm-0073_ch' + String(ch.n).padStart(2,'0') + '_concepts'
    try { await agent(prompt(ch), { label: 'retry-ch' + ch.n, phase: 'Extract' }) } catch(e) {}
    var cnt = 0
    try {
      var r = await agent(
        'python3 -c "import os; d=\'' + chap_staging + '\'; print(len([x for x in os.listdir(d) if os.path.isdir(os.path.join(d,x))]))"',
        { label: 'cnt-ch' + ch.n, phase: 'Extract' }
      )
      cnt = r ? parseInt(r.trim()) || 0 : 0
    } catch(e) {}
    log('Ch' + ch.n + ': ' + cnt + ' concepts')
    return cnt
  }
})

var results = await parallel(tasks)
var total = results.filter(Boolean).reduce(function(s,r){return s+r},0)
log('Retry total: ' + total)
return { total: total }
