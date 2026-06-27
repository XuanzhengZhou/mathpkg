---
role: proof
locale: en
of_concept: exponential-sequence
source_book: gtm052
source_chapter: "Appendix B"
source_section: "5"
---

Let us apply the exponential sequence to $X_h$, where $X$ is a projective variety over $\mathbf{C}$. By (III, Ex. 4.5), which is valid for any ringed space, we have $H^1(X_h, \mathcal{O}_{X_h}^*) \cong 	ext{Pic } X_h$. But Serre's theorem (2.1) also gives an equivalence of categories of coherent sheaves, so in particular, $	ext{Pic } X_h \cong 	ext{Pic } X$. So we can rewrite our sequence as

$$0 ightarrow H^1(X_h, \mathbf{Z}) ightarrow H^1(X, \mathcal{O}_X) ightarrow 	ext{Pic } X ightarrow H^2(X_h, \mathbf{Z}) ightarrow H^2(X, \mathcal{O}_X) ightarrow \dots.$$

The only nonalgebraic part is the integral cohomology of $X_h$. Since any algebraic variety is triangulable (see for example, Hironaka [5]), the cohomology groups $H^i(X_h, \mathbf{Z})$ are finitely generated abelian groups.

First of all, one sees easily that algebraically equivalent Cartier divisors give the same element in $H^2(X_h, \mathbf{Z})$. Therefore the Neron-Severi group of $X$ is a subgroup of $H^2(X_h, \mathbf{Z})$, and hence is finitely generated (V, Ex. 1.7). On the other hand, the group $	ext{Pic}^\circ X$ of divisors algebraically equivalent to zero modulo linear equivalence is isomorphic to $H^1(X, \mathcal{O}_X)/H^1(X_h, \mathbf{Z})$. One shows that this is a complex torus, and in fact it is an abelian variety, the Picard variety of $X$.