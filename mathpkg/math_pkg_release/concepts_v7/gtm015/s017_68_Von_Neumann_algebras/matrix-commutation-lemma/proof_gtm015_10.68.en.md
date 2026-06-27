---
role: proof
locale: en
of_concept: matrix-commutation-lemma
source_book: gtm015
source_chapter: "10"
source_section: "68"
---

# Proof of Commutation criterion for matricial representation of operators

Proof. For every $y \in K$, the $i$th coordinate of $y$ is $U_i^* y$, thus

$$(\tilde{T} P y)_i = U_i^*(\tilde{T} P y) = T (U_i^* P y) = T \sum_j U_i^* P U_j (U_j^* y) = \sum_j T P_{ij} (U_j^* y),$$

whereas

$$(P \tilde{T} y)_i = U_i^*(P \tilde{T} y) = \sum_j U_i^* P U_j (U_j^* \tilde{T} y) = \sum_j P_{ij} T (U_j^* y).$$

If $\tilde{T} P = P \tilde{T}$, then comparing the $i$th coordinates gives $T P_{ij} = P_{ij} T$ for all $i, j$. Conversely, if $T P_{ij} = P_{ij} T$ for all $i, j$, then the above computations show $(\tilde{T} P y)_i = (P \tilde{T} y)_i$ for every $y \in K$ and every $i$, hence $\tilde{T} P = P \tilde{T}$.
