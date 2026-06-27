import json, os

os.makedirs('/home/a123/文档/mathpkg/pipeline_output/def_reviews', exist_ok=True)

issues = (
    "1. MISSING FORMULA: Original definition states 'The size of the conjugacy class of x is |G : C_G(x)|' "
    "(orbit-stabilizer applied to conjugacy action). No lemma, theorem, or example captures this. "
    "The dependency 'orbit-stabilizer theorem' is listed in DEPS but never used. "
    "2. NO EXPLICIT CENTRALIZER DEFINITION: Original defines C_G(x) = {g in G | gx = xg}. "
    "Lean file only references Subgroup.centralizer in an example (line 143), never defines it as a concept. "
    "3. Line 48: variable (G : Type*) shadows the section variable from line 32. Redundant binder. "
    "4. Line 81 example is trivially rfl; does not actually demonstrate that conjugacy class of identity is a singleton."
)

suggested_fix = (
    "1. Add a lemma/example using Mathlib orbit-stabilizer: "
    "`example [Fintype G] (x : G) : Fintype.card (orbit (ConjAct G) x) * "
    "Fintype.card (MulAction.stabilizer (ConjAct G) x) = Fintype.card G := by "
    "simpa using card_orbit_mul_card_stabilizer_eq_card_group (ConjAct G) x`. "
    "2. Add: `abbrev centralizer (x : G) : Subgroup G := Subgroup.centralizer {x}`. "
    "3. Remove the redundant (G : Type*) binder on line 48, or add a `'` suffix. "
    "4. Replace line 81-82 with: `example : (ConjClasses.mk (1 : G)).carrier = {1} := by "
    "simpa [Set.ext_iff] using fun g => by simp [ConjClasses.mem_carrier_mk, ConjClasses.mk_eq_mk_iff_isConj]`."
)

review = {
    "idx": 1,
    "concept_id": "conjugacy_classes_and_centralizers",
    "verdict": "MINOR",
    "checks": {
        "has_import": True,
        "correct_def_type": True,
        "matches_math": False,
        "mathlib4_correct": True,
        "has_helpful_docstring": True,
        "has_working_example": True,
        "syntax_looks_valid": True
    },
    "issues": issues,
    "suggested_fix": suggested_fix
}

with open('/home/a123/文档/mathpkg/pipeline_output/def_reviews/review_1.json', 'w') as f:
    json.dump(review, f, indent=2)

print("REVIEWED")
