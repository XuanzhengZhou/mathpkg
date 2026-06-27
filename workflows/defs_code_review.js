export const meta = {
  name: 'defs-code-review',
  description: 'Code review 84 definitions: verify math correctness, Lean syntax, Mathlib4 refs, docstring quality',
  phases: [{ title: 'Review', detail: 'Each agent reviews one .lean file against original concept definition' }]
}

var INDICES = args.indices
var CONCEPTS = '/home/a123/文档/mathpkg/pipeline_output/191_definitions.json'
var LEAN_DIR = '/home/a123/文档/mathpkg/lean/MathPkg/MathPkg/Pipeline'
var REVIEW_DIR = '/home/a123/文档/mathpkg/pipeline_output/def_reviews'
var GID = args.group || 1
var MAX_RETRIES = 3

phase('Review')

function reviewPrompt(idx) {
  var rf = REVIEW_DIR + '/review_' + idx + '.json'
  return [
    '=== CODE REVIEW: Definition Translation ===',
    'Verify that the Lean 4 translation correctly captures the mathematical definition.',
    '',
    'STEP 0: Skip if already reviewed.',
    'python3 -c "import os; print(os.path.exists(\"' + rf + '\"))"',
    'If True -> do nothing, report complete.',
    '',
    'STEP 1: Read the original concept:',
    'python3 -c "import json; d=json.load(open(\"' + CONCEPTS + '\")); c=d[' + idx + ']; print(\"ID:\",c[\"id\"]); print(\"NAME:\",c[\"name\"]); print(\"STATEMENT:\",c[\"statement\"]); print(\"DEPS:\",c.get(\"depends_on\",[]))"',
    '',
    'STEP 2: Read the .lean file:',
    'Read ' + LEAN_DIR + '/<concept_id>.lean',
    '',
    'STEP 3: Review checklist (write JSON result to ' + rf + '):',
    '{',
    '  "idx": ' + idx + ',',
    '  "concept_id": "...",',
    '  "verdict": "PASS" | "MINOR" | "MAJOR",',
    '  "checks": {',
    '    "has_import": true/false,',
    '    "correct_def_type": true/false,        // def/class/structure/abbrev appropriate?',
    '    "matches_math": true/false,             // captures the mathematical meaning?',
    '    "mathlib4_correct": true/false,         // Mathlib4 references accurate?',
    '    "has_helpful_docstring": true/false,',
    '    "has_working_example": true/false,',
    '    "syntax_looks_valid": true/false',
    '  },',
    '  "issues": "list specific problems, or empty if PASS",',
    '  "suggested_fix": "what to change, or empty if PASS"',
    '}',
    '',
    'STEP 4: Write the review file:',
    'python3 -c "import json,os; os.makedirs(\"' + REVIEW_DIR + '\",exist_ok=True);',
    '  json.dump({...review data...}, open(\"' + rf + '\",\"w\")); print(\"REVIEWED\")"',
    '',
    'Grading: PASS=perfect, MINOR=small issues but usable, MAJOR=wrong definition needs rewrite'
  ].join('\n')
}

var tasks = INDICES.map(function(idx) {
  return async function() {
    var rf = REVIEW_DIR + '/review_' + idx + '.json'

    for (var attempt = 0; attempt < MAX_RETRIES; attempt++) {
      try {
        await agent(reviewPrompt(idx), { label: 'review-' + idx, phase: 'Review' })
      } catch (e) {}

      try {
        var r = await agent('python3 -c "import os; print(os.path.exists(\"' + rf + '\"))"', { label: 'ck-' + idx, phase: 'Review' })
        if (r !== null && r.indexOf('True') >= 0) {
          return { index: idx, status: 'reviewed' }
        }
      } catch (e) {}

      log('RETRY review-' + idx + ' (' + (attempt+1) + '/' + MAX_RETRIES + ')')
    }
    return { index: idx, status: 'exhausted' }
  }
})

var results = await parallel(tasks)
var done = results.filter(function(r) { return r && r.status === 'reviewed' }).length
log('Group ' + GID + ': ' + done + '/' + INDICES.length + ' reviewed')
return { group: GID, reviewed: done }
