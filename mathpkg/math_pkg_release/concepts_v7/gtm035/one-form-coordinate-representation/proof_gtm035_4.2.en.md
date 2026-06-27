---
role: proof
locale: en
of_concept: one-form-coordinate-representation
source_book: gtm035
source_chapter: "4"
source_section: "4.2"
---

# Proof of Coordinate Representation of 1-Forms

**Lemma 4.2.** Every 1-form $\omega$ admits a unique representation

$$\omega = \sum_{j=1}^{N} C_j \, dx_j,$$

the $C_j$ being scalar functions on $\Omega$.

## Proof

Recall from Definition 4.4 that a 1-form $\omega$ on $\Omega$ assigns to each $x \in \Omega$ an element $\omega(x) \in T_x^*$, the dual space of the tangent space $T_x$.

By Lemma 4.1, $\{\partial/\partial x_1|_x, \ldots, \partial/\partial x_N|_x\}$ is a basis for $T_x$. Let $\{dx_1|_x, \ldots, dx_N|_x\}$ be the dual basis of $T_x^*$, characterized by
$$dx_j|_x\left(\frac{\partial}{\partial x_k}\bigg|_x\right) = \delta_{jk}.$$

Since $T_x^*$ has dimension $N$ and $\{dx_j|_x\}$ is a basis, every element $\omega(x) \in T_x^*$ can be uniquely expressed as
$$\omega(x) = \sum_{j=1}^{N} C_j(x) \, dx_j|_x$$
where $C_j(x) = \omega(x)(\partial/\partial x_j|_x)$ are scalar coefficients depending on $x$.

Define scalar functions $C_j: \Omega \to \mathbb{C}$ by $C_j(x) = \omega(x)(\partial/\partial x_j|_x)$ for each $x \in \Omega$. Then the equality
$$\omega = \sum_{j=1}^{N} C_j \, dx_j$$
holds pointwise on $\Omega$.

**Uniqueness:** If $\omega = \sum_{j=1}^{N} C_j \, dx_j = \sum_{j=1}^{N} C_j' \, dx_j$, then evaluating at each $x \in \Omega$ on the basis vector $\partial/\partial x_k|_x$ yields $C_k(x) = C_k'(x)$ for all $k$, so the coefficients are uniquely determined. $\square$
