---
role: proof
locale: en
of_concept: primitive-recursive-function-characterization
source_book: gtm037
source_chapter: "2"
source_section: "Elementary and Primitive Recursive Functions"
---

This proposition is the defining characterization of the class of primitive recursive functions. It is analogous to Proposition 2.3 for elementary recursive functions. The forward direction follows by induction on the construction of primitive recursive functions: every primitive recursive function is built from the zero function $\varnothing$, projection functions $U_j^n$, composition, and the two primitive recursion schemas $R^m$ and $R^0$, so a generating sequence exists by collecting all intermediate functions in the construction. The reverse direction is immediate: if such a finite generating sequence exists, then each $g_i$ is primitive recursive by induction on $i$, since the initial functions and the closing operations are all primitive recursive.
