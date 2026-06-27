---
role: proof
locale: en
of_concept: unitary-equivalence-of-lax-operators
source_book: gtm060
source_chapter: "Appendix 13"
source_section: "The Korteweg–de Vries equation"
---

From Lax's theorem, the KdV equation is equivalent to $\dot{L} = [A, L]$. Define the one-parameter family of unitary operators $U(t)$ as the solution of
$$\frac{dU}{dt} = A U, \quad U(0) = I.$$
Since $A$ is skew-adjoint, $U(t)$ is unitary for all $t$ (with appropriate domain considerations). Then:
$$\frac{d}{dt}(U^{-1} L U) = -U^{-1}AU \cdot U^{-1}LU + U^{-1}[A,L]U + U^{-1}L \cdot AU$$
$$= U^{-1}(-AL + [A,L] + LA)U = U^{-1}(-AL + AL - LA + LA)U = 0.$$
Thus $U(t)^{-1} L(t) U(t) = L(0)$ is constant, so $L(t) = U(t) L(0) U(t)^{-1}$.

Since unitary equivalence preserves the spectrum, for any eigenvalue $\lambda(0)$ of $L(0)$ with eigenfunction $f(0)$, the function $f(t) = U(t) f(0)$ satisfies $L(t) f(t) = \lambda(0) f(t)$. Hence $\lambda$ is constant in time — a first integral of the KdV equation.

In the context of the Sturm-Liouville problem $Lf = \lambda f$ on the line with zero boundary conditions at infinity, this means that the discrete eigenvalues (bound states) and the continuous spectral data are all invariants of the KdV flow. This spectral invariance is the basis of the inverse scattering transform method for solving the KdV equation.
