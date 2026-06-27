---
role: proof
locale: en
of_concept: compatible-g-and-h-gradations
source_book: gtm023
source_chapter: "VI"
source_section: "§1. G-graded vector spaces"
---

**Forward direction.** Given compatible $G$ and $H$-gradations, define $E_{j,k} = E_j \cap F_k$. The compatibility condition states precisely that $E = \sum_{j,k} E_{j,k}$ is a direct decomposition. Assigning the degree $(j,k) \in G \oplus H$ to the subspace $E_{j,k}$ yields a $(G \oplus H)$-gradation.

**Converse direction.** Given a $(G \oplus H)$-gradation $E = \sum_{j,k} E_{j,k}$, define
$$E_j = \sum_{k \in H} E_{j,k}, \quad F_k = \sum_{j \in G} E_{j,k}.$$
Then $E = \sum_j E_j$ is a direct decomposition because the $E_{j,k}$ form a direct sum: any nontrivial relation $\sum_j e_j = 0$ with $e_j \in E_j$ would decompose as $\sum_{j,k} e_{j,k} = 0$ with $e_{j,k} \in E_{j,k}$, forcing each $e_{j,k} = 0$. This yields a $G$-gradation. Similarly for the $H$-gradation. These gradations are compatible because
$$E_j \cap F_k = \left( \sum_{k'} E_{j,k'} \right) \cap \left( \sum_{j'} E_{j',k} \right) = E_{j,k},$$
and the direct decomposition $E = \sum_{j,k} E_{j,k}$ is exactly the compatibility condition.
