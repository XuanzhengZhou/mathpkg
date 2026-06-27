---
role: exercise
locale: en
chapter: "7"
section: "Differential equations"
exercise_number: 9
---

# Exercise 9

Suppose $u: [0, \infty) \to \mathbb{C}$ is $C^\infty$ on $(0, \infty)$, all derivatives extend continuously to $0$, and $e^{-at} D^k u(t)$ is bounded on $[0, \infty)$ for each $k$, for some $a \in \mathbb{R}$. Let $u$ be extended to be $0$ on $(-\infty, 0)$, and let $F_0$ be the corresponding distribution in $\mathcal{L}'$. For each $k \geq 0$, let $F_k$ be the distribution corresponding to the function $D^k u$ (again extended by $0$ on the negative half-line). Show that

$$D F_0 = F_1 + u(0+) \delta,$$

and in general

$$D^k F_0 = F_k + \sum_{j=0}^{k-1} D^j u(0+) \, D^{k-1-j} \delta.$$
