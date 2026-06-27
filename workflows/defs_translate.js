export const meta = {
  name: 'defs-translate',
  description: 'Translate definitions only: grep Mathlib4 → write def/class/structure + example. NO compilation.',
  phases: [{ title: 'Translate', detail: 'Each agent translates one definition to Lean 4 def/class/structure' }]
}

var INDICES = args.indices
var INPUT = '/home/a123/文档/mathpkg/pipeline_output/191_definitions.json'
var LEAN_PROJ = '/home/a123/文档/mathpkg/lean/MathPkg'
var DONE_DIR = '/home/a123/文档/mathpkg/pipeline_output/def_done'
var GID = args.group || 1
var MAX_RETRIES = 5

phase('Translate')

function translatePrompt(idx) {
  var df = DONE_DIR + '/done_' + idx + '.json'
  return [
    '=== DEFINITION TRANSLATOR ===',
    'Translate ONE mathematical definition to Lean 4. No proofs needed.',
    '',
    'STEP 0: Skip if already done. python3 -c "import os; print(os.path.exists(\'' + df + '\'))" . If True -> exit.',
    '',
    'Read concept: python3 -c "import json; d=json.load(open(\'' + INPUT + '\')); c=d[' + idx + ']; print(\'ID:\',c[\'id\']); print(\'NAME:\',c[\'name\']); print(\'STATEMENT:\',c[\'statement\']); print(\'DEPS:\',c.get(\'depends_on\',[]))"',
    '',
    'STEPS:',
    '1. grep ~/lean-demo/.lake/packages/mathlib/Mathlib/ -r "keyword" --include="*.lean" -l | head -10',
    '   Find if Mathlib4 already has this definition. If yes, use it directly.',
    '',
    '2. Write .lean file to ' + LEAN_PROJ + '/MathPkg/Pipeline/<concept_id>.lean:',
    '   - import Mathlib',
    '   - Write ONE of: def / class / structure / abbrev',
    '   - Add an "example" showing the definition in use',
    '   - Add docstring (/- ... -/) explaining the definition',
    '   - NO theorem proofs needed — this is a DEFINITION only',
    '',
    '3. Write completion marker:',
    '   python3 -c "import json,os; os.makedirs(\'' + DONE_DIR + '\',exist_ok=True); json.dump({\"idx\":' + idx + ',\"status\":\"ok\"},open(\'' + DONE_DIR + '/done_' + idx + '.json\',\'w\')); print(\'DONE\')"',
    '',
    'CRITICAL: ONLY write def/class/structure, no theorems. Use Mathlib4 existing defs when available.'
  ].join('\n')
}

var tasks = INDICES.map(function(idx) {
  return async function() {
    var df = DONE_DIR + '/done_' + idx + '.json'

    for (var attempt = 0; attempt < MAX_RETRIES; attempt++) {
      try {
        await agent(translatePrompt(idx), { label: 'def-' + idx, phase: 'Translate' })
      } catch (e) {}

      try {
        var r = await agent('python3 -c "import os; print(os.path.exists(\"' + df + '\"))"', { label: 'ck-' + idx, phase: 'Translate' })
        if (r !== null && r.indexOf('True') >= 0) {
          log('DONE def-' + idx)
          return { index: idx, status: 'done' }
        }
      } catch (e) {}

      log('RETRY def-' + idx + ' (' + (attempt+1) + '/' + MAX_RETRIES + ')')
    }
    return { index: idx, status: 'exhausted' }
  }
})

var results = await parallel(tasks)
var done = results.filter(function(r) { return r && r.status === 'done' }).length
var exhausted = results.filter(function(r) { return r && r.status === 'exhausted' }).length
log('Group ' + GID + ': ' + done + ' done, ' + exhausted + ' exhausted')
return { group: GID, done: done, exhausted: exhausted }
