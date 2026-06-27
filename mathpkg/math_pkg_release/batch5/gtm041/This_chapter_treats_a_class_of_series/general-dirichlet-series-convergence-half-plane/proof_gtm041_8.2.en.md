---
role: proof
locale: en
of_concept: general-dirichlet-series-convergence-half-plane
source_book: gtm041
source_chapter: "8"
source_section: "8.2"
---

**Proof.** First we prove that $L \leq \sigma_0$. Let $A(n)$ denote the partial sums of the coefficients,

$$A(n) = \sum_{k=1}^n a(k).$$

Note that $\lambda(n) > 0$ for all sufficiently large $n$. If we prove that for every $\varepsilon > 0$ there exists an $N$ such that $n \geq N$ implies

$$\frac{\log|A(n)|}{\lambda(n)} < \sigma_0 + \varepsilon,$$

then $L \leq \sigma_0$ follows.

For this purpose we let $S(n) = \sum_{k=1}^n a(k)e^{-s_0\lambda(k)}$, the $n$-th partial sum of the series at $s = s_0$. Then $S(n) \to S(\infty)$ as $n \to \infty$, where $S(\infty)$ is the sum of the series. The $S(n)$ are bounded since the series $\sum_{k=1}^{\infty} a(k)e^{-s_0\lambda(k)}$ converges. Suppose that $|S(n)| < M$ for all $n$. To express $A(n)$ in terms of the $S(n)$ we use partial summation:

$$A(n) = \sum_{k=1}^{n} a(k) = \sum_{k=1}^{n} a(k)e^{-s_0\lambda(k)}e^{s_0\lambda(k)}$$
$$= \sum_{k=1}^{n} \{S(k) - S(k-1)\}e^{s_0\lambda(k)},$$

provided $S(0) = 0$. Thus

$$A(n) = \sum_{k=1}^{n} S(k)e^{s_0\lambda(k)} - \sum_{k=1}^{n-1} S(k)e^{s_0\lambda(k+1)}$$
$$= \sum_{k=1}^{n-1} S(k)\{e^{s_0\lambda(k)} - e^{s_0\lambda(k+1)}\} + S(n)e^{s_0\lambda(n)}.$$

Hence

$$|A(n)| < M \sum_{k=1}^{n-1}|e^{s_0\lambda(k)} - e^{s_0\lambda(k+1)}| + Me^{\sigma_0\lambda(n)}.$$

But

$$\sum_{k=1}^{n-1}|e^{s_0\lambda(k)} - e^{s_0\lambda(k+1)}| = \sum_{k=1}^{n-1}\left|s_0 \int_{\lambda(k)}^{\lambda(k+1)} e^{s_0u}\,du\right| \leq |s_0| \sum_{k=1}^{n-1}\int_{\lambda(k)}^{\lambda(k+1)} e^{\sigma_0u}\,du$$
$$= |s_0| \int_{\lambda(1)}^{\lambda(n)} e^{\sigma_0u}\,du = \frac{|s_0|}{\sigma_0}\left(e^{\sigma_0\lambda(n)} - e^{\sigma_0\lambda(1)}\right) \leq \frac{|s_0|}{\sigma_0} e^{\sigma_0\lambda(n)}.$$

Therefore

$$|A(n)| < M\left(\frac{|s_0|}{\sigma_0} + 1\right)e^{\sigma_0\lambda(n)}.$$

Taking logarithms and dividing by $\lambda(n)$ we obtain, for all sufficiently large $n$,

$$\frac{\log |A(n)|}{\lambda(n)} < \sigma_0 + \frac{\log M + \log(1 + |s_0|/\sigma_0)}{\lambda(n)}.$$

Given $\varepsilon > 0$, the last term is less than $\varepsilon$ for $n$ sufficiently large, so

$$\frac{\log |A(n)|}{\lambda(n)} < \sigma_0 + \varepsilon,$$

which proves $L \leq \sigma_0$.

Now we prove that the series converges for all $s$ with $\sigma > L$. We use partial summation to compare it to the partial sums $A(n) = \sum_{k=1}^{n} a(k)$. We have

$$\sum_{n=a}^{b} a(n) e^{-s \lambda(n)} = \sum_{n=a}^{b} \{A(n) - A(n-1)\} e^{-s \lambda(n)}$$
$$= \sum_{n=a}^{b} A(n) \{e^{-s \lambda(n)} - e^{-s \lambda(n+1)}\} + A(b) e^{-s \lambda(b+1)} - A(a-1) e^{-s \lambda(a)}.$$

This relation holds for any choice of $s$, $a$ and $b$. Now suppose $s$ is any complex number with $\sigma > L$. Let $\varepsilon = \frac{1}{2}(\sigma - L)$. Then $\varepsilon > 0$ and $\sigma = L + 2\varepsilon$. By the definition of $L$, for this $\varepsilon$ there is an integer $N(\varepsilon)$ such that for all $n \geq N(\varepsilon)$ we have

$$\frac{\log |A(n)|}{\lambda(n)} < L + \varepsilon.$$

We can also assume that $\lambda(n) > 0$ for $n \geq N(\varepsilon)$. Hence

$$|A(n)| < e^{(L+\varepsilon)\lambda(n)} \quad \text{for all } n \geq N(\varepsilon).$$

If we choose $b \geq a > N(\varepsilon)$ we get the estimate

$$\left| \sum_{n=a}^{b} a(n) e^{-s \lambda(n)} \right| \leq \sum_{n=a}^{b} e^{(L+\varepsilon)\lambda(n)} \left| e^{-s \lambda(n)} - e^{-s \lambda(n+1)} \right|$$
$$+ e^{(L+\varepsilon)\lambda(b+1)} e^{-\sigma \lambda(b+1)} + e^{(L+\varepsilon)\lambda(a)} e^{-\sigma \lambda(a)}.$$

The last two terms are $e^{-\varepsilon \lambda(b+1)} + e^{-\varepsilon \lambda(a)}$ since $L + \varepsilon - \sigma = -\varepsilon$. Each term on the right tends to $0$ as $a \to \infty$, so the Cauchy criterion shows that the series converges for all $s$ with $\sigma > L$.

This completes the proof. Note also that this proves uniform convergence on any compact subset of the half-plane $\sigma > L$, since on a compact set the argument can be made uniform in $t = \operatorname{Im}(s)$. $\square$
