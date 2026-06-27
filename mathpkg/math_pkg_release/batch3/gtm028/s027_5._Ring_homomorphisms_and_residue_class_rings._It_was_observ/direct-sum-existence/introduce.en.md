---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Given any finite collection of modules over a ring, one can construct a new module that decomposes as a direct sum of submodules isomorphic to the given ones. This construction -- the external direct sum -- is essentially unique and provides a way to build larger modules from smaller components. The proof uses the Cartesian product with componentwise operations.
ENDOFFILE

cat > "$BASE/direct-sum-existence/proof_gtm028_III_12.en.md" << 'EOF'
---
role: proof
locale: en
of_concept: direct-sum-existence
source_book: gtm028
source_chapter: "III"
source_section: "12"
---

Define $M$ as the Cartesian product $M'_1 \times \cdots \times M'_r$ with componentwise addition and scalar multiplication: $(x_1, \cdots, x_r) + (y_1, \cdots, y_r) = (x_1 + y_1, \cdots, x_r + y_r)$, and $a(x_1, \cdots, x_r) = (ax_1, \cdots, ax_r)$ for $a \in R$. This makes $M$ an $R$-module.

For each $i$, define $M_i$ as the set of tuples with zero entries except possibly at position $i$. Then $M_i \cong M'_i$ via the natural projection/inclusion. Every element of $M$ has a unique representation as a sum of elements from the $M_i$, so $M = M_1 \oplus \cdots \oplus M_r$.

For uniqueness: if $N = N_1 \oplus \cdots \oplus N_r$ with $N_i \cong M'_i$, then the isomorphism on each summand extends uniquely to an isomorphism $M \cong N$ by Theorem 24 (the universal property of direct sums).
