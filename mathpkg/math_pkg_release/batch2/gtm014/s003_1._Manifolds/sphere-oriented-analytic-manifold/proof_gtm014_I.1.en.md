---
role: proof
locale: en
of_concept: sphere-oriented-analytic-manifold
source_book: gtm014
source_chapter: "I. Preliminaries on Manifolds"
source_section: "§1. Manifolds"
---

Let $S^{n-1} \subset \mathbf{R}^n$ be the unit sphere, with north pole $N = (1,0,\ldots,0)$ and south pole $S = (-1,0,\ldots,0)$. The stereographic projections are
\[
\phi_N(x_1,\ldots,x_n) = \frac{1}{1-x_1}(x_2,\ldots,x_n), \qquad
\phi_S(x_1,\ldots,x_n) = \frac{1}{1+x_1}(x_2,\ldots,x_n).
\]
Both $\phi_N$ and $\phi_S$ are homeomorphisms from their domains onto $\mathbf{R}^{n-1}$ with real analytic inverses, hence the two charts $\{\phi_N, \phi_S\}$ form an analytic atlas for $S^{n-1}$.

To compute the transition map, note that $\phi_N^{-1}(y)$ for $y = (y_1,\ldots,y_{n-1}) \in \mathbf{R}^{n-1}$ reconstructs the point on the sphere by the standard inverse stereographic formula. A direct computation then yields
\[
\phi_S \circ \phi_N^{-1}(y) = \frac{y}{|y|^2}, \quad y \in \mathbf{R}^{n-1} \setminus \{0\}.
\]
Since $(\phi_S \circ \phi_N^{-1}) \circ (\phi_S \circ \phi_N^{-1}) = \mathrm{id}_{\mathbf{R}^{n-1}\setminus\{0\}}$, applying the chain rule gives
\[
\bigl(d(\phi_S \circ \phi_N^{-1})\bigr)_{\phi_S \circ \phi_N^{-1}(y)} \cdot \bigl(d(\phi_S \circ \phi_N^{-1})\bigr)_y = I_{n-1},
\]
so $\det\bigl(d(\phi_S \circ \phi_N^{-1})\bigr)_y = \pm 1$ for all $y \neq 0$. Evaluating at $y = (1,0,\ldots,0)$, a direct computation of the Jacobian of $y \mapsto y/|y|^2$ at this point gives $\det = -1$.

To make the atlas oriented, modify the last coordinate of $\phi_N$: define $\widetilde{\phi}_N(x_1,\ldots,x_n) = \frac{1}{1-x_1}(x_2,\ldots,-x_n)$. Then the transition map $\phi_S \circ \widetilde{\phi}_N^{-1}$ has Jacobian determinant $+1$, so $S^{n-1}$ admits the structure of an oriented analytic manifold.
