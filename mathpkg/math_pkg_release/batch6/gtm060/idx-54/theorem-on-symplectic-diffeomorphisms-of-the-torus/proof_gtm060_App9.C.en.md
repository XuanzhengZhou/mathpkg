---
role: proof
locale: en
of_concept: theorem-on-symplectic-diffeomorphisms-of-the-torus
source_book: gtm060
source_chapter: "Appendix 9"
source_section: "C"
---

The proof is based on consideration of the function on the torus given by the formula

$$\Phi(x, y) = \frac{1}{2} \int (X - x)(dY + dy) - (Y - y)(dX + dx).$$

The function $\Phi$ is well-defined on the torus because the center-of-gravity condition ensures the integral over any closed loop vanishes (the symplectic structure and the fixed center of gravity guarantee that $\Phi$ is single-valued).

At a fixed point of the diffeomorphism, $X = x$ and $Y = y$, so the integrand vanishes and $\Phi$ has a critical point. Conversely, under the eigenvalue assumption (no eigenvalue equals $-1$), every critical point of $\Phi$ is a fixed point of the mapping.

A smooth function on the torus has at least four critical points, counting multiplicity, of which at least three are geometrically different (this follows from Morse theory or Lusternik-Schnirelman category arguments for the torus $\mathbb{T}^2$). Therefore the diffeomorphism has at least four fixed points (counting multiplicity), with at least three geometrically distinct ones.

The restriction on eigenvalues (not equal to $-1$) is needed to ensure the non-degeneracy of the correspondence between critical points of $\Phi$ and fixed points. Attempts at proving the theorem without this restriction encounter difficulties similar to those in Poincaré's original annulus theorem.
