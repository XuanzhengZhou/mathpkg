export const meta = {
  name: 'lean-translate-batch-01',
  description: 'Batch 1: 50 distance=1 concepts to Lean 4 with self-heal',
  phases: [
    { title: 'Translate + Compile + Fix', detail: '50 agents parallel: gap-fill, Lean 4, compile, self-heal up to 10 rounds' }
  ]
}

var CONCEPT_IDS = [
  "indecomposable_group", "dedekind_domain", "roths_theorem", "syzygy_module",
  "ramification_degree_at_a_point", "hilbert_basis_theorem", "noetherian_ring_and_polynomial_ring",
  "hilbert_function_and_polynomial", "regular_local_ring_equivalent_definitions",
  "faithfully_flat_ring_extension", "integral_closure_in_a_finite_separable_extension",
  "complete_intersection_ideal", "krull_principal_ideal_theorem",
  "determination_of_f_automorphisms_by_generators", "primitive_element_theorem",
  "artin_schreier_theorem", "non_archimedean_absolute_value_valuation",
  "ostrowskis_theorem_on_absolute_values_of_q", "quadratic_forms_over_finite_fields_witts_theorem",
  "indecomposable_module", "indecomposable_decomposition_of_noetherian_modules",
  "fn_noetherian", "morphisms_of_affine_algebraic_sets", "krull_dimension",
  "flatness_criterion_via_relation", "faithfully_flat_descent", "associated_primes",
  "primary_decomposition_lichendroth", "cohen_macaulay_ring", "gorenstein_ring",
  "initial_forms_and_the_initial_ideal", "regular_sequence_and_koszul_complex",
  "depth_and_cohen_macaulay_modules", "local_cohomology_functor",
  "cech_cohomology_and_local_cohomology", "dualizing_complex", "injective_hull",
  "matlis_duality", "canonical_module", "auslander_buchsbaum_formula_theorem",
  "bass_numbers_of_a_graded_module", "serre_condition_s2",
  "determinant_of_a_matrix_of_linear_forms_is_absolutely_irreducible",
  "galois_group_of_a_polynomial", "finite_fields_are_perfect",
  "galois_extensions_and_their_characterizations", "formal_definition_of_conductor",
  "definition_of_groebner_basis", "buchbergers_criterion_and_algorithm",
  "division_algorithm_in_polynomial_rings", "s_polynomials_and_groebner_bases"
]

var BATCH_DIR = '/home/a123/文档/mathpkg/pipeline_output/concepts_batch1'
var LEAN_PROJ = '/home/a123/文档/mathpkg/lean/MathPkg'

phase('Translate + Compile + Fix')

var tasks = CONCEPT_IDS.map(function(conceptId, i) {
  return function() {
    var prompt = [
      'You are translating a mathematical concept to Lean 4. Use Bash, Read, Write, Edit, and Grep tools.',
      '',
      'Concept ID: ' + conceptId,
      '',
      '## Step 0: Read concept data',
      'Run this command to see what you are translating:',
      '  python3 -c "import json; c=json.load(open(\'' + BATCH_DIR + '/' + conceptId + '.json\')); print(\'NAME:\', c[\'name\']); print(\'TYPE:\', c[\'type\']); print(\'DEPENDS_ON:\', c.get(\'depends_on\',[])); print(\'STATEMENT:\', c[\'statement\']); print(\'PROOF_SKETCH:\', c.get(\'proof_sketch\',\'No proof sketch\'))"',
      '',
      '## Step 1: Gap-filling (for theorems/lemmas/propositions ONLY)',
      'If the concept is a DEFINITION, skip to Step 2.',
      'If the proof sketch is brief or uses "clearly/obviously/it follows": expand into EXPLICIT numbered steps.',
      'Rules:',
      '- Each step references a specific theorem/lemma/axiom/definition',
      '- NEVER use "clearly", "obviously", "it follows that", "one can show"',
      '- Each step is ONE logical inference',
      '- End with the QED symbol',
      '',
      '## Step 2: Find Mathlib4 theorems (DO BEFORE writing Lean code)',
      'Grep the Mathlib4 source for the theorems you need:',
      '  cd ~/lean-demo/.lake/packages/mathlib && grep -r "KEYWORD" Mathlib/ --include="*.lean" -l | head -10',
      '  cd ~/lean-demo/.lake/packages/mathlib && grep -r "THEOREM_PATTERN" Mathlib/ --include="*.lean" -n | head -20',
      'Try variants: exact name, PascalCase, camelCase, snake_case, alphanumeric-only.',
      'Record the EXACT Mathlib4 theorem names.',
      '',
      '## Step 3: Write Lean 4 code',
      'File path: ' + LEAN_PROJ + '/MathPkg/Pipeline/' + conceptId + '.lean',
      'Rules:',
      '- Start with: import Mathlib',
      '- Use "open" for namespaces',
      '- Theorems: write "theorem" with complete proof using tactics',
      '- Definitions: write "def", "class", or "structure" plus an "example"',
      '- Tactics: apply, rcases, intro, refine, simp, rw, exact, have, calc, ring, linarith',
      '- NEVER use #check in compiled modules — use "example" instead',
      '- Add [Fintype G] typeclass when working with finite groups',
      '- Use Fintype.card not Nat.card for finite type cardinalities',
      '',
      '## Step 4: Compile',
      '  cd ' + LEAN_PROJ + ' && export PATH="$HOME/.elan/bin:$PATH" && lake env lean MathPkg/Pipeline/' + conceptId + '.lean 2>&1',
      '',
      '## Step 5: Self-heal loop (up to 10 rounds)',
      'If compilation fails:',
      '1. READ all error messages carefully',
      '2. For "Unknown constant X.Y" -> grep Mathlib4 for correct name, then fix',
      '3. For "failed to synthesize Fintype H" -> add [Fintype H] argument',
      '4. For "Nat.card vs Fintype.card" -> use "simpa [Nat.card_eq_fintype_card]"',
      '5. For type mismatches -> grep Mathlib4 to check theorem signature',
      '6. Edit the file to fix ALL errors (not just the first one)',
      '7. Recompile (go back to Step 4)',
      '8. Repeat until compilation SUCCEEDS (exit code 0, no errors) or 10 rounds exhausted',
      '',
      'CRITICAL:',
      '- Use "lake env lean", NOT "lake build" and NOT bare "lean"',
      '- lake env lean reuses 8175 cached Mathlib .olean files',
      '- grep Mathlib4 BEFORE writing code',
      '- Fix ALL errors each round',
      '',
      '## Step 6: Report',
      'After compilation succeeds or 10 rounds exhausted, report the final result using the structured output.'
    ].join('\n')

    return agent(prompt, {
      label: conceptId,
      phase: 'Translate + Compile + Fix',
      schema: {
        type: 'object',
        properties: {
          concept_id: { type: 'string' },
          concept_name: { type: 'string' },
          status: { type: 'string', enum: ['success', 'partial', 'failed'] },
          rounds: { type: 'integer' },
          final_errors: { type: 'string' },
          lean_file_path: { type: 'string' },
          notes: { type: 'string' }
        },
        required: ['concept_id', 'status', 'rounds', 'lean_file_path']
      }
    })
  }
})

var results = await parallel(tasks)

var succeeded = results.filter(function(r) { return r && r.status === 'success' }).length
var partial = results.filter(function(r) { return r && r.status === 'partial' }).length
var failed = results.filter(function(r) { return r && r.status === 'failed' }).length
var total = results.filter(Boolean).length

log('Batch 1 complete: ' + succeeded + ' success, ' + partial + ' partial, ' + failed + ' failed (' + total + ' total)')

return { succeeded: succeeded, partial: partial, failed: failed, total: total, results: results.filter(Boolean) }
