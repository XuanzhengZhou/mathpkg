---
role: exercise
locale: en
chapter: "10"
section: "Compact Convex Sets"
exercise_number: 4
---

A real-valued function $\psi$ defined on $\mathbb{R}^n$ is called sublinear if it is convex and positive homogeneous (i.e., $\psi(\lambda x) = \lambda \psi(x)$ for all $x \in \mathbb{R}^n$ and all $\lambda \geq 0$).

(a) Every sublinear function on $\mathbb{R}^n$ is continuous; examples are $x \mapsto \sup x_i$, $x \mapsto [\sum |x_i|^q]^{1/q}$ ($q \geq 1$) ($i = 1, \ldots, n$). (Use Exercises 2, 3.)

(b) If $\psi$ is a sublinear function on $\mathbb{R}^n$ such that $\psi(x_1, \ldots, x_n) \geq 0$ whenever $x_i \geq 0$ ($i = 1, \ldots, n$) and $\psi(x_1, \ldots, x_n) \leq 0$ if all $x_i \leq 0$, and if $p_i$ are continuous semi-norms on a t.v.s. $E$, then $\psi(p_1, \ldots, p_n)$ is a continuous semi-norm on $E$.

(c) Assume that $\psi$ is a sublinear function on $\mathbb{R}^n$, as in (b), having the additional property that $x_i \geq 0$ ($i = 1, \ldots, n$) and $\psi(x_1, \ldots, x_n) = 0$ imply $x_i = 0$ ($i = 1, \ldots, n$). Show that if $(E_i, p_i)$ are $n$ normed spaces, then $(x_1, \ldots, x_n) \mapsto \psi[p_1(x_1), \ldots, p_n(x_n)]$ is a norm on $\prod_i E_i$ generating the product topology.
