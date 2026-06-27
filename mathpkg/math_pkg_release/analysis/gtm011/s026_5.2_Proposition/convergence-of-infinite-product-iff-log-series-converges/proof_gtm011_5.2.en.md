---
role: proof
locale: en
of_concept: convergence-of-infinite-product-iff-log-series-converges
source_book: gtm011
source_chapter: "5"
source_section: "5.2"
---

($\Leftarrow$) Suppose that the series $\sum \log z_n$ converges. Let $s_n = \sum_{k=1}^{n} \log z_k$ and $s_n \to s$. Then $\exp s_n \to \exp s$. But $\exp s_n = \prod_{k=1}^{n} z_k$, so that $\prod_{n=1}^{\infty} z_n$ is convergent to $z = e^s \neq 0$.

($\Rightarrow$) Let $p_n = z_1 \cdots z_n$, let $z = re^{i\theta}$ with $-\pi < \theta \leq \pi$, and let $\ell(p_n) = \log |p_n| + i\theta_n$ where $\theta - \pi < \theta_n \leq \theta + \pi$. If $s_n = \log z_1 + \cdots + \log z_n$ then $\exp(s_n) = p_n$, so that $s_n = \ell(p_n) + 2\pi i k_n$ for some integer $k_n$. Now suppose that $p_n \to z$. Then $s_n - s_{n-1} = \log z_n \to 0$; also $\ell(p_n) - \ell(p_{n-1}) \to 0$. Hence $(k_n - k_{n-1}) \to 0$ as $n \to \infty$. Since each $k_n$ is an integer, this gives that there is an $n_0$ and a $k$ such that $k_m = k_n = k$ for $m, n \geq n_0$. Therefore $s_n \to \ell(z) + 2\pi i k$; that is, the series $\sum \log z_n$ converges.
