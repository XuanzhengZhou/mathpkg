---
role: proof
locale: en
of_concept: tychonoff-product-theorem
source_book: gtm043
source_chapter: "6"
source_section: "6.8"
---

Let $X = \prod_\alpha X_\alpha$, where each $X_\alpha$ is compact. Then $X$ is completely regular.

Each projection $\pi_\alpha : X \to X_\alpha$ has a Stone extension $\bar{\pi}_\alpha : \beta X \to X_\alpha$. The mapping

$$p \mapsto (\bar{\pi}_\alpha(p))$$

sends $\beta X$ into $X$. In fact, it sends $\beta X$ onto $X$, because its restriction to $X$ is the identity. Since it is continuous, $\beta X \subset X$, so $X = \beta X$, and $X$ is compact.
