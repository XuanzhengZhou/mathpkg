---
role: proof
locale: en
of_concept: characteristic-function-tail-estimate
source_book: gtm095
source_chapter: "3"
source_section: "2"
---

# Proof of Tail Estimate via Characteristic Function

Let $F = F(x)$ be a distribution function on $\mathbb{R}$ with characteristic function

$$\varphi(t) = \int_{-\infty}^{\infty} e^{itx} \, dF(x), \quad t \in \mathbb{R}.$$

**Proof.** Since $\operatorname{Re} \varphi(t) = \int_{-\infty}^{\infty} \cos tx \, dF(x)$, we compute, using Fubini's theorem:

$$
\begin{aligned}
\frac{1}{a} \int_{0}^{a} \bigl[ 1 - \operatorname{Re} \varphi(t) \bigr] \, dt
&= \frac{1}{a} \int_{0}^{a} \left[ \int_{-\infty}^{\infty} (1 - \cos tx) \, dF(x) \right] dt \\[4pt]
&= \int_{-\infty}^{\infty} \left[ \frac{1}{a} \int_{0}^{a} (1 - \cos tx) \, dt \right] dF(x) \\[4pt]
&= \int_{-\infty}^{\infty} \left( 1 - \frac{\sin ax}{ax} \right) dF(x) \\[4pt]
&\geq \inf_{|y| \geq 1} \left( 1 - \frac{\sin y}{y} \right) \cdot \int_{|ax| \geq 1} dF(x) \\[4pt]
&= \frac{1}{K} \int_{|x| \geq 1/a} dF(x),
\end{aligned}
$$

where

$$\frac{1}{K} = \inf_{|y| \geq 1} \left( 1 - \frac{\sin y}{y} \right) = 1 - \sin 1 \geq \frac{1}{7}.$$

The infimum is attained at $y = 1$ since the function $y \mapsto 1 - \frac{\sin y}{y}$ is decreasing on $[1, \infty)$ (one can check that its derivative is negative for $y \geq 1$). The numerical value satisfies $1 - \sin 1 \approx 1 - 0.8415 = 0.1585 \geq \frac{1}{7} \approx 0.1429$.

Thus the inequality holds with $K = \frac{1}{1 - \sin 1} \leq 7$. Therefore

$$\int_{|x| \geq 1/a} dF(x) \leq 7 \cdot \frac{1}{a} \int_{0}^{a} \bigl[ 1 - \operatorname{Re} \varphi(t) \bigr] \, dt,$$

which establishes the lemma. $\square$
