---
role: proof
locale: en
of_concept: theorem-2-11
source_book: gtm011
source_chapter: "Harmonic Functions"
source_section: "2. Harmonic functions on a disk"
---

Proof. Let $a \in G$ and choose $\rho$ such that $\bar{B}(a; \rho) \subset G$; it is sufficient to show that $u$ is harmonic on $B(a; \rho)$. But according to Corollary 2.10 there is a continuous function $w: \bar{B}(a; \rho) \to \mathbb{R}$ which is harmonic in $B(a; \rho)$ and $w(a + \rho e^{i\theta}) = u(a + \rho e^{i\theta})$ for all $\theta$. Since $u - w$ satisfies the MVP and $(u - w)(z) = 0$ for $|z - a| = \rho$, it follows from Corollary 1.9 that $u \equiv w$ in $B(a; \rho)$; in particular, $u$ must be harmonic.

To prove the above theorem we used Corollary 2.10, which concerns functions harmonic in an arbitrary disk. It is desirable to derive a formula for the Poisson kernel of an arbitrary disk; to do this one need only make a change of variables in the formula (2.2).

If $R > 0$ then substituting $r/R$ for $r$ in the middle of (2.2) gives

$$\frac{R^2 - r^2}{R^2 - 2rR \cos \theta + r^2}$$

for $0 \leq r < R$ and all $\theta$. So if $u$ is continuous on $\bar{B}(a; R)$ and harmonic in $B(a; R)$ then

$$u(a + re^{i\theta}) = \frac{1}{2\pi} \int_{-\pi}^{\pi} \left[ \frac{R^2 - r^2}{R^2 - 2rR \cos
