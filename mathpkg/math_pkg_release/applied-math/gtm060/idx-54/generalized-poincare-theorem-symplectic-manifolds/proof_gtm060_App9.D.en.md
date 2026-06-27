---
role: proof
locale: en
of_concept: generalized-poincare-theorem-symplectic-manifolds
source_book: gtm060
source_chapter: "Appendix 9"
source_section: "D"
---

The proof proceeds by analyzing the intersection of Lagrangian submanifolds. Consider the graph of the symplectic diffeomorphism $g$ as a Lagrangian submanifold in the product symplectic manifold $(M \times M, \Omega \oplus (-\Omega))$. The fixed points of $g$ correspond to intersection points of the graph with the diagonal $\Delta = \{(x, x) : x \in M\}$, which is also Lagrangian.

Since $g$ is homologous to the identity, the graph is Hamiltonian isotopic to the diagonal. The number of intersection points of two Lagrangian submanifolds related by a Hamiltonian isotopy is bounded below by the minimal number of critical points of a Morse function on $M$ (by Floer homology or, in the perturbative regime, by finite-dimensional reduction using generating functions).

For the two-dimensional torus, a more explicit construction is available. The generating function $\Phi$ on the torus, defined by

$$\Phi(x,y) = \frac{1}{2} \int (X - x)(dY + dy) - (Y - y)(dX + dx),$$

has the property that its critical points correspond to fixed points (provided no eigenvalue is $-1$). By Morse theory, any smooth function on $\mathbb{T}^2$ has at least 4 critical points (counting multiplicity). For $\mathbb{R}^{2n} \times \mathbb{T}^{2n}$ phase spaces, a similar argument using generating functions $Xy + S(X, y)$ and the function $F(y) = S(X(f(y), y), y)$ yields the conclusion, with the lower bound $2^n$ coming from the Morse theory of the $n$-torus.
