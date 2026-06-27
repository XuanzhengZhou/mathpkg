---
role: proof
locale: en
of_concept: rotation-squared-equals-reflection-product
source_book: gtm020
source_chapter: "5"
source_section: "9"
---

Clearly, $\alpha(x_1)\alpha(x_2) = \beta(x_1)\beta(x_2)$ since $\alpha(x)y = -\beta(x)y$ and two negatives cancel. Moreover, if $y$ is orthogonal to both $x_1$ and $x_2$, we have $R(x_1, x_2)^2 y = \alpha(x_1)\alpha(x_2)y = \beta(x_1)\beta(x_2)y = y$, since reflections and $180^\circ$ rotations fix the orthogonal complement of their defining vectors.

It suffices to show that $R(x_1, x_2)^2 x_2 = \beta(x_1)\beta(x_2)x_2 = \beta(x_1)x_2$ equals the image of $x_2$ under a rotation of $180^\circ$ about $x_1$. But this is exactly the image of $x_2$ under a rotation about $x_1$ by an angle equal to twice the angle between $x_1$ and $x_2$, which is precisely what $R(x_1, x_2)^2$ does. Hence the three linear transformations coincide on a basis and therefore are equal.
