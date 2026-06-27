---
role: proof
locale: en
of_concept: extreme-points-nonempty-gibbs
source_book: gtm040
source_chapter: "12"
source_section: "4"
---

**Proof.** Let $B_e$ comprise the extreme points of the Martin boundary for $P$ started with $\pi$, and let $\lambda$ denote harmonic measure. Theorem 10-41 applied to the constant regular function $h = 1$ shows that $\Pr_{\pi}[y_{\nu} \in B_e] = \lambda(B_e) = 1$. Since $\{y_n\}$ visits each state $(m, \kappa^m)$ at most once, the Martin kernel is given by

$$
K((m, \kappa^m), (n, \kappa^n)) = \frac{P^{(n-m)}_{(m, \kappa^m)(n, \kappa^n)}}{\sum_{\kappa^0} \pi(\kappa^0) P_{(0, \kappa^0)(n, \kappa^n)}}, \qquad n \geq m,
$$

and equals $0$ otherwise. Thus $y_{\nu}(\omega) \in B_e$ means that

$$
K((m, \kappa^m), x) = \lim_{n \to \infty} \frac{\nu([\kappa^m, \kappa^n(\omega)])}{\nu([\kappa^m]) \nu([\kappa^n(\omega)])}
$$

exists for every $(m, \kappa^m)$, and is a minimal regular function of $(m, \kappa^m)$. By Theorem 12-25, $K(\cdot, x)$ is minimal regular if and only if the corresponding Gibbs measure is extreme. Hence $\nu^{\kappa^n(\omega)}$, which is the measure corresponding to the regular function $K(\cdot, y_{\nu}(\omega))$, belongs to $\mathcal{E}_V$ for $\nu$-almost every $\omega$.
