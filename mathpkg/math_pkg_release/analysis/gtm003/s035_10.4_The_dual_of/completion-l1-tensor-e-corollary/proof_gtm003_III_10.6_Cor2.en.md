---
role: proof
locale: en
of_concept: completion-l1-tensor-e-corollary
source_book: gtm003
source_chapter: "III"
source_section: "10.6"
---
The statement follows directly from Theorem 10.6 by passing to completions. By Theorem 10.6, the algebraic tensor product $l^1(\mathbf{A}) \otimes E$ is dense in both $l^1(\mathbf{A}, E)$ and $l^1[\mathbf{A}, E]$, and the induced topologies correspond respectively to the projective topology and the topology of bi-equicontinuous convergence.

Since $E$ is dense in its completion $\tilde{E}$, the space $l^1(\mathbf{A}) \otimes E$ is also dense in $l^1(\mathbf{A}) \otimes \tilde{E}$ under both topologies. Taking completions, the projective completion $l^1(\mathbf{A}) \mathbin{\tilde{\otimes}}_\pi E$ identifies with the completion of $l^1(\mathbf{A}, E)$, which is $l^1(\mathbf{A}, \tilde{E})$. Similarly, the bi-equicontinuous completion identifies with $l^1[\mathbf{A}, \tilde{E}]$.

The canonical map from the projective tensor product to the bi-equicontinuous tensor product extends continuously to a map between their completions, and under the above identifications this extension is precisely the canonical imbedding $l^1[\mathbf{A}, \tilde{E}] \hookrightarrow l^1(\mathbf{A}, \tilde{E})$. This map is injective because the algebraic tensor product is dense in both spaces and the identity map on the dense subspace extends uniquely.
