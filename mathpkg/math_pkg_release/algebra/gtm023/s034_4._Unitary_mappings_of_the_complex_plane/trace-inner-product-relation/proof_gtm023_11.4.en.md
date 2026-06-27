---
role: proof
locale: en
of_concept: trace-inner-product-relation
source_book: gtm023
source_chapter: "11"
source_section: "4"
---

Formula (11.31) implies that
$$
(z, \tau z) + (z, \tau^{-1} z) = |z|^2 \operatorname{tr} \tau
$$
for every vector $z \in C$. Observing that
$$
(z, \tau^{-1} z) = (\tau z, z) = \overline{(z, \tau z)},
$$
we obtain
$$
(z, \tau z) + \overline{(z, \tau z)} = |z|^2 \operatorname{tr} \tau,
$$
which is precisely
$$
2 \operatorname{Re} (z, \tau z) = |z|^2 \operatorname{tr} \tau.
$$
If $\det \tau = 1$, then $\operatorname{tr} \tau$ is determined by $\tau$ alone, so $\operatorname{Re}(z, \tau z)$ depends only on $|z|$.
