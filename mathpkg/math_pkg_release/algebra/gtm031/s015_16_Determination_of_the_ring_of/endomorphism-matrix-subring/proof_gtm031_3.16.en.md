---
role: proof
locale: en
of_concept: endomorphism-matrix-subring
source_book: gtm031
source_chapter: "3"
source_section: "16"
---

The condition $\delta_i \beta_{ij} \equiv 0 \pmod{\delta_j}$ is linear in the matrix entries. If $(\beta)$ and $(\beta')$ both satisfy the condition, then for any $\alpha \in \mathfrak{o}$:

$$\delta_i (\beta_{ij} + \beta'_{ij}) = \delta_i \beta_{ij} + \delta_i \beta'_{ij} \equiv 0 + 0 = 0 \pmod{\delta_j},$$

so $(\beta) + (\beta') \in \mathfrak{M}$. Similarly,

$$\delta_i (\alpha \beta_{ij}) = \alpha (\delta_i \beta_{ij}) \equiv \alpha \cdot 0 = 0 \pmod{\delta_j},$$

so $\alpha (\beta) \in \mathfrak{M}$.

For the product $(\beta)(\beta') = (\sum_k \beta_{ik} \beta'_{kj})$:

$$\delta_i \sum_k \beta_{ik} \beta'_{kj} = \sum_k (\delta_i \beta_{ik}) \beta'_{kj} \equiv \sum_k (\gamma_{ik} \delta_k) \beta'_{kj} = \sum_k \gamma_{ik} (\delta_k \beta'_{kj}) \equiv \sum_k \gamma_{ik} (\gamma'_{kj} \delta_j) = \left(\sum_k \gamma_{ik} \gamma'_{kj}\right) \delta_j \equiv 0 \pmod{\delta_j}.$$

Thus $\mathfrak{M}$ is closed under addition, additive inverses, and multiplication, and contains the identity matrix (since $\delta_i \cdot 1 \cdot \delta_{ij} \equiv 0 \pmod{\delta_j}$ for all $i,j$), hence $\mathfrak{M}$ is a subring of $\mathfrak{o}_t$.
