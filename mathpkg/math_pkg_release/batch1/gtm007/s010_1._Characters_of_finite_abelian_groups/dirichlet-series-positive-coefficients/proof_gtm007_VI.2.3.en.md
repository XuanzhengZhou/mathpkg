---
role: proof
locale: en
of_concept: dirichlet-series-positive-coefficients
source_book: gtm007
source_chapter: "VI"
source_section: "§2.3"
---

After replacing $z$ by $z - \rho$, we may assume $\rho = 0$. Since $f$ is holomorphic for $\Re(z) > 0$ and in a neighborhood of $0$, it is holomorphic in a disc $|z - 1| \leq 1 + \varepsilon$ with $\varepsilon > 0$. Its Taylor series at $z = 1$ converges in this disc.

By Lemma 1, the $p$-th derivative $f^{(p)}(1)$ is given by the differentiated series. Expanding $f(-\varepsilon)$ using the Taylor series:
$$f(-\varepsilon) = \sum_{p=0}^{\infty} \frac{f^{(p)}(1)}{p!} (-1-\varepsilon)^p = \sum_{p=0}^{\infty} \frac{1}{p!} (1+\varepsilon)^p \sum_n a_n \lambda_n^p e^{-\lambda_n}.$$
Since all terms are non-negative, we may rearrange:
$$f(-\varepsilon) = \sum_n a_n e^{-\lambda_n} \sum_{p=0}^{\infty} \frac{(\lambda_n(1+\varepsilon))^p}{p!} = \sum_n a_n e^{-\lambda_n} e^{\lambda_n(1+\varepsilon)} = \sum_n a_n e^{\lambda_n \varepsilon}.$$
This shows the Dirichlet series converges at $z = -\varepsilon$, hence for $\Re(z) > -\varepsilon$.
