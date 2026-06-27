---
role: exercise
locale: en
chapter: "6"
section: "2"
exercise_number: 5
---

# Exercise 5

Let $f_0, f_1: M \to \mathbb{R}$ be Morse functions. It may be impossible to find a $C^2$ homotopy $f: M \times [0,1] \to \mathbb{R}$ such that $f(x,0) = f_0(x)$, $f(x,1) = f_1(x)$ and each map $f_t(x) = f(x,t)$ is a Morse function, $0 \leq t \leq 1$. (Take $M = \mathbb{R}$, $f_0(x) = x^3 - x$, $f_1(x) = x^3 + x$.)

However, a $C^2$ homotopy from $f_0$ to $f_1$ can be found such that each $f_t$ is a Morse function except for a finite set $t_0, \ldots, t_m$; for each $j$, $f_{t_j}$ has only one degenerate critical point $z_j$; in suitable local coordinates at $z_j$, $f_{t_j}$ has the form:

$$-x_1^2 - \cdots - x_k^2 + x_{k+1}^2 + \cdots + x_{n-1}^2 \pm x_n^3 + R(x) + \text{constant}$$

where $R(x)/|x|^3 \to 0$ as $|x| \to 0$. (Assume $f$ is $C^3$ and make the map $(x,t) \mapsto j_x^2 f_t$ transverse to suitable submanifolds of $J^2(M,\mathbb{R})$.)
