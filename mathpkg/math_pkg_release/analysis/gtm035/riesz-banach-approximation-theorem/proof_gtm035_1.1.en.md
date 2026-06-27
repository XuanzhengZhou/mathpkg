---
role: proof
locale: en
of_concept: riesz-banach-approximation-theorem
source_book: gtm035
source_chapter: "1"
source_section: "1"
---

# Proof of Riesz-Banach Approximation Theorem

**Theorem (Riesz-Banach).** Let $X$ be a compact Hausdorff space, let $\mathcal{L}$ be a linear subspace of $C(X)$, and fix $g \in C(X)$. If for every (complex Baire) measure $\mu$ on $X$,

$$\mu \perp \mathcal{L} \quad \text{implies} \quad \mu \perp g,$$

then $g$ lies in the closure $\overline{\mathcal{L}}$ of $\mathcal{L}$ in $C(X)$. In particular, if $\mu \perp \mathcal{L}$ implies $\mu = 0$, then $\mathcal{L}$ is dense in $C(X)$.

## Proof

The result is a consequence of the Hahn-Banach separation theorem together with the Riesz representation theorem.

Let $\overline{\mathcal{L}}$ denote the uniform closure of $\mathcal{L}$ in $C(X)$. Suppose, for contradiction, that $g \notin \overline{\mathcal{L}}$.

Since $C(X)$ is a Banach space under the supremum norm, and $\overline{\mathcal{L}}$ is a closed linear subspace, there exists a nonzero bounded linear functional $\varphi \in C(X)^*$ such that

$$\varphi(f) = 0 \quad \text{for all } f \in \overline{\mathcal{L}}, \qquad \varphi(g) \neq 0.$$

This follows from the Hahn-Banach theorem: the quotient space $C(X)/\overline{\mathcal{L}}$ is a normed linear space, and the coset $g + \overline{\mathcal{L}}$ is nonzero, so there exists a bounded linear functional on $C(X)/\overline{\mathcal{L}}$ separating it from zero; composing with the quotient map yields $\varphi$.

By the Riesz representation theorem (for complex measures on a compact Hausdorff space), every bounded linear functional on $C(X)$ corresponds to a unique complex Baire measure $\mu$ on $X$ such that

$$\varphi(f) = \int_X f \, d\mu \quad \text{for all } f \in C(X).$$

Thus there exists a measure $\mu \neq 0$ on $X$ with

$$\int_X f \, d\mu = 0 \quad \text{for all } f \in \mathcal{L}, \qquad \int_X g \, d\mu \neq 0.$$

In the notation introduced above, this says $\mu \perp \mathcal{L}$ but $\mu \not\perp g$, contradicting the hypothesis.

Therefore $g \in \overline{\mathcal{L}}$.

For the particular case: if $\mu \perp \mathcal{L}$ implies $\mu = 0$, then the hypothesis of the theorem is vacuously satisfied for any $g \in C(X)$ (since $\mu \perp \mathcal{L}$ forces $\mu = 0$, which trivially satisfies $\mu \perp g$). Hence every $g \in C(X)$ lies in $\overline{\mathcal{L}}$, i.e., $\mathcal{L}$ is dense in $C(X)$. $\square$
