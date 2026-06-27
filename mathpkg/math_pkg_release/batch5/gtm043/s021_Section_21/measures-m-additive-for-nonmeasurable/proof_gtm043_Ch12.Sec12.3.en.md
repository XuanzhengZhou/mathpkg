---
role: proof
locale: en
of_concept: measures-m-additive-for-nonmeasurable
source_book: gtm043
source_chapter: "12"
source_section: "12.3"
---
If $\mu$ is not $\mathfrak{m}$-additive, there exists a family $(A_s)_{s \in S}$ of $\mathfrak{m}$ disjoint sets of measure $0$ whose union has measure $1$. Define a set-function $\lambda$ on the index set $S$ by:
$$\lambda(E) = \mu\left(\bigcup_{s \in E} A_s\right) \quad (E \subset S).$$
Then $\lambda$ is a countably additive $\{0,1\}$-valued measure on $S$ with $|S| = \mathfrak{m}$, $\lambda(S) = 1$, and $\lambda(\{s\}) = \mu(A_s) = 0$ for each $s \in S$. Thus $\lambda$ is nontrivial, so $\mathfrak{m}$ is measurable. By contraposition, if $\mathfrak{m}$ is nonmeasurable, $\mu$ must be $\mathfrak{m}$-additive.