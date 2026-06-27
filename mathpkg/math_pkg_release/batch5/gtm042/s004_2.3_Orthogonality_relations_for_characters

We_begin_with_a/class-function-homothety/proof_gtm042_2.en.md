---
role: proof
locale: en
of_concept: class-function-homothety
source_book: gtm042
source_chapter: "2"
source_section: "2.5"
---

We first show that $\rho_f$ commutes with $\rho_s$ for all $s \in G$. Compute
$$\rho_s^{-1}\rho_f\rho_s = \sum_{t \in G} f(t)\rho_s^{-1}\rho_t\rho_s = \sum_{t \in G} f(t)\rho_{s^{-1}ts}.$$

Substituting $u = s^{-1}ts$, so that $t = sus^{-1}$, and using that $f$ is a class function ($f(sus^{-1}) = f(u)$), we obtain
$$\rho_s^{-1}\rho_f\rho_s = \sum_{u \in G} f(sus^{-1})\rho_u = \sum_{u \in G} f(u)\rho_u = \rho_f.$$

Thus $\rho_f \rho_s = \rho_s \rho_f$ for all $s \in G$. By Schur's lemma (Proposition 4 of Chapter 2), any linear operator on an irreducible representation that commutes with all $\rho_s$ is a scalar multiple of the identity. Hence $\rho_f$ is a homothety $\lambda \cdot \operatorname{id}_V$.

To determine $\lambda$, take traces. The trace of $\lambda \cdot \operatorname{id}_V$ is $n\lambda$. The trace of $\rho_f$ is
$$\operatorname{Tr}(\rho_f) = \sum_{t \in G} f(t)\operatorname{Tr}(\rho_t) = \sum_{t \in G} f(t)\chi(t).$$

Therefore,
$$\lambda = \frac{1}{n} \sum_{t \in G} f(t)\chi(t) = \frac{g}{n}(f|\chi^*). \quad \square$$
