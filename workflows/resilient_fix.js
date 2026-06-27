export const meta = {
  name: 'resilient-fix',
  description: 'Resilient fix with retry: agent() returns null on API error → retry up to 5 times',
  phases: [{ title: 'Fix', detail: 'Each agent retries on API error. Checks disk state to resume from breakpoint.' }]
}

var INDICES = args.indices
var INPUT = '/home/a123/文档/mathpkg/pipeline_output/phase2_input_49.json'
var LEAN_PROJ = '/home/a123/文档/mathpkg/lean/MathPkg'
var GID = args.group || 1
var MAX_RETRIES = 5

phase('Fix')

var tasks = INDICES.map(function(idx) {
  return async function() {
    for (var attempt = 0; attempt < MAX_RETRIES; attempt++) {
      var result = await agent([
        '=== RESILIENT LEAN FIX AGENT ===',
        'If API was interrupted before: check disk state and RESUME, do not restart from scratch.',
        '',
        'STEP 0 — Check disk state first:',
        'python3 -c "import json,os; d=json.load(open(\'' + INPUT + '\')); cid=d[' + idx + '][\'id\']; f=\'' + LEAN_PROJ + '/MathPkg/Pipeline/\'+cid+\'.lean\'; print(\'ID:\',cid); print(\'FILE_EXISTS:\',os.path.exists(f))"',
        '',
        'IF FILE EXISTS:',
        '  cd ' + LEAN_PROJ + ' && export PATH="$HOME/.elan/bin:$PATH" && lake env lean MathPkg/Pipeline/<id>.lean 2>&1',
        '  If NO errors → DONE. If errors → fix up to 10 rounds:',
        '  For each error: grep ~/lean-demo/.lake/packages/mathlib/Mathlib/ for correct names, edit file, recompile.',
        '  Fix ALL errors each round.',
        '',
        'IF FILE MISSING:',
        '  python3 -c "import json; d=json.load(open(\'' + INPUT + '\')); c=d[' + idx + ']; print(\'STATEMENT:\',c[\'statement\']); print(\'GAPFILL:\',c[\'gapfill_proof\'][:2000])"',
        '  grep Mathlib4 for relevant theorems.',
        '  Write .lean file. Compile. Fix errors up to 10 rounds.',
        '',
        'CRITICAL: use "lake env lean", NOT "lake build". grep Mathlib4 BEFORE writing code.',
        'Stop when: exit code 0 AND no "error:" in output, OR 10 rounds exhausted.'
      ].join('\n'), { label: 'fix-' + idx, phase: 'Fix' })

      if (result !== null) {
        log('✅ fix-' + idx + ' completed on attempt ' + (attempt+1))
        return { index: idx, status: 'done', attempts: attempt+1 }
      }
      log('⚠️ fix-' + idx + ' API error, retry ' + (attempt+1) + '/' + MAX_RETRIES)
    }
    log('❌ fix-' + idx + ' exhausted ' + MAX_RETRIES + ' retries')
    return { index: idx, status: 'exhausted', attempts: MAX_RETRIES }
  }
})

var results = await parallel(tasks)
var done = results.filter(function(r) { return r && r.status === 'done' }).length
var exhausted = results.filter(function(r) { return r && r.status === 'exhausted' }).length
log('Group ' + GID + ': ' + done + ' done, ' + exhausted + ' exhausted')
return { group: GID, done: done, exhausted: exhausted }
