---
role: proof
locale: en
of_concept: hoeffding-inequality-bernoulli
source_book: gtm095
source_chapter: "1"
source_section: "6"
---

# Proof of the Hoeffding Inequality for the Bernoulli Scheme

Consider $n$ independent Bernoulli trials $\xi_1, \ldots, \xi_n$ with $P(\xi_i = 1) = p$, $P(\xi_i = 0) = q = 1-p$. Let $S_n = \sum_{i=1}^{n} \xi_i$.

We have established the exponential Chebyshev inequality

$$P\{X \geq \varepsilon\} \leq \inf_{\lambda > 0} E[e^{\lambda(X - \varepsilon)}]$$

for any nonnegative random variable $X$. Applying this to $X = S_n/n$ gives the Cramér–Chernoff bound:
for $p \leq a \leq 1$,
$$P\left\{ \frac{S_n}{n} \geq a \right\} \leq e^{-n H(a)},$$
where $H(a) = a\log\frac{a}{p} + (1-a)\log\frac{1-a}{1-p}$ is the binary relative entropy.

Setting $a = p + \varepsilon$ ($\varepsilon > 0$) and using the inequality $H(p+\varepsilon) \geq 2\varepsilon^2$ (which holds for all $0 \leq p \leq 1$, since $H(p+\varepsilon) \geq \frac{\varepsilon^2}{2p(1-p)} \geq 2\varepsilon^2$ because $p(1-p) \leq 1/4$), we obtain the one-sided bound

$$P\left\{ \frac{S_n}{n} - p \geq \varepsilon \right\} \leq e^{-2n\varepsilon^2}. \tag{40}$$

By an entirely symmetric argument (or by replacing successes with failures),

$$P\left\{ \frac{S_n}{n} - p \leq -\varepsilon \right\} \leq e^{-2n\varepsilon^2}. \tag{41}$$

The two-sided **Hoeffding inequality** now follows by the union bound:

$$P\left\{ \left| \frac{S_n}{n} - p \right| \geq \varepsilon \right\} \leq P\left\{ \frac{S_n}{n} - p \geq \varepsilon \right\} + P\left\{ \frac{S_n}{n} - p \leq -\varepsilon \right\} \leq 2e^{-2n\varepsilon^2}. \tag{42}$$

This inequality provides a universal, $p$-independent exponential bound on the probability that the empirical frequency $S_n/n$ deviates from the true probability $p$ by more than $\varepsilon$. It holds for every $\varepsilon > 0$, every $n \geq 1$, and every $0 \leq p \leq 1$.
