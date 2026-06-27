---
role: proof
locale: en
of_concept: visit-count-factorization
source_book: gtm040
source_chapter: "4"
source_section: "6"
---

For the first assertion, apply Theorem 4-11 with $f = n_j$ and the random time $t_j$ (the first time to reach $j$). Then $f' = n_j$ as well (the process after reaching $j$ restarts at $j$), and we obtain

$$M_i[n_j] = \sum_m \Pr\nolimits_i[x_{t_j} = m] \, M_m[n_j] = \Pr\nolimits_i[x_{t_j} = j] \, M_j[n_j] = H_{ij} \, N_{jj}.$$

For the second assertion, apply Theorem 4-11 with $f = \bar{n}_j$, $f' = n_j$, and the random time equal to $\bar{t}_j$. By the same kind of argument,

$$M_i[\bar{n}_j] = \bar{H}_{ij} \, M_j[n_j] = \bar{H}_{ij} \, N_{jj}.$$

The third identity follows from the first two together with Proposition 4-13: from $N = I + PN$ we have $N_{ii} = 1 + (PN)_{ii}$, and using the already-proven identities $(PN)_{ii} = \bar{N}_{ii} = \bar{H}_{ii} N_{ii}$, hence $N_{ii} = 1 + \bar{H}_{ii} N_{ii}$.
