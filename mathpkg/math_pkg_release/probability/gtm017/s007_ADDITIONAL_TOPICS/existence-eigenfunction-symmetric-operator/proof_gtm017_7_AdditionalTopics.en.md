---
role: proof
locale: en
of_concept: existence-eigenfunction-symmetric-operator
source_book: gtm017
source_chapter: "7"
source_section: "Additional Topics"
---

Assume $r(t,\tau) = r(\tau,t)$. Define $N_R = \sup_{\|f\|=1} |(Rf,f)|$. One can show $\|R\| = N_R$ for symmetric $R$. Let $f_n$ with $\|f_n\|=1$ satisfy $(Rf_n,f_n) \to \lambda = \|R\|$ (assuming $R$ positive definite).

Consider $\|Rf_n - \lambda f_n\|^2 = \|Rf_n\|^2 - 2\lambda(Rf_n,f_n) + \lambda^2\|f_n\|^2$. Since $\|Rf_n\| \leq \|R\| = \lambda$ and $(Rf_n,f_n) \to \lambda$, the RHS tends to $\leq \lambda^2 - 2\lambda^2 + \lambda^2 = 0$. Thus $Rf_n - \lambda f_n \to 0$ in mean square.

By complete continuity, there exists a convergent subsequence $Rf_{n_k}$. Since $Rf_{n_k} \to \lambda f_{n_k}$, $f_{n_k}$ itself converges to some $\varphi$. Taking limits gives $R\varphi = \lambda\varphi$ with $\lambda = \|R\|$.
