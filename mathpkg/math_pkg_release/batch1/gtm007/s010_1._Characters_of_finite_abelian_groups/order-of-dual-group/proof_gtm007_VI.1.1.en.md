---
role: proof
locale: en
of_concept: order-of-dual-group
source_book: gtm007
source_chapter: "VI"
source_section: "§1.1"
---

One uses induction on the order $n$ of $G$, the case $n = 1$ being trivial. If $n \geq 2$, choose a nontrivial cyclic subgroup $H$ of $G$. By the remark after Proposition 1, the restriction homomorphism $\rho: \widehat{G} \to \widehat{H}$ is surjective with kernel isomorphic to $\widehat{G/H}$. Hence we have the exact sequence
$$\{1\} \to \widehat{G/H} \to \widehat{G} \to \widehat{H} \to \{1\},$$
and the order of $\widehat{G}$ is the product of the orders of $\widehat{H}$ and $\widehat{G/H}$.

But the order of $H$ (resp. $G/H$) is equal to that of its dual, because $H$ is cyclic (resp. because $G/H$ is of order strictly smaller than $n$, so the induction hypothesis applies). We conclude that the order of $\widehat{G}$ equals the product of the orders of $H$ and $G/H$, hence equals the order of $G$.
