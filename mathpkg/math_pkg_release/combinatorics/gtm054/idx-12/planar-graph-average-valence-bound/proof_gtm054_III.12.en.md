---
role: proof
locale: en
of_concept: planar-graph-average-valence-bound
source_book: gtm054
source_chapter: "III"
source_section: "12"
---

(a) Since $1/\rho^{\perp}(\Gamma) \leq 1/3$ (by Corollary F7b, every region of a planar graph without isthmuses has covalence at least 3), Corollary F4 yields:
$$\frac{1}{\rho(\Gamma)} = \frac{1}{2} + \frac{1}{\nu_1(\Gamma)} - \frac{1}{\rho^{\perp}(\Gamma)} \geq \frac{1}{2} + \frac{1}{\nu_1(\Gamma)} - \frac{1}{3} > \frac{1}{6}.$$
Hence $\rho(\Gamma) < 6$. Since the average valence is less than 6, there must exist at least one vertex $x \in V$ with $\rho(x) < 6$, hence $\rho(x) \leq 5$.

(b) Similarly, if $\rho(\Gamma) \geq 3$, then from Corollary F4,
$$\frac{1}{\rho^{\perp}(\Gamma)} = \frac{1}{2} + \frac{1}{\nu_1(\Gamma)} - \frac{1}{\rho(\Gamma)} \geq \frac{1}{2} + \frac{1}{\nu_1(\Gamma)} - \frac{1}{3} > \frac{1}{6},$$
hence $\rho^{\perp}(\Gamma) < 6$.
