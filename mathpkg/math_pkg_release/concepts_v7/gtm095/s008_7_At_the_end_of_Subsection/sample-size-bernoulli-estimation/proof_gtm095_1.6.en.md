---
role: proof
locale: en
of_concept: sample-size-bernoulli-estimation
source_book: gtm095
source_chapter: "1"
source_section: "6"
---

# Proof of Sample Size for Bernoulli Probability Estimation

We seek the smallest number of observations $n$ that guarantees, for a given accuracy $\varepsilon > 0$ and confidence level $1 - \alpha$ ($0 < \alpha < 1$), the inequality

$$P\left\{ \left| \frac{S_n}{n} - p \right| \leq \varepsilon \right\} \geq 1 - \alpha, \tag{43}$$

uniformly for all $0 \leq p \leq 1$.

Equivalently, we require
$$P\left\{ \left| \frac{S_n}{n} - p \right| \geq \varepsilon \right\} \leq \alpha.$$

Applying the Hoeffding inequality (42),
$$P\left\{ \left| \frac{S_n}{n} - p \right| \geq \varepsilon \right\} \leq 2e^{-2n\varepsilon^2}.$$

It therefore suffices to have
$$2e^{-2n\varepsilon^2} \leq \alpha.$$

Taking logarithms,
$$-2n\varepsilon^2 \leq \log\frac{\alpha}{2} = -\log\frac{2}{\alpha},$$
so
$$n \geq \frac{\log(2/\alpha)}{2\varepsilon^2}.$$

The smallest integer $n$ satisfying this condition is given by the formula

$$n_3(\alpha) = \left[ \frac{\log(2/\alpha)}{2\varepsilon^2} \right], \tag{44}$$

where $[x]$ denotes the integral part (floor) of $x$.

**Comparison with Chebyshev's inequality.** The earlier estimate obtained from the ordinary Chebyshev inequality gave $n_1(\alpha) = [1/(4\alpha\varepsilon^2)]$. The ratio of the two estimates is

$$\frac{n_1(\alpha)}{n_3(\alpha)} = \frac{1}{2\alpha \log(2/\alpha)} \to \infty \quad \text{as } \alpha \downarrow 0.$$

This demonstrates that the estimate derived from the exponential Chebyshev (Hoeffding) inequality is asymptotically far more efficient than the one obtained from the ordinary Chebyshev inequality, especially when high confidence (small $\alpha$) is required.
