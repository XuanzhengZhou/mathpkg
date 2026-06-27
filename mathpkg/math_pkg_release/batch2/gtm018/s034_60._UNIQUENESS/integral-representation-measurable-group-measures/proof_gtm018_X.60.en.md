---
role: proof
locale: en
of_concept: integral-representation-measurable-group-measures
source_book: gtm018
source_chapter: "X"
source_section: "60. Uniqueness"
---

If $g(y) = f(y^{-1})/\nu(Ey)$, then the results in the preceding section imply that $g$ is a nonnegative measurable function along with $f$. As before, write
$$
S(x, y) = (x, xy) \quad \text{and} \quad T(x, y) = (yx, y).
$$
In the measure space $(X \times X, S \times S, \mu \times \nu)$, both transformations $S$ and $T$ are measure preserving, and therefore so is the transformation $S^{-1}T$. Since $S^{-1}T(x, y) = (yx, x^{-1})$, it follows from Fubini's theorem that
$$
\begin{aligned}
\mu(E) \int g(y)\, d\nu(y) &= \int_E d\mu(x) \int g(y)\, d\nu(y) \\
&= \iint \chi_E(x)\, g(y)\, d\mu(x)\, d\nu(y) \\
&= \iint \chi_E(yx)\, g(x^{-1})\, d\mu(x)\, d\nu(y) \\
&= \int g(x^{-1})\, \nu(Ex^{-1})\, d\mu(x).
\end{aligned}
$$
Since $g(x^{-1})\,\nu(Ex^{-1}) = f(x)$, the desired result follows from a comparison of the extreme terms of this chain of equalities:
$$
\mu(E) \int g(y)\, d\nu(y) = \int f(x)\, d\mu(x),
$$
which is exactly
$$
\int f(x)\, d\mu(x) = \mu(E) \int \frac{f(y^{-1})}{\nu(Ey)}\, d\nu(y).
$$
