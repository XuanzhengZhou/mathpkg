---
role: proof
locale: en
of_concept: proposition-1-45
source_book: gtm040
source_chapter: "1"
source_section: "45"
---

**Proof:** We first prove the assertion for $f$ and $g$ non-negative. For simple functions the assertion is trivial. If $f$ and $g$ are not both simple, apply Proposition 1-38 to find monotone sequences of non-negative measurable simple functions $\{t_n\}$ and $\{u_n\}$ converging to $f$ and $g$. Then $\{s_n = t_n + u_n\}$ converges to $h$, and since

$$\int_E s_n d\mu = \int_E t_n d\mu + \int_E u_n d\mu,$$

the result follows from Theorem 1-44. Next, if $f \geq 0$, $g \leq 0$, and $h = f + g \geq 0$, we have $f = h + (-g)$ with $h \geq 0$ and $(-g) \

$f < 0$ and $g \geq 0$. Theorem 1-41 then gives the desired result. Finally, for general $h$, write $h = h^+ - h^-$ and consider $h^+$ and $h^-$ separately.
