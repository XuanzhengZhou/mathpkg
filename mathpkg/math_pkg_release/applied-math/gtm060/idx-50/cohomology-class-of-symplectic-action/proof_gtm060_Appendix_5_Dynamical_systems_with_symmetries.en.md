---
role: proof
locale: en
of_concept: cohomology-class-of-symplectic-action
source_book: gtm060
source_chapter: "Appendix 5"
source_section: "Dynamical systems with symmetries"
---

From the Poisson action, we construct a linear mapping $a \mapsto H_a$ from the Lie algebra $\mathfrak{g}$ to Hamiltonian functions (choosing constants on a basis and extending linearly). The commutator relation gives $H_{[a,b]} = (H_a, H_b) + C(a,b)$ for a bilinear skew-symmetric function $C$.

The Jacobi identity in the Lie algebra, applied to the associativity of the Poisson bracket and the definition of $C$, yields:

$$C([a,b], c) + C([b,c], a) + C([c,a], b) = 0$$

which is precisely the $2$-cocycle condition. Thus $C$ is a $2$-cocycle of the Lie algebra $\mathfrak{g}$.

If we choose different additive constants for the Hamiltonian functions, each $H_a$ changes to $H'_a = H_a + \rho(a)$ for some linear functional $\rho$ on $\mathfrak{g}$. Then the new cocycle is:

$$C'(a,b) = H'_{[a,b]} - (H'_a, H'_b) = H_{[a,b]} + \rho([a,b]) - (H_a + \rho(a), H_b + \rho(b))$$
$$= H_{[a,b]} + \rho([a,b]) - (H_a, H_b) = C(a,b) + \rho([a,b])$$

since constants Poisson-commute with all functions. Thus $C'$ and $C$ are cohomologous. Therefore, the cohomology class $[C] \in H^2(\mathfrak{g}; \mathbb{R})$ is well-defined and is an invariant of the Poisson action.

This cohomology class vanishes precisely when there exists a choice of constants making $C \equiv 0$, i.e., when the linear map $a \mapsto H_a$ is a Lie algebra homomorphism. In that case, the action admits a moment map.
