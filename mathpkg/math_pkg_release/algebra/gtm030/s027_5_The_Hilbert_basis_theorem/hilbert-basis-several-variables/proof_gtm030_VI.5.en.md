---
role: proof
locale: en
of_concept: hilbert-basis-several-variables
source_book: gtm030
source_chapter: "VI"
source_section: "5. The Hilbert basis theorem"
---

By induction on $r$. The case $r = 1$ is the Hilbert Basis Theorem. Assume the result holds for $r-1$. Then $\mathfrak{A}[x_1, \dots, x_{r-1}]$ satisfies the ascending chain condition for left ideals. Identifying $\mathfrak{A}[x_1, \dots, x_r]$ with $(\mathfrak{A}[x_1, \dots, x_{r-1}])[x_r]$, the ring $\mathfrak{A}[x_1, \dots, x_{r-1}]$ is a ring with identity satisfying the ascending chain condition for left ideals. Applying the Hilbert Basis Theorem again, $(\mathfrak{A}[x_1, \dots, x_{r-1}])[x_r] = \mathfrak{A}[x_1, \dots, x_r]$ also satisfies the ascending chain condition. Hence every left ideal in $\mathfrak{A}[x_1, \dots, x_r]$ is finitely generated.
