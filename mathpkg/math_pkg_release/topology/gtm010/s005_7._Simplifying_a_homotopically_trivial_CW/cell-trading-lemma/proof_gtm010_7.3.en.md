---
role: proof
locale: en
of_concept: cell-trading-lemma
source_book: gtm010
source_chapter: "7"
source_section: "7"
---

Let $\varphi_i^r: I^r \to K$ be a characteristic map for $e_i^r$ ($i = 1, \dots, k_r$). So $\varphi_i^r(\partial I^r) \subset K^{r-1} = L^{r-1}$ and $\varphi_i^r: (I^r, \partial I^r) \to (K, L)$. Since $\pi_r(K, L) = 0$, there is a map $F_i: I^{r+1} \to K$ such that $F_i|I^r = \varphi_i^r$.

Construct $P = K \cup \bigcup_i E_i^{r+1}$ where each $E_i^{r+1}$ is attached along $F_i$. Then $P_0 = L \cup \bigcup e_i^r \cup \bigcup E_i^{r+1}$ is a subcomplex. Since each $E_i^{r+1}$ has $e_i^r$ as a face, $P_0 \searrow L$. Let $g: P_0 \to L$ be a cellular deformation corresponding to this collapse. Applying (5.9), $K \nearrow P \cup_g L$ rel $L$, where the cells of $P \cup_g L$ have been rearranged so that the $r$-cells disappear and additional $(r+1)$-cells appear.
