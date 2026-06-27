---
role: proof
locale: en
of_concept: existence-and-uniqueness-of-orthogonal-projection
source_book: gtm023
source_chapter: "VIII"
source_section: "8.11"
---

It is clear that $\pi$ is uniquely determined by $E_1$, since any vector $x$ decomposes uniquely as $x = y + z$ with $y \in E_1$ and $z \in E_1^\perp$. Define $\pi x = y$. Then $\pi^2 x = \pi y = y = \pi x$, so $\pi^2 = \pi$. Moreover, for any $x = y + z$ and $x' = y' + z'$ with $y, y' \in E_1$ and $z, z' \in E_1^\perp$:
$$(\pi x, x') = (y, y' + z') = (y, y') = (y + z, y') = (x, \pi x'),$$
so $\tilde{\pi} = \pi$. Thus $\pi$ is an orthogonal projection with $\operatorname{Im} \pi = E_1$.
