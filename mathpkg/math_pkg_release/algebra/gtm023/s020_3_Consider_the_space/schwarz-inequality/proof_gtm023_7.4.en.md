---
role: proof
locale: en
of_concept: schwarz-inequality
source_book: gtm023
source_chapter: "7"
source_section: "7.4"
---

Consider the quadratic function of the real variable $\lambda$:

$$|x + \lambda y|^2 = (x + \lambda y, x + \lambda y).$$

By definiteness of the inner product, $|x + \lambda y|^2 \geq 0$ for all $-\infty < \lambda < \infty$. Expanding the norm using bilinearity,

$$|x + \lambda y|^2 = \lambda^2 |y|^2 + 2\lambda(x, y) + |x|^2 \geq 0.$$

This is a quadratic expression in $\lambda$ that is everywhere nonnegative. Hence its discriminant must be non-positive:

$$\Delta = 4(x, y)^2 - 4|x|^2 |y|^2 \leq 0,$$

which yields the Schwarz inequality

$$(x, y)^2 \leq |x|^2 |y|^2.$$

Now assume that equality holds. Then the discriminant is zero, so the quadratic equation

$$\lambda^2 |y|^2 + 2\lambda(x, y) + |x|^2 = 0$$

has a real solution $\lambda_0$. It follows that

$$|\lambda_0 y + x|^2 = 0,$$

and by definiteness, $\lambda_0 y + x = 0$, i.e. $x = -\lambda_0 y$. Thus $x$ and $y$ are linearly dependent. Conversely, if $x$ and $y$ are linearly dependent, say $x = \alpha y$, then a direct computation shows equality holds.
