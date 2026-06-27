---
role: proof
locale: en
of_concept: bounded-functions-inf-order-almost-archimedean
source_book: gtm003
source_chapter: "V"
source_section: "Exercises"
---

To show the order is almost Archimedean: Suppose $-n^{-1}y \leq x \leq n^{-1}y$ for all $n \in \mathbf{N}$ and some $y \in E$. Then for each $n$, either $x = n^{-1}y$ or $\inf\{n^{-1}y(t) - x(t)\} > 0$. If $x \neq 0$, pick $t_0 \in T$ with $x(t_0) \neq 0$. Then $x(t_0) \leq n^{-1}y(t_0)$ for all $n$, so $x(t_0) \leq 0$. Similarly $-n^{-1}y(t_0) \leq x(t_0)$, so $x(t_0) \geq 0$. Hence $x(t_0) = 0$, contradiction. Thus $x = 0$.

To show the order is not Archimedean: Take two distinct points $t_1, t_2 \in T$. Define $x(t_1) = -1$, $x(t_2) = 0$, and $x(t) = 0$ elsewhere. Define $y(t_1) = 0$, $y(t_2) = 1$, and $y(t) = 0$ elsewhere. Then $x \leq n^{-1}y$ for all $n$ (since at $t_1$, $x(t_1) = -1 < 0 = n^{-1}y(t_1)$; at $t_2$, $x(t_2) = 0 < n^{-1} = n^{-1}y(t_2)$; elsewhere $x = y = 0$), yet $x \not\leq 0$, violating the Archimedean property.
