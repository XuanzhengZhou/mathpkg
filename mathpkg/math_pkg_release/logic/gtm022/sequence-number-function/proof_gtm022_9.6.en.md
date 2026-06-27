---
role: proof
locale: en
of_concept: sequence-number-function
source_book: gtm022
source_chapter: "IX"
source_section: "6"
---

Using triangular numbers $T(n) = n(n+1)/2$ and the pairing $P(x,y) = T(x+y-2) + y$, define left/right inverses $L(z), R(z)$. Then $\operatorname{seq}(b, r) = \text{remainder of } L(b) \div (1 + (r+1)R(b))$. For any finite sequence $t_0, \ldots, t_m$, using the Chinese Remainder Theorem one finds $b$ with $\operatorname{seq}(b, r) = t_r$ for all $r \leqslant m$.
