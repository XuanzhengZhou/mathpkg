---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Modular forms are among the most important objects in number theory, combining the symmetry of the modular group with holomorphicity conditions. A modular form of weight $2k$ is a holomorphic function on $H$ invariant under the weight-$2k$ action of $G$, with the additional requirement of holomorphicity at the cusp $\infty$. Cusp forms are modular forms whose constant term $a_0$ vanishes. The spaces $M_k$ and $M_k^0$ are finite-dimensional complex vector spaces, and their structure (dimensions, bases) is completely described by Theorem 4.
ENDOFFILE
echo "Done: modular-form"

# --- lattice-homothety-bijection (Proposition 3) ---
cat > "$BASE/lattice-homothety-bijection/concept.yaml" << 'EOF'
id: "lattice-homothety-bijection"
title_en: "Lattice-Homothety Bijection"
title_zh: ""
type: proposition
domain: number-theory
subdomain: modular-forms
difficulty: intermediate
tags: [lattices, homothety, modular-group, elliptic-curves]
depends_on: {required:[modular-group], recommended:[upper-half-plane], suggested:[]}
source_books: [{book_id:"gtm007",author:"Jean-Pierre Serre",title:"A Course in Arithmetic",chapter:"VII",section:"2. Modular functions",pages:"",role_in_book:"Proposition 3: The map (ω₁,ω₂) ↦ ω₁/ω₂ gives a bijection from R/C* (lattices up to homothety) onto H/G"}]
content_hash: ""
extraction_date: "2026-06-27"
extraction_agent: "v8-full-extract"
