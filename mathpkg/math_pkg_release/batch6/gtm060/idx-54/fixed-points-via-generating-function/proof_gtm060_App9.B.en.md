---
role: proof
locale: en
of_concept: fixed-points-via-generating-function
source_book: gtm060
source_chapter: "Appendix 9"
source_section: "B"
---

The generating function $Xy + S(X, y)$ satisfies

$$dS = (x - X)dy + (Y - y)dX.$$

At a fixed point, $X = x$ and $Y = y$, which implies $dS = 0$ along the annulus, so the fixed points are exactly the critical points of $F(x,y) = S(X(x,y), y)$ provided $\partial X/\partial x \neq 0$.

For the boundary behavior: on the inner boundary $x = a$, the twist condition $g(a, y) < 0$ implies the angular displacement is negative, so the gradient of $F$ points inward; on the outer boundary $x = b$, the condition $g(b, y) > 0$ implies the angular displacement is positive, so the gradient points outward (or vice versa depending on orientation). In either case, the gradient points consistently inward (or outward) on both components, and any smooth function with such boundary behavior on an annulus must have at least two critical points (a maximum and a minimum, or by Morse theory for functions with boundary conditions).

The restriction $\partial X/\partial x \neq 0$ can be relaxed: a refinement of the argument (with a different choice of generating function) shows it suffices that the eigenvalues of the Jacobi matrix $\frac{D(X,Y)}{D(x,y)}$ never be equal to $-1$ at any point, i.e., the mapping never flips the tangent space.
