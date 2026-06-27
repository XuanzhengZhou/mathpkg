---
role: proof
locale: en
of_concept: invertible-neighborhood-of-unity
source_book: gtm015
source_chapter: "VI"
source_section: "50"
---

# Proof that Elements Near Unity are Invertible

Let $A$ be a Banach algebra with unity $1$, and let $x \in A$ with $\|1 - x\| < 1$. Set $z = 1 - x$; then $\|z\| < 1$ and $x = 1 - z$.

By the Neumann series theorem (50.2), $1 - z$ is invertible with inverse
$$(1 - z)^{-1} = \sum_{n=0}^{\infty} z^n.$$
Thus $x$ is invertible.

More generally, if $\lambda \in \mathbb{C}$ with $\lambda \neq 0$, then $\lambda 1 - x = \lambda(1 - \lambda^{-1}x)$. If $\|\lambda^{-1}x\| < 1$ (i.e., $|\lambda| > \|x\|$), then $\lambda 1 - x$ is invertible with
$$(\lambda 1 - x)^{-1} = \lambda^{-1}(1 - \lambda^{-1}x)^{-1} = \lambda^{-1} \sum_{n=0}^{\infty} (\lambda^{-1}x)^n = \sum_{n=0}^{\infty} \lambda^{-n-1} x^n,$$
and
$$\|(\lambda 1 - x)^{-1}\| = |\lambda|^{-1}\|(1 - \lambda^{-1}x)^{-1}\| \leq \frac{|\lambda|^{-1}}{1 - \|\lambda^{-1}x\|} = \frac{1}{|\lambda| - \|x\|}. \; \square$$
