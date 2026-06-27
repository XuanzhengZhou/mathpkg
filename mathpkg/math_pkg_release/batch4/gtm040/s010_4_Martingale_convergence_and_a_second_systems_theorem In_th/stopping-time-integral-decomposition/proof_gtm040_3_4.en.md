---
role: proof
locale: en
of_concept: stopping-time-integral-decomposition
source_book: gtm040
source_chapter: "3"
source_section: "4"
---

We compute:

$$\int_{\Omega} f_t \, d\mu = \sum_{k=0}^{n} \int_{\{t = k\}} f_t \, d\mu + \int_{\{t > n\}} f_t \, d\mu$$

$$= \sum_{k=0}^{n} \int_{\{t = k\}} f_k \, d\mu + \int_{\{t > n\}} f_t \, d\mu.$$

By Lemma 3-6, for each $k \leq n$ we have

$$\int_{\{t = k\}} f_k \, d\mu = \int_{\{t = k\}} f_n \, d\mu,$$

since $\{t = k\}$ is a union of cells of $\mathcal{R}_k \subset \mathcal{R}_n$ and $f_k, f_n$ form a martingale. Summing over $k = 0, \ldots, n$,

$$\sum_{k=0}^{n} \int_{\{t = k\}} f_k \, d\mu = \sum_{k=0}^{n} \int_{\{t = k\}} f_n \, d\mu = \int_{\{t \leq n\}} f_n \, d\mu.$$

Therefore

$$\int_{\Omega} f_t \, d\mu = \int_{\{t \leq n\}} f_n \, d\mu + \int_{\{t > n\}} f_t \, d\mu,$$

as claimed.
