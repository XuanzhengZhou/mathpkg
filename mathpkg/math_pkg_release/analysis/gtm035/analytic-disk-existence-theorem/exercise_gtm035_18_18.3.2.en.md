---
role: exercise
locale: en
chapter: "18"
section: "18.3"
exercise_number: 2
---
# Exercise 18.2

Let $h$ be a smooth function on $\mathbb{R}^N$ which vanishes at $0$ of order $\geq 2$. Let $\Gamma = \{|\zeta| = 1\}$ and let $H_1$ be the Banach space of real-valued functions on $\Gamma$ with norm

$$\|x\|_1 = \sqrt{\int_\Gamma |x|^2 d\theta} + \sqrt{\int_\Gamma |\dot{x}|^2 d\theta},$$

and $\|x\|_\infty = \sup_{\zeta \in \Gamma} |x(\zeta)|$.

Show that there exists a constant $K$ depending only on $h$ such that for every map $x = (x_1, \ldots, x_N)$ of $\Gamma$ into $\mathbb{R}^N$ with each $x_i \in H_1$ and $\|x\|_\infty \leq 1$, the following inequality holds:

$$\|h(x)\|_1 \leq K (\|x\|_1)^2,$$

where $\|x\|_1 = \sqrt{\sum_{i=1}^N \|x_i\|_1^2}$.

*Hint.* Use Taylor expansion of $h$ around $0$, noting that the constant and linear terms vanish since $h(0) = 0$ and $dh(0) = 0$. Apply the Sobolev embedding $\|x\|_\infty \leq C\|x\|_1$ to bound the remainder.
