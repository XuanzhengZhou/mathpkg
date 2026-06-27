---
role: proof
locale: en
of_concept: restriction-and-contraction-are-matroids
source_book: gtm054
source_chapter: "X"
source_section: "D"
---

The proof follows from the definition of matroid via the circuit axioms. Since $\Lambda = (V, \mathcal{M})$ is a matroid, the system $\mathcal{M}$ satisfies the circuit axioms. The set systems $\Lambda_U$ and $\Lambda_{[U]}$ are defined using the projection $\pi_U: \mathcal{P}(V) \to \mathcal{P}(U)$ with $\pi_U(S) = U \cap S$.

For $\Lambda_U$, the circuits are $\mathcal{M}(\pi_U[\mathcal{E}])$ where $\mathcal{E}$ is the circuit family of $\Lambda$ (which is $\mathcal{M}$ itself). The minimal nonempty members of $\pi_U[\mathcal{M}]$ can be verified to satisfy the circuit axioms, establishing that $\Lambda_U$ is a matroid.

For $\Lambda_{[U]}$, the system $\Lambda_{[U]} = (U, \mathcal{M}(\pi_U[\mathcal{M}]))$ also produces circuits via the projection, and one verifies that the circuit axioms (mutual non-containment and the circuit elimination axiom) are preserved under this operation. Consequently both $\Lambda_U$ and $\Lambda_{[U]}$ are matroids.
