---
role: proof
locale: en
of_concept: index-of-covering-equals-sheets
source_book: gtm047
source_chapter: "7"
source_section: "24"
---

**Proof.** Let $g^{-1}(P_0) = \{ \tilde{P}_0, \tilde{P}_1, \ldots \}$, with $\tilde{P}_i \neq \tilde{P}_j$ for $i \neq j$. For each $i$, choose a path $\tilde{\gamma}_i$ from $\tilde{P}_0$ to $\tilde{P}_i$ in $\tilde{M}$, and let $\gamma_i = g \circ \tilde{\gamma}_i$. Then $\gamma_i$ is a path in $M$ from $P_0$ to $P_0$, hence a loop. The cosets $\overline{\gamma_i} \cdot \pi_0$ are distinct and exhaust $\pi(M, P_0)$. If $\overline{\gamma_i} \cdot \pi_0 = \overline{\gamma_j} \cdot \pi_0$, then $\overline{\gamma_i \gamma_j^{-1}} \in \pi_0$, so by Theorem 3, $\overline{\gamma_i \gamma_j^{-1}}$ has a lifting to a closed path based at $\tilde{P}_0$. This would imply $\tilde{P}_i = \tilde{P}_j$, a contradiction. Hence the cosets are distinct. Moreover, for any $\overline{p} \in \pi(M, P_0)$, its lift $\tilde{p}$ starting at $\tilde{P}_0$ ends at some $\tilde{P}_i$, so $\overline{p} \cdot \pi_0 = \overline{\gamma_i} \cdot \pi_0$. Thus the cosets form a partition of $\pi(M, P_0)$, and the number of cosets equals the number of points in $g^{-1}(P_0)$, which is $k$.
