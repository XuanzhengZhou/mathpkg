role: proof
locale: en
of_concept: dirichlets-formula-for-l1-chi-even
source_book: gtm050
source_chapter: "6. Determination of the Class Number"
source_section: "6.5 Dirichlet's evaluation of L(1,\\chi)"

Starting from the master formula

$$L(1, \chi_j) = (-1)^j m_j \sum_{k=0}^{\lambda-2} \beta^{-jk} \log \frac{1}{1-\sigma^k \alpha},$$

take $j = 2\nu$ to be even. Then $(-1)^j = 1$. The sum runs over $k = 0, 1, \dots, \lambda-2$. Since $\lambda-1 = 2\mu$, the summation splits naturally into $\mu$ pairs $(k, k+\mu)$.

Consider the two terms corresponding to $k$ and $k+\mu$:

$$\beta^{-2\nu k} \log \frac{1}{1-\sigma^k \alpha} + \beta^{-2\nu(k+\mu)} \log \frac{1}{1-\sigma^{k+\mu} \alpha}.$$

Since $\beta$ is a primitive $(\lambda-1)$st root of unity, $\beta^{\mu} = -1$. Therefore $\beta^{-2\nu \mu} = (\beta^{\mu})^{-2\nu} = (-1)^{-2\nu} = 1$. Hence the two terms combine as

$$\beta^{-2\nu k} \left( \log \frac{1}{1-\sigma^k \alpha} + \log \frac{1}{1-\sigma^{k+\mu} \alpha} \right).$$

Now $\sigma^{k+\mu} \alpha$ is the complex conjugate of $\sigma^k \alpha$, because $\gamma^{\mu} \equiv -1 \bmod \lambda$. Thus

$$\log \frac{1}{1-\sigma^k \alpha} + \log \frac{1}{1-\overline{\sigma^k \alpha}} = 2 \operatorname{Re} \log \frac{1}{1-\sigma^k \alpha} = -2 \log |1 - \sigma^k \alpha|.$$

Summing over $k = 0, 1, \dots, \mu-1$ yields

$$L(1, \chi_{2\nu}) = -2 m_{2\nu} \sum_{k=0}^{\mu-1} \beta^{-2\nu k} \log |1 - \sigma^k \alpha|,$$

as claimed. Note that the sum now involves only $\mu = (\lambda-1)/2$ terms instead of $\lambda-1$, reflecting the pairing of conjugates.
