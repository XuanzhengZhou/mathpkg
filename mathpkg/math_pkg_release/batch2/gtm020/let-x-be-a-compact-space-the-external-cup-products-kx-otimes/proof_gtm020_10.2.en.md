---
role: proof
locale: en
of_concept: let-x-be-a-compact-space-the-external-cup-products-kx-otimes
source_book: gtm020
source_chapter: "11. Bott Periodicity in the Complex Case"
source_section: "5"
---


Proof. First, we prove that $\omega_G$ is a principal $G$-bundle. The translation function $\tau(a,a')$ is given by the continuous function $x_i(a)x_i(a')^{-1}$ on the open set $(t_i^{-1}(0,1) \times t_i^{-1}(0,1]) \cap E_G^*$, where $E_G^*$ is the subspace of pairs $(a,a')$ with $p(a) = p(a')$ in $B_G$. Finally, we observe that the open sets $t_i^{-1}(0,1) \times t_i^{-1}(0,1]$ for $0 \leq i$ cover $E_G^*$. Consequently, $\omega_G$ is a principal $G$-bundle.

Since $t_i(ay) = t_i(a)$ for $y \in G$, we can define a unique map $u_i: B_G \rightarrow [0,1]$ with the property that $u_i p = t_i$ on $E_G$. Now we show that $\omega_G$ is trivial over each $V_i = u_i^{-1}(0,1] = p(t_i^{-1}(0,1])$ by defining a cross section $s_i$ of $\omega_G$ over $V_i$. For this we use the map $s_i': t_i^{-1}(0,1] \rightarrow t_i^{-1}(0,1]$ defined by $s_i'(a) = ax_i(a)^{-1}$. This map has the property that $s_i'(ay) = ay(x_i(ay))

the antipodal map. The space $B_G(n)$ is $RP^n$. The inclusions $E_G(n) \subset E_G(n + 1)$ and $B_G(n) \subset B_G(n + 1)$ are just the natural inclusions $S^n \subset S^{n+1}$ and $RP^n \subset RP^{n+1}$. The space $E_G$ is $S^\infty$ and $B_G$ is $RP^\infty$.

The bundle $(S^{n+1}, p, RP^{n+1})$ is universal for dimensions $\leq n$.

11.4 Example $G = S^1$. The space $E_G(n)$ is just the $(2n + 1)$-sphere $S^{2n+1}$ up to a homeomorphism, and the action of $S^1$ on $E_G(n) = S^{2n+1}$ is by the relation $(z_0, z_1, \ldots, z_n)e^{i\theta} = (e^{i\theta}z_0, e^{i\theta}z_1, \ldots, e^{i\theta}z_n)$ for each $e^{i\theta} \in S^1$. The space $B_G(n)$ is $CP^n$, complex $n$-dimensional projective space. The inclusions $E_G(n) \subset E_G(n + 1)$ and $B_G(n) \subset B_G(n + 1)$ are just the natural inclusions $S^{2n+1} \subset S^{2n+3}$ and $CP^n \subset CP^{n+1}$. The space $E_G$ is $S^\infty$, and $B_G$ is $CP^\infty$.

The bundle $(S^{2n+1}, p, CP^n)$ is universal for dimensions $\leq 2n$.

12. Homotopy Classification of Numerable Principal $G$-Bundles

In this section, we prove that the bundle $\omega_G$ which comes from the Milnor construction is a universal principal $G$-bundle.
