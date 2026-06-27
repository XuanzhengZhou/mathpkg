---
role: proof
locale: en
of_concept: poisson-structure-across-discriminant
source_book: gtm060
source_chapter: "Appendix 13"
source_section: "F. Period Mappings and Poisson Structures"
---

The proof uses the Picard-Lefschetz theory of the period mapping. On the complement of the discriminant, the fibration is locally trivial and the period mapping $P(\lambda) = \int_{\gamma} y \, dx$ (where $\gamma$ is a cycle in the fibre) defines a nondegenerate map from the base to the cohomology of the Milnor fibre. The intersection form $I$ on $H_1(F, \mathbb{Z})$ is skew-symmetric (since $\dim F = 2$) and equips the base with a Poisson structure via the dual isomorphism $T^*B \cong H_1(F)$.

Near the discriminant, the periods have at worst logarithmic singularities (by the regularity of the Gauss-Manin connection). The Poisson bracket expressed in terms of periods extends analytically because the singular terms cancel in the skew-symmetric pairing. More precisely, writing the Poisson bivector in canonical coordinates $(\lambda_1, \lambda_2, \lambda_3)$, the components are expressed as rational functions of the periods, and the Picard-Lefschetz formulas show that these rational functions have removable singularities along the discriminant. The result is a holomorphic Poisson structure on the entire base space, invariant under diffeomorphisms preserving the discriminant.

In the $A_3$ example $y^2 = x^4 + \lambda_1 x^2 + \lambda_2 x + \lambda_3$, explicit computation shows the Poisson brackets are $\{\lambda_1, \lambda_3\} = 1$, $\{\lambda_1, \lambda_2\} = \{\lambda_2, \lambda_3\} = 0$, so the symplectic leaves are $\lambda_2 = \text{const}$ with symplectic form $d\lambda_1 \wedge d\lambda_3$.
