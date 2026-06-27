---
role: proof
locale: en
of_concept: distribution-function-5
source_book: gtm095
source_chapter: "Chapter 3"
source_section: "§5. Inversion formula, moments and semi-invariants"
---

# Proof of Theorem 7 (Uniqueness of distribution via moment growth condition)

**Theorem 7.** Let $F = F(x)$ be a distribution function and $\mu_n = \int_{-\infty}^{\infty} |x|^n dF(x)$. If

$$\limsup_{n \to \infty} \frac{\mu_n^{1/n}}{n} < \infty, \tag{56}$$

then the moments $\{m_n\}_{n \geq 1}$, where $m_n = \int_{-\infty}^{\infty} x^n dF(x)$, determine the distribution function $F = F(x)$ uniquely.

## Proof

It follows from condition (56) and conclusion (7) of Theorem 1 (which gives $\mu_n \leq C^n n!$ for sufficiently large $n$, ensuring the characteristic function is analytic) that there exists $t_0 > 0$ such that, for all $|t| \leq t_0$, the characteristic function

$$\varphi(t) = \int_{-\infty}^{\infty} e^{itx} dF(x)$$

can be represented as a convergent power series

$$\varphi(t) = \sum_{k=0}^{\infty} \frac{(it)^k}{k!} m_k.$$

Consequently the moments $\{m_n\}_{n \geq 1}$ uniquely determine the characteristic function $\varphi(t)$ for $|t| \leq t_0$.

Now take a point $s$ with $|s| \leq t_0/2$. From the analyticity of $\varphi$ (which follows from (56)), we can expand around $s$:

$$\varphi(t) = \sum_{k=0}^{\infty} \frac{(t-s)^k}{k!} \varphi^{(k)}(s)$$

for $|t-s| \leq t_0$, where

$$\varphi^{(k)}(s) = i^k \int_{-\infty}^{\infty} x^k e^{isx} dF(x)$$

is uniquely determined by the moments $\{m_n\}_{n \geq 1}$ (since the integral involves moments of the measure $e^{isx} dF(x)$, whose moments are linear combinations of the $m_n$). Consequently the moments determine $\varphi(t)$ uniquely for $|t| \leq \frac{3}{2}t_0$.

Continuing this process iteratively, we extend the interval on which $\varphi$ is uniquely determined: after $N$ steps, $\varphi(t)$ is determined for $|t| \leq t_0 + N \cdot (t_0/2)$. Thus $\{m_n\}_{n \geq 1}$ determines $\varphi(t)$ uniquely for all $t \in \mathbb{R}$, and therefore also determines $F(x)$ by Theorem 2 (uniqueness theorem for characteristic functions).

**Remark.** The odd moments can be estimated in terms of the even ones (by the Cauchy-Schwarz inequality: $|\int x^{2k+1} dF|^2 \leq \int x^{2k} dF \cdot \int x^{2k+2} dF$), so it suffices to verify condition (56) for even $n$.

**Example.** For the normal distribution $F(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \int_{-\infty}^{x} e^{-t^2/2\sigma^2} dt$, we have $m_{2n+1} = 0$, $m_{2n} = \frac{(2n)!}{2^n n!} \sigma^{2n}$. Condition (57) is satisfied, so these moments uniquely characterize the normal distribution.
