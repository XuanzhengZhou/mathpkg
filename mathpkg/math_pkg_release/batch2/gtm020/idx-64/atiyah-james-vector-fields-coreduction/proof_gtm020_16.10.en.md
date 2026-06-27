---
role: proof
locale: en
of_concept: atiyah-james-vector-fields-coreduction
source_book: gtm020
source_chapter: "16"
source_section: "10"
---

**Proof.** By the construction in 12(1.1), there are $\rho(n)$ orthonormal vector fields on $S^{qn-1}$ for any integer $q$, and by (9.4), if $qn \geq 2(\rho(n) + 1)$, the shunted projective space $\mathbf{R}P^{qn-1}/\mathbf{R}P^{qn-\rho(n)-2}$ is reducible.

Let $r$ denote the order of $J(\xi_{\rho(n)})$ in $J(\mathbf{R}P^{\rho(n)})$, where $J$ denotes the $J$-homomorphism and $\xi_{\rho(n)}$ is the canonical $\rho(n)$-dimensional vector bundle over $\mathbf{R}P^{\rho(n)}$. For all integers $p$ satisfying $rp - qn = m \geq 1$, the shunted projective space $\mathbf{R}P^{m+\rho(m)}/\mathbf{R}P^{m-1}$ is an $S$-dual of $\mathbf{R}P^{qn-1}/\mathbf{R}P^{qn-\rho(n)-2}$. By $S$-duality, the reducibility of the latter implies the $S$-coreducibility of the former, and therefore $\mathbf{R}P^{m+\rho(m)}/\mathbf{R}P^{m-1}$ is $S$-coreducible for $m \geq \rho(n) + 3$.

By (2.2), for large $m$, the space $\mathbf{R}P^{m+\rho(m)}/\mathbf{R}P^{m-1}$ is $S$-coreducible if and only if it is coreducible (without stabilization).

Finally, if $p$ is chosen to be divisible by $2n$ and $q$ is odd, then $m = rp - qn$ takes the form $m = tn$ where $t$ is an odd number. In this case, $\rho(m) = \rho(n)$ by the periodicity properties of the Radon-Hurwitz number $\rho$. This proves the theorem.
