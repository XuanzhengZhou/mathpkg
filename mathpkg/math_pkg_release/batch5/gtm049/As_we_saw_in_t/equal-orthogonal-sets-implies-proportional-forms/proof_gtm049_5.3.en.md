---
role: proof
locale: en
of_concept: equal-orthogonal-sets-implies-proportional-forms
source_book: gtm049
source_chapter: "5"
source_section: "5.3"
---

**First proof.** The condition $\bot(\sigma) = \bot(\tau)$ implies that $[a]^{\perp(\sigma)} = [a]^{\perp(\tau)}$ for all $a$ in $V$ and hence that

$$\sigma(a, b) = 0 \text{ if, and only if, } \tau(a, b) = 0 \text{ for all } a, b \text{ in } V. \tag{1}$$

This condition in turn implies that $\top(\sigma) = \top(\tau)$. We may therefore choose an ordered basis $(a_1, \ldots, a_n)$ of $V$ such that $(a_{r+1}, \ldots, a_n)$ is a basis of $V^\perp = V^\top$ (cf. exercise 5 of §5.2). Let $S$ and $T$ be the matrices of $\sigma$ and $\tau$ with respect to this basis. Then (1) implies that

$$[x S]^{\perp(\rho)} = [x T]^{\perp(\rho)} \quad \text{for all } x \text{ in } F^n$$

and hence (exercise 6 of §5.2) we have

$$[x S] = [x T] \quad \text{for all } x \text{ in } F^n.$$

In particular, if $(e_1, \ldots, e_n)$ is the standard basis of $F^n$, we have

$$e_1 S = z_1 e_1 T,$$

$$\ldots$$

$$e_r S = z_r e_r T,$$

and

$$(e_1 + \ldots + e_r) S = z(e_1 + \ldots + e_r) T,$$

where $z_1, \ldots, z_r, z$ are non-zero scalars. (Recall that $e_i S$, $e_i T$ are the $i$-th rows of $S$, $T$, respectively.) It follows that

$$(z_1 e_1 + \ldots + z_r e_r) T = z(e_1 + \ldots + e_r) T,$$

and the linear independence of the first $r$ rows of $T$ allows us to deduce that $z_1 = z_2 = \cdots = z_r = z$. Bearing in mind the fact that the remaining rows of $S$ and $T$ are zero, we have $S = z T$ and so $\sigma = z \tau$, as required.

**Second proof.** By Lemma 1 of the previous section (p. 94), $M^{\perp(\sigma)} = (M \sigma)^\circ$ and $M^{\perp(\tau)} = (M \tau)^\circ$. Thus $M \sigma = M \tau$ for all subspaces $M$ of $V$. In the language of §4.2 this means that the projectivities $\mathcal{P}(\sigma)$ and $\mathcal{P}(\tau)$ agree on all subspaces. By the projectivity uniqueness theorem, this implies $\sigma$ and $\tau$ are proportional.
