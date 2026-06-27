---
role: proof
locale: en
of_concept: eigenvector-equation-equivalence
source_book: gtm049
source_chapter: "6"
source_section: "6.5"
---

The given equation is equivalent to $f = \tau g^{-1}$. Let $a_1$ be an eigenvector of $f$, so $a_1 f = \lambda a_1$ for some $\lambda \in F$. Without loss of generality assume $\sigma(a_1, a_1) = 1$ (we may scale $a_1$ appropriately).

Suppose $\sigma(a_1, b) = 0$. Since $f = \tau g^{-1}$, we have $f g = \tau$. Now compute
$$\sigma(a_1 f, b) = \sigma(\lambda a_1, b) = \lambda \sigma(a_1, b) = 0.$$
Thus $\sigma(a_1 f, b) = 0$ whenever $\sigma(a_1, b) = 0$.

From the relation $f = \tau g^{-1}$ we obtain $\tau = f g$, hence
$$\tau(a_1, b) = \sigma(a_1 f g, b).$$
But $a_1 f = \lambda a_1$, so $a_1 f g = \lambda a_1 g$. Since $g$ preserves the orthogonal relationship (by the properties of the sesquilinear form), it follows that $\sigma(a_1, b) = 0$ implies $\tau(a_1, b) = 0$.

Therefore $[a_1]^{\perp(\sigma)} \subset [a_1]^{\perp(\tau)}$. Writing $W = [a_1] \oplus [a_1]^{\perp(\sigma)}$, we have $\dim W < \dim V$ and the equation restricts to $W$. By the induction hypothesis on $\dim W$, the result holds.
