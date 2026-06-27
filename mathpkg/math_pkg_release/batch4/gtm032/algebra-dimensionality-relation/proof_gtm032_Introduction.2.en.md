---
role: proof
locale: en
of_concept: algebra-dimensionality-relation
source_book: gtm032
source_chapter: "Introduction"
source_section: "2"
---

Let $\{u_i\}$, $1 \leq i \leq n$, be a basis for $\mathfrak{A}/\Phi$ and $\{\gamma_j\}$, $1 \leq j \leq m$, a basis for $\Phi/\mathrm{E}$. We claim that $\{\gamma_j u_i\}$ is a basis for $\mathfrak{A}/\mathrm{E}$.

First, let $a \in \mathfrak{A}$. Write $a = \sum_{i=1}^{n} \alpha_i u_i$ with $\alpha_i \in \Phi$. Each $\alpha_i = \sum_{j=1}^{m} \xi_{ij} \gamma_j$ with $\xi_{ij} \in \mathrm{E}$. Then $a = \sum_{i,j} \xi_{ij} (\gamma_j u_i)$, so the set $\{\gamma_j u_i\}$ spans $\mathfrak{A}/\mathrm{E}$.

For linear independence, suppose $\sum_{i,j} \xi_{ij} \gamma_j u_i = 0$ with $\xi_{ij} \in \mathrm{E}$. Then $\sum_i (\sum_j \xi_{ij} \gamma_j) u_i = 0$. Since the $u_i$ are linearly independent over $\Phi$ and each $\sum_j \xi_{ij} \gamma_j \in \Phi$, we have $\sum_j \xi_{ij} \gamma_j = 0$ for each $i$. Since the $\gamma_j$ are linearly independent over $\mathrm{E}$, each $\xi_{ij} = 0$. Thus $\{\gamma_j u_i\}$ is a basis, and $[\mathfrak{A}:\mathrm{E}] = nm = [\mathfrak{A}:\Phi][\Phi:\mathrm{E}]$.
