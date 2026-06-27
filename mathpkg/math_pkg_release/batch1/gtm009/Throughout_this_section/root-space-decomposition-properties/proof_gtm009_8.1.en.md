---
role: proof
locale: en
of_concept: root-space-decomposition-properties
source_book: gtm009
source_chapter: "8"
source_section: "8.1"
---

(1) The first assertion follows from the Jacobi identity: $x \in L_\alpha, y \in L_\beta$, $h \in H$ imply that
$$\mathrm{ad}\, h([xy]) = [[hx]y] + [x[hy]] = \alpha(h)[xy] + \beta(h)[xy] = (\alpha+\beta)(h)[xy].$$

(2) The second assertion is an immediate consequence of the first: if $x \in L_\alpha$ with $\alpha \neq 0$, then iterated brackets with $x$ keep pushing into higher and higher root spaces (which are finitely many), so eventually the bracket vanishes, making $\mathrm{ad}\, x$ nilpotent.

(3) For the remaining assertion, find $h \in H$ for which $(\alpha+\beta)(h) \neq 0$. Then if $x \in L_\alpha, y \in L_\beta$, associativity of the form allows us to write
$$\kappa([hx], y) = -\kappa([xh], y) = -\kappa(x, [hy]),$$
or
$$\alpha(h) \kappa(x, y) = -\beta(h) \kappa(x, y),$$
hence $(\alpha+\beta)(h) \kappa(x, y) = 0$. This forces $\kappa(x, y) = 0$.
