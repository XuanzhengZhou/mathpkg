---
role: proof
locale: en
of_concept: character-of-induced-representation
source_book: gtm042
source_chapter: "3"
source_section: "3.3"
---

Let $R$ be a system of representatives of $G/H$. For each $r \in R$, let $\rho_r W$ be the corresponding subspace of $V$. For $u \in G$, the matrix of $\rho_u$ with respect to the decomposition $V = \bigoplus_{r \in R} \rho_r W$ is a block matrix $(\rho_{u,r})$ where $\rho_{u,r}$ is the restriction of $\rho_u$ to $\rho_r W$.

Let $R_u = \{ r \in R \mid r^{-1}ur \in H \}$. Observe that $r \in R_u$ if and only if $ur$ can be written as $rt$ with $t \in H$. Then
$$\chi_\rho(u) = \sum_{r \in R_u} \operatorname{Tr}_{\rho_r W}(\rho_{u,r}).$$

To compute $\operatorname{Tr}_{\rho_r W}(\rho_{u,r})$ for $r \in R_u$, note that $\rho_r$ defines an isomorphism of $W$ onto $\rho_r W$, and
$$\rho_r \circ \theta_t = \rho_{u,r} \circ \rho_r, \quad \text{with } t = r^{-1}ur \in H.$$

The trace of $\rho_{u,r}$ is thus equal to that of $\theta_t$, namely $\chi_\theta(t) = \chi_\theta(r^{-1}ur)$. Hence
$$\chi_\rho(u) = \sum_{r \in R_u} \chi_\theta(r^{-1}ur).$$

The second formula follows from the first by noting that all elements $s \in G$ in the left coset $rH$ (with $r \in R_u$) satisfy $\chi_\theta(s^{-1}us) = \chi_\theta(r^{-1}ur)$, and there are $|H|$ elements in each coset.
