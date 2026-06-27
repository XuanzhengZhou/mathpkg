---
role: proof
locale: en
of_concept: optional-stopping-theorem
source_book: gtm040
source_chapter: "3"
source_section: "4"
---

By condition (1), $\int_{\Omega} f_t \, d\mu$ exists, so that Lemma 3-14 applies. Thus, for any $n$,

$$\int_{\Omega} f_t \, d\mu = \int_{\{t \leq n\}} f_n \, d\mu + \int_{\{t > n\}} f_t \, d\mu$$

$$= \int_{\Omega} f_n \, d\mu - \int_{\{t > n\}} f_n \, d\mu + \int_{\{t > n\}} f_t \, d\mu.$$

By Lemma 3-10, since $(f_n, \mathcal{R}_n)$ is a martingale,

$$\int_{\Omega} f_n \, d\mu = \int_{\Omega} f_0 \, d\mu.$$

Therefore

$$\int_{\Omega} f_t \, d\mu = \int_{\Omega} f_0 \, d\mu - \int_{\{t > n\}} f_n \, d\mu + \int_{\{t > n\}} f_t \, d\mu.$$

Using condition (1) together with Corollary 1-17 and the complete additivity of the integral as a set function, we see that

$$\lim_{n \to \infty} \int_{\{t > n\}} f_t \, d\mu = 0.$$

Since $\int_{\{t > n\}} f_n \, d\mu \to 0$ by hypothesis (condition (2)), taking the limit as $n \to \infty$ yields

$$\int_{\Omega} f_t \, d\mu = \int_{\Omega} f_0 \, d\mu.$$
