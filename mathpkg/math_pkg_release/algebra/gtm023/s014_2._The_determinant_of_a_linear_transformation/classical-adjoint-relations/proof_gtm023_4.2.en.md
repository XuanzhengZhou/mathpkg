---
role: proof
locale: en
of_concept: classical-adjoint-relations
source_book: gtm023
source_chapter: "4"
source_section: "2"
---

Replacing $x$ by $\varphi x$ in the defining equation (4.14) for $\operatorname{ad}(\varphi)$ we obtain

$$\sum_{j=1}^{n} (-1)^{j-1} \Delta(\varphi x, \varphi x_1, \ldots, \widehat{\varphi x_j}, \ldots, \varphi x_n) x_j = \Delta(x_1, \ldots, x_n) \operatorname{ad}(\varphi x).$$

Now observe that, in view of the definition of the determinant and Proposition IV,

$$\sum_{j=1}^{n} (-1)^{j-1} \Delta(\varphi x, \varphi x_1, \ldots, \widehat{\varphi x_j}, \ldots, \varphi x_n) x_j$$
$$= \det \varphi \cdot \sum_{j=1}^{n} (-1)^{j-1} \Delta(x, x_1, \ldots, \hat{x_j}, \ldots, x_n) x_j$$
$$= \det \varphi \cdot \Delta(x_1, \ldots, x_n) \cdot x.$$

Composing these two relations yields

$$\Delta(x_1, \ldots, x_n) \operatorname{ad}(\varphi x) = \det \varphi \cdot \Delta(x_1, \ldots, x_n) \cdot x$$

and since the basis vectors can be chosen such that $\Delta(x_1, \ldots, x_n) \neq 0$, we conclude $\operatorname{ad}(\varphi) \circ \varphi = \iota \cdot \det \varphi$.

The second relation is established by applying $\varphi$ to the defining equation and using the identity in Proposition IV, with $x_i$ replaced by $\varphi x_i$ ($i = 1, \ldots, n$).
