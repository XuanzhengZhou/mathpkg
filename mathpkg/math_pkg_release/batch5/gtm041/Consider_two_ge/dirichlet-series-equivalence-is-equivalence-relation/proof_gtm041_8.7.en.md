---
role: proof
locale: en
of_concept: dirichlet-series-equivalence-is-equivalence-relation
source_book: gtm041
source_chapter: "8"
source_section: "8.7"
---

Every series is equivalent to itself since we may take each $y_n = 0$. The corresponding $x_n$ will then be zero.

If $b(n) = a(n)e^{ix_n}$ then $a(n) = b(n)e^{-ix_n}$. Since $X = R_B Y$ we have $-X = R_B(-Y)$ so the relation is symmetric.

To prove transitivity we may use the same basis throughout and assume that $b(n) = a(n)e^{ix_n}$, where $X = R_B Y$ for some $Y$, and that $a(n) = c(n)e^{iu_n}$, where $U = R_B V$ for some $V$. Then $b(n) = c(n)e^{i(x_n + u_n)}$ where
$$X + U = R_B Y + R_B V = R_B(Y + V).$$
This completes the proof.
