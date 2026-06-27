---
role: proof
locale: en
of_concept: finite-join-indecomposable-decomposition-dcc
source_book: gtm030
source_chapter: "3"
source_section: "5"
---

The argument is the analogue of the one used in the group case. Suppose an element $a \in L$ cannot be expressed as a finite join of independent indecomposable elements. Then $a$ itself is decomposable, so $a = a_1 \cup a_2$ where $a_1, a_2$ are independent and $a_1 < a$, $a_2 < a$. At least one of $a_1, a_2$ must fail to admit such a decomposition (otherwise their join would provide one for $a$). Choose such an $a^{(1)} < a$ and repeat. This produces a strictly descending infinite chain $a > a^{(1)} > a^{(2)} > \cdots$, contradicting the descending chain condition. Hence every element can be so decomposed. The independence of the resulting indecomposable components follows from the construction.
