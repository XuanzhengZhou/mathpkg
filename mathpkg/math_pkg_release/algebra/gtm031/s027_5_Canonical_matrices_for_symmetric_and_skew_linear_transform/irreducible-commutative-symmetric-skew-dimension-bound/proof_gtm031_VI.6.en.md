---
role: proof
locale: en
of_concept: irreducible-commutative-symmetric-skew-dimension-bound
source_book: gtm031
source_chapter: "VI"
source_section: "6"
---

Let $\pi(\lambda)$ be an irreducible factor of the characteristic polynomial of any $A \in \Omega$. Then the characteristic space $\mathfrak{R}_{\pi(\lambda)}$ of $A$ is invariant relative to $\Omega$. Since $\mathfrak{R}$ is irreducible relative to $\Omega$, we have $\mathfrak{R}_{\pi(\lambda)} = \mathfrak{R}$, so that $\pi(A) = 0$.

If $A$ is symmetric, then we know that $\pi(\lambda) = \lambda - \rho$; hence, in this case, $A$ is a scalar multiplication.

If $A$ is skew, either $\pi(\lambda) = \lambda$, in which case $A = 0$, or $\pi(\lambda) = \lambda^2 + \delta^2$, $\delta \neq 0$. In the latter case $A^2 = -\delta^2 1$; hence $A^{-1}$ exists and is skew. Then if $B$ is any other skew transformation in the set,

$$M = BA^{-1} = A^{-1}B = (-A^{-1})'(-B') = (A^{-1})'B' = M'$$

is symmetric. Since $M$ commutes with every member of $\Omega$, the argument used before shows that $M$ is a scalar multiplication. Hence $B = \mu A$.

Thus we see that either the set $\Omega$ consists of scalar multiplications only, or $\Omega$ consists of scalar multiplications and multiples of a single skew $A$ in this set. In the former case every subspace of $\mathfrak{R}$ is invariant relative to $\Omega$; irreducibility then forces $\dim \mathfrak{R} = 1$. In the latter case, the irreducible space can be at most two-dimensional, as the action is governed by the single skew transformation $A$.
