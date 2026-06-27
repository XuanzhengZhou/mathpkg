---
role: proof
locale: en
of_concept: polynomial-ring-inductive-structure
source_book: gtm028
source_chapter: "II"
source_section: "18"
---

Consider the set $S^\prime$ of polynomials $f \in R[X_1, \dots, X_n]$ that are independent of $X_n$, i.e., polynomials for which $(i_1, \dots, i_n)f = 0$ whenever $i_n \neq 0$. For such a polynomial $f$, define $\tilde{f}: I_{n-1} \to R$ by $(i_1, \dots, i_{n-1})\tilde{f} = (i_1, \dots, i_{n-1}, 0)f$. This gives a bijection between $S^\prime$ and the set of finitely-supported mappings $I_{n-1} \to R$, which is precisely $R[X_1, \dots, X_{n-1}]$. The bijection preserves addition and multiplication (since the zero in the $n$-th coordinate does not affect the convolution formula), hence is a ring isomorphism.

Now every polynomial $f \in R[X_1, \dots, X_n]$ can be uniquely written as $f = \sum_{k=0}^d g_k X_n^k$ where each $g_k \in R[X_1, \dots, X_{n-1}]$ (identified with $S^\prime$). This is exactly the representation of elements of $(R[X_1, \dots, X_{n-1}])[X_n]$, establishing the isomorphism $R[X_1, \dots, X_n] \cong (R[X_1, \dots, X_{n-1}])[X_n]$.
