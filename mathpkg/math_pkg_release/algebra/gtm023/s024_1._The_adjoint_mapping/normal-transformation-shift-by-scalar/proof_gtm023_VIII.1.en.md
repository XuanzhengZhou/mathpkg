---
role: proof
locale: en
of_concept: normal-transformation-shift-by-scalar
source_book: gtm023
source_chapter: "VIII"
source_section: "§1. The adjoint mapping"
---

Observe that the adjoint of $\varphi - \lambda \iota$ is $\tilde{\varphi} - \lambda \iota$, since the adjoint of the identity is the identity and the adjoint is linear. Then

$$(\widetilde{\varphi - \lambda \iota}) \circ (\varphi - \lambda \iota) = (\tilde{\varphi} - \lambda \iota)(\varphi - \lambda \iota) = \tilde{\varphi}\varphi - \lambda\tilde{\varphi} - \lambda\varphi + \lambda^2\iota.$$

Similarly,

$$(\varphi - \lambda \iota) \circ (\widetilde{\varphi - \lambda \iota}) = (\varphi - \lambda \iota)(\tilde{\varphi} - \lambda \iota) = \varphi\tilde{\varphi} - \lambda\varphi - \lambda\tilde{\varphi} + \lambda^2\iota.$$

Since $\varphi$ is normal, $\tilde{\varphi}\varphi = \varphi\tilde{\varphi}$, so the two expressions are equal. Hence $\varphi - \lambda \iota$ is normal.
