---
role: proof
locale: en
of_concept: law-of-large-numbers
source_book: gtm095
source_chapter: "Chapter 1"
source_section: "§7. Variance, covariance, Chebyshev inequality"
---

# Proof of Corollary (Chebyshev's inequality corollaries)

The corollary consists of two inequalities, both following directly from Chebyshev's inequality.

**First inequality.** Let $\xi$ be any random variable on $(\Omega, \mathcal{A})$. Then $|\xi|$ is a nonnegative random variable. Applying Chebyshev's inequality to $|\xi|$, we obtain for any $\varepsilon > 0$:

$$P\{|\xi| \geq \varepsilon\} \leq \frac{E|\xi|}{\varepsilon}.$$

**Second inequality.** Apply the first inequality to the random variable $|\xi - E\xi|$. This yields

$$P\{|\xi - E\xi| \geq \varepsilon\} \leq \frac{E|\xi - E\xi|}{\varepsilon}.$$

Alternatively, we can obtain a bound in terms of the variance by applying Chebyshev's inequality directly to the nonnegative random variable $(\xi - E\xi)^2$ with threshold $\varepsilon^2$:

$$P\{|\xi - E\xi| \geq \varepsilon\} = P\{(\xi - E\xi)^2 \geq \varepsilon^2\} \leq \frac{E(\xi - E\xi)^2}{\varepsilon^2} = \frac{\operatorname{Var}\xi}{\varepsilon^2}.$$

Both inequalities are immediate consequences of Chebyshev's inequality applied to suitably chosen nonnegative random variables.

---

**Application: Bernoulli's law of large numbers.** Taking $\xi = S_n/n - p$ where $S_n \sim \operatorname{Binomial}(n, p)$, we have $E\xi = 0$ and $\operatorname{Var}\xi = \operatorname{Var}(S_n)/n^2 = npq/n^2 = pq/n$. The second inequality then gives

$$P\left\{\left|\frac{S_n}{n} - p\right| \geq \varepsilon\right\} \leq \frac{pq}{n\varepsilon^2} \leq \frac{1}{4n\varepsilon^2},$$

since $pq = p(1-p) \leq 1/4$ for $0 \leq p \leq 1$. As $n \to \infty$, the right-hand side tends to $0$, establishing the law of large numbers.
