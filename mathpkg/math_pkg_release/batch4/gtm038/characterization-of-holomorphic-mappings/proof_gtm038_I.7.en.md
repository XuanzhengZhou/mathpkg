---
role: proof
locale: en
of_concept: characterization-of-holomorphic-mappings
source_book: gtm038
source_chapter: "I"
source_section: "7. Holomorphic Mappings"
---

**Theorem 7.1.** Let $B \subset \mathbb{C}^n$ be a region, $f = (f_1, \ldots, f_m): B \to \mathbb{C}^m$ a mapping. $f$ is holomorphic if and only if each component function $f_{\mu}: B \to \mathbb{C}$ is holomorphic.

**Proof.** If $f$ is holomorphic, then by definition each $f_{\mu}$ is complex differentiable at every point of $B$, hence holomorphic. Conversely, if each $f_{\mu}$ is holomorphic, then at each $z_0 \in B$ we have $f_{\mu}(z) = f_{\mu}(z_0) + \sum_{v=1}^{n} (z_v - z_v^{(0)}) \Delta_v^{(\mu)}(z)$ with $\Delta_v^{(\mu)}$ continuous at $z_0$. Then $f(z) = f(z_0) + \sum_{v=1}^{n} (z_v - z_v^{(0)}) \Delta_v(z)$ where $\Delta_v = (\Delta_v^{(1)}, \ldots, \Delta_v^{(m)})$, showing $f$ is complex differentiable at $z_0$.
