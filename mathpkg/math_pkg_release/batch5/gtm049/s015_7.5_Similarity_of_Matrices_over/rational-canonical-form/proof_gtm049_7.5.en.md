---
role: proof
locale: en
of_concept: rational-canonical-form
source_book: gtm049
source_chapter: "7"
source_section: "7.5"
---

The result is a consequence of the invariant factor decomposition of $V_f$ given by Theorem 1:

$$V_f = M_1 \oplus \cdots \oplus M_k,$$

where each $M_i \cong F[X]/(p_i)$ is a cyclic $F[X]$-module with $p_1 \mid p_2 \mid \cdots \mid p_k$ being the invariant factors of $f$. By Lemma 1, for each cyclic summand $M_i = [a_i]_f$ with generator $a_i$, the ordered basis $(a_i, a_i f, \ldots, a_i f^{s_i-1})$ yields the companion matrix $B_i$ whose last row encodes the coefficients of the minimal polynomial $m_{a_i}(X) = p_i(X)$. Taking the concatenation of these bases gives an ordered basis of $V$ in which the matrix of $f$ is the block diagonal matrix $\operatorname{diag}(B_1, \ldots, B_k)$.
