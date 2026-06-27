---
role: proof
locale: en
of_concept: invariance-frenet-connection-forms-reparametrization
source_book: gtm051
source_chapter: "1"
source_section: "1.3"
---

Let $\tilde{c}(s) = c(\phi(s))$ with $\phi: J \to I$ a diffeomorphism. Then $\tilde{c}'(s) = \dot{c}(\phi(s)) \phi'(s)$ and $|\tilde{c}'(s)| = |\dot{c}(\phi(s))| |\phi'(s)|$. For the distinguished Frenet frames we have $\tilde{e}_i(s) = e_i(\phi(s))$ (preserving orientation), hence

$$\tilde{e}'_i(s) = \dot{e}_i(\phi(s)) \phi'(s).$$

Therefore

$$\frac{\tilde{\omega}_{ij}(s)}{|\tilde{c}'(s)|} = \tilde{e}'_i(s) \cdot \frac{\tilde{e}_j(s)}{|\tilde{c}'(s)|} = \dot{e}_i(\phi(s))\phi'(s) \cdot \frac{e_j(\phi(s))}{|\dot{c}(\phi(s))| |\phi'(s)|} = \frac{\dot{e}_i(\phi(s)) \cdot e_j(\phi(s))}{|\dot{c}(\phi(s))|} = \frac{\omega_{ij}(\phi(s))}{|\dot{c}(\phi(s))|}.$$
