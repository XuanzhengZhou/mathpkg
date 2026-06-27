---
role: proof
locale: en
of_concept: "jessen-the-relation"
source_book: gtm025
source_chapter: "Further Topics"
source_section: "22.17"
---

We wish to apply the limit theorem (20.56). To do this, consider the $\sigma$-algebra $\mathcal{M}_{\Omega_n}$ of subsets of $T

(22.12) and (21.13), we write

$$\eta(A) = \int_T \xi_A(t) f(t) d\mu(t)$$

$$= \int_{T_{\Omega_n} \times T_{\Omega'_n}} \xi_A_{\Omega_n} \times T_{\Omega'_n} (t_{\Omega_n}, t_{\Omega'_n}) f(t_{\Omega_n}, t_{\Omega'_n}) d(\mu_{\Omega_n} \times \mu_{\Omega'_n}) (t_{\Omega_n}, t_{\Omega'_n})$$

$$= \int_{T_{\Omega_n} \times T_{\Omega'_n}} \xi_A_{\Omega_n} \times T_{\Omega'_n} (t_{\Omega_n}, t_{\Omega'_n}) f(t_{\Omega_n}, t_{\Omega'_n}) d\mu_{\Omega'_n} (t_{\Omega'_n}) d\mu_{\Omega_n} (t_{\Omega_n}).$$

(2)

Since $\xi_A_{\Omega_n} \times T_{\Omega'_n} (t_{\Omega_n}, t_{\Omega'_n}) = \xi_A_{\Omega_n} (t_{\Omega_n})$, the last integral in (2) is equal to

$$\int_{T_{\Omega_n}} \xi_A_{\Omega_n} (t_{\Omega_n}) \int_{T_{\Omega'_n}} f(t_{\Omega_n}, t_{\Omega'_n}) d\mu_{\Omega'_n} (t_{\Omega'_n}) d\mu_{\Omega_n} (t_{\Omega_n})$$

$$= \int_{T_{\Omega_n}} \xi_A_{\Omega_n} (t_{\Omega_n}) f_n(t_{\Omega_n}) d\mu_{\Omega_n} (t_{\Omega_n}).$$

(3)

A similar but simpler computation using (22.12) and (21.13) shows that the right side of (3) is in fact

$$\int_T \xi_A(t) f_n(t) d\mu(t).$$

$= \eta_n(\{1\}) = \frac{1}{2}$. If $n$ is odd, then $\eta_n(\{0\}) = 1$ and $\eta_n(\{1\}) = 0$. Show that $\eta$ and $\mu$ are mutually singular. Let $M^{(n)}$ be defined as in (22.16). Show that $\eta$ on $M^{(n)}$ is absolutely continuous with respect to $\mu$ on $M^{(n)}$ and that $2^n \xi_{S_n}$ is its LEBESGUE-RADON-NIKODYM derivative. Now apply (20.56).]

(c) Find a set $D$ of $\eta$-measure 1 and $\mu$-measure 0 such that $\lim_{n \to \infty} 2^n \xi_{S_n}(t) = \infty$ $\eta$-almost everywhere on $D$. Note that this is consistent with (20.53.iv).

We now present an important corollary of Theorem (22.17).
