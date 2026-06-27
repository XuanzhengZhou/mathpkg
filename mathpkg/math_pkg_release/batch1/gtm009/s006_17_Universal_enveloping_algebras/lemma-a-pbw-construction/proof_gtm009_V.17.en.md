---
role: proof
locale: en
of_concept: lemma-a-pbw-construction
source_book: gtm009
source_chapter: "V"
source_section: "17.4"
---
The proof proceeds by induction on $m$. For $m = 0$, $S_0 = F$, and one defines $f_0(x_\lambda \otimes 1) = z_\lambda$, which clearly satisfies $(A_0)$, $(B_0)$, and $(C_0)$ (the latter vacuously since $S_{-1} = 0$).

Assume $f_{m-1}$ has been constructed and satisfies the three conditions. To define $f_m$ on $x_\lambda \otimes z_\Sigma$ with $z_\Sigma \in S_m$, write $\Sigma = (\mu, \Psi)$ where $\mu$ is the first (smallest) index in $\Sigma$ and $z_\Psi \in S_{m-1}$. Three cases are distinguished:

Case 1: $\lambda \leq \mu$. Define $f_m(x_\lambda \otimes z_\Sigma) = z_\lambda z_\Sigma$ (forced by $(A_m)$).

Case 2: $\lambda > \mu$. By induction, $f_{m-1}(x_\mu \otimes z_\Psi) = z_\mu z_\Psi + w$ with $w \in S_{m-2}$ by $(B_{m-2})$. Then define
$$
f_m(x_\lambda \otimes z_\Sigma) = z_\mu f_{m-1}(x_\lambda \otimes z_\Psi) + f_{m-1}([x_\lambda x_\mu] \otimes z_\Psi) + f_{m-1}(x_\lambda \otimes w).
$$
This definition is forced by the requirement that $(C_m)$ hold (applied with the roles of $\lambda$ and $\mu$ reversed and using the induction hypothesis). One verifies that this definition satisfies $(A_m)$, $(B_m)$, and $(C_m)$ for all choices of indices, completing the induction step. The verification of $(C_m)$ uses the Jacobi identity in $L$ and the induction hypothesis on lower $m$.
