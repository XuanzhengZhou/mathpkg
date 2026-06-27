---
role: exercise
locale: en
chapter: "7"
section: "Differential equations"
exercise_number: 5
---

# Exercise 5

Suppose $u_0 : (0, \infty) \to \mathbb{C}$ is such that

$$D^k u_0(0+) = b_k, \qquad 0 \leq k \leq n-1.$$

Show that $u$ is a solution of

$$p(D)u(t) = f(t), \quad t > 0,$$
$$D^k u(0+) = b_k, \quad 0 \leq k < n$$

if and only if $u = u_0 + u_1$, where $u_1$ is the solution of

$$p(D)u_1(t) = f(t) - p(D)u_0(t), \quad t > 0,$$
$$D^k u_1(0+) = 0, \quad 0 \leq k \leq n-1.$$
