---
role: proof
locale: en
of_concept: finite-generation-of-integral-extension
source_book: gtm028
source_chapter: "V"
source_section: "1"
---

The theorem is true for $n = 1$ by condition (c'), since $x_1$ is integral over $A$ implies $A[x_1]$ is a finite $A$-module.

Proceed by induction on $n$. Assume that the ring $B' = A[x_1, \dots, x_{n-1}]$ is a finite $A$-module. By the case $n = 1$, the ring $A[x_1, \dots, x_n] = B'[x_n]$ is a finite $B'$-module, since $x_n$, being integral over $A$, is a fortiori integral over $B'$.

Now, $A[x_1, \dots, x_n]$ is finite over $B'$, and $B'$ is finite over $A$. Hence, by Remark 3 (transitivity of the finite module property), $A[x_1, \dots, x_n]$ is a finite $A$-module. $\square$
