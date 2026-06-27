---
role: proof
locale: en
of_concept: continuity-of-borel-distance-function
source_book: gtm018
source_chapter: "XII"
source_section: "61"
---

If $\epsilon > 0$, then, because of the regularity of $\mu$, there exists a compact set $C$ such that $\rho(E,C) < \frac{\epsilon}{4}$ and there exists an open Borel set $U$ containing $C$ such that $\rho(U,C) < \frac{\epsilon}{4}$. Let $V$ be a neighborhood of $e$ such that $V = V^{-1}$ and $VC \subset U$. If $y^{-1}x \in V$, then $x^{-1}y \in V$ and therefore

$$\rho(xC,yC) = \mu(xC - yC) + \mu(yC - xC) = \mu(y^{-1}xC - C) + \mu(x^{-1}yC - C) \leq 2\mu(VC - C) \leq 2\mu(U - C) < \frac{\epsilon}{2}.$$

It follows that

$$|\rho(xE,E) - \rho(yE,E)| \leq \rho(xE,yE) \leq \rho(xE,xC) + \rho(xC,yC) + \rho(yC,yE) < \epsilon.$$
