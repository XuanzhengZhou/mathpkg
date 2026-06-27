---
role: proof
locale: en
of_concept: bernoulli-large-deviations-exponential-bound
source_book: gtm095
source_chapter: "1"
source_section: "6"
---

# Proof of the Exponential Large Deviations Bound for the Bernoulli Scheme

We build on the Cramér–Chernoff bound established previously. For independent Bernoulli trials $\xi_1, \ldots, \xi_n$ with $P(\xi_i = 1) = p$ and $S_n = \sum_{i=1}^{n} \xi_i$, the Chernoff bound states that for $p \leq a \leq 1$,

$$P\left\{ \frac{S_n}{n} \geq a \right\} \leq e^{-n H(a)},$$

where $H(a) = a \log \frac{a}{p} + (1-a) \log \frac{1-a}{1-p}$ is the binary relative entropy.

To obtain a simpler exponential bound in terms of $\varepsilon$, set $a = p + \varepsilon$ for $\varepsilon > 0$. By Taylor expansion,
$$H(p + \varepsilon) = \frac{\varepsilon^2}{2} \cdot \frac{1}{p(1-p)} + O(\varepsilon^3).$$

More directly, one can show the elementary inequality (valid for all $0 \leq p \leq 1$ and $\varepsilon > 0$ with $p + \varepsilon \leq 1$):

$$H(p + \varepsilon) \geq 2\varepsilon^2.$$

This follows from the fact that $H(p+\varepsilon) = \sup_{s > 0} [(p+\varepsilon) s - \log(1-p+pe^s)]$ and a direct optimization argument, or equivalently from the inequality $H(p+\varepsilon) \geq \inf_{p} \frac{d^2 H}{dp^2}\big|_{p} \cdot \frac{\varepsilon^2}{2} = \frac{\varepsilon^2}{2 p(1-p)} \geq 2\varepsilon^2$, since $p(1-p) \leq 1/4$.

Applying this inequality to the Chernoff bound yields the **one-sided exponential bound**:

$$P\left\{ \frac{S_n}{n} - p \geq \varepsilon \right\} \leq e^{-2n\varepsilon^2}. \tag{40}$$

By symmetry (replacing successes by failures), we also obtain

$$P\left\{ \frac{S_n}{n} - p \leq -\varepsilon \right\} \leq e^{-2n\varepsilon^2}. \tag{41}$$

These bounds are valid for every $\varepsilon > 0$ and every $0 \leq p \leq 1$. They demonstrate that the probability of a deviation of size $\varepsilon$ in the sample mean decays at least as fast as $e^{-2n\varepsilon^2}$ — a Gaussian-type exponential rate that is universal (independent of $p$).
