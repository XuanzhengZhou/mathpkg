---
role: proof
locale: en
of_concept: schwarz-equality-condition
source_book: gtm023
source_chapter: "7"
source_section: "7.4"
---

Assume equality holds in the Schwarz inequality, i.e. $(x, y)^2 = |x|^2 |y|^2$. Then the discriminant of the quadratic equation

$$\lambda^2 |y|^2 + 2\lambda(x, y) + |x|^2 = 0$$

is zero: $\Delta = 4(x, y)^2 - 4|x|^2 |y|^2 = 0$. Hence the quadratic equation has a real solution $\lambda_0$. It follows that

$$|\lambda_0 y + x|^2 = \lambda_0^2 |y|^2 + 2\lambda_0(x, y) + |x|^2 = 0,$$

and by definiteness of the inner product, $\lambda_0 y + x = 0$, i.e. $x = -\lambda_0 y$. Thus $x$ and $y$ are linearly dependent.

Conversely, if $x$ and $y$ are linearly dependent, say $x = \alpha y$ for some scalar $\alpha$, then

$$(x, y)^2 = (\alpha y, y)^2 = \alpha^2 (y, y)^2 = \alpha^2 |y|^4,$$
$$|x|^2 |y|^2 = |\alpha y|^2 |y|^2 = \alpha^2 |y|^2 |y|^2 = \alpha^2 |y|^4,$$

so equality holds.
