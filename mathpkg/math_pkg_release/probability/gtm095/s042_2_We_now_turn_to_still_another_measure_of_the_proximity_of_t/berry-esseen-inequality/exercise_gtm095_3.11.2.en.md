---
role: exercise
locale: en
chapter: "3"
section: "11.1"
exercise_number: 2
---

# Exercise 2

Let $\xi_1, \xi_2, \ldots$ be independent identically distributed random variables with $\mathbb{E}\xi_1 = 0$, $\mathbb{V}\text{ar}\,\xi_1 = \sigma^2$, and $\mathbb{E}|\xi_1|^3 < \infty$. It is known that the following nonuniform inequality holds: for all $x \in \mathbb{R}$,

$$|F_n(x) - \Phi(x)| \leq \frac{C\,\mathbb{E}|\xi_1|^3}{\sigma^3 \sqrt{n}} \cdot \frac{1}{(1 + |x|)^3}.$$

Prove this, at least for Bernoulli random variables.

Here $F_n(x) = \mathbb{P}(S_n \leq x)$ with $S_n = (\xi_1 + \cdots + \xi_n)/(\sigma\sqrt{n})$, and $\Phi(x)$ is the standard normal distribution function.
