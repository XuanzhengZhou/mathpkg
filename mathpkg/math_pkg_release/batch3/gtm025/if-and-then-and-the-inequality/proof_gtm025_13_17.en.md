---
role: proof
locale: en
of_concept: "if-and-then-and-the-inequality"
source_book: gtm025
source_chapter: "Spaces of Integrable Functions"
source_section: "13.17"
---

Let $r = \frac{q}{p} > 1$. For any $f \in \mathfrak{L}_q$, we have

$$\int |f|^p d\mu \leq \left( \int |f|^{pr} d\mu \right)^{\frac{1}{r}} \left( \int 1^r d\mu \right)^{\frac{1}{r'}} = \left( \int |f|^q d\mu \right)^{\frac{p}{q}} (\mu(X))^{\frac{q-p}{q}}.$$

It follows that $f \in \mathfrak{L}_p$, and that

$$\|f\|_p \leq \|f\|_q (\mu(X))^{\frac{q-p}{pq}} = \|f\|_q (\mu(X))^{\frac{1}{p}} - \frac{1}{q}.$$
