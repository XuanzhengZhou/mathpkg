---
role: proof
locale: en
of_concept: polynomial-and-derivative-relatively-prime
source_book: gtm023
source_chapter: "XII"
source_section: "2"
---

Forward direction: If $f = f_1^{k_1} \cdots f_r^{k_r}$ with some $k_i > 1$, write $f = h f_i^2$. Then $f' = h' f_i^2 + 2h f_i f_i' = f_i(h' f_i + 2h f_i')$, so $f_i$ divides both $f$ and $f'$, hence they are not relatively prime.

Conversely, assume $k_i = 1$ for all $i$. Then $f = f_1 \cdots f_r$. Computing $f'$ via the product rule gives $f' = \sum_i f_1 \cdots f_i' \cdots f_r$. If a common divisor $d$ divides $f$ and $f'$, then $d$ must divide $f_i \cdot (f_1 \cdots f_i' \cdots f_r)$ for each $i$. Since the $f_i$ are irreducible and distinct (hence relatively prime), $d$ dividing $f$ means $d$ is a product of some $f_i$'s. But $d$ dividing $f'$ forces $d$ to divide each term $f_1 \cdots f_i' \cdots f_r$. For the term with $f_i$ in $d$, we get $f_i \mid f_i'$, impossible since $\deg f_i' < \deg f_i$. Thus $d = 1$.
