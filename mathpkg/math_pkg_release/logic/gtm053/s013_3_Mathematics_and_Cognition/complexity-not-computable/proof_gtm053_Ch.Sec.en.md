---
role: proof
locale: en
of_concept: complexity-not-computable
source_book: gtm053
source_chapter: "VI"
source_section: "9"
---

Suppose $C(f_k)|_{D(g)} \sim g(k)$. Construct a general recursive $h: \mathbb{Z}^+ \to \mathbb{Z}^+$ whose image is in $D(g)$ and such that $g \circ h$ is monotone increasing. Then by the estimate for composition, $C(f_{h(k)}) \leqslant \text{const}\cdot C(k)$, while by assumption $C(f_{h(k)}) \geqslant \text{const}\cdot g(h(k)) \geqslant \text{const}\cdot k$. But $\lim\inf C(k)/k = 0$, contradiction.
