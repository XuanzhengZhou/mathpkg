export const meta = {
  name: 'skel-fix',
  description: 'Fix skeleton type signatures: checker_skel.py compiles, fixer rewrites type signature only',
  phases: [{ title: 'Fix', detail: 'Checker compiles skeleton, fixer fixes TYPE SIGNATURE only (proof = sorry)' }]
}

var INDICES = args.indices
var INPUT = '/home/a123/文档/mathpkg/pipeline_output/dedup/canonical_with_distance.json'
var LEAN_PROJ = '/home/a123/文档/mathpkg/lean/MathPkg'
var DONE_DIR = '/home/a123/文档/mathpkg/pipeline_output/skel_done'
var CHECKER = '/home/a123/文档/mathpkg/pipeline_output/checker_skel.py'
var GID = args.group || 1
var MAX_RETRIES = 8

phase('Fix')

function fixerPrompt(idx) {
  var ff = DONE_DIR + '/fail_' + idx + '.json'
  return [
    '=== FIX SKELETON TYPE SIGNATURE ===',
    'Read concept: python3 -c "import json; d=json.load(open(\"' + INPUT + '\")); all=[c for c in d if c.get(\"mathlib4_distance\")==1]; c=all[' + idx + ']; print(\"ID:\",c[\"id\"]); print(\"TYPE:\",c[\"type\"]); print(\"STATEMENT:\",c[\"statement\"]); print(\"DEPS:\",c.get(\"depends_on\",[]))"',
    'Read errors: python3 -c "import json; f=json.load(open(\"' + ff + '\")); print(\"ERRORS:\"); [print(e) for e in f[\"errors\"]]"',
    '',
    'Fix the skeleton at ' + LEAN_PROJ + '/MathPkg/Skeleton/<id>.lean:',
    '1. grep ~/lean-demo/.lake/packages/mathlib/Mathlib/ -r "keyword" --include="*.lean" -l | head -10',
    '2. Fix the TYPE SIGNATURE only. The proof stays as "by sorry".',
    '3. Format MUST be:',
    '   import Mathlib',
    '   /- docstring -/',
    '   theorem/def/lemma <name> <correct_type> := by',
    '     sorry',
    '4. cd ' + LEAN_PROJ + ' && export PATH="$HOME/.elan/bin:$PATH" && lake env lean MathPkg/Skeleton/<id>.lean 2>&1',
    '5. Fix errors, recompile. Max 10 rounds.',
    'CRITICAL: Only fix the TYPE SIGNATURE. Keep ":= by\\n  sorry". NO proof body.'
  ].join('\n')
}

var tasks = INDICES.map(function(idx) {
  return async function() {
    var df = DONE_DIR + '/done_' + idx + '.json'
    var ff = DONE_DIR + '/fail_' + idx + '.json'

    for (var attempt = 0; attempt < MAX_RETRIES; attempt++) {
      // CHECKER
      try { await agent('python3 ' + CHECKER + ' ' + idx, { label: 'chk-' + idx, phase: 'Fix' }) } catch (e) {}

      var doneExists = false
      try { var r = await agent('python3 -c "import os; print(os.path.exists(\"' + df + '\"))"', { label: 'dck-' + idx, phase: 'Fix' }); doneExists = r !== null && r.indexOf('True') >= 0 } catch (e) {}
      if (doneExists) { log('DONE skel-' + idx); return { index: idx, status: 'done', attempts: attempt+1 } }

      var failExists = false
      try { var r2 = await agent('python3 -c "import os; print(os.path.exists(\"' + ff + '\"))"', { label: 'fck-' + idx, phase: 'Fix' }); failExists = r2 !== null && r2.indexOf('True') >= 0 } catch (e) {}

      if (failExists) {
        log('FIX skel-' + idx + ' (' + (attempt+1) + ')')
        try { await agent(fixerPrompt(idx), { label: 'fix-' + idx, phase: 'Fix' }) } catch (e) {}
        try { await agent('rm -f ' + ff, { label: 'rmf-' + idx, phase: 'Fix' }) } catch (e) {}
      }
      if (!doneExists && !failExists) log('NO MARKER skel-' + idx + ', retry ' + (attempt+1))
    }
    log('EXHAUSTED skel-' + idx)
    return { index: idx, status: 'exhausted' }
  }
})

var results = await parallel(tasks)
var done = results.filter(function(r) { return r && r.status === 'done' }).length
log('Skel fix G' + GID + ': ' + done + '/' + INDICES.length)
return { group: GID, done: done }
