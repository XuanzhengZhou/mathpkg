---
role: proof
locale: en
of_concept: polynomial-representation-several-variables
source_book: gtm030
source_chapter: "II"
source_section: "10"
---

By the iterated adjunction identity (21), $A[u_1, \dots, u_r] = A[u_1][u_2] \cdots [u_r]$. Each step $A[u_1, \dots, u_{k-1}][u_k]$ adjoins a single commuting element $u_k$, so by the one-variable polynomial representation, its elements are polynomials in $u_k$ with coefficients in $A[u_1, \dots, u_{k-1}]$. Unfolding this iteration via induction on $r$, every element of $A[u_1, \dots, u_r]$ is a finite sum of the form

$$
\sum a_{i_1 i_2 \cdots i_r} u_1^{i_1} u_2^{i_2} \cdots u_r^{i_r}
$$

with $a_{i_1 i_2 \cdots i_r} \in A$ and only finitely many non-zero coefficients. The computation of such expressions in $B$ uses the ring operations together with the commutativity hypotheses on the $u_i$ and on the $u_i$ with $A$.
