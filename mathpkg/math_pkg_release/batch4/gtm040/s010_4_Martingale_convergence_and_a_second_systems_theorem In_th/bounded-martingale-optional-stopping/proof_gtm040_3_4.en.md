---
role: proof
locale: en
of_concept: bounded-martingale-optional-stopping
source_book: gtm040
source_chapter: "3"
source_section: "4"
---

We must show the two conditions of Theorem 3-15 are satisfied.

For condition (1): Since $|f_n| \leq K$ for all $n$, we have $|f_t| \leq K$ by definition of $f_t$, and hence $f_t$ is integrable because $\Omega$ has finite total measure.

For condition (2): We estimate

$$\left| \int_{\{t > n\}} f_n \, d\mu \right| \leq \int_{\{t > n\}} |f_n| \, d\mu \leq \int_{\{t > n\}} K \, d\mu = K \cdot \mu(\{\omega \mid t(\omega) > n\}).$$

Since $t$ is a stopping time, it is finite almost everywhere, which means

$$\bigcap_{n=1}^{\infty} \{\omega \mid t(\omega) \geq n\}$$

has measure zero. Therefore $\mu(\{t > n\}) \to 0$ as $n \to \infty$, and consequently

$$\lim_{n \to \infty} \int_{\{t > n\}} f_n \, d\mu = 0.$$

Both conditions of Theorem 3-15 are satisfied, so $M[f_t] = M[f_0]$.
