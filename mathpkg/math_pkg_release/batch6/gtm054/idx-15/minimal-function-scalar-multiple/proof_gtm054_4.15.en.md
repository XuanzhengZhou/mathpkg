---
role: proof
locale: en
of_concept: minimal-function-scalar-multiple
source_book: gtm054
source_chapter: "IV"
source_section: "15"
---

By hypothesis, $\sigma(h_1) \neq \emptyset$, so fix $x \in \sigma(h_1)$. Define $\eta = h_2(x)/h_1(x) \in \mathbb{Q}$. Consider $h_3 = h_2 - \eta h_1 \in L$. For any $y \in \sigma(h_1)$, if $h_3(y) \neq 0$ then $\sigma(h_3) \subsetneq \sigma(h_1)$, contradicting minimality of $h_1$. Thus $h_3 = 0$ on $\sigma(h_1)$, and since $\sigma(h_2) \subseteq \sigma(h_1)$, we have $h_3 = 0$ everywhere, so $h_2 = \eta h_1$.
