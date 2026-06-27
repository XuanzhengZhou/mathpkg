---
role: proof
locale: en
of_concept: normalized-matrix-explicit-form
source_book: gtm031
source_chapter: "3"
source_section: "16"
---

The general condition is $\delta_i \beta_{ij} \equiv 0 \pmod{\delta_j}$ for all $i, j$. We analyze the four cases using the divisibility chain $\delta_1 \mid \delta_2 \mid \cdots \mid \delta_u$ and $\delta_j = 0$ for $j > u$.

**Case 1 ($i \geq j$):** Since $\delta_i \mid \delta_i$ and $\delta_j \mid \delta_i$, we have $\delta_i$ is a multiple of $\delta_j$, so $\delta_i \equiv 0 \pmod{\delta_j}$. Thus $\delta_i \beta_{ij} \equiv 0 \cdot \beta_{ij} = 0 \pmod{\delta_j}$ for any $\beta_{ij}$. No restriction.

**Case 2 ($i \leq u$, $j > u$):** Here $\delta_j = 0$. The condition $\delta_i \beta_{ij} \equiv 0 \pmod{0}$ means $\delta_i \beta_{ij}$ must be a multiple of $0$, i.e., $\delta_i \beta_{ij} = 0$. Since $\delta_i \neq 0$ (as $i \leq u$), this forces $\beta_{ij} = 0$.

**Case 3 ($i, j > u$):** Here $\delta_i = \delta_j = 0$. The condition $0 \cdot \beta_{ij} \equiv 0 \pmod{0}$ is vacuously satisfied. No restriction.

**Case 4 ($i < j \leq u$):** Here $\delta_i \mid \delta_j$ but $\delta_i \neq \delta_j$ in general. Since $\delta_i \mid \delta_j$, we can write $\delta_j = \delta_i \eta_{ij}$ with $\eta_{ij} \in \mathfrak{o}$. The condition $\delta_i \beta_{ij} \equiv 0 \pmod{\delta_j} = \pmod{\delta_i \eta_{ij}}$ is equivalent to $\delta_i \beta_{ij} = \gamma \delta_i \eta_{ij}$ for some $\gamma$, i.e., $\delta_i (\beta_{ij} - \gamma \eta_{ij}) = 0$. Since $\mathfrak{o}$ is an integral domain and $\delta_i \neq 0$, this gives $\beta_{ij} = \gamma \eta_{ij}$, so $\beta_{ij} \equiv 0 \pmod{\eta_{ij}}$.
