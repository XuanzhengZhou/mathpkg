---
role: proof
locale: en
of_concept: local-decomposition-poisson-manifold
source_book: gtm060
source_chapter: "Appendix 13"
source_section: "B. Poisson Mappings"
---

The proof proceeds via the local structure theory of Poisson manifolds. At a generic point where the rank of the Poisson bivector is locally constant (equal to $2r$), the symplectic leaf has dimension $2r$. The Darboux-Weinstein theorem on Poisson manifolds guarantees the existence of local coordinates $(p_1, \ldots, p_r, q_1, \ldots, q_r, c_1, \ldots, c_{n-2r})$ such that the Poisson bracket takes the canonical form

$$\{p_i, q_j\} = \delta_{ij}, \quad \{p_i, p_j\} = \{q_i, q_j\} = 0, \quad \{c_k, \cdot\} = 0.$$

The functions $c_k$ are Casimir functions — they lie in the center of the Poisson algebra. The coordinates $(p_i, q_i)$ parametrize the symplectic leaf through the given point, while the $c_k$ parametrize the transverse direction. The fact that $\{c_k, c_l\} = 0$ means the transverse space carries the trivial Poisson structure. Near a nongeneric point where the rank drops, the same local product structure holds with respect to the (lower-dimensional) symplectic leaf through that point, as shown by Weinstein's splitting theorem.
