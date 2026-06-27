---
role: proof
locale: en
of_concept: direct-sum-characterization-via-projections
source_book: gtm003
source_chapter: "I"
source_section: "2"
---

**Proof.** Consider the canonical bijective linear map $\psi : \prod_{i=1}^n M_i \to L$ defined by $\psi(x_1, \ldots, x_n) = \sum_{i=1}^n x_i$. Its inverse is $\psi^{-1} : x \mapsto (u_1 x, \ldots, u_n x)$, where $u_i : L \to M_i$ are the algebraic projections associated with the direct sum decomposition. By definition of the product topology, a map into a product is continuous if and only if each of its component maps is continuous. Therefore $\psi^{-1}$ is continuous exactly when every $u_i$ is continuous.

Since the inclusion maps $M_i \hookrightarrow L$ are continuous (each $M_i$ carries the subspace topology) and addition in $L$ is continuous by $(LT)_1$, the map $\psi$ is always continuous. Consequently, $\psi$ is a homeomorphism (equivalently, a topological isomorphism) if and only if $\psi^{-1}$ is continuous, which happens precisely when all projections $u_i$ are continuous. $\square$

**Remark.** The identity map $e = u_1 + u_2 + \cdots + u_n$ is continuous on $L$. Therefore, if $n-1$ of the projections are known to be continuous, the remaining one, being the difference $e - \sum_{j \neq i} u_j$, is automatically continuous.
