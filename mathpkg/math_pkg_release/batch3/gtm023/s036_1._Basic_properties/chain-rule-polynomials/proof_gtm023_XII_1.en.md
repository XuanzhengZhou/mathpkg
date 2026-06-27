---
role: proof
locale: en
of_concept: chain-rule-polynomials
source_book: gtm023
source_chapter: "XII"
source_section: "1"
---

First note that $dg^k = k g^{k-1} dg$ for $k \geq 1$ (by induction using the Leibniz rule) and $dg^0 = 0$. Now write $f = \sum_k \alpha_k t^k$. Then $f(g) = \sum_k \alpha_k g^k$. Differentiating:
$$(f(g))' = \sum_k \alpha_k d(g^k) = \sum_k \alpha_k k g^{k-1} \cdot dg$$
$$= \sum_k k \alpha_k g^{k-1} \cdot g' = f'(g) \cdot g'.$$
The last equality follows since $f' = \sum_k k\alpha_k t^{k-1}$, and evaluating at $g$ gives $f'(g) = \sum_k k\alpha_k g^{k-1}$.
