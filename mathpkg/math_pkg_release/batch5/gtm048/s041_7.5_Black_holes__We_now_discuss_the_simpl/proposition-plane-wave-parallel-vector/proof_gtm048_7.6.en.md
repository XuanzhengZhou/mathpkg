---
role: proof
locale: en
of_concept: proposition-plane-wave-parallel-vector
source_book: gtm048
source_chapter: "7"
source_section: "7.6.3"
---

**Proof.** Suppose $X = aY$. Then for all $(z, Z) \in TM$,
$$D_Z X = a\{Z[\omega^i(Y)] + \omega_j^i(Z)\omega^j(Y)\} X_i = a\omega_3^i(Z) X_i = 0,$$
using the connection forms computed in the proof of Proposition 7.6.1. Conversely, suppose $DX = 0$. Then $\hat{R}(\cdot, X, \cdot, \cdot) = 0$ by the definition of the curvature tensor (Section 1.0.2). Computing this condition using Corollary 7.6.2 forces $X$ to be proportional to $Y$.
