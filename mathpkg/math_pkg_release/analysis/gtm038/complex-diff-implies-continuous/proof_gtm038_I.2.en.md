---
role: proof
locale: en
of_concept: complex-diff-implies-continuous
source_book: gtm038
source_chapter: "I"
source_section: "2. Complex Differentiable Functions"
---

**Theorem 2.2.** Let $B \subset \mathbb{C}^n$ be a region and $f$ complex differentiable at $z_0 \in B$. Then $f$ is continuous at $z_0$.

**Proof.** By definition of complex differentiability, we have

$$f(z) = f(z_0) + \sum_{v=1}^{n} (z_v - z_v^{(0)}) \Delta_v(z)$$

where each $\Delta_v$ is continuous at $z_0$. The right side of this equation is clearly continuous at $z_0$: $f(z_0)$ is constant, each $(z_v - z_v^{(0)})$ is continuous and vanishes at $z_0$, and each $\Delta_v$ is continuous at $z_0$. Hence $f$ is continuous at $z_0$.
