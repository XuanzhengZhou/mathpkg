---
role: proof
locale: en
of_concept: arcsine-law
source_book: gtm095
source_chapter: "Chapter 1"
source_section: "§3. Random walk, arcsine law, ruin problem"
---

# Proof of Theorem (Arcsine Law)

Let $\gamma(2n)$ be the number of time units that the particle spends on the positive axis in the interval $[0, 2n]$. By Lemma 2, the probability that $\gamma(2n) = 2k$ is

$$P_{2k, 2n} = u_{2k} \cdot u_{2n-2k},$$

where $u_{2k} = P(S_{2k} = 0) = C_{2k}^k \cdot 2^{-2k}$.

By Stirling's formula,

$$u_{2k} \sim \frac{1}{\sqrt{\pi k}}, \quad k \to \infty.$$

Consequently,

$$P_{2k, 2n} = u_{2k} \, u_{2(n-k)} \sim \frac{1}{\pi \sqrt{k(n-k)}}$$

as $k \to \infty$ and $n-k \to \infty$.

For $x < 1$, the probability that the fraction of time spent on the positive side is at most $x$ is given by the sum

$$P\left\{\frac{\gamma(2n)}{2n} \leq x\right\} = \sum_{\{k: k/n \leq x\}} P_{2k, 2n}.$$

Using the asymptotic form of $P_{2k, 2n}$, this sum is approximated by the Riemann sum

$$\sum_{\{k: k/n \leq x\}} \frac{1}{\pi n} \frac{1}{\sqrt{\frac{k}{n}\left(1 - \frac{k}{n}\right)}}.$$

As $n \to \infty$, this Riemann sum converges to the integral

$$\frac{1}{\pi} \int_{0}^{x} \frac{dt}{\sqrt{t(1-t)}}.$$

Evaluating this integral:

$$\frac{1}{\pi} \int_{0}^{x} \frac{dt}{\sqrt{t(1-t)}} = \frac{1}{\pi} \left[ 2 \arcsin \sqrt{t} \right]_{0}^{x} = \frac{2}{\pi} \arcsin \sqrt{x}.$$

Thus we obtain the arcsine law:

$$\sum_{\{k : k/n \leq x\}} P_{2k,2n} \;\longrightarrow\; \frac{2}{\pi} \arcsin \sqrt{x} \quad \text{as } n \to \infty.$$

The integrand $u(t) = (t(1-t))^{-1/2}$ represents a $U$-shaped curve that tends to infinity as $t \to 0$ or $1$. This implies that for large $n$,

$$P\left\{0 < \frac{\gamma(2n)}{2n} \leq \Delta\right\} > P\left\{\frac{1}{2} < \frac{\gamma(2n)}{2n} \leq \frac{1}{2} + \Delta\right\},$$

i.e., it is more likely that the fraction of time spent by the particle on the positive side is close to zero or one, than to the intuitive value $\frac{1}{2}$.
