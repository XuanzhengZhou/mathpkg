---
role: proof
locale: en
of_concept: matrix-endomorphism-homomorphism
source_book: gtm031
source_chapter: "3"
source_section: "16"
---

Define $\varphi: \mathfrak{M} \to \mathfrak{B}$ by $\varphi(\beta) = B$ where $f_i B = \sum_j \beta_{ij} f_j$. This is well-defined by the existence result: the condition $\delta_i \beta_{ij} \equiv 0 \pmod{\delta_j}$ guarantees that the images $g_i = \sum_j \beta_{ij} f_j$ satisfy $\epsilon_i \mid \delta_i$, so $B$ is a valid $\mathfrak{o}$-endomorphism.

For additivity, if $\varphi(\beta) = B$ and $\varphi(\beta') = B'$, then $f_i(B+B') = f_i B + f_i B' = \sum_j \beta_{ij} f_j + \sum_j \beta'_{ij} f_j = \sum_j (\beta_{ij} + \beta'_{ij}) f_j$, so $\varphi(\beta + \beta') = B + B'$.

For multiplication, $f_i (B \circ B') = (f_i B) B' = (\sum_k \beta_{ik} f_k) B' = \sum_k \beta_{ik} (f_k B') = \sum_k \beta_{ik} \sum_j \beta'_{kj} f_j = \sum_j (\sum_k \beta_{ik} \beta'_{kj}) f_j$, so $\varphi(\beta \beta') = B \circ B'$.

Surjectivity follows from the determination lemma: every $B \in \mathfrak{B}$ is determined by the $g_i = f_i B$, and writing $g_i = \sum_j \beta_{ij} f_j$ yields a matrix $(\beta)$ which necessarily satisfies the congruence condition, so $(\beta) \in \mathfrak{M}$ and $\varphi(\beta) = B$.
