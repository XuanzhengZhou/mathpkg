---
role: proof
locale: en
of_concept: forgetful-functor-grp-lifts-limits
source_book: gtm005
source_chapter: "V"
source_section: "1. Creation of Limits"
---

By Theorem 1 (Completeness of $\mathbf{Set}$), take $L = \operatorname{Cone}(*, UH)$, the set of all cones from the one-point set to $UH$. Define the product of two such cones $\sigma, \tau \in L$ by $(\sigma \tau)_j = \sigma_j \tau_j$, using the group multiplication in each $H_j$. The identity cone has $1_j = 1_{H_j}$, and the inverse of $\sigma$ is given by $(\sigma^{-1})_j = (\sigma_j)^{-1}$. These operations are well-defined because each $H_u : H_j \to H_k$ (for $u: j \to k$ in $J$) is a group homomorphism, so $H_u(\sigma_j \tau_j) = H_u(\sigma_j) H_u(\tau_j) = \sigma_k \tau_k$, ensuring the product cone is compatible. The group axioms in $L$ follow directly from the group axioms in each $H_j$. By construction, each $v_j: L \to UH_j$ is a group homomorphism. Any other cone $\tau: M \to H$ in $\mathbf{Grp}$ from a group $M$ yields, via $U$, a cone in $\mathbf{Set}$, which factors uniquely through $v$ by the universal property in $\mathbf{Set}$. The unique factoring map is a group homomorphism because its components are. Hence $L$ with cone $v$ is the limit in $\mathbf{Grp}$.
