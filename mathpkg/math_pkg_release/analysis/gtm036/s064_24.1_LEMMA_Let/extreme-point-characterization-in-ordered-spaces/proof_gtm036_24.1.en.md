---
role: proof
locale: en
of_concept: extreme-point-characterization-in-ordered-spaces
source_book: gtm036
source_chapter: "24"
source_section: "24.1"
---

Suppose that $x$ is an extreme point of $A$ and that $x \geq y \geq 0$. If $x = 0$, then $f(x) = f(y) = 0$; by (iii) it follows that $y = 0$, and hence $y = f(y)x$. If $x \neq 0$ then, since $f(x) \leq 1$ and both $0$ and $x/f(x)$ belong to $A$, $f(x) = 1$; otherwise $x$ could not be an extreme point. If $x \neq 0$ and $x - y = 0$, then again $y = f(y)x$. If neither $y$ nor $x - y$ is $0$, then $f(y) + f(x - y) = 1$, and writing
$$x = f(y)\left[\frac{y}{f(y)}\right] + f(x - y)\left[\frac{x - y}{f(x - y)}\right],$$
the fact that $x$ is extreme implies that $y/f(y) = x$.

To prove the converse, suppose that $x$ is a member of $A$ such that $y = f(y)x$ for each $y$ with $x \geq y \geq 0$. If $x = t a + (1-t) b$ with $a, b \in A$ and $0 < t < 1$, then $x \geq t a \geq 0$ and $x \geq (1-t)b \geq 0$, so by the hypothesis $ta = f(ta)x$ and $(1-t)b = f((1-t)b)x$. Since $f$ is positive and $A \subseteq$ positive cone, $f(ta), f((1-t)b) \geq 0$. Moreover $f(x) = f(ta) + f((1-t)b)$, and since $f(x) = 1$ (because $x \neq 0$ and by (iii)), the convex combination $x = f(ta)x + f((1-t)b)x$ forces $a = b = x$. Hence $x$ is an extreme point of $A$.
