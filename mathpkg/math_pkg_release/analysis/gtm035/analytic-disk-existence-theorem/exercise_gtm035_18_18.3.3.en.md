---
role: exercise
locale: en
chapter: "18"
section: "18.3"
exercise_number: 3
---
# Exercise 18.3

Let $h$ be a smooth function on $\mathbb{R}^N$ which vanishes at $0$ of order $\geq 2$. Let the notation be as in Exercise 18.2.

Show that there exists a constant $K$ depending only on $h$ such that for every pair of maps $x, y$ of $\Gamma$ into $\mathbb{R}^N$ with $\|x\|_\infty \leq 1$ and $\|y\|_\infty \leq 1$, the following inequality holds:

$$\|h(x) - h(y)\|_1 \leq K \|x - y\|_1 (\|x\|_1 + \|y\|_1).$$

*Hint.* Write

$$h(x) - h(y) = \int_0^1 \frac{d}{dt} h(y + t(x - y)) dt = \int_0^1 \nabla h(y + t(x - y)) \cdot (x - y) dt.$$

Since $\nabla h(0) = 0$, Taylor-expand $\nabla h$ around $0$ and use the estimate from Exercise 18.2 on the resulting expression, together with the Sobolev embedding.
