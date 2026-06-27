---
role: proof
locale: en
of_concept: product-continuity-normed-algebra
source_book: gtm015
source_chapter: "VI"
source_section: "49"
---

# Proof of Continuity of Multiplication in a Normed Algebra

Let $A$ be a normed algebra. The multiplication mapping $m: A \times A \to A$, $m(x, y) = xy$, is to be shown jointly continuous.

(i) **Continuity at a point $(x_0, y_0)$:** Write
$$xy - x_0y_0 = (x - x_0)(y - y_0) + x_0(y - y_0) + (x - x_0)y_0.$$

Taking norms and using the submultiplicative property $\|ab\| \leq \|a\|\|b\|$,
$$\|xy - x_0y_0\| \leq \|x - x_0\|\|y - y_0\| + \|x_0\|\|y - y_0\| + \|x - x_0\|\|y_0\|.$$

As $(x, y) \to (x_0, y_0)$, the right-hand side tends to $0$, proving continuity at $(x_0, y_0)$. Since every point is a continuity point, multiplication is jointly continuous on $A \times A$.

(ii) **Multiplication of Cauchy sequences:** Suppose $(x_n)$ and $(y_n)$ are Cauchy sequences in $A$. Since $\|x_n\|$ and $\|y_n\|$ are bounded (by (16.4), norms of Cauchy sequences are bounded), it follows from
$$\|x_m y_m - x_n y_n\| = \|x_m y_m - x_m y_n + x_m y_n - x_n y_n\| \leq \|x_m\|\|y_m - y_n\| + \|x_m - x_n\|\|y_n\|$$
that $(x_n y_n)$ is also Cauchy. This establishes the continuity of the extension of multiplication to the completion. $\square$
