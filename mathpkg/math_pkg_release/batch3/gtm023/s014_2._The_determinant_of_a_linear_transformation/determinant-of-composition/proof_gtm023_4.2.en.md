---
role: proof
locale: en
of_concept: determinant-of-composition
source_book: gtm023
source_chapter: "4"
source_section: "2"
---

Let $\Delta \neq 0$ be a determinant function on $E$. Using Definition 4.4 twice,

$$\Delta(\psi \varphi x_1, \ldots, \psi \varphi x_n) = \det \psi \, \Delta(\varphi x_1, \ldots, \varphi x_n) = \det \psi \, \det \varphi \, \Delta(x_1, \ldots, x_n).$$

But by definition, the left-hand side also equals $\det(\psi \circ \varphi) \, \Delta(x_1, \ldots, x_n)$. Hence

$$\det(\psi \circ \varphi) = \det \psi \, \det \varphi.$$

For the inverse, apply this formula with $\psi = \varphi^{-1}$:

$$\det(\varphi^{-1}) \, \det \varphi = \det(\varphi^{-1} \circ \varphi) = \det \iota = 1,$$

so $\det(\varphi^{-1}) = (\det \varphi)^{-1}$.
