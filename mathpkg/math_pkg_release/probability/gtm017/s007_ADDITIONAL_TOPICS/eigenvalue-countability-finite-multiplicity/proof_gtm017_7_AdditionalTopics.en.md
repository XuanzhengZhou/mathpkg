---
role: proof
locale: en
of_concept: eigenvalue-countability-finite-multiplicity
source_book: gtm017
source_chapter: "7"
source_section: "Additional Topics"
---

Let $\varphi_i$, $i=1,\ldots,n$, be orthonormal eigenfunctions with eigenvalues $\lambda_i$. Set $s_n(t,\tau) = r(t,\tau) - \sum_{i=1}^n \varphi_i(t)\varphi_i(\tau)/\lambda_i$. By positive definiteness, for any $g$ orthogonal to $\varphi_1,\ldots,\varphi_n$, $\iint g(t)s_n(t,\tau)g(\tau)dt d\tau \geq 0$. Integrating appropriately yields $\int_0^T r(t,t)dt \geq \sum_{i=1}^n 1/\lambda_i$.

For finite multiplicity: if infinitely many eigenfunctions shared one eigenvalue $\lambda$, the RHS would diverge, contradicting $\int r(t,t)dt < \infty$. For countability: if uncountably many eigenvalues existed, infinitely many would lie in some interval $(2^{-(k+1)},2^{-k}]$, again making the RHS unbounded.
