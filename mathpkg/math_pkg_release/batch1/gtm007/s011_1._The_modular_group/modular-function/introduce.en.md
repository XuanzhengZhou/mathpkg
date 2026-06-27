---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

A modular function is a weakly modular function that satisfies an additional growth condition at infinity. The change of variable $q = e^{2\pi i z}$ transforms the periodicity $f(z+1) = f(z)$ into a Laurent expansion in $q$, and meromorphicity at infinity means that this Laurent expansion has only finitely many negative powers of $q$. This condition is essential for the finite-dimensionality of spaces of modular forms and for the validity of the valence formula.
ENDOFFILE
echo "Done: modular-function"

# --- modular-form (Definition 4) ---
cat > "$BASE/modular-form/concept.yaml" << 'EOF'
id: "modular-form"
title_en: "Modular Form and Cusp Form"
title_zh: ""
type: definition
domain: number-theory
subdomain: modular-forms
difficulty: basic
tags: [modular-forms, cusp-forms, holomorphic]
depends_on: {required:[modular-function], recommended:[weakly-modular-characterization], suggested:[]}
source_books: [{book_id:"gtm007",author:"Jean-Pierre Serre",title:"A Course in Arithmetic",chapter:"VII",section:"2. Modular functions",pages:"",role_in_book:"Definition 4: A modular form of weight 2k is a modular function holomorphic on H and at infinity; a cusp form additionally vanishes at infinity"}]
content_hash: ""
extraction_date: "2026-06-27"
extraction_agent: "v8-full-extract"
