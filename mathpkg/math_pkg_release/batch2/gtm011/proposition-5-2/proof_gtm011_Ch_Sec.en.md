---
role: proof
locale: en
of_concept: proposition-5-2
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. Let $p_n = (z_1 \cdots z_n), z = re^{i\theta}, -\pi < \theta \leq \pi$, and $\ell(p_n) = \log |p_n| + i\theta_n$ where $\theta - \pi < \theta_n \leq \theta + \pi$. If $s_n = \log z_1 + \cdots + \log z_n$ then $\exp (s_n) = p_n$ so that $s_n = \ell(p_n) + 2\pi ik_n$ for some integer $k_n$. Now suppose that $p_n \to z$. Then $s_n - s_{n-1} = \log z_n \to 0$; also $\ell(p_n) - \ell(p_{n-1}) \to 0$, Hence, $(k_n - k_{n-1}) \to 0$ as $n \to \infty$. Since each $k_n$ is an integer this gives that there is an $n_0$ and a $k$ such that $k_m = k_n = k$ for $m, n \geq n_0$. So $s_n \to \ell(z) + 2\pi ik$; that is, the series $\sum \log z_n

We wish to define the absolute convergence of an infinite product. The first temptation should be avoided. That is, we do not want to say that $\prod |z_n|$ converges. Why? If $\prod |z_n|$ converges it does not follow that $\prod z_n$ converges. In fact, let $z_n = -1$ for all $n$; then $|z_n| = 1$ for all $n$ so that $\prod |z_n|$ converges to 1. However $\prod_{k=1}^{n} z_k$ is $\pm 1$ depending on whether $n$ is even or odd, so that $\prod z_n$ does not converge. Thus, if absolute convergence is to imply convergence, we must seek a different definition.

On the basis of Proposition 5.2 the following definition is justified.
