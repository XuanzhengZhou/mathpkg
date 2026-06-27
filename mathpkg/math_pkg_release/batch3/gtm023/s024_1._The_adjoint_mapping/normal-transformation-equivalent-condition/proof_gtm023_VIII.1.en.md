---
role: proof
locale: en
of_concept: normal-transformation-equivalent-condition
source_book: gtm023
source_chapter: "VIII"
source_section: "§1. The adjoint mapping"
---

Assume $\varphi$ is normal, i.e., $\tilde{\varphi} \circ \varphi = \varphi \circ \tilde{\varphi}$. Then for all $x, y \in E$:

$$(\varphi x, \varphi y) = (x, \tilde{\varphi} \varphi y) = (x, \varphi \tilde{\varphi} y) = (\tilde{\varphi} x, \tilde{\varphi} y).$$

Conversely, assume $(\varphi x, \varphi y) = (\tilde{\varphi} x, \tilde{\varphi} y)$ for all $x, y$. Then

$$(y, \tilde{\varphi} \varphi x) = (\varphi y, \varphi x) = (\tilde{\varphi} y, \tilde{\varphi} x) = (y, \varphi \tilde{\varphi} x)$$

for all $x, y \in E$. By nondegeneracy of the inner product, $\tilde{\varphi} \varphi x = \varphi \tilde{\varphi} x$ for all $x$, so $\varphi$ is normal.

Setting $y = x$ in the equivalent condition gives $|\varphi x|^2 = |\tilde{\varphi} x|^2$. Conversely, the norm-squared equality for all $x$ implies the inner product equality by polarization.
