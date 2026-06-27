export const meta = {
  name: 'resilient-fix-v4',
  description: 'Checker calls external python3 script (no inline code). Fixer only runs on .fail.',
  phases: [{ title: 'Fix', detail: 'Checker: python3 checker.py <idx>. Fixer: only when .fail exists.' }]
}

var INDICES = args.indices
var INPUT = '/home/a123/文档/mathpkg/pipeline_output/phase2_input_49.json'
var LEAN_PROJ = '/home/a123/文档/mathpkg/lean/MathPkg'
var DONE_DIR = '/home/a123/文档/mathpkg/pipeline_output/done_markers'
var CHECKER = '/home/a123/文档/mathpkg/pipeline_output/checker.py'
var GID = args.group || 1
var MAX_RETRIES = 10

phase('Fix')

function fixerPrompt(idx, attempt) {
  var ff = DONE_DIR + '/fail_' + idx + '.json'
  return [
    '=== FIXER ===',
    'Read failure info: python3 -c "import json; f=json.load(open(\"' + ff + '\")); print(\"CID:\",f[\"cid\"]); print(\"ERRORS:\"); [print(e) for e in f[\"errors\"]]"',
    'Read concept: python3 -c "import json; d=json.load(open(\"' + INPUT + '\")); c=d[' + idx + ']; print(\"STATEMENT:\",c[\"statement\"]); gf=c.get(\"gapfill_proof\",\"\"); print(\"GAPFILL:\",gf[:1500] if gf else \"(def)\")"',
    'Fix the file at ' + LEAN_PROJ + '/MathPkg/Pipeline/<cid>.lean:',
    '1. grep ~/lean-demo/.lake/packages/mathlib/Mathlib/ -r "keyword" --include="*.lean" -l | head -10',
    '2. Edit file to fix ALL errors',
    '3. cd ' + LEAN_PROJ + ' && export PATH="$HOME/.elan/bin:$PATH" && lake env lean MathPkg/Pipeline/<cid>.lean 2>&1',
    '4. Still errors? grep, fix, recompile. Up to 10 rounds.',
    '5. If no file exists: grep Mathlib4, write new .lean, compile, fix.',
    'Use: apply, rcases, intro, refine, simp, rw, exact, have, calc. NEVER #check.'
  ].join('\n')
}

var tasks = INDICES.map(function(idx) {
  return async function() {
    var df = DONE_DIR + '/done_' + idx + '.json'
    var ff = DONE_DIR + '/fail_' + idx + '.json'

    for (var attempt = 0; attempt < MAX_RETRIES; attempt++) {
      // === CHECKER: one-line call to external script ===
      try {
        await agent('python3 ' + CHECKER + ' ' + idx, { label: 'check-' + idx, phase: 'Fix' })
      } catch (e) {
        // checker agent API error, retry
      }

      // Check .done on disk
      var doneExists = false
      try {
        var r = await agent('python3 -c "import os; print(os.path.exists(\"' + df + '\"))"', { label: 'dck-' + idx, phase: 'Fix' })
        doneExists = r !== null && r.indexOf('True') >= 0
      } catch (e) {}

      if (doneExists) {
        log('DONE fix-' + idx + ' (attempt ' + (attempt+1) + ')')
        return { index: idx, status: 'done', attempts: attempt+1 }
      }

      // Check .fail on disk
      var failExists = false
      try {
        var r2 = await agent('python3 -c "import os; print(os.path.exists(\"' + ff + '\"))"', { label: 'fck-' + idx, phase: 'Fix' })
        failExists = r2 !== null && r2.indexOf('True') >= 0
      } catch (e) {}

      if (failExists) {
        // === FIXER ===
        log('FIXING fix-' + idx + ' (attempt ' + (attempt+1) + ')')
        try {
          await agent(fixerPrompt(idx, attempt), { label: 'fix-' + idx, phase: 'Fix' })
        } catch (e) {
          // fixer API error, checker will re-evaluate next round
        }
        // Remove .fail so checker re-evaluates
        try { await agent('rm -f ' + ff, { label: 'rmf-' + idx, phase: 'Fix' }) } catch (e) {}
      }

      // If neither .done nor .fail: checker was interrupted mid-write. Retry.
      if (!doneExists && !failExists) {
        log('NO MARKER fix-' + idx + ', retry ' + (attempt+1) + '/' + MAX_RETRIES)
      }
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
