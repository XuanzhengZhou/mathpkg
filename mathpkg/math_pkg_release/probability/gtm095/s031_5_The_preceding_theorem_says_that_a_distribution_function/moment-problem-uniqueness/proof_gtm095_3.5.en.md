---
role: proof
locale: en
of_concept: moment-problem-uniqueness
source_book: gtm095
source_chapter: "Chapter 3"
source_section: "§5. Inversion formula, moments and semi-invariants"
---

# Proof of Theorem 7 (Uniqueness of the moment problem)

**Theorem 7.** Let $F = F(x)$ be a distribution function and $\mu_n = \int_{-\infty}^{\infty} |x|^n dF(x)$. If

$$\limsup_{n \to \infty} \frac{\mu_n^{1/n}}{n} < \infty,$$

then the moments $\{m_n\}_{n \geq 1}$, where $m_n = \int_{-\infty}^{\infty} x^n dF(x)$, determine the distribution function $F = F(x)$ uniquely.

## Proof

From the growth condition on $\mu_n$ and conclusion (7) of Theorem 1 (which implies that $\mu_n \leq C^n n!$ for large $n$, ensuring analyticity of the characteristic function), there exists $t_0 > 0$ such that for all $|t| \leq t_0$, the characteristic function

$$\varphi(t) = \int_{-\infty}^{\infty} e^{itx} dF(x)$$

expands as an absolutely convergent power series

$$\varphi(t) = \sum_{k=0}^{\infty} \frac{(it)^k}{k!} m_k.$$

Thus the moments $\{m_n\}_{n \geq 1}$ uniquely determine $\varphi(t)$ on $[-t_0, t_0]$.

Now take $s$ with $|s| \leq t_0/2$. From the analyticity of $\varphi$, we can expand around $s$:

$$\varphi(t) = \sum_{k=0}^{\infty} \frac{(t-s)^k}{k!} \varphi^{(k)}(s)$$

for $|t-s| \leq t_0$, where

$$\varphi^{(k)}(s) = i^k \int_{-\infty}^{\infty} x^k e^{isx} dF(x)$$

is expressed in terms of the moments of the (complex) measure $e^{isx} dF(x)$. Expanding $e^{isx} = \sum_{j=0}^{\infty} (isx)^j/j!$ shows that each $\varphi^{(k)}(s)$ is an absolutely convergent series in the $m_n$, hence uniquely determined by them. Consequently $\varphi(t)$ is uniquely determined for $|t| \leq 3t_0/2$.

Repeating this process (analytic continuation along the real line), we extend to all $t \in \mathbb{R}$: after $N$ iterations, $\varphi(t)$ is determined for $|t| \leq t_0 + N \cdot (t_0/2)$. Thus $\{m_n\}_{n \geq 1}$ determines $\varphi(t)$ for all $t$, and by Theorem 2 (uniqueness of distribution given characteristic function), $F(x)$ is uniquely determined.

**Remark.** It suffices to verify the condition for even moments, since odd moments can be estimated from even ones via the Cauchy-Schwarz inequality:

$$|m_{2k+1}|^2 = \left|\int x^{2k+1} dF\right|^2 \leq \int x^{2k} dF \cdot \int x^{2k+2} dF = m_{2k} m_{2k+2}.$$

**Counterexample (non-uniqueness).** Without the growth condition, uniqueness can fail. Consider the distribution with density

$$f(x) = \begin{cases} k e^{-\alpha x^\lambda}, & x > 0, \\ 0, & x \leq 0, \end{cases}$$

where $\alpha > 0$, $0 < \lambda < 1/2$. Define $\beta = \alpha \tan \lambda\pi$ and

$$g(x) = \begin{cases} k e^{-\alpha x^\lambda}[1 + \varepsilon \sin(\beta x^\lambda)], & x > 0, \\ 0, & x \leq 0, \end{cases}$$

with $|\varepsilon| < 1$. Then $f$ and $g$ are distinct densities having the same moments of all orders, since

$$\int_0^\infty x^n e^{-\alpha x^\lambda} \sin(\beta x^\lambda) dx = 0$$

for all $n \geq 0$ (verified via the gamma function identity $\int_0^\infty t^{p-1} e^{-qt} dt = \Gamma(p)/q^p$ with $p = (n+1)/\lambda$, $q = \alpha + i\beta$).
