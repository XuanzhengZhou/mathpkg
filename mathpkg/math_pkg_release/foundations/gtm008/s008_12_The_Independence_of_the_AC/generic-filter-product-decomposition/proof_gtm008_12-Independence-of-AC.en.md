---
role: proof
locale: en
of_concept: generic-filter-product-decomposition
source_book: gtm008
source_chapter: "12"
source_section: "12. The Independence of the AC"
---

\textbf{Proof of Theorem 12.6.} Let $S$ be dense in $P$ in $M$. Define $S_2 = \{p_2 \in P_2 \mid \langle p_1, p_2 \rangle \in S \text{ for some } p_1 \in G_1\}$. Then $S_2 \in M[G_1]$. We claim $S_2$ is dense in $P_2$. Let $q_2 \in P_2$ and define $S_1 = \{p_1 \in P_1 \mid (\{p_1\} \times [q_2]) \cap S \neq 0\}$. Since $S$ is dense, $(\forall q_1 \in P_1)(\exists p_1 \leq q_1)(\exists p_2 \leq q_2)[\langle p_1, p_2 \rangle \in S]$. Hence $S_1$ is dense in $P_1$, so $G_1 \cap S_1 \neq 0$, implying $(G_1 \times [q_2]) \cap S \neq 0$. Thus $S_2$ is dense, and since $G_2$ is $P_2$-generic over $M[G_1]$, $G_2 \cap S_2 \neq 0$, so $(G_1 \times G_2) \cap S \neq 0$. Therefore $G_1 \times G_2$ is $P$-generic over $M$.

\textbf{Proof of Theorem 12.7.} Let $G$ be $P$-generic over $M$. Define $G_1 = \{p_1 \in P_1 \mid \langle p_1, 1 \rangle \in G\}$ and $G_2 = \{p_2 \in P_2 \mid \langle 1, p_2 \rangle \in G\}$. Using density arguments similar to Theorem 12.6, one verifies that $G_1$ is $P_1$-generic over $M$, $G_2$ is $P_2$-generic over $M[G_1]$, and $G = G_1 \times G_2$.
