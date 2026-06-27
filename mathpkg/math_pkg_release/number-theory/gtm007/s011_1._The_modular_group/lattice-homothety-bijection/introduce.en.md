---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Proposition 3 establishes a fundamental dictionary between the geometry of the modular group and the theory of lattices. The quotient $H/G$ parameterizes lattices in $\mathbf{C}$ up to scaling (homothety), which in turn correspond to isomorphism classes of elliptic curves over $\mathbf{C}$. This bijection is the geometric foundation for the study of modular forms: a modular function can be viewed as a function on lattices that depends only on the homothety class.
ENDOFFILE
echo "Done: lattice-homothety-bijection"

# --- lattice-series-convergence (Lemma 1) ---
cat > "$BASE/lattice-series-convergence/concept.yaml" << 'EOF'
id: "lattice-series-convergence"
title_en: "Convergence of Lattice Series"
title_zh: ""
type: lemma
domain: number-theory
subdomain: modular-forms
difficulty: basic
tags: [lattices, series-convergence, eisenstein-series]
depends_on: {required:[], recommended:[], suggested:[]}
source_books: [{book_id:"gtm007",author:"Jean-Pierre Serre",title:"A Course in Arithmetic",chapter:"VII",section:"2. Modular functions",pages:"",role_in_book:"Lemma 1: The number of lattice points with absolute value between n and n+1 is O(n), so the series Σ 1/|γ|^σ converges for σ > 2"}]
content_hash: ""
extraction_date: "2026-06-27"
extraction_agent: "v8-full-extract"
