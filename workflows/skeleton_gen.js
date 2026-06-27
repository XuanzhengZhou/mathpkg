export const meta = {
  name: 'skeleton-gen',
  description: 'Generate Lean skeletons: translate statement to type signature only, sorry for proof',
  phases: [{ title: 'Skeleton', detail: 'Each agent translates ONE statement to Lean type signature with sorry' }]
}

var INDICES = args.indices
var INPUT = '/home/a123/文档/mathpkg/pipeline_output/need_skeleton_240.json'
var LEAN_PROJ = '/home/a123/文档/mathpkg/lean/MathPkg'
var DONE_DIR = '/home/a123/文档/mathpkg/pipeline_output/skel_done'
var GID = args.group || 1
var MAX_RETRIES = 5

phase('Skeleton')

function skelPrompt(idx) {
  var df = DONE_DIR + '/skel_' + idx + '.json'
  return [
    '=== SKELETON GENERATOR ===',
    'Translate ONE mathematical statement to a Lean 4 TYPE SIGNATURE only. NO PROOF.',
    '',
    'STEP 0: Skip if done.',
    'python3 -c "import os; print(os.path.exists(\"' + df + '\"))"',
    'If True -> exit.',
    '',
    'Read concept: python3 -c "import json; d=json.load(open(\"' + INPUT + '\")); c=d[' + idx + ']; print(\"ID:\",c[\"id\"]); print(\"TYPE:\",c[\"type\"]); print(\"STATEMENT:\",c[\"statement\"]); print(\"DEPS:\",c.get(\"depends_on\",[]))"',
    '',
    'Write skeleton to ' + LEAN_PROJ + '/MathPkg/Pipeline/<id>.lean:',
    '```lean',
    'import Mathlib',
    '',
    '/- <concept name> -/',
    '<theorem|def|lemma> <name> <type_signature> := by',
    '  sorry',
    '```',
    '',
    'RULES:',
    '- Translate ONLY the type signature, not the proof',
    '- Use Mathlib4 types: Nat, ZMod, Fintype, Group, Ring, Module, etc.',
    '- For theorems: write the full statement as a Lean proposition',
    '- For definitions: write def/class/structure with the defining properties',
    '- "by sorry" at the end — NO proof body at all',
    '- This MUST compile as a valid Lean type signature',
    '',
    'Write completion marker:',
    'python3 -c "import json,os; os.makedirs(\"' + DONE_DIR + '\",exist_ok=True); json.dump({\"idx\":' + idx + '},open(\"' + df + '\",\"w\")); print(\"DONE\")"'
  ].join('\n')
}

var tasks = INDICES.map(function(idx) {
  return async function() {
    var df = DONE_DIR + '/skel_' + idx + '.json'
    for (var attempt = 0; attempt < MAX_RETRIES; attempt++) {
      try { await agent(skelPrompt(idx), { label: 'skel-' + idx, phase: 'Skeleton' }) } catch (e) {}
      try {
        var r = await agent('python3 -c "import os; print(os.path.exists(\"' + df + '\"))"', { label: 'ck-' + idx, phase: 'Skeleton' })
        if (r !== null && r.indexOf('True') >= 0) return { index: idx, status: 'done' }
      } catch (e) {}
      log('RETRY skel-' + idx + ' (' + (attempt+1) + '/' + MAX_RETRIES + ')')
    }
    return { index: idx, status: 'exhausted' }
  }
})

var results = await parallel(tasks)
var done = results.filter(function(r) { return r && r.status === 'done' }).length
var exhausted = results.filter(function(r) { return r && r.status === 'exhausted' }).length
log('Group ' + GID + ': ' + done + ' done, ' + exhausted + ' exhausted')
return { group: GID, done: done, exhausted: exhausted }
