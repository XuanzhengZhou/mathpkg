---
role: proof
locale: en
of_concept: orthogonality-distinct-eigenfunctions
source_book: gtm017
source_chapter: "7"
source_section: "Additional Topics"
---

Using the eigenvalue equations and symmetry $r(t,\tau) = r(\tau,t)$,
$$\frac{1}{\lambda_1} \int_0^T \varphi_1(t)\varphi_2(t)dt = \iint_0^T \varphi_1(t)r(t,\tau)\varphi_2(\tau)d\tau dt$$
$$= \iint_0^T \varphi_2(\tau)r(\tau,t)\varphi_1(t)dt d\tau = \frac{1}{\lambda_2}\int_0^T \varphi_1(t)\varphi_2(t)dt.$$
Thus $(\frac{1}{\lambda_1} - \frac{1}{\lambda_2})\int \varphi_1\varphi_2 dt = 0$. Since $\lambda_1 \neq \lambda_2$, the integral vanishes.
