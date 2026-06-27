---
role: proof
locale: en
of_concept: first-passage-time-matrix-relation
source_book: gtm040
source_chapter: "6"
source_section: "4"
---

Apply Theorem 4-11 (the strong Markov property for mean first passage times) with the random time equal to one (i.e., condition on the first step). Then for $i 
eq j$:

egin{align*}
M_i[ar{t}_j] &= \sum_k P_{ik} M_k[ar{t}_j + 1] \
&= \sum_k P_{ik}(M_{kj} + 1) \
&= \sum_k P_{ik} M_{kj} + \sum_k P_{ik} \
&= (PM)_{ij} + 1.
\end{align*}

For an ergodic chain $P$, the mean recurrence time matrix $ar{M}$ (with $ar{M}_{ij} = M_i[ar{t}_j]$, where $ar{t}_j$ is the first passage time to $j$ allowing $i = j$) is related to $M$ by
$$ar{M} = D + M,$$
where $D$ is the diagonal matrix with $D_{ii} = 1/lpha_i$ and $lpha 1 = 1$ is the unique regular measure.
