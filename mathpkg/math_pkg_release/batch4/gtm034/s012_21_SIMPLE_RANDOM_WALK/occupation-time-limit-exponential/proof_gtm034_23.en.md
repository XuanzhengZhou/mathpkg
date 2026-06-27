---
role: proof
locale: en
of_concept: occupation-time-limit-exponential
source_book: gtm034
source_chapter: "V"
source_section: "23"
---

Translating the interval $[-N,N]$ to $[0,2N]$ (so the start $x_0 = 0$ becomes $x_0 = N$ and $y$ becomes $y+N$), a computation using the Markov property yields
$$p_N(y) = \frac{g_{2N}(N, N+y)}{g_{2N}(N+y, N+y)}, \quad r_N(y) = 1 - \frac{1}{g_{2N}(N+y, N+y)},$$
and
$$P_0[\mathbf{N}_N(y) > N x] = p_N(y) [r_N(y)]^{[N x]}.$$

By Theorem T1, $\lim_{N \to \infty} p_N(y) = 1$. To estimate $r_N(y)$, observe that
$$\frac{\sigma^2}{4N} g_{2N}(N+y, N+y) = \frac{1}{4} - \frac{y^2}{4N^2} + \epsilon_N(y)$$
where $\epsilon_N(y) \to 0$ uniformly in $y$. Consequently,
$$r_N(y) = 1 - \frac{\sigma^2}{N} + o\left(\frac{1}{N}\right),$$
where $N o(1/N) \to 0$ as $N \to \infty$. Therefore
$$\lim_{N \to \infty} [r_N(y)]^{[N x]} = \lim_{N \to \infty} \left(1 - \frac{\sigma^2}{N}\right)^{N x} = e^{-\sigma^2 x}.$$
