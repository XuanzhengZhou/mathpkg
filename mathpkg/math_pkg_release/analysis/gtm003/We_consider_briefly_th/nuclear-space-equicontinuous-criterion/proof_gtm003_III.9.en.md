---
role: proof
locale: en
of_concept: nuclear-space-equicontinuous-criterion
source_book: gtm003
source_chapter: "III"
source_section: "9. Tensor Products and Nuclear Spaces"
---

**Necessity.** Assume $E$ is nuclear and let $A \subset E'_{\sigma}$ be closed, convex, circled, and equicontinuous. Then $U = A^{\circ}$ is a convex, circled $0$-neighborhood in $E$. Since $E$ is nuclear, there exists by (III, 7.2) a convex, circled $0$-neighborhood $V \subset U$ such that the canonical map $\phi_{U,V} : \tilde{E}_V \to \tilde{E}_U$ is nuclear. Set $B = V^{\circ}$. Then $A \subset B$ (since $V \subset U$ implies $U^{\circ} \subset V^{\circ}$), and the map $\psi_{B,A} : E'_A \to E'_B$ is the adjoint of $\phi_{U,V}$, hence also nuclear.

**Sufficiency.** Let $U$ be a given convex, circled $0$-neighborhood in $E$. Put $A = U^{\circ}$, a closed, convex, circled, equicontinuous subset of $E'_{\sigma}$. By hypothesis, there exist closed, convex, circled, equicontinuous subsets $B, C$ of $E'_{\sigma}$ with $A \subset B \subset C$ such that the canonical maps $\psi_{C,B}$ and $\psi_{B,A}$ are both nuclear. Define $W = B^{\circ}$, $V = C^{\circ}$ (polars with respect to $\langle E, E' \rangle$). Let $F, G, H$ be the strong duals of $E'_C, E'_B, E'_A$ respectively. Then $F, G, H$ are the respective strong biduals of $\tilde{E}_V, \tilde{E}_W, \tilde{E}_U$, and the second adjoints
$$\psi_{C,B}'' : H \to G, \qquad \psi_{B,A}'' : G \to F$$
are nuclear. Consequently the composition $\psi_{B,A}'' \circ \psi_{C,B}''$ is nuclear. The canonical map $\phi_{U,V} : \tilde{E}_V \to \tilde{E}_U$ factors through these maps, hence is nuclear. By (III, 7.2), $E$ is nuclear.
