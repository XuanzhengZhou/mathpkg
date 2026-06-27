---
role: proof
locale: en
of_concept: spatial-isotropy-of-stress-energy-tensor
source_book: gtm048
source_chapter: "5"
source_section: "7"
---

*Proof.* Suppose $\sigma \in \mathcal{O}^3$ and denote the extension of $\sigma$ to $(r, s)$ tensors by $\sigma_s^r: T_s^r(M_z) 	o T_s^r(M_z)$ (Exercise 0.0.14). Then $\sigma_2^0(g_z) = g_z$ and $\sigma$ preserves the time orientation (Section 2.1.7). $\sigma$ is therefore a diffeomorphism of the future lightcone $\mathcal{L}_z^+$ onto itself. By Proposition 5.6.1 the natural volume element $\Lambda_z$ of $\mathcal{L}_z^+$ must obey $(\sigma^{-1})^*\Lambda_z = \Lambda_z$. Thus for all $\omega \in M_z^*$, we have (integration over $\mathcal{L}_z^+$ will be understood in the following):

$$(\sigma_0^2\hat{T})(\omega, \omega) = \hat{T}(\sigma_1^0\omega, \sigma_1^0\omega)$$

$$= \int [(\sigma_1^0\omega)^\sim]^2 F\Lambda_z$$

$$= \int 	ilde{\omega}^2(F \circ \sigma^{-1})[(\sigma^{-1})^*\Lambda_z]$$

$$= \int 	ilde{\omega}^2 F\Lambda_z = \hat{T}(\omega, \omega).$$

Thus $\sigma_0^2\hat{T} = \hat{T}$---that is, $\hat{T}$ is spatially isotropic for $(z, Z)$.
