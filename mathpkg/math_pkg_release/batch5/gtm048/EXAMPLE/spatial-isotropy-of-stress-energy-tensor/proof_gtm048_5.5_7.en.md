---
role: proof
locale: en
of_concept: spatial-isotropy-of-stress-energy-tensor
source_book: gtm048
source_chapter: "5"
source_section: "5.7"
---

Let $(z, Z)$ be an instantaneous observer such that $F$ is spatially isotropic for $(z, Z)$. This means $F(z, \psi Y) = F(z, Y)$ for all $\psi \in \mathcal{O}^3$ (the orthogonal group of the spatial subspace $Z^\perp$) and all $Y \in \mathcal{L}_z^+$.

Let $\sigma \in \mathcal{O}^3$ and denote by $\sigma_s^r: T_s^r(M_z) \to T_s^r(M_z)$ the extension of $\sigma$ to $(r,s)$-tensors (see Exercise 0.0.14). Since $\sigma \in \mathcal{O}^3$, we have:
\begin{itemize}
    \item $\sigma_2^0(g_z) = g_z$ (the metric is invariant under spatial rotations),
    \item $\sigma$ preserves the time orientation (Section 2.1.7).
\end{itemize}

Consequently, $\sigma$ maps the future lightcone $\mathcal{L}_z^+$ diffeomorphically onto itself: if $Y \in \mathcal{L}_z^+$ is future-pointing null, then $\sigma Y$ is also future-pointing null because $\sigma$ preserves both the metric and the time orientation.

By Proposition 5.6.1, the natural volume element $\Lambda_z$ on $\mathcal{L}_z^+$ is invariant under such diffeomorphisms: $(\sigma^{-1})^* \Lambda_z = \Lambda_z$.

Now, for any $\omega \in M_z^*$, we compute (all integrals are over $\mathcal{L}_z^+$):
\begin{align*}
(\sigma_0^2 \hat{T}_z)(\omega, \omega)
&= \hat{T}_z(\sigma_1^0 \omega, \sigma_1^0 \omega) \\
&= \int [(\sigma_1^0 \omega)^\sim]^2 F \Lambda_z \\
&= \int [\tilde{\omega} \circ \sigma^{-1}]^2 F \Lambda_z \\
&= \int \tilde{\omega}^2 (F \circ \sigma^{-1}) [(\sigma^{-1})^* \Lambda_z] \\
&= \int \tilde{\omega}^2 F \Lambda_z \\
&= \hat{T}_z(\omega, \omega).
\end{align*}

In step (3) we used $(\sigma_1^0 \omega)^\sim = \tilde{\omega} \circ \sigma^{-1}$, which follows from the definition of the extension $\sigma_0^1$ on covectors. In step (4) we performed the change of variables $Y \mapsto \sigma^{-1} Y$. In step (5) we used the spatial isotropy condition $F \circ \sigma^{-1} = F$ and the volume element invariance $(\sigma^{-1})^* \Lambda_z = \Lambda_z$.

Since $\hat{T}_z$ is symmetric, the equality of quadratic forms implies equality of the tensors:
$$\sigma_0^2 \hat{T}_z = \hat{T}_z.$$

Thus $\hat{T}_z$ is invariant under the action of $\mathcal{O}^3$ on $(2,0)$-tensors, which is precisely the definition of spatial isotropy for $(z, Z)$.
