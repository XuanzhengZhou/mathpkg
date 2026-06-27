---
role: proof
locale: en
of_concept: dense-functor-characterization
source_book: gtm005
source_chapter: "X"
source_section: "6"
---

$K: A \to C$ is dense iff the "nerve" functor $N_K: C \to \mathbf{Set}^{A^{\mathrm{op}}}$ defined by $N_K(c)(a) = C(K(a), c)$ is fully faithful.

Proof: Density means $\operatorname{Ran}_K K \cong 1_C$, which is the statement that for all $c, c' \in C$,
$$C(c, c') \cong \operatorname{Nat}_{A^{\mathrm{op}}}(C(K(-), c), C(K(-), c')).$$
But the right-hand side is precisely $\operatorname{Hom}_{\mathbf{Set}^{A^{\mathrm{op}}}}(N_K(c), N_K(c'))$, and the map $c \mapsto N_K(c)$ induces a function $C(c, c') \to \operatorname{Nat}(N_K(c), N_K(c'))$ by composition. This is a bijection iff $N_K$ is fully faithful.

Thus $K$ is dense iff $N_K$ is fully faithful, meaning $C$ embeds as a full subcategory of the presheaf category via $N_K$.
