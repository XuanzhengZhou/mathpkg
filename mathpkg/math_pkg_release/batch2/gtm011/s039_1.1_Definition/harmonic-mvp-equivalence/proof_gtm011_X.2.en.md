---
role: proof
locale: en
of_concept: harmonic-mvp-equivalence
source_book: gtm011
source_chapter: "X"
source_section: "2.11"
---

Let $a \in G$ and choose $\rho$ such that $\overline{B}(a; \rho) \subset G$; it is sufficient to show that $u$ is harmonic on $B(a; \rho)$. But according to Corollary 2.10 there is a continuous function $w: \overline{B}(a; \rho) \to \mathbb{R}$ which is harmonic in $B(a; \rho)$ and satisfies $w(a + \rho e^{i\theta}) = u(a + \rho e^{i\theta})$ for all $\theta$.

Since $u - w$ satisfies the MVP (both $u$ and $w$ do, the latter because it is harmonic) and $(u - w)(z) = 0$ for $|z - a| = \rho$, it follows from Corollary 1.9 that $u \equiv w$ in $B(a; \rho)$. In particular, $u$ must be harmonic on $B(a; \rho)$, and hence on all of $G$.
