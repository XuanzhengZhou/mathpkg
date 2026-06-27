export const meta = {
  name: 'resilient-fix-v3',
  description: 'try-catch around agent() to catch API errors inside retry loop',
  phases: [{ title: 'Fix', detail: 'API errors caught by try-catch, retry continues until .done file exists' }]
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
  return [
    '=== LEAN FIX AGENT (attempt ' + (attempt+1) + ') ===',
    '',
    'STEP 0: Check if already done.',
    'python3 -c "import os; print(\"DONE:\", os.path.exists(\"' + df + '\"))"',
    'If DONE: True -> task complete, no action needed.',
    '',
    'STEP 1: Read concept.',
    'python3 -c "import json,os; d=json.load(open(\"' + INPUT + '\")); c=d[' + idx + ']; cid=c[\"id\"]; fp=\"' + LEAN_PROJ + '/MathPkg/Pipeline/\"+cid+\".lean\"; print(\"ID:\",cid); print(\"FILE_EXISTS:\",os.path.exists(fp)); print(\"STATEMENT:\",c[\"statement\"]); gf=c.get(\"gapfill_proof\",\"\"); print(\"GAPFILL:\",gf[:1500] if gf else \"(def)\")"',
    '',
    'STEP 2: If FILE_EXISTS=True -> compile + fix.',
    '  cd ' + LEAN_PROJ + ' && export PATH="$HOME/.elan/bin:$PATH"',
    '  lake env lean MathPkg/Pipeline/<id>.lean 2>&1',
    '  Errors? grep ~/lean-demo/.lake/packages/mathlib/Mathlib/ -r "keyword" --include="*.lean" -l | head -10',
    '  Fix ALL errors, recompile, max 10 rounds.',
    '',
    'STEP 3: If FILE_EXISTS=False -> create file.',
    '  grep Mathlib4 for relevant theorems.',
    '  Write .lean (import Mathlib, tactics: apply/rcases/intro/refine/simp/rw/exact/have/calc).',
    '  NEVER #check. Add [Fintype] when needed.',
    '  Compile + fix up to 10 rounds.',
    '',
    'STEP 4: ONCE COMPILE SUCCEEDS (exit 0, no errors):',
    '  python3 -c "import json,os; os.makedirs(\"' + DONE_DIR + '\",exist_ok=True); json.dump({\"idx\":' + idx + ',\"status\":\"ok\"}, open(\"' + df + '\",\"w\")); print(\"MARKER_OK\")"',
    '',
    'CRITICAL: Only write marker AFTER lake env lean returns exit 0 with zero errors.'
  ].join('\n')
}

var tasks = INDICES.map(function(idx) {
  return async function() {
    var df = DONE_DIR + '/done_' + idx + '.json'

    for (var attempt = 0; attempt < MAX_RETRIES; attempt++) {
      // === TRY-CATCH: agent() may throw on API error ===
      try {
        await agent(makePrompt(idx, attempt), { label: 'fix-' + idx, phase: 'Fix' })
      } catch (e) {
        log('API ERROR fix-' + idx + ' attempt ' + (attempt+1) + ': ' + String(e).substring(0, 60))
      }

      // Check .done marker ON DISK (survives API errors)
      try {
        var checkResult = await agent(
          'python3 -c "import os; print(\"DONE:\", os.path.exists(\"' + df + '\"))"',
          { label: 'check-' + idx, phase: 'Fix' }
        )
        if (checkResult !== null && checkResult.indexOf('DONE: True') >= 0) {
          log('DONE fix-' + idx + ' (attempt ' + (attempt+1) + ')')
          return { index: idx, status: 'done', attempts: attempt+1 }
        }
      } catch (e2) {
        // check agent also failed, that's fine - retry main agent
      }

      log('RETRY fix-' + idx + ' (' + (attempt+1) + '/' + MAX_RETRIES + ')')
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
