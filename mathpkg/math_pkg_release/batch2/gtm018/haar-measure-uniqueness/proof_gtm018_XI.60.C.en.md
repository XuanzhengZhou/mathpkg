---
role: proof
locale: en
of_concept: haar-measure-uniqueness
source_book: gtm018
source_chapter: "XI"
source_section: "60"
---

If $\mathbf{S}_0$ is the class of all Baire sets in $X$, then $(X, \mathbf{S}_0, \mu)$ and $(X, \mathbf{S}_0, \nu)$ are measurable groups and hence, by Theorem B, $\mu(E) = c\nu(E)$ for every Baire set $E$, with a nonnegative finite constant $c$; the fact that $c$ is positive may be inferred by choosing $E$ to be any bounded open Baire set. Any two regular Borel measures which agree on all Baire sets are identical (by 53.D), and therefore $\mu = c\nu$ on all Borel sets.

The supporting Theorem B states: If $\mu$ and $\nu$ are two measures such that $(X, \mathbf{S}, \mu)$ and $(X, \mathbf{S}, \nu)$ are measurable groups, and if $E$ in $\mathbf{S}$ is such that $0 < \nu(E) < \infty$, then, for every $F$ in $\mathbf{S}$, $\mu(E)\nu(F) = \nu(E)\mu(F)$. This follows from Theorem A by setting $f$ to be the characteristic function of $F$:

First, applying Theorem A with both measures equal to $\nu$, we have

$$\int f(x) d\nu(x) = \nu(E) \int \frac{f(y^{-1})}{\nu(Ey)} d\nu(y).$$

Multiplying by $\mu(E)$ and applying Theorem A (with the original $\mu$ and $\nu$), we obtain

$$\mu(E) \int f(x) d\nu(x) = \nu(E) \int f(x) d\mu(x).$$

Since $f = \chi_F$, this yields $\mu(E)\nu(F) = \nu(E)\mu(F)$.

Theorem A itself (which expresses a $\mu$-integral in terms of a $\nu$-integral) is proved via Fubini's theorem and the measure-preserving transformations $S(x,y) = (x, xy)$ and $T(x,y) = (yx, y)$ on $X \times X$ with the product measure $\mu \times \nu$; the transformation $S^{-1}T(x,y) = (yx, x^{-1})$ is also measure preserving, and the desired equality follows from computing the integral of a suitable function in two ways.
