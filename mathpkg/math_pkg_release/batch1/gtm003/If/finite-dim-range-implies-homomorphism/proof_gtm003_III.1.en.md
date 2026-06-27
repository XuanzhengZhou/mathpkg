---
role: proof
locale: en
of_concept: finite-dim-range-implies-homomorphism
source_book: gtm003
source_chapter: "III"
source_section: "1"
---

The following three statements are equivalent for a continuous linear map $u: L \to M$:
(a) $u$ is a topological homomorphism.
(b) $u^{-1}(0)$ is closed.
(c) $u_0$ is an isomorphism.

(a) $\Rightarrow$ (b): Since $u(L)$ is Hausdorff, $\{0\}$ is closed and thus $u^{-1}(0)$ is closed if $u$ is continuous.

(b) $\Rightarrow$ (c): If $u^{-1}(0)$ is closed, then $L/u^{-1}(0)$ is a Hausdorff t.v.s. of finite dimension, whence by (I, 3.4), $u_0$ is an isomorphism. It follows from (1.2) that $u$ is a topological homomorphism.

(c) $\Rightarrow$ (a) is clear from the definition.
