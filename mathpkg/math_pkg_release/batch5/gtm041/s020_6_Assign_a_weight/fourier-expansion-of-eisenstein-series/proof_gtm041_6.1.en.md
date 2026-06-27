---
role: proof
locale: en
of_concept: fourier-expansion-of-eisenstein-series
source_book: gtm041
source_chapter: "6"
source_section: "6.1"
---

The Fourier expansion of $G_{2k}(\tau)$ is stated in this section as:

$$G_{2k}(\tau) = 2\zeta(2k) + \frac{2(2\pi i)^{2k}}{(2k-1)!} \sum_{n=1}^{\infty} \sigma_{2k-1}(n) e^{2\pi i n \tau}.$$

The derivation proceeds by separating the lattice sum $G_{2k}(\tau) = \sum_{(m,n) \neq (0,0)} (m + n\tau)^{-2k}$ into the term with $n = 0$ (giving the constant $2\zeta(2k) = 2\sum_{m=1}^{\infty} m^{-2k}$) and the terms with $n \neq 0$. For fixed $n \neq 0$, summing over all $m \in \mathbb{Z}$ and using the identity

$$\sum_{m=-\infty}^{\infty} \frac{1}{(m + n\tau)^{2k}} = \frac{(2\pi i)^{2k}}{(2k-1)!} \sum_{d=1}^{\infty} d^{2k-1} e^{2\pi i d n \tau}$$

(derived via Poisson summation or the Lipschitz summation formula) yields the Fourier coefficients. Reindexing with $d \mid n$ produces the divisor sum $\sigma_{2k-1}(n)$. The full proof is presented in detail in later sections of the book.
