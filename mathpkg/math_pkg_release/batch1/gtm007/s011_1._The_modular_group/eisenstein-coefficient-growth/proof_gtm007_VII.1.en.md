---
role: proof
locale: en
of_concept: eisenstein-coefficient-growth
source_book: gtm007
source_chapter: "VII"
source_section: "§1. The modular group"
---

This follows from the explicit computation of the Fourier expansion of $G_k$ using the Poisson summation formula or the Lipschitz summation formula. The key identity:
$$
\sum_{(m,n) \neq (0,0)} \frac{1}{(mz+n)^k} = 2\zeta(k) + \frac{2(2\pi i)^k}{(k-1)!} \sum_{n=1}^\infty \sigma_{k-1}(n) q^n.
$$
The divisor function $\sigma_{k-1}(n) = \sum_{d \mid n} d^{k-1}$ satisfies $\sigma_{k-1}(n) \leq n^{k-1} \sum_{d=1}^\infty 1/d^{k-1} = O(n^{k-1})$.
