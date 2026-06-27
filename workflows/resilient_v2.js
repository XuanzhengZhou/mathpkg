export const meta = {
  name: 'resilient-fix-v2',
  description: '.done marker file as completion proof. Retry loop checks disk.',
  phases: [{ title: 'Fix', detail: 'Agent writes .done file when compilation succeeds' }]
}

var INDICES = args.indices
var INPUT = '/home/a123/文档/mathpkg/pipeline_output/phase2_input_49.json'
var LEAN_PROJ = '/home/a123/文档/mathpkg/lean/MathPkg'
var DONE_DIR = '/home/a123/文档/mathpkg/pipeline_output/done_markers'
var GID = args.group || 1
var MAX_RETRIES = 8

phase('Fix')

function makePrompt(idx, attempt) {
  var df = DONE_DIR + '/done_' + idx + '.json'
  var parts = [
    '=== LEAN FIX AGENT (attempt ' + (attempt+1) + ') ===',
    '',
    'STEP 0: Check if already completed from a previous run.',
    'Run: python3 -c "import os; print(\"DONE:\", os.path.exists(\"' + df + '\"))"',
    'If DONE: True, the work is complete. No further action needed.',
    '',
    'STEP 1: Read concept data.',
    'Run: python3 -c "import json,os; d=json.load(open(\"' + INPUT + '\")); c=d[' + idx + ']; cid=c[\"id\"]; fp=\"' + LEAN_PROJ + '/MathPkg/Pipeline/\"+cid+\".lean\"; print(\"ID:\",cid); print(\"FILE_EXISTS:\",os.path.exists(fp)); print(\"STATEMENT:\",c[\"statement\"]); gf=c.get(\"gapfill_proof\",\"\"); print(\"GAPFILL:\",gf[:1500] if gf else \"(definition)\")"',
    '',
    'STEP 2: If FILE_EXISTS=True, compile it.',
    '  cd ' + LEAN_PROJ + ' && export PATH="$HOME/.elan/bin:$PATH"',
    '  lake env lean MathPkg/Pipeline/<id>.lean 2>&1',
    '  If NO errors -> go to STEP 5.',
    '  If errors: grep ~/lean-demo/.lake/packages/mathlib/Mathlib/ for correct theorem names.',
    '  Fix ALL errors by editing the file. Recompile. Repeat up to 10 rounds.',
    '',
    'STEP 3: If FILE_EXISTS=False, create it.',
    '  grep ~/lean-demo/.lake/packages/mathlib/Mathlib/ -r "keyword" --include="*.lean" -l | head -10',
    '  Write .lean file using import Mathlib.',
    '  For definitions: write def/class/structure + example.',
    '  For theorems: write full tactic proof using the gapfill proof as guide.',
    '  Use: apply, rcases, intro, refine, simp, rw, exact, have, calc.',
    '  NEVER use #check in compiled modules.',
    '  Compile and fix errors up to 10 rounds.',
    '',
    'STEP 4: Compile check.',
    '  cd ' + LEAN_PROJ + ' && export PATH="$HOME/.elan/bin:$PATH"',
    '  lake env lean MathPkg/Pipeline/<id>.lean 2>&1',
    '  Goal: exit code 0 AND no "error:" in output.',
    '',
    'STEP 5: Write completion marker (ONLY if compile succeeded).',
    '  python3 -c "import json,os; os.makedirs(\"' + DONE_DIR + '\",exist_ok=True); json.dump({\"idx\":' + idx + ',\"status\":\"ok\"}, open(\"' + df + '\",\"w\")); print(\"MARKER_WRITTEN\")"',
    '',
    'CRITICAL: Only write the marker AFTER compilation succeeds with zero errors.'
  ]
  return parts.join('\n')
}

var tasks = INDICES.map(function(idx) {
  return async function() {
    var df = DONE_DIR + '/done_' + idx + '.json'

    for (var attempt = 0; attempt < MAX_RETRIES; attempt++) {
      await agent(makePrompt(idx, attempt), { label: 'fix-' + idx, phase: 'Fix' })

      // Check .done marker on disk
      var checkCmd = 'python3 -c "import os; print(\"DONE:\", os.path.exists(\"' + df + '\"))"'
      var checkResult = await agent(checkCmd, { label: 'check-' + idx, phase: 'Fix' })

      if (checkResult !== null && checkResult.indexOf('DONE: True') >= 0) {
        log('DONE fix-' + idx + ' (attempt ' + (attempt+1) + ')')
        return { index: idx, status: 'done', attempts: attempt+1 }
      }
      log('RETRY fix-' + idx + ' (attempt ' + (attempt+1) + '/' + MAX_RETRIES + ')')
    }
    log('EXHAUSTED fix-' + idx)
    return { index: idx, status: 'exhausted', attempts: MAX_RETRIES }
  }
})

var results = await parallel(tasks)
var done = results.filter(function(r) { return r && r.status === 'done' }).length
var exhausted = results.filter(function(r) { return r && r.status === 'exhausted' }).length
log('Group ' + GID + ': ' + done + ' done, ' + exhausted + ' exhausted')
return { group: GID, done: done, exhausted: exhausted }
