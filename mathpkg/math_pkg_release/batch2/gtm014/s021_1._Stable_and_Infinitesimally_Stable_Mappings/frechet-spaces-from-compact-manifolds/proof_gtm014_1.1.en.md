---
role: proof
locale: en
of_concept: frechet-spaces-from-compact-manifolds
source_book: gtm014
source_chapter: "III"
source_section: "§1. Stable and Infinitesimally Stable Mappings"
---

**Proof.** (a) Cover $X$ by a finite number of open sets $U_\alpha$ where $\overline{U}_\alpha$ is contained in a coordinate patch. This is possible since $X$ is compact. Let $g: X \to \mathbf{R}$ be smooth. For each multi-index $\alpha$ and each $k$, define the $C^k$ seminorm
$$
|g|_{k, U_\alpha} = \sup_{x \in U_\alpha} \sum_{|\beta| \leq k} |D^\beta g(x)|.
$$
The countable family of seminorms $\{| \cdot |_{k, U_\alpha}\}$ induces the Whitney $C^\infty$ topology, making $C^\infty(X, \mathbf{R})$ into a Fr\'{e}chet space.

(b) Using a partition of unity and local trivializations of $E$, the space $C^\infty(E)$ of smooth sections inherits a Fr\'{e}chet space structure from the coordinate patches.

(c) Given $f: X \to Y$ smooth, the pullback bundle $f^* TY$ is a vector bundle over the compact manifold $X$. A vector field along $f$ is precisely a section of $f^* TY$, so by part (b) the space $C_f^\infty(X, TY)$ is a Fr\'{e}chet space.
