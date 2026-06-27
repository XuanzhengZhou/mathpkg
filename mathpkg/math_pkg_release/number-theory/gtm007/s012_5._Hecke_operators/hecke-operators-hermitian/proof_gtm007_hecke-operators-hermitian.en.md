---
role: proof
locale: en
of_concept: hecke-operators-hermitian
source_book: gtm007
source_chapter: "VII"
source_section: "5.6"
---
The invariance of the measure $\mu(f,g) = f(z)\overline{g(z)} y^{2k} dxdy/y^2$ under the modular group follows from the modular transformation properties of $f$ and $g$: under $z \mapsto (az+b)/(cz+d)$, we have $f(z) \mapsto (cz+d)^{2k}f(z)$, and $y \mapsto y/|cz+d|^2$, so $f(z)\overline{g(z)} y^{2k}$ transforms by $|cz+d|^{4k}/|cz+d|^{4k} = 1$. The measure $dxdy/y^2$ is also invariant. The integral over $H/G$ is well-defined because the measure is bounded on the fundamental domain $D$.

One can verify that $\langle T(n)f, g \rangle = \langle f, T(n)g \rangle$ by a direct computation using the explicit formula for $T(n)$ and a change of variables in the integral over $D$. With this Hermitian property and the commutativity of the $T(n)$, a standard theorem of linear algebra (commuting family of Hermitian operators on a finite-dimensional inner product space) implies the existence of an orthogonal basis of simultaneous eigenfunctions. The integrality of the characteristic polynomial of $T(n)$ on $M_k(\mathbf{Z})$ (Proposition 12) shows eigenvalues are algebraic integers; total reality follows from the Hermitian property.
