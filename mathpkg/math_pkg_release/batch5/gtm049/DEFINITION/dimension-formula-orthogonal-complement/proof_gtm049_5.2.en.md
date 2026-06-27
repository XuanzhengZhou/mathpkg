---
role: proof
locale: en
of_concept: dimension-formula-orthogonal-complement
source_book: gtm049
source_chapter: "V"
source_section: "5.2"
---

**Proof.** Let $M$ have dimension $r$ and let $\dim(M \cap V^{\top}) = s$. Choose a basis $(a_1, \ldots, a_s)$ of $M \cap V^{\top}$ and extend it to a basis $(a_1, \ldots, a_r)$ of $M$.

The condition for $b = \sum y_j a_j$ (in terms of some basis extending $(a_i)$ to all of $V$) to lie in $M^{\perp}$ is that

$$\sigma(a_i, b) = 0 \quad (i = 1, \ldots, r).$$

Since $\sigma(a_i, b) = 0$ holds automatically for $i = 1, \ldots, s$ because $a_i \in V^{\top}$, we only need to satisfy $r - s$ linear equations. These equations are linearly independent: if $\sum_{i=s+1}^{r} x_i \sigma(a_i, b) = 0$ for all $b$, then $\sigma(\sum x_i a_i, b) = 0$ for all $b$, so $\sum x_i a_i \in M \cap V^{\top}$, which forces all $x_i = 0$ by the choice of basis.

Thus we have $r - s$ linearly independent linear equations in $n$ variables. By the rank-nullity theorem, the solution space has dimension $n - (r - s)$. Hence

$$\dim M^{\perp} = n - r + s = \dim V - \dim M + \dim(M \cap V^{\top}),$$

which yields the formula. The dual formula is proved in the same way.
