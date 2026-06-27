---
role: proof
locale: en
of_concept: euler-characteristic-via-betti-number
source_book: gtm047
source_chapter: "22"
source_section: "1"
---

Let $h$ be the number of handles and $m$ the number of cross-caps ($0 \leqslant m \leqslant 2$).

For $m = 0$ (orientable): $\chi(M) = 2 - 2h$ (Theorem 5) and $p^1(M) = 2h$ (Theorem 6). Hence $\chi(M) = 2 - p^1(M)$.

For $m = 1$: $\chi(M) = 2 - (2h + 1) = 1 - 2h$, and $p^1(M) = 2h$. Hence $\chi(M) = 1 - p^1(M)$.

For $m = 2$: $\chi(M) = 2 - (2h + 2) = -2h$, and $p^1(M) = 2h + 1$. Hence $\chi(M) = 1 - (2h + 1) = 1 - p^1(M)$.

In all non-orientable cases ($m = 1, 2$), we obtain $\chi(M) = 1 - p^1(M)$, while in the orientable case $\chi(M) = 2 - p^1(M)$. $\square$
