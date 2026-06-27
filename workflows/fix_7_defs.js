export const meta = {
  name: 'fix-7-major-defs',
  description: 'Fix 7 MAJOR definitions using checker_defs.py + targeted fixer',
  phases: [{ title: 'Fix', detail: 'Checker compiles, fixer reads review + errors to fix' }]
}

var INDICES = [14, 30, 40, 43, 59, 64, 78]
var INPUT = '/home/a123/文档/mathpkg/pipeline_output/191_definitions.json'
var REVIEW_DIR = '/home/a123/文档/mathpkg/pipeline_output/def_reviews'
var LEAN_PROJ = '/home/a123/文档/mathpkg/lean/MathPkg'
var DONE_DIR = '/home/a123/文档/mathpkg/pipeline_output/def_done'
var CHECKER = '/home/a123/文档/mathpkg/pipeline_output/checker_defs.py'
var MAX_RETRIES = 8

phase('Fix')

function fixerPrompt(idx) {
  var ff = DONE_DIR + '/fail_' + idx + '.json'
  var rf = REVIEW_DIR + '/review_' + idx + '.json'
  return [
    '=== FIX MAJOR DEFINITION ===',
    'Read review: python3 -c "import json; r=json.load(open(\"' + rf + '\")); print(\"ISSUES:\",r.get(\"issues\",\"\")); print(\"SUGGESTED_FIX:\",r.get(\"suggested_fix\",\"\"))"',
    'Read concept: python3 -c "import json; d=json.load(open(\"' + INPUT + '\")); c=d[' + idx + ']; print(\"ID:\",c[\"id\"]); print(\"NAME:\",c[\"name\"]); print(\"STATEMENT:\",c[\"statement\"]); print(\"DEPS:\",c.get(\"depends_on\",[]))"',
    'Read fail info: python3 -c "import json; f=json.load(open(\"' + ff + '\")); print(\"ERRORS:\"); [print(e) for e in f[\"errors\"]]"',
    '',
    'Fix the .lean file at ' + LEAN_PROJ + '/MathPkg/Pipeline/<cid>.lean:',
    '1. grep ~/lean-demo/.lake/packages/mathlib/Mathlib/ -r "keyword" --include="*.lean" -l | head -10',
    '2. Fix ALL issues from the review AND compilation errors',
    '3. NO fabricated Mathlib4 lemma names — verify every name with grep',
    '4. cd ' + LEAN_PROJ + ' && export PATH="$HOME/.elan/bin:$PATH" && lake env lean MathPkg/Pipeline/<cid>.lean 2>&1',
    '5. Repeat fix+compile until exit 0 and no errors. Max 10 rounds.'
  ].join('\n')
}

var tasks = INDICES.map(function(idx) {
  return async function() {
    var df = DONE_DIR + '/done_' + idx + '.json'
    var ff = DONE_DIR + '/fail_' + idx + '.json'

    for (var attempt = 0; attempt < MAX_RETRIES; attempt++) {
      // CHECKER
      try { await agent('python3 ' + CHECKER + ' ' + idx, { label: 'chk-' + idx, phase: 'Fix' }) } catch (e) {}

      // Check .done
      var doneExists = false
      try { var r = await agent('python3 -c "import os; print(os.path.exists(\"' + df + '\"))"', { label: 'dck-' + idx, phase: 'Fix' }); doneExists = r !== null && r.indexOf('True') >= 0 } catch (e) {}
      if (doneExists) { log('DONE fix-' + idx); return { index: idx, status: 'done', attempts: attempt+1 } }

      // Check .fail
      var failExists = false
      try { var r2 = await agent('python3 -c "import os; print(os.path.exists(\"' + ff + '\"))"', { label: 'fck-' + idx, phase: 'Fix' }); failExists = r2 !== null && r2.indexOf('True') >= 0 } catch (e) {}

      if (failExists) {
        log('FIXING def-' + idx + ' (attempt ' + (attempt+1) + ')')
        try { await agent(fixerPrompt(idx), { label: 'fix-' + idx, phase: 'Fix' }) } catch (e) {}
        try { await agent('rm -f ' + ff, { label: 'rmf-' + idx, phase: 'Fix' }) } catch (e) {}
      }

      if (!doneExists && !failExists) log('NO MARKER def-' + idx + ', retry ' + (attempt+1))
    }
    log('EXHAUSTED def-' + idx)
    return { index: idx, status: 'exhausted' }
  }
})

var results = await parallel(tasks)
var done = results.filter(function(r) { return r && r.status === 'done' }).length
log('Defs fix: ' + done + '/' + INDICES.length + ' done')
return { done: done, total: INDICES.length }
