---
role: proof
locale: en
of_concept: asymptotic-quantization-condition-with-maslov-index
source_book: gtm060
source_chapter: "Appendix 11"
source_section: "C. Indices of closed curves"
---

The derivation of this asymptotic formula relies on the construction linking the Morse index of a phase curve in $\mathbb{R}^{2n}$ to the Maslov index of a curve on an $(n+1)$-dimensional Lagrangian manifold in a suitable $(2n+2)$-dimensional phase space. With coordinates $(p_0, p; q_0, q)$ in $\mathbb{R}^{2n+2}$, set $q_0 = t$ and $p_0 = -H(p, q)$. As the point $(p, q)$ ranges over the $n$-dimensional Lagrangian manifold obtained from the original after time $t$ by the phase flow, the points $(p_0, p; q_0, q)$ form an $(n+1)$-dimensional Lagrangian manifold. The graph of the motion of a phase point is a curve on this manifold, and its Maslov index agrees with the Morse index of the original phase curve.

The indices of closed curves enter asymptotic formulas for stationary problems via the theory of characteristic oscillations. The congruence condition $\frac{2\mu_N}{\pi} \oint_\gamma p\,dq \equiv \operatorname{ind}\gamma \pmod{4}$ emerges from the requirement that the asymptotic eigenfunctions be single-valued after accounting for the Maslov index phase shifts at caustics. In the one-dimensional case, the Lagrangian manifold is a circle (the energy curve), and its Maslov index equals $2$ (since the tangent line makes two full rotations through the Lagrangian Grassmannian after one circuit). Substituting $\operatorname{ind}\gamma = 2$ gives $\frac{2\mu_N}{\pi} \oint p\,dq \equiv 2 \pmod{4}$, or equivalently $\mu_N \oint p\,dq = 2\pi(N + \frac{1}{2})$.
