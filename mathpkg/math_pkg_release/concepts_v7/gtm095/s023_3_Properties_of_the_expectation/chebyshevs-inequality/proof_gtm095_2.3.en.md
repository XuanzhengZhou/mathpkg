---
role: proof
locale: en
of_concept: chebyshevs-inequality
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof of Chebyshev's Inequality

**Chebyshev's Inequality.** If $\xi$ is any random variable, then for every $\varepsilon > 0$,

$$P(|\xi| \geq \varepsilon) \leq \frac{E\xi^2}{\varepsilon^2},$$

and

$$P(|\xi - E\xi| \geq \varepsilon) \leq \frac{\operatorname{Var}\xi}{\varepsilon^2},$$

where $\operatorname{Var}\xi = E(\xi - E\xi)^2$ is the variance of $\xi$.

*Proof.* For the first inequality, note that $|\xi| \geq \varepsilon$ implies $|\xi|^2/\varepsilon^2 \geq 1$ on the set $\{|\xi| \geq \varepsilon\}$. Hence

$$I_{\{|\xi| \geq \varepsilon\}} \leq \frac{\xi^2}{\varepsilon^2}.$$

Taking expectations of both sides (using Property B, monotonicity of expectation),

$$P(|\xi| \geq \varepsilon) = E[I_{\{|\xi| \geq \varepsilon\}}] \leq E\left[\frac{\xi^2}{\varepsilon^2}\right] = \frac{E\xi^2}{\varepsilon^2}.$$

For the second inequality, apply the first inequality to the random variable $\xi - E\xi$, noting that $E[(\xi - E\xi)^2] = \operatorname{Var}\xi$. Then

$$P(|\xi - E\xi| \geq \varepsilon) \leq \frac{E[(\xi - E\xi)^2]}{\varepsilon^2} = \frac{\operatorname{Var}\xi}{\varepsilon^2}.$$

$\square$
