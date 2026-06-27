export const meta = {
  name: 'phase1-gapfill-redo',
  description: 'Phase 1 redo: Gap-fill 14 failed concepts. No schema — write directly to file.',
  phases: [{ title: 'Gap-fill', detail: '14 agents: expand proofs, write results to JSON file' }]
}

var INPUT = '/home/a123/文档/mathpkg/pipeline_output/p1_gapfill_redo.json'
var OUTDIR = '/home/a123/文档/mathpkg/pipeline_output/gapfill_output'
var TOTAL = 14

phase('Gap-fill')

var tasks = Array.from({length: TOTAL}, function(_, i) {
  return function() {
    return agent([
      'Expand this mathematical proof into explicit numbered steps. Do NOT write Lean code.',
      '',
      'STEP 1 — Read concept:',
      'python3 -c "import json; d=json.load(open(\'' + INPUT + '\')); c=d[' + i + ']; print(\'NAME:\',c[\'name\']); print(\'STATEMENT:\',c[\'statement\']); print(\'PROOF:\',c.get(\'proof_sketch\',\'\'))"',
      '',
      'STEP 2 — Expand into numbered steps. Each step:',
      '- ONE logical inference',
      '- References a specific theorem/lemma/definition by name',
      '- NO: clearly, obviously, it follows, one can show, trivial, easy to see, straightforward',
      '- End with "∎"',
      '',
      'STEP 3 — Write result file (USE WRITE TOOL, full path):',
      'File: ' + OUTDIR + '/gap_' + (i + 100) + '.json',
      'Content: {"concept_index":' + (i + 100) + ',"expanded_proof":"1. ...\\n2. ...\\n∎"}'
    ].join('\n'), { label: 'gap-redo-' + i, phase: 'Gap-fill' })
  }
})

var results = await parallel(tasks)
log('Phase 1 redo: ' + results.filter(Boolean).length + '/' + TOTAL + ' attempted')
return { attempted: results.filter(Boolean).length }
