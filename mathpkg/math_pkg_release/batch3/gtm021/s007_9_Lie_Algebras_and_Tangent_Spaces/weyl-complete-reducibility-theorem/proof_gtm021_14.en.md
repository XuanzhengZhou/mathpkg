---
role: proof
locale: en
of_concept: weyl-complete-reducibility-theorem
source_book: gtm021
source_chapter: "14"
source_section: "Semisimple Groups"
---
Weyl's theorem for Lie algebras states that every finite dimensional representation of a semisimple Lie algebra is completely reducible. In characteristic 0, via Theorem 13.2, the rational representations of $G$ correspond to representations of $\mathfrak{g}$, so Weyl's theorem transfers to $G$.

The key application to Hilbert's 14th Problem: Let $\rho: G \to \operatorname{GL}(n, K)$ be a rational representation, so $G$ acts on the polynomial ring $R = K[T_1, \ldots, T_n]$. Since $G$ is semisimple, the representation on each homogeneous component $R_d$ is completely reducible. Write $R = R^G \oplus S$, where $S$ is the sum of all $G$-submodules on which $G$ acts irreducibly and nontrivially. Then $R^G \cap R^G S = 0$, and since $R^G S$ is $G$-stable, complete reducibility implies $R^G S \subset S$.

Now if $f_1, \ldots, f_t \in R^G$, the preceding argument implies
$$\left(\sum f_i R\right) \cap R^G = \sum f_i R^G.$$
Thus, extending an ideal of $R^G$ to $R$ and then restricting back to $R^G$ recovers the original ideal. This means $R^G$ satisfies the ascending chain condition on ideals, since $R$ does. Hence $R^G$ is Noetherian.

In particular, the homogeneous ideal of polynomials of positive degree has a finite set of generators $f_1, \ldots, f_t$ (which may be assumed homogeneous). Every homogeneous $f \in R^G$ of positive degree is a polynomial in the $f_i$, by an induction on degree, so $R^G = K[f_1, \ldots, f_t]$.
