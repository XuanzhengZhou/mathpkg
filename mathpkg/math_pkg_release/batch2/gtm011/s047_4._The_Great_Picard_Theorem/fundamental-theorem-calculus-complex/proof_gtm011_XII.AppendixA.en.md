---
role: proof
locale: en
of_concept: fundamental-theorem-calculus-complex
source_book: gtm011
source_chapter: "XII"
source_section: "Appendix A. Calculus for Complex Valued Functions on an Interval"
---

Let $g$ be a primitive of $\operatorname{Re} f$ and $h$ be a primitive of $\operatorname{Im} f$. Such primitives exist by the Fundamental Theorem of Calculus for real-valued functions, since $\operatorname{Re} f$ and $\operatorname{Im} f$ are continuous real-valued functions on $[a, b]$. Define $F = g + i h$. Then

$$F'(x) = g'(x) + i h'(x) = \operatorname{Re} f(x) + i \operatorname{Im} f(x) = f(x),$$

so $F$ is a primitive of $f$.

If $F_1$ and $F_2$ are two primitives of $f$, then $(F_1 - F_2)' = F_1' - F_2' = f - f = 0$. By Proposition A.2, this implies $F_1 - F_2$ is constant.

By definition of the integral of a complex-valued function,

$$\int_a^b f(x) \, dx = \int_a^b \operatorname{Re} f(x) \, dx + i \int_a^b \operatorname{Im} f(x) \, dx.$$

Applying the real Fundamental Theorem of Calculus to each term,

$$\int_a^b \operatorname{Re} f(x) \, dx = g(b) - g(a), \quad \int_a^b \operatorname{Im} f(x) \, dx = h(b) - h(a).$$

Therefore,

$$\int_a^b f(x) \, dx = [g(b) - g(a)] + i [h(b) - h(a)] = (g(b) + i h(b)) - (g(a) + i h(a)) = F(b) - F(a).$$

The result follows.
