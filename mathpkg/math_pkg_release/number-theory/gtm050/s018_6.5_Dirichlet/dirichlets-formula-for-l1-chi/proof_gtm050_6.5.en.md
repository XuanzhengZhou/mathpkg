role: proof
locale: en
of_concept: dirichlets-formula-for-l1-chi
source_book: gtm050
source_chapter: "6. Determination of the Class Number"
source_section: "6.5 Dirichlet's evaluation of L(1,\\chi)"

From the definition $L(1, \chi) = \sum_{n=1}^{\infty} \chi(n)/n$, one expands using the discrete Fourier transform with respect to the primitive $\lambda$th root of unity $\alpha$. Since $\chi$ is a nonprincipal character, the sum of its values is zero, giving $c_0 = 0$.

The coefficients $c_\nu$ are defined by

$$c_\nu = \frac{1}{\lambda} \sum_{j=1}^{\lambda-1} \chi(j) \alpha^{-j\nu},$$

so that

$$L(1, \chi) = \sum_{\nu=1}^{\lambda-1} c_\nu \log \frac{1}{1-\alpha^\nu}.$$

This is formulas (2) and (3) of the text.

To simplify, reorder the terms using a primitive root $\gamma$ modulo $\lambda$. Write the $\lambda-1$ terms with powers of $\alpha$ in the order $\alpha, \sigma\alpha, \sigma^2\alpha, \ldots$ where $\sigma : \alpha \mapsto \alpha^\gamma$. Defining $b_k = c_\nu$ with $\nu \equiv \gamma^k \bmod \lambda$, we have

$$b_k = c_\nu = \frac{1}{\lambda} \sum_{j=1}^{\lambda-1} \chi(j) \sigma^k \alpha^{-j} = \sigma^k(b_0).$$

Thus

$$L(1, \chi) = \sum_{k=0}^{\lambda-2} b_k \log \frac{1}{1-\sigma^k \alpha}.$$

Let $\rho = \chi(\gamma)$. Then $b_k = \rho^{-k} b_0$, since $\sigma$ acts as multiplication by $\rho^{-1}$ on the coefficient $b_0$ (because $\chi(\gamma^{-1}) = \rho^{-1}$). This gives

$$L(1, \chi) = b_0 \sum_{k=0}^{\lambda-2} \rho^{-k} \log \frac{1}{1-\sigma^k \alpha}.$$

The factor $\rho^{-\mu}$ (where $\mu = (\lambda-1)/2$) occurring in $b_0$ is $\pm 1$ because $(\rho^{\mu})^2 = \rho^{\lambda-1} = \chi(\gamma^{\lambda-1}) = \chi(1) = 1$.

Let $\beta$ be a primitive $(\lambda-1)$st root of unity. Then $\rho = \beta^j$ for some $j$. Since $\beta^{\mu} = -1$, we have $\rho^{-\mu} = (-1)^j$. Let $\chi_j$ denote the character with $\chi_j(\gamma) = \beta^j$. Then the above formulas give

$$L(1, \chi_j) = (-1)^j m_j \sum_{k=0}^{\lambda-2} \beta^{-jk} \log \frac{1}{1-\sigma^k \alpha},$$

where

$$m_j = \frac{1}{\lambda} \sum_{k=0}^{\lambda-2} \beta^{jk} \sigma^k \alpha.$$

This completes the derivation of the master formula. The further separation into even and odd cases ($\chi_{2\nu}$ and $\chi_{2\nu+1}$) is handled in the respective theorems.
