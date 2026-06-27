---
role: proof
locale: en
of_concept: "sequence-number-function"
source_book: gtm022
source_chapter: "IX"
source_section: "6"
---
Proof. Define the triangular number $T(n) = n(n+1)/2$. For each $z > 0$, $z$ uniquely decomposes as $z = T(n) + y$ with $0 < y \leqslant n+1$. Put $x = n+2-y$. Then $L(z) = x$, $R(z) = y$, and $P(x,y) = T(x+y-2) + y$. These functions are definable using addition and multiplication. The sequence function $\operatorname{seq}(b, r)$ is defined as the remainder on division of $L(b)$ by $1 + (r+1)R(b)$, which encodes the $r$-th element of a sequence coded by $b$. $\square$
