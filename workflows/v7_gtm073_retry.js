export const meta = {
  name: 'v7-gtm073-retry',
  description: 'Retry failed chapters of GTM073: ch05 + ch07',
  phases: [{ title: 'Extract', detail: '2 agents re-extract failed chapters' }]
}

var STAGING = '/home/a123/文档/mathpkg/pipeline_output/v7_test/staging/gtm-0073'
var CHAPTERS = [
  { file: '05_CHAPTER VI.md',  name: 'Ch6_Fields',   n: 5 },
  { file: '07_CHAPTER VIII.md',name: 'Ch8_CommRings',n: 7 },
]
var BASE = '/home/a123/文档/mathpkg/pipeline_output/stitched/(GTM073)Algebra'

phase('Extract')

var tasks = CHAPTERS.map(function(ch) {
  return async function() {
    var chap_file = BASE + '/' + ch.file
    var chap_staging = STAGING + '/gtm-0073_ch' + String(ch.n).padStart(2,'0') + '_concepts'
    try {
      await agent([
        '=== RETRY: Read chapter and extract concepts. ===',
        'Read: ' + chap_file,
        '',
        'STEP 0: Check what already exists:',
        'python3 -c "import os; d=\'' + chap_staging + '\'; print(len([x for x in os.listdir(d) if os.path.isdir(os.path.join(d,x))]) if os.path.exists(d) else 0)"',
        'If > 0, those are already extracted. Extract the REMAINING concepts.',
        '',
        'Same format as before: concept.yaml + theorem.tex + introduce.en.md + proof files.',
        'Slug = semantic English. source_books = array of objects. theorem.tex = pure LaTeX.',
        '',
        'Extract ALL remaining concepts. Write .done when complete:',
        'echo DONE > ' + chap_staging + '/.done'
      ].join('\n'), { label: 'retry-' + ch.name, phase: 'Extract' })
    } catch(e) {}
    // Count
    var cnt = 0
    try {
      var r = await agent(
        'python3 -c "import os; d=\'' + chap_staging + '\'; print(len([x for x in os.listdir(d) if os.path.isdir(os.path.join(d,x))]))"',
        { label: 'cnt-' + ch.name, phase: 'Extract' }
      )
      cnt = r ? parseInt(r.trim()) || 0 : 0
    } catch(e) {}
    log(ch.name + ': ' + cnt + ' concepts')
    return { chapter: ch.name, concepts: cnt }
  }
})

var results = await parallel(tasks)
var added = results.filter(Boolean).reduce(function(s, r) { return s + r.concepts }, 0)
log('Retry added: ' + added + ' concepts')
return { added: added }
