---
role: proof
locale: en
of_concept: lemma-2c2913cc
source_book: gtm077
source_chapter: "VIII"
source_section: "54"
---
# Proof of Lemma (a) — Positive Definite Forms Bounded Below

**Statement.** For each positive definite quadratic form $Q(x_1, \ldots, x_n)$ there is a positive quantity $c$, such that for all real $x_1, \ldots, x_n$

$$Q(x_1, \ldots, x_n) \geq c(x_1^2 + x_2^2 + \cdots + x_n^2).$$

**Proof.** By hypothesis $Q(y_1, \ldots, y_n) > 0$ for all points of the $n$-dimensional sphere

$$y_1^2 + y_2^2 + \cdots + y_n^2 = 1.$$

The sphere is a compact set, and $Q$ is a continuous function (it is a polynomial in $y_1, \ldots, y_n$). Consequently, $Q$ attains a positive minimum $c > 0$ on the surface of the sphere. That is, for all $(y_1, \ldots, y_n)$ with $\sum y_i^2 = 1$, we have

$$Q(y_1, \ldots, y_n) \geq c.$$

For an arbitrary nonzero vector $(x_1, \dots, x_n) \neq (0,\dots,0)$, set $r = \sqrt{x_1^2 + \cdots + x_n^2} > 0$ and define $y_i = x_i / r$. Then $\sum y_i^2 = 1$ and by homogeneity of the quadratic form,

$$Q(x_1, \ldots, x_n) = Q(r y_1, \ldots, r y_n) = r^2 Q(y_1, \ldots, y_n) \geq r^2 \cdot c = c(x_1^2 + \cdots + x_n^2).$$

For the zero vector the inequality holds trivially. Thus the lemma is proved.

*This lemma is fundamental for establishing the uniform convergence of $n$-tuple theta-series, which in turn leads to the transformation formula for theta-functions and ultimately to the analytic proof of the quadratic reciprocity law in arbitrary algebraic number fields.*
