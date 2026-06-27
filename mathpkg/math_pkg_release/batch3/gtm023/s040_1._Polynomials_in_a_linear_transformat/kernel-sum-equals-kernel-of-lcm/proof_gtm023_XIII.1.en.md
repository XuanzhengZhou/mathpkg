---
role: proof
locale: en
of_concept: kernel-sum-equals-kernel-of-lcm
source_book: gtm023
source_chapter: "XIII"
source_section: "§1. Polynomials in a linear transformation"
---

Since $f \mid v$ and $g \mid v$, it follows from (13.1) that $K(f) \subset K(v)$ and $K(g) \subset K(v)$; hence

$$K(v) \supset K(f) + K(g). \tag{13.5}$$

On the other hand, since $v$ is the least common multiple of $f$ and $g$, there exist polynomials $f_1, g_1$ such that

$$f_1 f = v = g_1 g$$

and $f_1, g_1$ are relatively prime. Choose polynomials $f_2, g_2$ with $f_2 f_1 + g_2 g_1 = 1$; then

$$f_2(\varphi) f_1(\varphi) + g_2(\varphi) g_1(\varphi) = 1.$$

Consequently each $x \in E$ can be written as $x = x_1 + x_2$ where

$$x_1 = f_2(\varphi) f_1(\varphi) x, \qquad x_2 = g_2(\varphi) g_1(\varphi) x.$$

Now suppose $x \in K(v)$. Then

$$f_1(\varphi) f(\varphi) x = g_1(\varphi) g(\varphi) x = v(\varphi) x = 0,$$

which implies $f(\varphi) x_1 = 0$ and $g(\varphi) x_2 = 0$. Hence $x_1 \in K(f)$, $x_2 \in K(g)$, so $x \in K(f) + K(g)$. Thus

$$K(v) \subset K(f) + K(g). \tag{13.7}$$

Together, (13.5) and (13.7) yield $K(v) = K(f) + K(g)$.
