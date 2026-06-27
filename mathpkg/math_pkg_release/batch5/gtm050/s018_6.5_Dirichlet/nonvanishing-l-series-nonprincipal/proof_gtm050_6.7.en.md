---
role: proof
locale: en
of_concept: nonvanishing-l-series-nonprincipal
source_book: gtm050
source_chapter: "6"
source_section: "6.7"
---
Let $\chi$ be a nonprincipal character modulo the prime $\lambda$. Let $\rho = \chi(\gamma)$ where $\gamma$ is a primitive root modulo $\lambda$. By assumption $\rho \neq 1$.

If $\rho \neq -1$, then $\rho$ is not real and the complex conjugate $\bar{\chi}$ is distinct from $\chi$. Since $L(1, \bar{\chi}) = \overline{L(1, \chi)}$, if $L(1, \chi) = 0$ then both $\chi$ and $\bar{\chi}$ would have vanishing $L$-series. Thus it suffices to show that $L(1, \chi) = 0$ for at most one nonprincipal character, and that $L(1, \chi_{\mu}) \neq 0$ for the character $\chi_{\mu}$ with $\chi_{\mu}(\gamma) = -1$ (where $\mu = (\lambda-1)/2$).

For $\chi_{\mu}$, the explicit formula from Section 6.5 gives:

$$L(1, \chi_{\mu}) = \pm m_{\mu} \sum_{k=0}^{\lambda-2} (-1)^k \log \frac{1}{1-\sigma^k \alpha}$$

$$= \pm \frac{\theta_0 - \theta_1}{\lambda} \left[ \log \frac{\prod(1-\sigma^{2\nu+1}\alpha)}{\prod(1-\sigma^{2\nu}\alpha)} + 2\pi i n \right]$$

where $\theta_0$ is a period of length $\mu$ containing $\alpha$, $\theta_1 = \sigma\theta_0$, and $n$ is an integer. 

The first factor $\theta_0 - \theta_1$ cannot be zero, because $\theta_0 = \theta_1 = \sigma\theta_0$ would imply $\theta_0$ is an ordinary integer while $0 = 1 + \theta_0 + \theta_1 = 1 + 2\theta_0$, which is impossible.

The second factor cannot be zero because the ratio of products inside the logarithm cannot equal 1. If it did, the numerator and denominator would be equal, giving a common value that would be an integer (since it is invariant under $\sigma$). This leads to a contradiction.

Therefore $L(1, \chi_{\mu}) \neq 0$, and since at most one character can have vanishing $L$-series, it follows that $L(1, \chi) \neq 0$ for all nonprincipal characters modulo $\lambda$.
