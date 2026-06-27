---
role: proof
locale: en
of_concept: convergence-of-independent-series
source_book: gtm018
source_chapter: "IX. Probability"
source_section: "§46. Series of Independent Functions"
---

Write

$$s_n(x) = \sum_{i=1}^{n} f_i(x), \quad n = 1, 2, \dots,$$

$$a_m(x) = \sup \{ |s_{m+k}(x) - s_m(x)| : k = 1, 2, \dots \},$$

$$a(x) = \inf \{ a_m(x) : m = 1, 2, \dots \}.$$

A necessary and sufficient condition for the convergence of $\sum_{n=1}^{\infty} f_n(x)$ at $x$ is that $a(x) = 0$.

By Kolmogorov's inequality (Theorem A), for every positive number $\epsilon$ and every pair of positive integers $m$ and $n$,

$$\mu(\{x : \max_{1 \leq k \leq n} |s_{m+k}(x) - s_m(x)| \geq \epsilon\}) \leq \frac{1}{\epsilon^2} \sum_{k=m+1}^{m+n} \sigma^2(f_k).$$

Letting $n \to \infty$, we obtain

$$\mu(\{x : a_m(x) \geq \epsilon\}) \leq \frac{1}{\epsilon^2} \sum_{k=m+1}^{\infty} \sigma^2(f_k).$$

Since $\sum_{n=1}^{\infty} \sigma^2(f_n) < \infty$, the right-hand side tends to $0$ as $m \to \infty$. Hence $a_m(x) \to 0$ in measure, which implies that a subsequence converges to $0$ almost everywhere. Since $\{a_m(x)\}$ is a decreasing sequence, it follows that $a(x) = 0$ almost everywhere, i.e., the series converges almost everywhere.
