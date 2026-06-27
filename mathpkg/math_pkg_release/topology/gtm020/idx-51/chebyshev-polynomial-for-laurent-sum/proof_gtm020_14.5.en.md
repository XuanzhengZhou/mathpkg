---
role: proof
locale: en
of_concept: chebyshev-polynomial-for-laurent-sum
source_book: gtm020
source_chapter: "14"
source_section: "5"
---

It suffices to establish the recursion formula. For this, we calculate

$$(x^m + x^{-m})(x + x^{-1}) = (x^{m+1} + x^{-(m+1)}) + (x^{m-1} + x^{-(m-1)}).$$

Substituting $f_n(x + x^{-1})$ for $x^n + x^{-n}$, this becomes

$$f_m(y) \cdot y = f_{m+1}(y) + f_{m-1}(y),$$

where $y = x + x^{-1}$. Rearranging yields

$$f_{m+1}(y) = y f_m(y) - f_{m-1}(y).$$

The base cases are $f_0(y) = x^0 + x^{-0} = 2 = 1 + 1$ (actually $f_0(y) = 1$ by convention after adjusting) and $f_1(y) = x + x^{-1} = y$. The existence of $f_m \in \mathbb{Z}[y]$ follows by induction on $m$ using this recurrence.
