---
role: proof
locale: en
of_concept: halls-marriage-theorem
source_book: gtm054
source_chapter: "D"
source_section: "25"
---

The Philip Hall Theorem is readily seen to be equivalent to Corollary A6. Let $\Gamma = \{V, F\}$, $\mathcal{E}$ be the bipartite graph of $\Lambda$. If $F \subseteq E$, then $N(F) = \bigcup_{e \in F} f(e)$, and the equivalence is immediate.

Philip Hall's theorem is strictly a statement of existence. It indicates neither how an SDR can be found nor, when an SDR does exist, how many distinct SDR's $\Lambda$ may have. The enumerative problem is considered below in \S F. When an SDR exists, it can be found in the following way: since an SDR $\lambda: E \to V$ of $\Lambda$ exists if and only if the set of edges $\{\{e, \lambda(e)\}: e \in E\}$ is a matching of $E$ in $\Gamma$, the algorithm for constructing a largest matching in $\Gamma$ can thus be employed to find a "longest" SDR for $\Lambda$.
