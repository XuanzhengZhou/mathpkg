---
role: proof
locale: en
of_concept: poincare-series-of-direct-sum
source_book: gtm023
source_chapter: "VI"
source_section: "§1. G-graded vector spaces"
---

For the direct sum $E \oplus F$, the $k$-th homogeneous component is $(E \oplus F)_k = E_k \oplus F_k$. Since $E$ and $F$ are almost finite, $\dim E_k < \infty$ and $\dim F_k < \infty$, hence $\dim (E_k \oplus F_k) = \dim E_k + \dim F_k < \infty$, so $E \oplus F$ is almost finite. The Poincaré series is
$$P_{E \oplus F}(t) = \sum_k \dim(E_k \oplus F_k) \, t^k = \sum_k (\dim E_k + \dim F_k) \, t^k = \sum_k \dim E_k \, t^k + \sum_k \dim F_k \, t^k = P_E(t) + P_F(t).$$
