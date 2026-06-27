---
role: proof
locale: en
of_concept: isomorphism-for-any-index-set
source_book: gtm003
source_chapter: "III"
source_section: "10.5"
---
Suppose that each summable sequence in $E$ is absolutely summable. Assume, for contradiction, that $\{x_\alpha : \alpha \in \mathbf{A}\}$ is a summable family in $E$ which is not absolutely summable. Then $\mathbf{A}$ is necessarily infinite, and there exists $U \in \mathfrak{U}$ such that

$$\sum_\alpha r_U(x_\alpha) = +\infty$$

where $r_U$ denotes the gauge (Minkowski functional) of $U$. Since the terms $r_U(x_\alpha)$ are nonnegative and the sum over the uncountable (or infinite) index set $\mathbf{A}$ is defined as the supremum of sums over finite subsets, the divergence $\sum_\alpha r_U(x_\alpha) = +\infty$ implies that there exists a countably infinite subset $\{\alpha_1, \alpha_2, \dots\} \subseteq \mathbf{A}$ such that

$$\sum_{k=1}^\infty r_U(x_{\alpha_k}) = +\infty.$$

Thus the sequence $(x_{\alpha_k})_{k \in \mathbb{N}}$ is summable in $E$ (since the original family is summable, every subfamily is summable) but not absolutely summable, contradicting the hypothesis. Therefore every summable family over $\mathbf{A}$ must be absolutely summable, which means the canonical imbedding $l^1[\mathbf{A}, E] \to l^1(\mathbf{A}, E)$ is surjective. When the imbedding is a topological isomorphism for $\mathbf{A} = \mathbb{N}$, the same argument applied to the topologies yields the topological isomorphism for arbitrary $\mathbf{A}$.
