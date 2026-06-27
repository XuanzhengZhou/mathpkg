---
role: proof
locale: en
of_concept: proportionality-measurable-group-measures
source_book: gtm018
source_chapter: "X"
source_section: "60. Uniqueness"
---

Let $f$ be the characteristic function of $F$. Since Theorem A is true, in particular, if the two measures $\mu$ and $\nu$ are both equal to $\nu$, we have
$$
\int f(x)\, d\nu(x) = \nu(E) \int \frac{f(y^{-1})}{\nu(Ey)}\, d\nu(y).
$$
Multiplying by $\mu(E)$ and applying Theorem A (now with the original measures $\mu$ and $\nu$), we obtain
$$
\mu(E) \int f(x)\, d\nu(x) = \nu(E) \int f(x)\, d\mu(x).
$$
Since $f$ is the characteristic function of $F$, $\int f(x)\, d\nu(x) = \nu(F)$ and $\int f(x)\, d\mu(x) = \mu(F)$. Therefore
$$
\mu(E)\,\nu(F) = \nu(E)\,\mu(F),
$$
which is exactly the statement of the theorem. The equivalent formulation $\mu(F) = c\,\nu(F)$ follows by setting $c = \mu(E)/\nu(E)$, which is a nonnegative finite constant independent of $F$.
