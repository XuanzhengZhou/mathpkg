---
role: proof
locale: en
of_concept: bounded-left-difference-quotients-first-category
source_book: gtm002
source_chapter: "11"
source_section: "Nowhere Differentiable Functions"
---

Consider the isometry $T: C \to C$ induced by the substitution of $1 - x$ for $x$, that is, $(Tf)(x) = f(1-x)$. This map is a bijective isometry of $C$ onto itself.

If a function $f \in C$ has a bounded left difference quotient at a point $x_0 \in (0,1]$, then the function $Tf$ has a bounded right difference quotient at $1 - x_0 \in [0,1)$. Explicitly, for $h > 0$ sufficiently small,
$$\frac{(Tf)((1-x_0) + h) - (Tf)(1-x_0)}{h} = \frac{f(x_0 - h) - f(x_0)}{h} = -\frac{f(x_0 + (-h)) - f(x_0)}{-h},$$
so a bound on the right difference quotient of $Tf$ corresponds to a bound on the left difference quotient of $f$.

Since the set of functions with bounded right difference quotients is of first category, and $T$ is a homeomorphism (hence preserves first category sets), the set of functions with bounded left difference quotients is also of first category.
