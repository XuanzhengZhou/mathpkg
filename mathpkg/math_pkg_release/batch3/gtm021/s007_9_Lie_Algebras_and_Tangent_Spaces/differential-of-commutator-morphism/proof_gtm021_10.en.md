---
role: proof
locale: en
of_concept: differential-of-commutator-morphism
source_book: gtm021
source_chapter: "10"
source_section: "Differentials of Morphisms"
---
Factor $\gamma_x(y) = y \cdot (x y^{-1} x^{-1})$. The derivative of $y \mapsto y$ at $e$ is the identity. The derivative of $y \mapsto x y^{-1} x^{-1}$ at $e$ is $\operatorname{Ad} x \circ d\iota_e = \operatorname{Ad} x \circ (-1) = -\operatorname{Ad} x$, by the chain rule and Proposition 10.1(b).

Therefore, by Proposition 10.1(a):
$$(d\gamma_x)_e(X) = X + (-\operatorname{Ad} x(X)) = (1 - \operatorname{Ad} x)(X).$$
