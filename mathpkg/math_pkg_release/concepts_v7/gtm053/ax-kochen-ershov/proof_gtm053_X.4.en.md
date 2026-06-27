---
role: proof
locale: en
of_concept: ax-kochen-ershov
source_book: gtm053
source_chapter: "X"
source_section: "4"
---

# Proof of the Ax-Kochen-Ershov Theorem

**Theorem 4.13 (J. Ax-S. Kochen, Yu. Ershov, A. Macintyre).** The theory $T\mathbb{Q}_p$ (the complete theory of the $p$-adic numbers $\mathbb{Q}_p$ in the language of valued fields) is complete, decidable, and admits elimination of quantifiers in the language $L_{\mathrm{valf}}^{\mathrm{Mac}}$ (the language of valued fields extended by unary predicates $P_n$, $n \geq 2$, where $P_n(x)$ means $\exists y (y^n = x)$, i.e., $x$ is an $n$-th power).

*Note.* The full proof of this theorem is not given in the source text (GTM053). As stated by the author: "We do not give a proof of the theorem here. The model-theoretic methods of known proofs are essentially the same as above but the algebra is much more involved."

The first proofs of completeness and decidability were given by Ax and Kochen in 1965, with Yu. Ershov independently proving completeness and decidability. Macintyre proved elimination of quantifiers in the present form (with the $P_n$ predicates) in 1976.

The proof strategy follows the same pattern as for $\mathrm{ACF}_p$ and $\mathrm{RCF}$: one proves that any two saturated models of the theory are isomorphic via a back-and-forth argument, using a suitable algebraic decomposition theorem (the Ax-Kochen-Ershov principle on the structure of henselian valued fields of residue characteristic $0$). The predicates $P_n$ play a role analogous to the ordering relation in $\mathrm{RCF}$ and the $n$-th power predicate $x \geq 0$ in the reals — they make the quantifier elimination statement more useful and powerful.

The first major consequence of this quantifier elimination was the manifestation of deep analogies between the theory of the reals and the theory of the $p$-adics, particularly regarding the description of definable sets and the rationality of Poincare series (as shown by Denef).
