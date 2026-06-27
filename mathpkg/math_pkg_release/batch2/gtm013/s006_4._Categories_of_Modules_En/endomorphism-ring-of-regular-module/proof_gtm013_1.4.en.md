---
role: proof
locale: en
of_concept: endomorphism-ring-of-regular-module
source_book: gtm013
source_chapter: "1"
source_section: "4"
---

By Proposition 4.5, there is a left $R$-isomorphism $\rho: R \to \operatorname{Hom}_R(R_R, R_R)$ given by $\rho(r)(s) = rs$ for $r, s \in R$. The inverse sends $f \in \operatorname{Hom}_R(R_R, R_R)$ to $f(1)$. 

To see this is a ring isomorphism, note that for $r_1, r_2 \in R$, $\rho(r_1 r_2)(s) = r_1 r_2 s = \rho(r_1)(r_2 s) = \rho(r_1)(\rho(r_2)(s)) = (\rho(r_1) \circ \rho(r_2))(s)$. Thus $\rho(r_1 r_2) = \rho(r_1) \circ \rho(r_2)$, and $\rho(1) = \operatorname{id}_R$.

For the right module version, the right $R$-isomorphism from (4.5) gives $\lambda: R \to \operatorname{Hom}_R(_R R, _R R)$ with $\lambda(r)(s) = sr$, and similarly $\lambda(r_1 r_2) = \lambda(r_2) \circ \lambda(r_1)$. As rings, $\operatorname{End}(_R R) \cong R^{\mathrm{op}}$, but since the endomorphisms act on the right, the natural map $\rho: R \to \operatorname{End}(_R R)$ sending $r$ to right-multiplication-by-$r$ is a ring isomorphism. Specifically, $\rho(r)(s) = sr$, and $\rho(r_1 r_2)(s) = s(r_1 r_2) = (s r_1) r_2 = \rho(r_2)(\rho(r_1)(s)) = (\rho(r_1) \circ \rho(r_2))(s)$, so $\rho$ is an anti-isomorphism. For right operators, composition order is reversed, giving a ring isomorphism.

Because both $\lambda$ and $\rho$ are isomorphisms, the regular bimodule $_R R_R$ is faithfully balanced by definition.
