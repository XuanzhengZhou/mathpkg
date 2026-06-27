---
role: proof
locale: en
of_concept: lax-representation-kdv
source_book: gtm060
source_chapter: "Appendix 13"
source_section: "The Korteweg–de Vries equation"
---

The Lax representation for the KdV equation was discovered by Peter Lax in 1968. The key idea is to find two differential operators $L$ and $A$ (depending on $u$) such that the commutator equation $\dot{L} = [A, L]$ is equivalent to the KdV equation.

For the KdV equation, take:
- $L = -\partial_x^2 + u$ (the Schrödinger operator with potential $u(x,t)$)
- $A = 4\partial_x^3 - 3(u\partial_x + \partial_x u)$ (a skew-adjoint third-order operator)

Compute the commutator:
$$[A, L] = AL - LA.$$

Since $L = -\partial_x^2 + u$ (where $u$ acts as multiplication), we have:
$$AL = (4\partial_x^3 - 3u\partial_x - 3\partial_x u)(-\partial_x^2 + u)$$
$$= -4\partial_x^5 + 4\partial_x^3 u + 3u\partial_x^3 + 3\partial_x u \partial_x^2 - 3u\partial_x u - 3(\partial_x u)u.$$

After computing $LA$ similarly and subtracting, all terms involving fifth and fourth derivatives cancel because both $L$ and $A$ are constructed precisely for this purpose. The remaining terms involve $u_{xxx}$ and $uu_x$, reproducing the KdV equation when $\dot{L} = \dot{u}$ (since $L$ depends on $t$ only through $u$):

$$\frac{dL}{dt} = \frac{\partial u}{\partial t} = [A, L] = 6uu_x - u_{xxx}.$$

The Lax equation $\dot{L} = [A, L]$ implies that $L(t)$ evolves by unitary equivalence:
$$L(t) = U(t) L(0) U(t)^{-1},$$
where $U(t)$ solves $\dot{U} = AU$ with $U(0) = I$. Consequently, the spectrum of $L(t)$ is independent of $t$, and the eigenvalues $\lambda$ of the Sturm-Liouville problem $Lf = \lambda f$ (with zero boundary conditions at infinity) are first integrals of the KdV equation.
