---
role: proof
locale: en
of_concept: compactly-supported-vector-field-diffeomorphism
source_book: gtm014
source_chapter: "III"
source_section: "3. A Characterization of Trivial Deformations"
---

*Proof.* Since $\zeta$ is compactly supported and $\partial/\partial t_k$ has a globally defined one parameter group, Corollary 6.5 of Chapter I guarantees that $\zeta + \partial/\partial t_k$ has a globally defined one parameter group

$$\phi: (X \times \mathbf{R}^k) \times \mathbf{R} \rightarrow X \times \mathbf{R}^k.$$

Let $e_k = (0, \ldots, 0, 1) \in \mathbf{R}^k$. We claim that $\phi_s: X \times \{v\} \rightarrow X \times \{v + s e_k\}$. Let $p = (x, v) \in X \times \{v\}$. Then

$$(d\rho)_{p}(\zeta_p + \partial/\partial t_k|_p) = (d\rho)_p(\zeta_p) + (d\rho)_p(\partial/\partial t_k|_p).$$

Since the $\mathbf{R}^k$-component of $\zeta$ is zero, $(d\rho)_p(\zeta_p) = 0$. Also $(d\rho)_p(\partial/\partial t_k|_p) = \partial/\partial t_k|_{\rho(p)} = \partial/\partial t_k|_v$, which is precisely the generator of translation by $e_k$ in $\mathbf{R}^k$. Hence the flow $\phi_s$ of $\zeta + \partial/\partial t_k$ projects under $\rho: X \times \mathbf{R}^k \to \mathbf{R}^k$ to the flow of $\partial/\partial t_k$ on $\mathbf{R}^k$, which is translation by $s e_k$. This proves the claim.

Now define $g = \phi_1$, the time-one map of the flow. Then $g$ is a diffeomorphism (being the time-one map of a global flow). By the claim, $g$ maps $X \times \{v\}$ to $X \times \{v + e_k\}$, so $g$ is a deformation of $\text{id}_X$. Finally, by the definition of the flow,

$$(dg)_{g^{-1}(p)}\left(\frac{\partial}{\partial t_k}\bigg|_{g^{-1}(p)}\right) = \frac{d}{ds}\bigg|_{s=0} \phi_s(g^{-1}(p)) = (\zeta + \partial/\partial t_k)_p,$$

which is exactly the pushforward identity $(*)$. $\square$
