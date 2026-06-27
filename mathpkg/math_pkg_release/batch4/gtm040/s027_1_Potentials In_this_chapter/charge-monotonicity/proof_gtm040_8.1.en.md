---
role: proof
locale: en
of_concept: charge-monotonicity
source_book: gtm040
source_chapter: "8"
source_section: "1"
---

By the dual of Proposition 8-23, we may find a sequence of finite measures $\pi^{(n)}$ such that $\alpha$ is the monotone limit of $\pi^{(n)} N$. Since $N\bar{f} \leq Nf$, we have $\pi^{(n)}(N\bar{f}) \leq \pi^{(n)}(Nf)$ and
$$\lim_n \pi^{(n)}(N\bar{f}) \leq \lim_n \pi^{(n)}(Nf).$$
Since $\bar{f} \geq 0$,
$$\pi^{(n)}(N\bar{f}) = (\pi^{(n)} N)\bar{f},$$
and
$$\lim_n \pi^{(n)}(N\bar{f}) = (\lim_n \pi^{(n)} N)\bar{f} = \alpha \bar{f}$$
by monotone convergence with $\bar{f}$ as the measure. And since $\pi^{(n)} N f^+ \leq \alpha f^+ < \infty$ and $\pi^{(n)} N f^- \leq \alpha f^- < \infty$,
$$\pi^{(n)}(Nf) = \pi^{(n)} N f^+ - \pi^{(n)} N f^-.$$
Hence
$$\lim_n \pi^{(n)}(Nf) = \alpha f^+ - \alpha f^- = \alpha f$$
by monotone convergence for each term. Thus $\alpha \bar{f} \leq \alpha f < \infty$.
