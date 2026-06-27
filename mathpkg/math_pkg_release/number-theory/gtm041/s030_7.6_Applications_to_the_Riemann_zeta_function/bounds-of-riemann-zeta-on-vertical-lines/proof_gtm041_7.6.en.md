---
role: proof
locale: en
of_concept: bounds-of-riemann-zeta-on-vertical-lines
source_book: gtm041
source_chapter: "7"
source_section: "7.6"
---

For $\sigma > 1$ we have the trivial bound $|\zeta(\sigma + it)| \leq \zeta(\sigma)$, so $M(\sigma) \leq \zeta(\sigma)$. The supremum is attained at $t = 0$ (on the real axis), giving $M(\sigma) = \zeta(\sigma)$.

To obtain the result for $m(\sigma)$ we estimate the reciprocal $|1/\zeta(s)|$. For $\sigma > 1$ we have
$$\left| \frac{1}{\zeta(s)} \right| = \prod_p |1 - p^{-s}| \leq \prod_p (1 + p^{-\sigma}) = \frac{\zeta(\sigma)}{\zeta(2\sigma)}.$$
Hence $|\zeta(s)| \geq \zeta(2\sigma)/\zeta(\sigma)$, so $m(\sigma) \geq \zeta(2\sigma)/\zeta(\sigma)$.

To prove the reverse inequality $m(\sigma) \leq \zeta(2\sigma)/\zeta(\sigma)$, we use Kronecker's theorem. Choose any $\varepsilon$ with $0 < \varepsilon < \pi/2$ and any integer $n \geq 1$. Apply Kronecker's theorem to the numbers
$$\theta_k = \frac{-1}{2\pi} \log p_k, \quad k = 1, 2, \ldots, n,$$
where $p_1, \ldots, p_n$ are the first $n$ primes. The $\theta_i$ are linearly independent over the integers because
$$\sum_{i=1}^{n} a_i \log p_i = 0 \implies \log(p_1^{a_1} \cdots p_n^{a_n}) = 0,$$
so $p_1^{a_1} \cdots p_n^{a_n} = 1$, hence each $a_i = 0$. Take $\alpha_1 = \alpha_2 = \cdots = \alpha_n = \frac{1}{2}$. By Theorem 7.9 (Kronecker's theorem) there exists a real $t$ and integers $h_1, \ldots, h_n$ such that $|t\theta_k - \alpha_k - h_k| < \varepsilon/(2\pi)$, which means
$$|-t \log p_k - \pi - 2\pi h_k| < \varepsilon. \tag{18}$$

For this $t$ we compute
$$1 - p_k^{-s} = 1 - p_k^{-\sigma} e^{-it \log p_k} = 1 + p_k^{-\sigma} e^{i(-t \log p_k - \pi)}$$
$$= 1 + p_k^{-\sigma} \cos(-t \log p_k - \pi) + i p_k^{-\sigma} \sin(-t \log p_k - \pi),$$
so
$$|1 - p_k^{-s}| \geq 1 + p_k^{-\sigma} \cos(-t \log p_k - \pi).$$

From (18) we have
$$\cos(-t \log p_k - \pi) = \cos(-t \log p_k - \pi - 2\pi h_k) > \cos \varepsilon.$$

Using this estimate with $n \geq n_0$ we find
$$\frac{1}{|\zeta(s)|} = \prod_{k=1}^{n} |1 - p_k^{-s}| \prod_{k=n+1}^{\infty} |1 - p_k^{-s}| > (1 - \varepsilon) \prod_{k=1}^{n} (1 + p_k^{-\sigma} \cos \varepsilon).$$

This holds for $n \geq n_0$ and a certain $t$ depending on $n$ and $\varepsilon$. Hence
$$\frac{1}{m(\sigma)} = \frac{1}{\inf_t |\zeta(\sigma + it)|} = \sup_t \frac{1}{|\zeta(\sigma + it)|} \geq (1 - \varepsilon) \prod_{k=1}^{n} (1 + p_k^{-\sigma} \cos \varepsilon).$$

Letting $n \to \infty$ we obtain
$$\frac{1}{m(\sigma)} \geq (1 - \varepsilon) \prod_{k=1}^{\infty} (1 + p_k^{-\sigma} \cos \varepsilon).$$

The infinite product converges uniformly for $0 \leq \varepsilon \leq \pi/2$ because a product $\prod (1 + f_n(z))$ converges uniformly on a set if and only if the series $\sum f_n(z)$ converges uniformly there. Here the series $\sum p_k^{-\sigma} \cos \varepsilon$ is dominated by $\sum p_k^{-\sigma} \leq \sum n^{-\sigma} = \zeta(\sigma)$, which converges for $\sigma > 1$. Therefore we can let $\varepsilon \to 0$ and pass to the limit term by term:
$$\frac{1}{m(\sigma)} \geq \prod_{k=1}^{\infty} (1 + p_k^{-\sigma}) = \frac{\zeta(\sigma)}{\zeta(2\sigma)}.$$

This gives $m(\sigma) \leq \zeta(2\sigma)/\zeta(\sigma)$, completing the proof.
