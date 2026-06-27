---
role: proof
locale: en
of_concept: polynomial-division-algorithm
source_book: gtm030
source_chapter: "3"
source_section: "5"
---

If $\deg f(x) < \deg g(x)$, take $q_1(x) = 0$ and $r_1(x) = f(x)$. Otherwise, let $n = \deg f$ and $m = \deg g$ with $n \geq m$. Write $f(x) = a_n x^n + \cdots$ with $a_n \neq 0$ and $g(x) = b_m x^m + \cdots$ with $b_m$ a unit. Define $f_1(x) = f(x) - a_n b_m^{-1} x^{n-m} g(x)$, which has degree strictly less than $n$. By induction on the degree, $f_1(x) = q_1'(x)g(x) + r_1(x)$ with $\deg r_1(x) < \deg g(x)$. Then $f(x) = (a_n b_m^{-1} x^{n-m} + q_1'(x))g(x) + r_1(x)$, establishing existence.

For uniqueness, suppose $f = q_1 g + r_1 = \tilde{q}_1 g + \tilde{r}_1$ with $\deg r_1, \deg \tilde{r}_1 < \deg g$. Then $(q_1 - \tilde{q}_1)g = \tilde{r}_1 - r_1$. The degree of the right-hand side is $< \deg g$, while the degree of the left-hand side is either $-\infty$ or $\geq \deg g$ (since the leading coefficient of $g$ is a unit, hence not a zero-divisor). Therefore both sides have degree $-\infty$, meaning $r_1 = \tilde{r}_1$ and $q_1 = \tilde{q}_1$.
