---
role: proof
locale: en
of_concept: brownian-motion-quadratic-variation
source_book: gtm095
source_chapter: "2"
source_section: "6"
---

# Proof of Quadratic Variation of Standard Brownian Motion

**Theorem.** Let $B = (B_t)_{t \geq 0}$ be the standard Brownian motion. Then, with probability one,

$$\lim_{n \to \infty} \sum_{k=1}^{2^n} \left[ B_{k2^{-n}} - B_{(k-1)2^{-n}} \right]^2 = T$$

for any $T > 0$.

*Proof.* Without loss of generality we can take $T = 1$; the general case follows by scaling. For each $n \geq 1$ and $\varepsilon > 0$, define

$$A_n^\varepsilon = \left\{ \omega : \left| \sum_{k=1}^{2^n} \left( B_{k2^{-n}} - B_{(k-1)2^{-n}} \right)^2 - 1 \right| \geq \varepsilon \right\}.$$

Since $B$ has independent increments, the random variables $\Delta_k^{(n)} = B_{k2^{-n}} - B_{(k-1)2^{-n}}$, $k = 1, \ldots, 2^n$, are independent. Moreover, each $\Delta_k^{(n)}$ is Gaussian with mean zero and variance $2^{-n}$.

For a Gaussian random variable $X \sim \mathcal{N}(0, \sigma^2)$, we have $\mathbb{E}[X^2] = \sigma^2$ and $\mathbb{E}[X^4] = 3\sigma^4$, hence $\operatorname{Var}(X^2) = \mathbb{E}[X^4] - (\mathbb{E}[X^2])^2 = 2\sigma^4$. Applying this with $\sigma^2 = 2^{-n}$,

$$\mathbb{E}\!\left[(\Delta_k^{(n)})^2\right] = 2^{-n}, \qquad \operatorname{Var}\!\left((\Delta_k^{(n)})^2\right) = 2 \cdot 2^{-2n} = 2^{-2n+1}.$$

Now set $S_n = \sum_{k=1}^{2^n} (\Delta_k^{(n)})^2$. By independence,

$$\mathbb{E}[S_n] = \sum_{k=1}^{2^n} \mathbb{E}\!\left[(\Delta_k^{(n)})^2\right] = 2^n \cdot 2^{-n} = 1,$$

$$\operatorname{Var}(S_n) = \sum_{k=1}^{2^n} \operatorname{Var}\!\left((\Delta_k^{(n)})^2\right) = 2^n \cdot 2^{-2n+1} = 2^{-n+1}.$$

By Chebyshev's inequality,

$$\mathsf{P}(A_n^\varepsilon) = \mathsf{P}(|S_n - 1| \geq \varepsilon) \leq \frac{\operatorname{Var}(S_n)}{\varepsilon^2} = \frac{2^{-n+1}}{\varepsilon^2}.$$

Therefore

$$\sum_{n=1}^{\infty} \mathsf{P}(A_n^\varepsilon) \leq \frac{1}{\varepsilon^2} \sum_{n=1}^{\infty} 2^{-n+1} = \frac{2}{\varepsilon^2} < \infty.$$

By the first Borel--Cantelli lemma, $\mathsf{P}\!\left(\limsup_n A_n^\varepsilon\right) = 0$. Consequently, for almost every $\omega$, there exists $N = N(\omega, \varepsilon)$ such that for all $n \geq N$,

$$\left| \sum_{k=1}^{2^n} \left( B_{k2^{-n}} - B_{(k-1)2^{-n}} \right)^2 - 1 \right| < \varepsilon.$$

Since $\varepsilon > 0$ is arbitrary, we conclude that with probability one,

$$\lim_{n \to \infty} \sum_{k=1}^{2^n} \left[ B_{k2^{-n}} - B_{(k-1)2^{-n}} \right]^2 = 1.$$

For general $T > 0$, apply the scaling property $B_t \stackrel{d}{=} \sqrt{T}\,B_{t/T}$ (or more precisely, partition $[0,T]$ into $2^n$ equal subintervals and repeat the argument with variance $T/2^n$ per increment). The same Borel--Cantelli argument yields $\lim_n \sum_{k=1}^{2^n} (B_{kT/2^n} - B_{(k-1)T/2^n})^2 = T$ almost surely. $\square$

**Remark.** This result — that the quadratic variation of Brownian motion over any interval $[0,T]$ equals $T$ almost surely — is the probabilistic foundation of Itô calculus, where the heuristic rule $(dB_t)^2 = dt$ formalizes the fact that Brownian motion accumulates quadratic variation at unit rate.
