---
role: proof
locale: en
of_concept: karhunen-loeve-coefficient-orthonormality
source_book: gtm017
source_chapter: "7"
source_section: "Additional Topics"
---

Using the definition and $E[X_t X_\tau] = r(t,\tau)$,
$$E Z_i Z_j = \sqrt{\lambda_i \lambda_j} \iint_0^T \varphi_i(t) \varphi_j(\tau) r(t,\tau) \, dt d\tau.$$
By the eigenvalue equation $\int_0^T r(t,\tau)\varphi_j(\tau)d\tau = \varphi_j(t)/\lambda_j$, this becomes $\sqrt{\lambda_i\lambda_j} \int_0^T \varphi_i(t)\varphi_j(t)/\lambda_j dt = \sqrt{\lambda_i/\lambda_j}\int_0^T \varphi_i(t)\varphi_j(t)dt = \delta_{ij}$, using orthonormality of the $\varphi_i$.
