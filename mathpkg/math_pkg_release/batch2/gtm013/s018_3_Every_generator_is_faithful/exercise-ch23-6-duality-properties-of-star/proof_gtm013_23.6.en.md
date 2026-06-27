---
role: proof
locale: en
of_concept: exercise-ch23-6-duality-properties-of-star
source_book: gtm013
source_chapter: "6"
source_section: "23. Exercises"
---
By (24.6.3), finitely generated modules are $U$-reflexive. The lattice anti-isomorphism of (24.5) interchanges finitely generated submodules with finitely cogenerated factor modules of the dual. Exactness follows from Corollary 24.2. Simplicity follows from the two-element submodule lattice characterization. Composition length equality follows from the lattice anti-isomorphism. The socle and radical relations follow from the annihilator correspondences in (24.5). Injectivity/projectivity duality follows from exactness of the Hom functor. Envelope/cover duality follows from the previous items. The generator/cogenerator duality follows from trace-reject duality. The annihilator identity and primitive idempotent formula follow from direct computation using the duality.
ENDOFFILE

echo "Done ch23-6"

# === exercise-ch23-7-duality-finite-length-injective-bimodule ===
mkdir -p "$BASE/exercise-ch23-7-duality-finite-length-injective-bimodule"

cat > "$BASE/exercise-ch23-7-duality-finite-length-injective-bimodule/concept.yaml" << 'EOF'
id: exercise-ch23-7-duality-finite-length-injective-bimodule
title_en: "Duality for Modules of Finite Length with Injective Bimodule"
title_zh: ""
type: proposition
domain: algebra
subdomain: module-theory
difficulty: advanced
tags: [duality, finite-length, injective-bimodule, hom-functor]
depends_on:
  required: [morita-duality, finite-length-module, injective-module]
  recommended: [u-dual]
  suggested: []
source_books:
  - book_id: gtm013
    author: "Frank W. Anderson, Kent R. Fuller"
    title: "Rings and Categories of Modules"
    chapter: "6"
    section: "23. Exercises"
    pages: ""
    role_in_book: "Exercise 23.7"
content_hash: ""
extraction_date: "2026-06-27"
extraction_agent: "v8-full-extract"
