---
role: proof
locale: en
of_concept: triangle-equality-condition
source_book: gtm023
source_chapter: "7"
source_section: "7.6"
---

Assume $|x + y| = |x| + |y|$. Squaring both sides:

$$|x + y|^2 = (|x| + |y|)^2,$$
$$|x|^2 + 2(x, y) + |y|^2 = |x|^2 + 2|x| |y| + |y|^2,$$

which simplifies to $(x, y) = |x| |y|$. This means equality holds in the Schwarz inequality, so $x$ and $y$ are linearly dependent: $x = \lambda y$ for some scalar $\lambda$.

Substituting back: $(x, y) = (\lambda y, y) = \lambda |y|^2$ and $|x| |y| = |\lambda| |y|^2$. The equality $(x, y) = |x| |y|$ becomes $\lambda |y|^2 = |\lambda| |y|^2$, hence $\lambda = |\lambda|$, which implies $\lambda > 0$.

Conversely, if $x = \lambda y$ with $\lambda > 0$, then

$$|x + y| = |\lambda y + y| = (\lambda + 1)|y| = \lambda|y| + |y| = |x| + |y|.$$
