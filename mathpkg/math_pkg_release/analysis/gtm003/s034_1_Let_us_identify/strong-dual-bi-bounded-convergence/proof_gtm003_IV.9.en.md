---
role: proof
locale: en
of_concept: strong-dual-bi-bounded-convergence
source_book: gtm003
source_chapter: "IV"
source_section: "9"
---

We first prove the assertion, assuming that both $E$ and $F$ are (DF)-spaces. Then clearly $E \times F$ is a (DF)-space and the topology of bi-bounded convergence on $\mathcal{B}(E, F)$ is the topology of bounded convergence in $E \times F$, hence metrizable. Since this topology is coarser than $\beta(\mathcal{B}(E, F), E \tilde{\otimes} F)$, it suffices to show that the identity map of $\mathcal{B}_b(E, F)$ onto $\mathcal{B}_{\beta}(E, F)$ is continuous; for this, in turn, it suffices that every null sequence in $\mathcal{B}_b(E, F)$ be equicontinuous.

It follows that $u \in \mathcal{L}(E'_\beta, F_H)$. Moreover, $B$ is clearly simply bounded in $\mathcal{L}(E'_\beta, F_H)$ and hence equicontinuous; consequently, there exists a convex, circled 0-neighborhood $V$ in $E'_\beta$ such that $B(V) \subset H$. Now denote by $E_1$ the Banach space which is the completion of $[E']_V$; since $E'_\beta$ is nuclear by (9.6), the canonical map $\phi_V$ of $E'_\beta$ into $E_1$ is nuclear, say of the form $\sum_{i=1}^{\infty} \lambda_i x_i \otimes y_i$, where $\sum_{i=1}^{\infty} |\lambda_i| \leq 1$, and $\{x_i\}, \{y_i\}$ are bounded sequences in $E, E_1$, respectively. If $\tilde{u}$ denotes the linear map of $E_1$ into $F_H$ associated with $u \in B$, then the family $B_2 = \{\tilde{u}(y_i): u \in B, i \in \mathbb{N}\}$ is bounded in $F_H$ (hence in $F$), and we obtain

$$u = \sum_{i=1}^{\infty} \lambda_i x_i \otimes \tilde{u}(y_i)$$

for all $u \in B$. Letting $B_1 = \{x_i: i \in \mathbb{N}\}$, it follows that $B \subset (\Gamma B_1 \otimes B_2)^-$, since the series for $u$ converges in $E \tilde{\otimes} F$; the proof is complete.
