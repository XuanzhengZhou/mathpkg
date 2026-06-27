#!/bin/bash
# Batch semantic rename of GTM042 bad-slug concepts
# Maps numbered theorem/lemma/prop/cor names to semantic slugs based on Serre's book

set -e
BASE="/home/a123/文档/mathpkg/pipeline_output/math_pkg_tmp/concepts_batch5/gtm042"
cd "$BASE"

# Mapping: bad_slug -> semantic_slug
declare -A MAP

# === THEOREMS ===
MAP[thm-theorem-1]="complete-reducibility"
MAP[thm-theorem-4]="character-orthogonality-theorem"
MAP[thm-theorem-5]="irreducibility-criterion"
MAP[thm-theorem-6]="orthonormal-basis-of-irreducible-characters"
MAP[thm-theorem-9]="abelian-group-irreducible-representations"
MAP[thm-theorem-11]="existence-of-induced-representation"
MAP[thm-theorem-14]="p-group-is-supersolvable"
MAP[thm-theorem-17]="artins-theorem"
MAP[thm-theorem-18]="brauer-characterization-theorem"
MAP[thm-theorem-21]="characterization-of-characters"
MAP[thm-theorem-22]="integrality-criterion-for-characters"
MAP[thm-theorem-29]="realization-over-cyclotomic-fields"
MAP[thm-theorem-32]="independence-of-decomposition-map"
MAP[thm-theorem-33]="surjectivity-of-decomposition-homomorphism"
MAP[thm-theorem-34]="injectivity-of-cde-homomorphism-e"
MAP[thm-theorem-35]="fong-swan-theorem"
MAP[thm-theorem-39]="generalized-brauer-theorem"
MAP[thm-theorem-40]="generalized-artin-theorem"
MAP[thm-theorem-41]="existence-of-normal-p-complement"
MAP[thm-theorem-42]="modular-characters-form-basis"
MAP[thm-theorem-43]="lifting-modular-characters"

# === PROPOSITIONS ===
MAP[prop-proposition-1]="character-properties"
MAP[prop-proposition-2]="character-of-direct-sum-and-tensor-product"
MAP[prop-proposition-5]="regular-representation-character"
MAP[prop-proposition-6]="class-function-homothety-on-irreducibles"
MAP[prop-proposition-7]="explicit-orthogonality-relations"
MAP[prop-proposition-9]="semisimplicity-of-group-algebra"
MAP[prop-proposition-15]="irreducible-characters-form-basis"
MAP[prop-proposition-16]="integrality-of-central-idempotents"
MAP[prop-proposition-17]="degree-divides-center-index"
MAP[prop-proposition-18]="criterion-for-induced-representation"
MAP[prop-proposition-20]="properties-of-induced-class-function"
MAP[prop-proposition-21]="frobenius-reciprocity"
MAP[prop-proposition-23]="mackey-irreducibility-criterion"
MAP[prop-proposition-24]="clifford-theorem-restriction-to-normal-subgroup"
MAP[prop-proposition-27]="artins-theorem-on-induced-characters"
MAP[prop-proposition-31]="connectedness-of-spectrum"
MAP[prop-proposition-32]="schur-indices-and-representations-over-k"
MAP[prop-proposition-33]="realizability-criterion-over-subfield"
MAP[prop-proposition-34]="finite-index-of-character-ring"
MAP[prop-proposition-40]="projective-modules-basis-of-r_l_g"
MAP[prop-proposition-41]="projective-envelope"
MAP[prop-proposition-43]="group-algebra-semisimple-over-field-of-char-p"
MAP[prop-proposition-45]="condition-for-lifting-idempotents"
MAP[prop-proposition-46]="cartan-invariants-and-decomposition-numbers"

# === LEMMAS ===
MAP[lemma-lemma-2]="character-of-orthogonal-representation"
MAP[lemma-lemma-3]="fixed-point-lemma-for-p-group"
MAP[lemma-lemma-6]="class-function-with-integer-values-by-g"
MAP[lemma-lemma-7]="integrality-of-character-values"
MAP[lemma-lemma-11]="brauer-lemma-on-p-regular-elements"
MAP[lemma-lemma-12]="decomposition-map-preserves-scalar-product"
MAP[lemma-lemma-13]="integrality-in-completion"
MAP[lemma-lemma-14]="finitely-many-prime-ideals-over-p"
MAP[lemma-lemma-15]="lifting-functions-constant-on-gamma-k-classes"
MAP[lemma-lemma-17]="lifting-brauer-characters-to-char-0"
MAP[lemma-lemma-20]="projective-lattice-characterization"
MAP[lemma-lemma-21]="projective-module-over-local-ring"

# === COROLLARIES ===
MAP[cor-corollary]="gamma-q-conjugacy-criterion"
MAP[cor-corollary-1]="extension-of-scalars-for-character-ring"
MAP[cor-corollary-2]="uniqueness-of-projective-lattice"
MAP[cor-corollary-3]="number-of-simple-kg-modules"

# Execute renames
renamed=0
skipped=0
for bad in "${!MAP[@]}"; do
    good="${MAP[$bad]}"
    if [ ! -d "$bad" ]; then
        echo "SKIP (no source): $bad"
        ((skipped++)) || true
        continue
    fi

    # Create target if needed
    mkdir -p "$good"

    # Copy all files from bad to good
    for f in "$bad"/*; do
        if [ -f "$f" ]; then
            basef=$(basename "$f")
            # Only copy if target doesn't already have this file
            if [ ! -f "$good/$basef" ]; then
                cp "$f" "$good/"
            fi
        fi
    done

    # Update id field in concept.yaml
    if [ -f "$good/concept.yaml" ]; then
        sed -i "s/^id:.*/id: $good/" "$good/concept.yaml"
    fi

    echo "DONE: $bad -> $good"
    ((renamed++)) || true
done

echo ""
echo "Renamed: $renamed, Skipped: $skipped"
