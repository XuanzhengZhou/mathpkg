---
role: proof
locale: en
of_concept: lebesgue-countable-additivity
source_book: gtm025
source_chapter: "3"
source_section: "12"
---

For every positive integer $m$, $\sum_{j=1}^{\infty} f_j \geq \sum_{j=1}^{m} f_j$, so $\int_X (\sum f_j) d\mu \geq \sum_{j=1}^{m} \int_X f_j d\mu$, giving $\int_X (\sum f_j) d\mu \geq \sum_{j=1}^{\infty} \int_X f_j d\mu$.\n\nFor the reverse inequality, let $g_k = \sum_{j=1}^k f_j$. Then $g_k \uparrow \sum_{j=1}^\infty f_j$. By (12.11),\n$$\int_X \left(\sum_{j=1}^{\infty} f_j\right) d\mu = \lim_{k \to \infty} \int_X g_k d\mu \leq \lim_{k \to \infty} \int_X (f_1 + \cdots + f_k) d\mu = \lim_{k \to \infty} \sum_{j=1}^k \int_X f_j d\mu = \sum_{j=1}^{\infty} \int_X f_j d\mu.$$
