---
role: proof
locale: en
of_concept: cell-trading-lemma
source_book: gtm010
source_chapter: "7"
source_section: "7"
---

Let $\varphi_i^r: I^r \rightarrow K$ be a characteristic map for $e_i^r$ ($i = 1, 2, \ldots, k_r$). So $\varphi_i^r(\partial I^r) \subset K^{r-1} = L^{r-1}$ and $\varphi_i^r:(I^r, \partial I^r) \rightarrow (K, L)$. Since $\pi_r(K, L) = 0$ there is a map $F_i: I^{r+1} \rightarrow K$ with $F_i|I^r = \varphi_i^r$ and $F_i(\partial I^{r+1} - I^r) \subset L$. These maps are used to enlarge the complex and then collapse it, effectively trading $r$-cells for $(r+1)$-cells.

Consider $P_0 = L \cup \bigcup e_i^r \cup \bigcup E_i^{r+1}$. Since $\psi_i(\partial J^{r+1}) = F_i(\partial I^{r+1}) \subset K^r$, $P_0$ is a well-defined subcomplex of $P$. Also $I^r$ is a face of $J^{r+1}$ such that $\psi_i|I^r = \varphi_i$, a characteristic map for $e_i^r$. So we have $P_0 \searrow L$. Let $g: P_0 \rightarrow L$ be a cellular deformation corresponding to this collapse. Applying (5.9), and letting $G: P \rightarrow P \cup_g L$ be the map induced by $g$, we have $K \nearrow P \cup_g L$, rel $L$. The proof is completed by setting $M = P \cup_g L$.
