---
role: proof
locale: en
of_concept: levy-upward-theorem
source_book: gtm040
source_chapter: "3"
source_section: "4"
---

We may assume that $f \geq 0$ since the general case follows by considering $f^+$ and $f^-$ separately. Then $g_n \geq 0$ for all $n$.

First we show that $(g_n, \mathcal{R}_n)$ is a martingale. For any cell $R \in \mathcal{R}_n$,

$$\int_R g_{n+1} \, d\mu = \int_R M[f \mid \mathcal{R}_{n+1}] \, d\mu = \int_R f \, d\mu$$

by the definition of conditional expectation. Also,

$$\int_R g_n \, d\mu = \int_R M[f \mid \mathcal{R}_n] \, d\mu = \int_R f \, d\mu$$

since $R \in \mathcal{R}_n \subset \mathcal{R}_{n+1}$. Hence $\int_R g_{n+1} \, d\mu = \int_R g_n \, d\mu$ for all $R \in \mathcal{R}_n$, which means $M[g_{n+1} \mid \mathcal{R}_n] = g_n$, so $(g_n, \mathcal{R}_n)$ is a martingale.

Next we show the $g_n$ are uniformly integrable. For any $\epsilon > 0$, choose $\delta > 0$ so that $\mu(E) < \delta$ implies $\int_E f \, d\mu < \epsilon$ (by absolute continuity of the integral). Choose $N$ large enough so that

$$\frac{1}{N} \int_{\Omega} f \, d\mu < \delta.$$

Then for all $n$, by Chebyshev-type inequality,

$$\mu(\{g_n \geq N\}) \leq \frac{1}{N} \int_{\Omega} g_n \, d\mu = \frac{1}{N} \int_{\Omega} f \, d\mu < \delta.$$

Hence $\int_{\{g_n \geq N\}} g_n \, d\mu = \int_{\{g_n \geq N\}} f \, d\mu < \epsilon$ by Lemma 3-6, establishing uniform integrability.

By Theorem 3-12 (Martingale Convergence Theorem), $g_n$ converges almost everywhere to some limit $g$. By uniform integrability and Proposition 1-52, for any set $E$ in $\bigcup \mathcal{R}_n^*$ and $m \geq n$ with $E \in \mathcal{R}_m^*$,

$$\int_E g_m \, d\mu = \int_E f \, d\mu.$$

Letting $m \to \infty$ and using uniform integrability,

$$\int_E g \, d\mu = \int_E f \, d\mu$$

for all $E$ in $\bigcup \mathcal{R}_n^*$. The two sides, considered as set functions, are equal on the field $\bigcup \mathcal{R}_n^*$. By the uniqueness half of Theorem 1-19 (extension of measures), they must be equal on the generated augmented Borel field $\mathcal{R}^*$. That is, $f$ and $g$ are measurable with respect to $\mathcal{R}^*$ and satisfy

$$\int_E f \, d\mu = \int_E g \, d\mu$$

for all $E \in \mathcal{R}^*$. Taking $E$ successively to be the set where $f \geq g$ and the set where $f \leq g$, and applying Corollary 1-40, we find that $f = g$ almost everywhere.
