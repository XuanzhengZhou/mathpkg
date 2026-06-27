---
role: proof
locale: en
of_concept: nuclear-space-characterization-via-dual-imbeddings
source_book: gtm003
source_chapter: "III"
source_section: "Appendix: Tensor Products and Nuclear Spaces"
---

**Necessity.** Suppose $E$ is nuclear and let $A \subset E'_\sigma$ be closed, convex, circled, and equicontinuous. Then $U = A^\circ$ is a convex, circled $0$-neighborhood in $E$. By the definition of nuclearity (III, 7.2), there exists a convex, circled $0$-neighborhood $V \subset U$ such that the canonical map $\phi_{U,V} : \tilde{E}_V \to \tilde{E}_U$ is nuclear. Set $B = V^\circ$. Then $B$ is closed, convex, circled, and equicontinuous, with $A = U^\circ \subset V^\circ = B$. The canonical imbedding $\psi_{B,A} : E'_A \to E'_B$ is the adjoint of $\phi_{U,V}$, hence is also nuclear.

**Sufficiency.** Let $U$ be a given convex, circled $0$-neighborhood in $E$. By (III, 7.2) it suffices to exhibit a convex, circled $0$-neighborhood $V \subset U$ such that $\phi_{U,V}$ is nuclear. Put $A = U^\circ$, which is a closed, convex, circled, equicontinuous subset of $E'_\sigma$. By hypothesis, there exist closed, convex, circled, equicontinuous subsets $B, C$ of $E'_\sigma$ such that $A \subset B \subset C$ and the canonical maps $\psi_{C,B}$ and $\psi_{B,A}$ are both nuclear. Let $W = B^\circ$ and $V = C^\circ$ (polars with respect to the duality $\langle E, E' \rangle$).

Denote by $F, G, H$ the strong duals of $E'_C, E'_B, E'_A$, respectively. Then $F, G, H$ are the respective strong biduals of $\tilde{E}_V, \tilde{E}_W, \tilde{E}_U$, and the second adjoints of the canonical maps $\tilde{E}_V \to \tilde{E}_W$ and $\tilde{E}_W \to \tilde{E}_U$ are precisely the maps $\psi_{C,B}$ and $\psi_{B,A}$. Since the latter are nuclear, it follows that $\phi_{U,V} : \tilde{E}_V \to \tilde{E}_U$, being the composition of two nuclear maps, is itself nuclear. Hence $E$ is nuclear.

*Note: The source text is truncated at the end of this section; the conclusion of the proof follows from the fact that the composition of the two nuclear canonical maps $\phi_{W,V} : \tilde{E}_V \to \tilde{E}_W$ and $\phi_{U,W} : \tilde{E}_W \to \tilde{E}_U$ (whose second adjoints are the given nuclear maps $\psi_{C,B}$ and $\psi_{B,A}$) yields $\phi_{U,V}$, and nuclearity is preserved under composition.*
