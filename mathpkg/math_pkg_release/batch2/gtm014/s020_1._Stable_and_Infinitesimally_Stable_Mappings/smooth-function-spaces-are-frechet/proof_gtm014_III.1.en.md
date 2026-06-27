---
role: proof
locale: en
of_concept: smooth-function-spaces-are-frechet
source_book: gtm014
source_chapter: "III"
source_section: "§1. Stable and Infinitesimally Stable Mappings"
---

We sketch the proof of part (a). Cover $X$ by a finite number of open sets $U_\alpha$ whose closures $\overline{U}_\alpha$ are contained in coordinate patches. This is possible since $X$ is compact.

Let $g: X \to \mathbf{R}$ be smooth. For each non-negative integer $k$, define the $C^k$-norm on the coordinate patch $U_\alpha$ by

$$|g|_{k, U_\alpha} = \sup_{x \in U_\alpha} \sum_{|I| \leq k} |D^I g(x)|,$$

where the sum runs over all multi-indices $I$ of order at most $k$ in the local coordinates. The Frechet "norm" on $C^\infty(X, \mathbf{R})$ is then defined using a suitable combination of these seminorms over all $k$ and all coordinate patches. Completeness follows from the fact that a Cauchy sequence in all $C^k$ seminorms converges uniformly in all derivatives to a smooth limit function.

For part (b), the same construction works locally using trivializations of the vector bundle $E$. For part (c), $C_f^\infty(X, TY)$ is identified with smooth sections of the pullback bundle $f^* TY$ over $X$, reducing to case (b).
