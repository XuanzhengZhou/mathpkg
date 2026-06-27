---
role: proof
locale: en
of_concept: lcm-of-relatively-prime
source_book: gtm023
source_chapter: "XII"
source_section: "2"
---

For $r = 2$, by Proposition III with $f = 1$ (since the polynomials are relatively prime), we have $h_1 = f_1$ and $h_2 = f_2$, so $f_1 \wedge f_2 = f_1 f_2$. For $r > 2$, use induction: assume true for $r-1$, then $f_1 \wedge \cdots \wedge f_r = (f_1 \wedge \cdots \wedge f_{r-1}) \wedge f_r = (f_1 \cdots f_{r-1}) \wedge f_r$. Since the $f_i$ are pairwise relatively prime, $f_1 \cdots f_{r-1}$ is relatively prime to $f_r$, so the result is $f_1 \cdots f_r$.
