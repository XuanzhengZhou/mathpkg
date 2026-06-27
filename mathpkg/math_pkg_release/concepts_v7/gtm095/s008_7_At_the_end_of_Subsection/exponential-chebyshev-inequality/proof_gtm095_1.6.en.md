---
role: proof
locale: en
of_concept: exponential-chebyshev-inequality
source_book: gtm095
source_chapter: "1"
source_section: "6"
---

# Proof of the Exponential Chebyshev Inequality

Let $X \geq 0$ be a nonnegative random variable and let $\varepsilon > 0$, $\lambda > 0$. Then

$$P\{X \geq \varepsilon\} = P\{e^{\lambda X} \geq e^{\lambda \varepsilon}\}.$$

Since $e^{\lambda X} \geq 0$, by Markov's inequality (the "exponential form" of Chebyshev's inequality),

$$P\{e^{\lambda X} \geq e^{\lambda \varepsilon}\} \leq \frac{E[e^{\lambda X}]}{e^{\lambda \varepsilon}} = E[e^{\lambda(X - \varepsilon)}].$$

Because the positive number $\lambda$ is arbitrary, we may take the infimum over all $\lambda > 0$, yielding

$$P\{X \geq \varepsilon\} \leq \inf_{\lambda > 0} E[e^{\lambda(X - \varepsilon)}].$$

This inequality transforms the problem of bounding tail probabilities into an optimization over exponential moments, and serves as the foundation for the Chernoff (Cramér) bound technique applied to sums of independent random variables.
