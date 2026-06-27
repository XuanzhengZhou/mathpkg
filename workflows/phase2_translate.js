export const meta = {
  name: 'phase2-lean-translate',
  description: 'Phase 2: Translate gap-filled proofs + definitions to Lean 4, compile with lake env lean',
  phases: [
    { title: 'Translate', detail: 'grep Mathlib4, write .lean file, compile. Definition-only concepts skip gap-fill.' }
  ]
}

// Input files
var GAP_DIR = '/home/a123/文档/mathpkg/pipeline_output/gapfill_output'
var DEF_FILE = '/home/a123/文档/mathpkg/pipeline_output/p1_defonly.json'
var GAP_INPUT = '/home/a123/文档/mathpkg/pipeline_output/p1_gapfill.json'
var LEAN_PROJ = '/home/a123/文档/mathpkg/lean/MathPkg'

phase('Translate')

// Read concept data: for gap-filled concepts, combine with gap fill; for defs, use as-is
var prompt = [
  'You are a Lean 4 expert. Translate a mathematical concept to compilable Lean 4 code.',
  '',
  '## Input',
  'Read your assigned concept. The concept index is passed as args[0].',
  'If a gap fill file exists at ' + GAP_DIR + '/gap_<index>.json, read BOTH files.',
  '',
  '## Steps',
  '1. **Grep Mathlib4 first** (CRITICAL):',
  '   cd ~/lean-demo/.lake/packages/mathlib && grep -r "KEYWORD" Mathlib/ --include="*.lean" -l | head -10',
  '   Try variants: exact name, PascalCase, camelCase, snake_case.',
  '   Record the EXACT theorem names you will use.',
  '',
  '2. **Write Lean 4 code** to: ' + LEAN_PROJ + '/MathPkg/Pipeline/<concept_id>.lean',
  '   - Start with: import Mathlib',
  '   - For theorems: write "theorem <name> ... : ... := by" with a complete tactic proof',
  '   - For definitions: write "def", "class", "structure", or "abbrev" with an "example"',
  '   - Tactics: apply, rcases, intro, refine, simp, rw, exact, have, calc, ring, linarith',
  '   - NEVER use #check — use "example" instead',
  '   - Add [Fintype G] etc. when needed',
  '',
  '3. **Compile**:',
  '   cd ' + LEAN_PROJ + ' && export PATH="$HOME/.elan/bin:$PATH" && lake env lean MathPkg/Pipeline/<concept_id>.lean 2>&1',
  '',
  '4. **If compile fails**:',
  '   - READ all errors carefully',
  '   - For "Unknown constant X" → grep Mathlib4 for correct name → fix',
  '   - For "failed to synthesize Fintype" → add typeclass argument',
  '   - For type mismatches → check Mathlib4 theorem signature',
  '   - Fix ALL errors, recompile, repeat up to 10 rounds',
  '',
  '5. **Report result** using structured output.',
  '',
  'CRITICAL: Use "lake env lean", NOT "lake build", NOT bare "lean".',
  'CRITICAL: grep Mathlib4 BEFORE writing code.',
  'CRITICAL: Fix all errors each round, not just the first one.'
].join('\n')

// We handle two groups: gap-filled concepts and definition-only concepts
// Both follow the same Phase 2 process (translate + compile)

// For simplicity, process all 49 concepts. Each agent reads its own data.
var TOTAL = 49 // 21 gap-filled + 28 def-only

var tasks = Array.from({length: TOTAL}, function(_, i) {
  return function() {
    return agent(
      'Concept index: ' + i + '\n\n' +
      'First read your concept data:\n' +
      'python3 -c "\n' +
      'import json, os\n' +
      "gap_file = '" + GAP_DIR + "/gap_' + str(" + i + ") + '.json'\n" +
      "if os.path.exists(gap_file):\n" +
      '    g = json.load(open(gap_file))\n' +
      "    print(\"GAP_FILL_PROOF:\", g.get(\"expanded_proof\",\"\")[:3000])\n" +
      "if " + i + " < 21:\n" +
      "    data = json.load(open('" + GAP_INPUT + "'))\n" +
      "    c = data[" + i + "]\n" +
      "else:\n" +
      "    data = json.load(open('" + DEF_FILE + "'))\n" +
      "    c = data[" + i + " - 21]\n" +
      'print("ID:", c["id"])\n' +
      'print("NAME:", c["name"])\n' +
      'print("TYPE:", c["type"])\n' +
      'print("STATEMENT:", c["statement"])\n' +
      'print("DEPENDS_ON:", c.get("depends_on",[]))\n' +
      'print("PROOF_SKETCH:", c.get("proof_sketch","")[:1000])\n' +
      'print("MATHLIB4_PATH:", c.get("mathlib4_path",""))\n' +
      'print("CONCEPT_ID:", c["id"])\n' +
      '"\n\n' +
      prompt + '\n\n' +
      'Use CONCEPT_ID from the output above as your <concept_id> in file paths.',
      {
        label: 'translate-' + i,
        phase: 'Translate',
        schema: {
          type: 'object',
          properties: {
            concept_id: { type: 'string' },
            concept_name: { type: 'string' },
            status: { type: 'string', enum: ['success', 'partial', 'failed'] },
            rounds: { type: 'integer' },
            final_errors: { type: 'string' },
            lean_file_path: { type: 'string' },
            mathlib4_theorems_used: { type: 'string' },
            notes: { type: 'string' }
          },
          required: ['concept_id', 'status', 'rounds', 'lean_file_path']
        }
      }
    )
  }
})

var results = await parallel(tasks)
var succeeded = results.filter(function(r) { return r && r.status === 'success' }).length
var partial = results.filter(function(r) { return r && r.status === 'partial' }).length
var failed = results.filter(function(r) { return r && r.status === 'failed' }).length

log('Phase 2 complete: ' + succeeded + ' success, ' + partial + ' partial, ' + failed + ' failed')

return {
  succeeded: succeeded, partial: partial, failed: failed,
  total: results.filter(Boolean).length,
  results: results.filter(Boolean)
}
