---
role: proof
locale: en
of_concept: poisson-structure-from-period-mapping
source_book: gtm060
source_chapter: "Appendix 13"
source_section: "F. Period Mappings and Poisson Structures"
---

The nondegenerate period mapping identifies the tangent bundle $TB$ with the cohomology bundle $H^d(F, \mathbb{C})$, and dually the cotangent bundle $T^*B$ with the homology bundle $H_d(F, \mathbb{C})$. The intersection form $I: H_d(F) \times H_d(F) \to \mathbb{C}$ on the middle-dimensional homology is skew-symmetric by hypothesis. Under the dual isomorphism, this defines a bivector field $\pi$ on $B$: for cotangent vectors $\alpha, \beta$ at a point $b \in B$, we set $\pi(\alpha, \beta) = I(\alpha^\sharp, \beta^\sharp)$ where $\alpha^\sharp$ is the corresponding homology class in the fibre over $b$.

The Jacobi identity for $\pi$ follows from the fact that the intersection form is constant in the canonical integer trivialization (i.e., it does not depend on the point $b$). Since the identification respects the integer lattice in homology, the Gauss-Manin connection is flat on the cohomology bundle, and the transported intersection form satisfies the Jacobi identity because it is a constant skew-symmetric bilinear form when expressed in a parallel frame. Thus $\pi$ defines a Poisson structure with constant Poisson brackets in the coordinates provided by the period mapping.
