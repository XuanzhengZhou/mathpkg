---
role: proof
locale: en
of_concept: zeta-function-simple-pole
source_book: gtm007
source_chapter: "VI"
source_section: "§1. Characters of finite abelian groups"
---

From Proposition 10, $\zeta(s) = 1/(s-1) + \phi(s)$ with $\phi$ holomorphic. Hence $\zeta(s)$ has a simple pole at $s=1$ with residue $1$. Taking the logarithm of the Euler product,
$$
\log \zeta(s) = \sum_{p} \sum_{n=1}^\infty \frac{1}{n p^{ns}} = \sum_p \frac{1}{p^s} + \sum_p \sum_{n \geq 2} \frac{1}{n p^{ns}}.
$$
The double sum converges for $s=1$, so it remains bounded. Hence $\sum_p 1/p^s = \log \zeta(s) + O(1) \sim \log\frac{1}{s-1}$.
