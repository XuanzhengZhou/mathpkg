---
role: proof
locale: en
of_concept: canonical-imbedding-tensor-l1-a-e
source_book: gtm003
source_chapter: "III"
source_section: "10.6"
---
The last assertion is almost immediate from the definition of the semi-norms $p_U$ and $q_U$, and the first assertion is a special case of (III, 6.5). Hence let us identify $l^1(\mathbf{A}) \otimes E$ algebraically with its canonical image in $l^1[\mathbf{A}, E]$ and show that the induced topology is the topology of bi-equicontinuous convergence.

By the corollary of (10.3), the dual of the Banach space $l^1(\mathbf{A})$ is the space of bounded scalar families. If $B$ is the unit ball of $l^1(\mathbf{A})$, its polar $B^\circ$ (under the weak topology) can be identified with the compact space $Z^\mathbf{A}$, where $Z = \{\lambda : |\lambda| \leq 1\}$ is the unit disk in $\mathbb{K}$.

Let $\sum_i \xi_i \otimes x_i$ be any element of $l^1(\mathbf{A}) \otimes E$ and let $U \in \mathfrak{U}$. By definition of $q_U$ we have
$$q_U\!\left(\sum_i \xi_i \otimes x_i\right) = \sup_{x' \in U^\circ} \sum_\alpha \left|\sum_i \xi_\alpha^{(i)} \langle x_i, x' \rangle\right|.$$

For each $\alpha \in \mathbf{A}$, the map $x' \mapsto \sum_i \xi_\alpha^{(i)} \langle x_i, x' \rangle$ is a continuous linear functional on $E'_{U^\circ}$. Since $U^\circ$ is equicontinuous and hence relatively compact in the weak dual topology, the definition of the bi-equicontinuous convergence topology on $l^1(\mathbf{A}) \otimes E$ is given precisely by semi-norms of the form
$$\sup\left\{\sum_\alpha \left|\sum_i \xi_\alpha^{(i)} \langle x_i, x'_\alpha \rangle\right| : \{x'_\alpha\} \in M\right\}$$
where $M$ runs through the equicontinuous subsets of the dual of $l^1(\mathbf{A}) \otimes E$. The identification of $B^\circ$ with $Z^\mathbf{A}$ and the fact that the $\xi_\alpha^{(i)}$ are summable in $\alpha$ yield that these semi-norms coincide with the $q_U$ semi-norms restricted to the algebraic tensor product, establishing the topological isomorphism.
