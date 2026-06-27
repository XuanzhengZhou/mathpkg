---
role: proof
locale: en
of_concept: kam-fixed-points-mappings
source_book: gtm060
source_chapter: "Appendix 8"
source_section: "D.6"
---

The proof begins by linearizing the symplectic mapping at the fixed point. The assumption that all $2n$ eigenvalues lie on the unit circle and satisfy no low-order resonances ($\prod \lambda_i^{k_i} \neq 1$ for $\sum |k_i| \leq 4$) allows reduction to Birkhoff normal form:
$$(\tau, \varphi) \to (\tau, \varphi + \alpha(\tau)), \qquad \alpha(\tau) = \frac{\partial S}{\partial \tau},$$
where $S = \sum \omega_k \tau_k + \frac{1}{2} \sum \omega_{kl} \tau_k \tau_l$ and higher-order terms are truncated. Here $\tau_k = (p_k^2 + q_k^2)/2$ are action variables in polar symplectic coordinates.

The generating function $S$ plays the role of the unperturbed integrable Hamiltonian in the continuous case. The nondegeneracy condition $\det |\omega_{kl}| \neq 0$ allows the Kolmogorov-Newton iterative scheme to preserve $n$-dimensional invariant tori $\tau = \text{const}$. For $n = 1$, the existence of invariant circles near the fixed point ensures stability. Moser originally required 333 derivatives for smoothing at each Newton step; this was improved to 6 derivatives by Moser and Russmann using a refined smoothing technique (Nash-Moser implicit function theorem).
