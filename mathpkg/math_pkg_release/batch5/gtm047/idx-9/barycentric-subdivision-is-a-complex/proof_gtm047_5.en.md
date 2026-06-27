---
role: proof
locale: en
of_concept: barycentric-subdivision-is-a-complex
source_book: gtm047
source_chapter: "5"
source_section: "5"
---

The proof proceeds by induction on the dimension of the skeleton. $bK^0 = K^0$ is trivially a complex (a set of vertices). Assuming $bK^i$ is a complex, $bK^{i+1}$ is formed by adjoining, for each $(i+1)$-simplex $\sigma^{i+1} \in K$, the join of its barycenter $v$ with each $i$-simplex $\sigma^i \in bK^i$ that is contained in $\sigma^{i+1}$. Since the join of a point with a simplex yields a simplex, and the new simplices intersect properly (they meet only in common faces within $bK^i$), the result $bK^{i+1}$ is again a simplicial complex. The process terminates because $K$ has bounded dimension.
