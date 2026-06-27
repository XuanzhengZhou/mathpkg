---
role: proof
locale: en
of_concept: division-ring-from-skewfield-is-division-ring
source_book: gtm006
source_chapter: "IX"
source_section: "4"
---

Since $F$ has finite dimension over its centre $Z$, and $D$ has dimension 2 over $F$, $D$ has finite dimension over $K = Z \cap \operatorname{Fix}(\theta)$ as well. Let $k = \dim_F K$, then $\dim_K D = 2k$. The field $K$ is contained in the centre of $D$. By Exercise 8.3, since $D$ is finite-dimensional over its centre, it suffices to show that $(x + \lambda y)(z + \lambda t) = 0$ implies $x + \lambda y = 0$ or $z + \lambda t = 0$.

Setting the multiplication formula equal to $0$:
\[
xz + a t y^\theta = 0, \tag{4a}
\]
\[
z y + x^\theta t + y^\theta b t = 0. \tag{4b}
\]

Multiply (4a) on the right by $y$, (4b) on the left by $x$, and subtract:
\[
a t y^{1+\theta} - x^{1+\theta} t - x y^\theta b t = 0. \tag{5}
\]

If $t = 0$, then (4) gives $xz = zy = 0$, so either $x = y = 0$ or $z = 0$. Assume $t \neq 0$. Since $y^{1+\theta} \in Z$, (5) becomes:
\[
a y^{1+\theta} - x^{1+\theta} - x y^\theta b = 0. \tag{6}
\]

If $y = 0$, then (6) gives $x^{1+\theta} = 0$, so $x = 0$. Assume $y \neq 0$ and write $x = x_1 y$. Then $x^\theta = y^\theta x_1^\theta$ and $x^{1+\theta} = x_1 y^{1+\theta} x_1^\theta = x_1^{1+\theta} y^{1+\theta}$ (since $y^{1+\theta} \in Z$). Equation (6) becomes:
\[
a y^{1+\theta} - x_1^{1+\theta} y^{1+\theta} - x_1 y y^\theta b = 0,
\]
which yields $a = x_1^{1+\theta} + x_1 b$, contradicting condition (2). Thus the only solutions to $(x + \lambda y)(z + \lambda t) = 0$ are the trivial ones. $\square$
