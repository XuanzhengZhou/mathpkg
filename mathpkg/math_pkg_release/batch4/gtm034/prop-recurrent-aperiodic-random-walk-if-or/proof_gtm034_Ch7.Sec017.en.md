---
role: proof
locale: en
of_concept: prop-recurrent-aperiodic-random-walk-if-or
source_book: gtm034
source_chapter: "7"
source_section: "017"
---

Proof: The first part of P1 is simply a restatement of part (b) of T28.1. The second part requires proof. In view of T28.1, $a(x)$ satisfies equation (1). But also $f(x) = x$ satisfies (1)—this is clear since recurrent random walk with $\sigma^2 < \infty$ has mean zero. Thus $f(x) = a(x) + \alpha x$ satisfies (1), but it is not necessarily non-negative on $R - \{0\}$, as required. Now the condition that $|\alpha

which implies that $|\alpha| \leq (\sigma^2)^{-1}$. To prove sufficiency, suppose that $|\alpha| \leq (\sigma^2)^{-1}$. We know that

$$0 \leq g_{(0)}(x,y) = a(x) + a(-y) - a(x-y).$$

Using T29.1 to let $y \rightarrow +\infty$ and $y \rightarrow -\infty$, we obtain

$$0 \leq a(x) + \frac{x}{\sigma^2}, \quad 0 \leq a(x) - \frac{x}{\sigma^2}, \quad x \in R.$$

Since these functions are non-negative, so is $a(x) + \alpha x$ whenever $|\alpha| \leq (\sigma^2)^{-1}$.

We are now ready to prove uniqueness, which constitutes a considerably more delicate task.
