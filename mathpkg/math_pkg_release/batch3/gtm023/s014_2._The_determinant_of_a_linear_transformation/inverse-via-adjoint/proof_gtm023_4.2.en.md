---
role: proof
locale: en
of_concept: inverse-via-adjoint
source_book: gtm023
source_chapter: "4"
source_section: "2"
---

If $\det \varphi \neq 0$, then by the determinant-regularity theorem $\varphi$ is a linear automorphism, hence has an inverse. From Proposition V we have

$$\operatorname{ad}(\varphi) \circ \varphi = \iota \cdot \det \varphi.$$

Composing both sides with $\varphi^{-1}$ on the right yields

$$\operatorname{ad}(\varphi) = \varphi^{-1} \cdot \det \varphi,$$

and dividing by $\det \varphi$ (which is non-zero) gives $\varphi^{-1} = \frac{1}{\det \varphi} \operatorname{ad}(\varphi)$. The second relation $\varphi \circ \operatorname{ad}(\varphi) = \iota \cdot \det \varphi$ confirms consistency.
