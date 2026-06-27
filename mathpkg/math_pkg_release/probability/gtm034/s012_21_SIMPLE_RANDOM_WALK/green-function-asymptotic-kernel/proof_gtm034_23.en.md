---
role: proof
locale: en
of_concept: green-function-asymptotic-kernel
source_book: gtm034
source_chapter: "V"
source_section: "23"
---

Assume without loss of generality that $y \leq x$ (the other case follows from the reversed random walk). Using the factorization from P22.4, one writes
$$g(x,y) = \frac{2}{\sigma^2} (y+1) + \rho(x,y)$$
where $\rho(x,y)$ satisfies $|\rho(x,y)| \leq \sum_{k=0}^{y} \epsilon(k)$ with $\epsilon(n) \to 0$.

Using the subtraction formula P1,
$$\frac{\sigma^2}{2N} g_N(x,y) - R\left(\frac{x}{N}, \frac{y}{N}\right) = \frac{\sigma^2}{2N} g(x,y) - \frac{\sigma^2}{2N} \sum_{k=1}^{\infty} R_N(x,k) g(N+k,y) - \frac{y}{N}\left(1 - \frac{x}{N}\right)$$
$$= \frac{y+1}{N} + \frac{1}{N} \rho(x,y) - \frac{y+1}{N} R_N(x) - \frac{1}{N} \sum_{k=1}^{\infty} R_N(x,k) \rho(N+k,y) - \frac{y}{N}\left(1 - \frac{x}{N}\right).$$

The error terms are estimated as follows: $|\frac{1}{N} \rho(x,y)| \leq \frac{1}{N} \sum_{k=0}^{N} \epsilon(k)$ and $|\frac{1}{N} \sum_{k} R_N(x,k) \rho(N+k,y)| \leq \epsilon(y) \frac{y}{N} \leq \frac{1}{N} \sum_{k=0}^{N} \epsilon(k)$. Both tend to zero uniformly as $N \to \infty$ since $\epsilon(k) \to 0$ implies Cesàro convergence. Applying T22.1 ($R_N(x) \to x/N$ uniformly) and simplifying yields the result.
