---
role: proof
locale: en
of_concept: phi-squared-in-q1
source_book: gtm023
source_chapter: "11"
source_section: "4"
---

For $\varphi \in Q_1$, we have $\operatorname{tr} \varphi = 0$. From the defining condition (11.33), $\varphi + \tilde{\varphi} = \iota \cdot \operatorname{tr} \varphi = 0$, so $\tilde{\varphi} = -\varphi$. Substituting into the fundamental identity (11.34), $\varphi \tilde{\varphi} = \iota \cdot \det \varphi$, we get
$$
\varphi (-\varphi) = \iota \cdot \det \varphi \quad \Longrightarrow \quad \varphi^2 = -\det \varphi \cdot \iota.
$$
Now, from the definition of the inner product, $(\varphi, \varphi) = \frac{1}{2} \operatorname{tr}(\varphi \circ \tilde{\varphi}) = \frac{1}{2} \operatorname{tr}(-\varphi^2) = \frac{1}{2} \operatorname{tr}(\det \varphi \cdot \iota) = \det \varphi$, since $\operatorname{tr} \iota = 2$ for transformations of the complex plane. Therefore $\varphi^2 = -(\varphi, \varphi) \iota$.
