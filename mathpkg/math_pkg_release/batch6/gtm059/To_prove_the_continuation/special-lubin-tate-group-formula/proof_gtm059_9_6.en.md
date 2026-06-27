---
role: proof
locale: en
of_concept: special-lubin-tate-group-formula
source_book: gtm059
source_chapter: "9"
source_section: "6"
---

By Theorem 3.20 of Chapter 8, we know that the group law on the special Lubin-Tate group $B$ satisfies
$$F(X, Y) = X + Y + \text{terms of degree } \ge n.$$

If $n, y, p_n$ it follows that
$$x +_B y = p(x) + y \quad \text{and} \quad p^n.$$

But $p^n \in [x | B_n)$. Hence again addition on $B_n$ and addition on $G_n$ are interchangeable on the left of the symbol $(x, w_n)$ under the stated conditions, and the rest of the proof is identical with that of Theorem 6.2.

The key insight is that the Frobenius power series $F(X) = X + L w_i w_j B$ controls the deviation between the formal group addition $+_B$ and ordinary addition $+$. The condition that the higher-degree terms start at degree at least $n$ ensures that the error terms are negligible with respect to the relevant valuations, which guarantees the interchangeability under the stated bounds on $i$ and $j$.
