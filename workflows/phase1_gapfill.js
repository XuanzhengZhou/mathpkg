export const meta = {
  name: 'phase1-gapfill',
  description: 'Phase 1: Gap-fill 21 theorems. Expand proof sketches into explicit numbered steps.',
  phases: [
    { title: 'Gap-fill', detail: '21 agents: expand brief proofs into detailed numbered steps with theorem references' }
  ]
}

var INPUT = '/home/a123/文档/mathpkg/pipeline_output/p1_gapfill.json'
var OUTDIR = '/home/a123/文档/mathpkg/pipeline_output/gapfill_output'

phase('Gap-fill')

var tasks = Array.from({length: 21}, function(_, i) {
  return function() {
    var prompt = [
      'Read concept #' + i + ' from the JSON array and expand its proof sketch into explicit numbered steps.',
      '',
      'Command to read the concept:',
      'python3 -c "import json; data=json.load(open(\'' + INPUT + '\')); c=data[' + i + ']; print(\'NAME:\', c[\'name\']); print(\'TYPE:\', c[\'type\']); print(\'STATEMENT:\', c[\'statement\']); print(\'PROOF_SKETCH:\', c.get(\'proof_sketch\',\'\'))"',
      '',
      'Then expand the proof. Rules:',
      '1. Each step is ONE logical inference',
      '2. Each step MUST reference a specific theorem/lemma/definition/axiom by name',
      '3. NEVER use: clearly, obviously, it follows that, one can show, trivially, easy to see, straightforward, the result follows',
      '4. If the proof sketch references "Theorem X" or "Lemma Y", explain HOW it applies, not just that it applies',
      '5. A first-year graduate student should follow every line without guessing',
      '6. End with the theorem statement as the conclusion',
      '',
      'Output format — write as a JSON file to: ' + OUTDIR + '/gap_' + i + '.json',
      'Use this structure:',
      '{',
      '  "concept_index": ' + i + ',',
      '  "expanded_proof": "1. [First step with theorem reference]\\n2. [Second step]\\n...\\nN. [Conclusion] ∎"',
      '}',
      '',
      'Write the file with: cat > ' + OUTDIR + '/gap_' + i + '.json << \'ENDOFFILE\'',
      '...json content...',
      'ENDOFFILE',
      '',
      'IMPORTANT: Do NOT translate to Lean. Do NOT write .lean files. ONLY expand the proof in natural language.'
    ].join('\n')

    return agent(prompt, {
      label: 'gap-' + i,
      phase: 'Gap-fill'
    })
  }
})

var results = await parallel(tasks)
var done = results.filter(Boolean).length
log('Phase 1 complete: ' + done + '/21 gap-fills attempted')
return { attempted: done, total: 21 }
