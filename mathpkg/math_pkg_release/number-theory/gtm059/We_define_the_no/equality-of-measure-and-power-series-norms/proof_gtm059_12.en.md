---
role: proof
locale: en
of_concept: equality-of-measure-and-power-series-norms
source_book: gtm059
source_chapter: "12"
source_section: "Operations on Measures and Power Series"
---

Since

$$c_i = \int \binom{x}{i} d\mu(x)$$

we get trivially $|f| \leq |x|$. Conversely, given a level $p^N$, let $x_i \in \mathbb{Z}_p$ and let $\varphi$ be the locally constant function such that

$$\varphi(x_i) = 1, \quad \text{and} \quad \varphi(x) = 0 \; \text{if} \; x \neq x_i, \; x \in \mathbb{Z}_p.$$

Then

$$\int \varphi \, d\mu = \mu(x_i) = x_i,$$

and on the other hand, from the corollary of Theorem 1.3, we get

$$\left| \int \varphi \, d\mu \right| \leq |f|.$$

Thus $|x_i| \leq |f|$, and taking the supremum over all $i$ yields $|x| \leq |f|$. Together with the trivial inequality, we obtain $|f| = |x|$.
