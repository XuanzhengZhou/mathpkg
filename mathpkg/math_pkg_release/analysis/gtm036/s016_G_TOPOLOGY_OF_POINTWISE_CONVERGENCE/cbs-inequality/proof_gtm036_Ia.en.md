---
role: proof
locale: en
of_concept: cbs-inequality
source_book: gtm036
source_chapter: "I"
source_section: "I(a)"
---

Consider the vector $z = (y,y)x - (x,y)y$. Computing its inner product with itself:
$$
\begin{aligned}
(z,z) &= ((y,y)x - (x,y)y, (y,y)x - (x,y)y) \\
&= (y,y)^2 (x,x) - (y,y)(x,y)(x,y) - (y,y)\overline{(x,y)}(y,x) + |(x,y)|^2 (y,y) \\
&= (y,y)^2 (x,x) - (y,y)|(x,y)|^2 - (y,y)|(x,y)|^2 + |(x,y)|^2 (y,y) \\
&= (y,y)\big[(y,y)(x,x) - |(x,y)|^2\big].
\end{aligned}
$$

Since $(z,z) \geq 0$, we have $(y,y)(x,x) - |(x,y)|^2 \geq 0$ whenever $(y,y) > 0$. If $(y,y) = 0$, then $y = 0$ and the inequality holds trivially. Thus $|(x,y)|^2 \leq (x,x)(y,y)$.

If $x$ and $y$ are linearly dependent, say $x = \lambda y$, then $|(x,y)|^2 = |\lambda|^2 (y,y)^2 = (\lambda y, \lambda y)(y,y) = (x,x)(y,y)$. Conversely, if equality holds, then $(z,z) = 0$, so $z = 0$, i.e., $(y,y)x = (x,y)y$, showing $x$ and $y$ are linearly dependent.
