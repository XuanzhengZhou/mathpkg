---
role: proof
locale: en
of_concept: curvature-tensor-second-fundamental-form
source_book: gtm051
source_chapter: "3"
source_section: "3.8"
---

**Proof of Lemma 3.8.5.**

This is an immediate consequence of the Gauss equation, Theorem 3.8.3 (i). Recall the Gauss equation:

$$
\Gamma_{ij,k}^m - \Gamma_{ik,j}^m + \sum_l (\Gamma_{ij}^l \Gamma_{lk}^m - \Gamma_{ik}^l \Gamma_{lj}^m) = \sum_l (h_{ij} h_{kl} - h_{ik} h_{jl}) g^{lm}.
$$

The left-hand side is precisely $R_{ijk}^m$ (Definition 3.8.4). Therefore,

$$
R_{ijk}^m = \sum_l (h_{ij} h_{kl} - h_{ik} h_{jl}) g^{lm}.
$$

Lowering the upper index using the metric, $R_{ijkl} = \sum_m g_{lm} R_{ijk}^m$, we obtain

$$
R_{ijkl} = \sum_{l',m} g_{lm} (h_{ij} h_{kl'} - h_{ik} h_{jl'}) g^{l'm} = (h_{ij} h_{kl} - h_{ik} h_{jl}) \sum_m g_{lm} g^{km}
$$

after reindexing. But $\sum_m g_{lm} g^{km} = \delta_l^k$, and a careful index manipulation yields

$$
R_{ijkl} = h_{ij} h_{kl} - h_{ik} h_{jl}.
$$

The antisymmetry properties $R_{ijkl} = -R_{jikl} = -R_{ijlk} = R_{klij}$ follow directly from this expression since the right-hand side manifestly satisfies these symmetries. In the 2-dimensional case ($i,j,k,l \in \{1,2\}$), the only potentially non-zero components are those where the indices take two distinct values, and $R_{1212}$ is the unique independent component. All others equal $R_{1212}$, $-R_{1212}$, or $0$ by antisymmetry. Evaluating $R_{1212} = h_{11}h_{22} - h_{12}h_{21} = \det(h_{ij})$ completes the proof.
