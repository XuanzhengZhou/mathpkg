---
role: proof
locale: en
of_concept: proportional-forms-with-same-orthogonality
source_book: gtm049
source_chapter: "5"
source_section: "5.3"
---

**PROOF.** The condition $\bot(\sigma) = \bot(\tau)$ implies that $[a]^{\perp(\sigma)} = [a]^{\perp(\tau)}$ for all $a$ in $V$ and hence that

$$\sigma(a, b) = 0 \quad \text{if, and only if,} \quad \tau(a, b) = 0 \quad \text{for all } a, b \in V. \tag{1}$$

This condition in turn implies that $\top(\sigma) = \top(\tau)$. We may therefore choose an ordered basis $(a_1, \ldots, a_n)$ of $V$ such that $(a_{r+1}, \ldots, a_n)$ is a basis of $V^\perp$ and the first $r$ rows of the matrices $S$ and $T$ of $\sigma$ and $\tau$ are linearly independent. Then (1) implies that

$$[x S]^{\perp(\rho)} = [x T]^{\perp(\rho)} \quad \text{for all } x \in F^n$$

and hence

$$[x S] = [x T] \quad \text{for all } x \in F^n.$$

In particular, if $(e_1, \ldots, e_n)$ is the standard basis of $F^n$, we have

$$e_1 S = z_1 e_1 T, \quad \ldots, \quad e_r S = z_r e_r T,$$

and

$$(e_1 + \cdots + e_r) S = z(e_1 + \cdots + e_r) T,$$

where $z_1, \ldots, z_r, z$ are non-zero scalars. It follows that

$$(z_1 e_1 + \cdots + z_r e_r) T = z(e_1 + \cdots + e_r) T,$$

and the linear independence of the first $r$ rows of $T$ allows us to deduce that $z_1 = z_2 = \cdots = z_r = z$. Bearing in mind the fact that the remaining rows of $S$ and $T$ are zero, we have $S = z T$ and so $\sigma = z \tau$, as required.
