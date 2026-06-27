---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

An acceptable map is a structure-preserving map between two acceptable triples. It must be a medium $M$-map (a homomorphism with respect to the Silver machine operations), preserve $\alpha \leq \alpha'$, and act as the identity on ordinals below $\alpha$. These maps serve as the connecting morphisms in $\kappa$-direct limit systems used throughout Silver's theory.
IEOF
echo "acceptable-map ok"

# === elementary-equivalence-transitive-sets ===
cat > "$BASE/elementary-equivalence-transitive-sets/concept.yaml" << 'YEOF'
id: elementary-equivalence-transitive-sets
title_en: "Elementary Equivalence of Transitive Sets"
title_zh: ""
type: definition
domain: foundations
subdomain: set-theory
difficulty: intermediate
tags: [elementary-equivalence, transitive-sets, model-theory]
depends_on: {required:[], recommended:[], suggested:[]}
source_books:
  - book_id: gtm001
    author: "Gaisi Takeuti, Wilson M. Zaring"
    title: "Introduction to Axiomatic Set Theory"
    chapter: "17"
    section: "17.1"
    pages: ""
    role_in_book: "Defines when two transitive sets satisfy the same sentences"
content_hash: ""
extraction_date: "2026-06-27"
extraction_agent: "v8-full-extract"
