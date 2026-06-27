---
role: proof
locale: en
of_concept: partition-of-unity-existence
source_book: gtm014
source_chapter: "1"
source_section: "4"
---

Let $\{V_\beta\}_{\beta \in J}$ be the locally finite refinement of $\{U_\alpha\}_{\alpha \in I}$ whose existence is guaranteed by Corollary 4.4. Define $g_\beta: X \rightarrow \mathbf{R}$ by

$$g_\beta(p) = \begin{cases} \gamma(\phi_\beta(p)) & \text{if } p \in V_\beta \\ 0 & \text{otherwise} \end{cases}$$

where $\gamma: \mathbf{R}^n \rightarrow \mathbf{R}$ is a smooth function which is positive on $B_2$ and zero off $B_2$ (using Lemma 4.5). Let $h(p) = \sum_{\beta \in J} g_\beta(p)$. Then $h$ is well-defined (i.e., the sum is finite), and $C^k$ since $\{V_\beta\}_{\beta \in J}$ is a locally finite covering for $X$. Also $h(p) > 0$ for all $p$. Let $\rho_\beta = (1/h)g_\beta$. Then $\{\rho_\beta\}_{\beta \in J}$ is a partition of unity subordinate to the cover $\{U_\alpha\}_{\alpha \in I}$.

For the moreover part, let $U_1, U_2, \ldots$ be the covering and let $f_i = \sum_{\beta \in J_i} \rho_\beta$ where $\beta \in J_i$ if $\mathrm{supp}\,\rho_\beta \subset U_i$ and $\mathrm{supp}\,\rho_\beta$ is not contained in any $U_k$ with $k < i$. Then the functions $f_i$ form the desired partition of unity with $\mathrm{supp}\,f_i \subset U_i$.
