---
role: proof
locale: en
of_concept: determinant-of-exponential-of-trace
source_book: gtm023
source_chapter: "8"
source_section: "8.28"
---

Let $\Delta \neq 0$ be a determinant function in $E$. Then $\Delta(\varphi(t)x_1, \dots, \varphi(t)x_n) = \det \varphi(t) \cdot \Delta(x_1, \dots, x_n)$. Differentiating and using $\dot{\varphi}(t) = \psi(t) \circ \varphi(t)$:

$$\sum_v \Delta(\varphi(t)x_1, \dots, \psi(t)\varphi(t)x_v, \dots, \varphi(t)x_n) = \frac{d}{dt}\det \varphi(t) \cdot \Delta(x_1, \dots, x_n).$$

The left side equals $\operatorname{tr} \psi(t) \cdot \det \varphi(t) \cdot \Delta(x_1, \dots, x_n)$ by the multilinearity of the determinant and the definition of trace. Therefore $\frac{d}{dt} \det \varphi(t) = \operatorname{tr} \psi(t) \cdot \det \varphi(t)$. Integrating with $\det \varphi(t_0) = \det \iota = 1$ gives $\det \varphi(t) = \exp(\int_{t_0}^{t} \operatorname{tr} \psi(t) \, dt)$.
