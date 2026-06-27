---
role: proof
locale: en
of_concept: symplectic-structure-on-poisson-leaves
source_book: gtm060
source_chapter: "Appendix 13"
source_section: "B. Poisson Mappings"
---

Define the 2-form $\omega$ on each leaf by $\omega(X_H, X_K) = \{H, K\}$ for Hamiltonian vector fields $X_H, X_K$ with Hamiltonian functions $H, K$ respectively.

First, the value $\{H, K\}(x)$ depends only on the vectors $X_H(x), X_K(x)$, not on the choice of Hamiltonians. If $H'$ is another function with $X_{H'} = X_H$ at $x$, then $X_{H-H'} = 0$ at $x$, so the derivative of every function along $X_{H-H'}$ vanishes, implying $\{H - H', K\}(x) = 0$ and thus $\{H, K\}(x) = \{H', K\}(x)$. The same argument applies to $K$. Hence $\omega$ is well-defined.

Nondegeneracy: Suppose $\omega(v, w) = 0$ for all $w$ tangent to the leaf. Take any function $f$; its Hamiltonian vector field $X_f$ is tangent to the leaf (since leaves are invariant under Hamiltonian flows). Then $\omega(v, X_f) = 0$ means $v(f) = 0$ for all $f$, so $v = 0$.

Closedness: By the Jacobi identity, $d\omega(X_H, X_K, X_L) = \{\{H, K\}, L\} + \{\{K, L\}, H\} + \{\{L, H\}, K\} = 0$ for Hamiltonian vector fields, which span the tangent space at each point of a generic leaf.

Even-dimensionality follows from the fact that a symplectic form on a vector space can only exist in even dimension.
