export const meta = {
  name: 'phase2-fix-batch',
  description: 'Fix failed concepts: read existing .lean and self-heal, or full translate if no file',
  phases: [{ title: 'Fix', detail: 'Agents self-heal existing .lean files or translate from scratch if missing' }]
}

// args: { indices: [0,2,7,...], input_file: "phase2_input_49.json", group: 1 }
var INDICES = args.indices
var INPUT = '/home/a123/文档/mathpkg/pipeline_output/phase2_input_49.json'
var LEAN_PROJ = '/home/a123/文档/mathpkg/lean/MathPkg'
var RESULT_DIR = '/home/a123/文档/mathpkg/pipeline_output/fix_results'
var GID = args.group || 1

phase('Fix')

var tasks = INDICES.map(function(idx) {
  return function() {
    return agent([
      'Fix or translate concept at index ' + idx + ' from ' + INPUT + '.',
      '',
      'STEP 0 — Check if .lean file exists:',
      'ls ' + LEAN_PROJ + '/MathPkg/Pipeline/<concept_id>.lean 2>&1',
      'Get concept_id from: python3 -c "import json; d=json.load(open(\'' + INPUT + '\')); print(d[' + idx + '][\'id\'])"',
      '',
      'IF FILE EXISTS (self-heal mode):',
      '1. Run: cd ' + LEAN_PROJ + ' && export PATH="$HOME/.elan/bin:$PATH" && lake env lean MathPkg/Pipeline/<id>.lean 2>&1',
      '2. If NO errors → done, go to REPORT step',
      '3. If errors: READ each error, grep Mathlib4 for correct names, edit file, recompile',
      '4. Repeat up to 10 rounds until exit code 0 and no "error:" in output',
      '',
      'IF FILE MISSING (full translate mode):',
      '1. Read concept: python3 -c "import json; d=json.load(open(\'' + INPUT + '\')); c=d[' + idx + ']; print(\'STATEMENT:\',c[\'statement\']); print(\'GAPFILL:\',c[\'gapfill_proof\'][:2000])"',
      '2. grep Mathlib4: cd ~/lean-demo/.lake/packages/mathlib && grep -r "KEYWORD" Mathlib/ --include="*.lean" -l | head -10',
      '3. Write .lean file to ' + LEAN_PROJ + '/MathPkg/Pipeline/<id>.lean',
      '4. Compile: cd ' + LEAN_PROJ + ' && export PATH="$HOME/.elan/bin:$PATH" && lake env lean MathPkg/Pipeline/<id>.lean 2>&1',
      '5. If errors: fix up to 10 rounds (grep Mathlib4, edit, recompile)',
      '',
      'REPORT — Write result JSON:',
      'cat > ' + RESULT_DIR + '/result_' + idx + '.json << \'EOF\'',
      '{"index":' + idx + ',"concept_id":"<id>","status":"success|partial|failed","rounds":N,"errors":""}',
      'EOF'
    ].join('\n'), { label: 'fix-' + idx, phase: 'Fix' })
  }
})

var results = await parallel(tasks)
log('Group ' + GID + ': ' + results.filter(Boolean).length + '/' + INDICES.length + ' attempted')
return { group: GID, attempted: results.filter(Boolean).length }
