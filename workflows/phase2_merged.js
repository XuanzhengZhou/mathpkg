export const meta = {
  name: 'phase2-translate-compile-heal',
  description: 'Phase 2 (merged): grep Mathlib4 → translate → compile → self-heal (10 rounds). 49 concepts.',
  phases: [
    { title: 'Translate+Compile+Heal', detail: '49 agents: read concept+gapfill, grep Mathlib4, write .lean, compile, self-heal up to 10 rounds' }
  ]
}

var INPUT = '/home/a123/文档/mathpkg/pipeline_output/phase2_input_49.json'
var LEAN_PROJ = '/home/a123/文档/mathpkg/lean/MathPkg'
var TOTAL = 49

phase('Translate+Compile+Heal')

var tasks = Array.from({length: TOTAL}, function(_, idx) {
  return function() {
    return agent([
      '=== PHASE 2: Lean 4 Translation + Compilation + Self-Heal ===',
      '',
      'Read concept #' + idx + ':',
      'python3 -c "import json; d=json.load(open(\'' + INPUT + '\')); c=d[' + idx + ']; print(\'ID:\',c[\'id\']); print(\'NAME:\',c[\'name\']); print(\'TYPE:\',c[\'type\']); print(\'STATEMENT:\',c[\'statement\']); print(\'DEPS:\',c[\'depends_on\']); print(\'MATHLIB4_HINT:\',c[\'mathlib4_path\']); print(\'GAPFILL_PROOF:\',c[\'gapfill_proof\'][:2000] if c[\'gapfill_proof\'] else \'(definition — write def/class/structure)\')"',
      '',
      '=== STEP 1: grep Mathlib4 for existing theorems (DO FIRST) ===',
      'Search ~/lean-demo/.lake/packages/mathlib/Mathlib/ for relevant theorems.',
      'Try: exact name, PascalCase, camelCase, snake_case, alphanumeric-only variants.',
      'Record EXACT module paths and theorem names.',
      '',
      '=== STEP 2: Write Lean 4 code ===',
      'File: ' + LEAN_PROJ + '/MathPkg/Pipeline/<concept_id>.lean',
      '- Start with: import Mathlib',
      '- Definitions: write def/class/structure + an example showing it works',
      '- Theorems: write a full theorem with tactic proof (use gapfill proof for structure)',
      '- Tactics: apply, rcases, intro, refine, simp, rw, exact, have, calc',
      '- NEVER use #check — use example instead',
      '- Add typeclass args ([Fintype G], [Fact p.Prime], etc.) as needed',
      '',
      '=== STEP 3: Compile ===',
      'cd ' + LEAN_PROJ + ' && export PATH="$HOME/.elan/bin:$PATH" && lake env lean MathPkg/Pipeline/<concept_id>.lean 2>&1',
      '',
      '=== STEP 4: Self-heal (if compile fails, up to 10 rounds) ===',
      'For each error:',
      '- "Unknown constant X.Y" → grep Mathlib4 for correct name → fix',
      '- "failed to synthesize Fintype" → add [Fintype ...] argument',
      '- "Nat.card vs Fintype.card" → use simpa [Nat.card_eq_fintype_card]',
      '- Type mismatches → grep Mathlib4 to check theorem signature',
      '- Fix ALL errors, NOT just the first one',
      '- Recompile',
      'Stop when: exit code 0 AND no "error:" in output.',
      '',
      '=== QUALITY GATE: lake env lean MUST return exit code 0 ==='
    ].join('\n'), {
      label: 'p2-' + idx,
      phase: 'Translate+Compile+Heal',
      schema: {
        type: 'object',
        properties: {
          concept_id: { type: 'string' },
          status: { type: 'string', enum: ['success', 'partial', 'failed'] },
          rounds: { type: 'integer' },
          lean_file: { type: 'string' },
          errors_remaining: { type: 'string' },
          mathlib4_theorems: { type: 'string' }
        },
        required: ['concept_id', 'status', 'rounds', 'lean_file']
      }
    })
  }
})

var results = await parallel(tasks)
var ok = results.filter(function(r) { return r && r.status === 'success' }).length
var partial = results.filter(function(r) { return r && r.status === 'partial' }).length
var fail = results.filter(function(r) { return r && r.status === 'failed' }).length
var total = results.filter(Boolean).length

log('Phase 2: ' + ok + ' success, ' + partial + ' partial, ' + fail + ' failed (' + total + '/' + TOTAL + ')')
return { success: ok, partial: partial, failed: fail, total: total, results: results.filter(Boolean) }
