---
role: proof
locale: en
of_concept: absolute-value-of-complex-exponential
source_book: gtm011
source_chapter: "2"
source_section: "2.13"
---

Since all coefficients of the power series $\exp z = \sum_{n=0}^\infty z^n/n!$ are real, we have $\overline{\exp z} = \exp \bar{z}$. For any $z \in \mathbb{C}$,

$$|e^z|^2 = e^z \overline{e^z} = e^z e^{\bar{z}} = e^{z + \bar{z}} = \exp(2 \operatorname{Re} z) = \left(\exp(\operatorname{Re} z)\right)^2.$$

Since $|e^z| \geq 0$ and $\exp(\operatorname{Re} z) > 0$, taking square roots yields

$$|\exp z| = \exp(\operatorname{Re} z).$$
