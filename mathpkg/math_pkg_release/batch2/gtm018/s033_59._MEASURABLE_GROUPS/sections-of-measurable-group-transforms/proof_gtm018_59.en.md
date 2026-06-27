---
role: proof
locale: en
of_concept: sections-of-measurable-group-transforms
source_book: gtm018
source_chapter: "XI"
source_section: "59. Measurable Groups"
---

The result for $S$ follows from the relation

$$\chi_{S(E)}(x,y) = \chi_E(x,x^{-1}y),$$

together with the facts that $y \in (S(E))_x$ if and only if $\chi_{S(E)}(x,y) = 1$, and $x^{-1}y \in E_x$ if and only if $\chi_E(x,x^{-1}y) = 1$.

Indeed, by definition of the shearing transformation,

$$(x,y) \in S(E) \iff S^{-1}(x,y) = (x, x^{-1}y) \in E,$$

so $\chi_{S(E)}(x,y) = \chi_E(x, x^{-1}y)$. Now $y \in (S(E))_x$ means $(x,y) \in S(E)$, i.e., $\chi_{S(E)}(x,y) = 1$, which is equivalent to $\chi_E(x, x^{-1}y) = 1$, i.e., $x^{-1}y \in E_x$. This means $y \in xE_x$, so $(S(E))_x = xE_x$.

The proof for $T$ is similar. Using the relation $T(x,y) = (yx,y)$, we have

$$(x,y) \in T(E) \iff T^{-1}(x,y) = (xy^{-1}, y) \in E,$$

so $\chi_{T(E)}(x,y) = \chi_E(xy^{-1}, y)$. Then $x \in (T(E))^y$ means $(x,y) \in T(E)$, i.e., $\chi_E(xy^{-1}, y) = 1$, which means $xy^{-1} \in E^y$, i.e., $x \in E^y y = yE^y$. Hence $(T(E))^y = yE^y$.
