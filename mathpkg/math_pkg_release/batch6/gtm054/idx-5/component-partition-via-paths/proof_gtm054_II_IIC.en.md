---
role: proof
locale: en
of_concept: component-partition-via-paths
source_book: gtm054
source_chapter: "II"
source_section: "IIC"
---

**Proof of C20 Proposition.**

Assume $\Lambda_{V_1}, \ldots, \Lambda_{V_k}$ are the components of $\Lambda = (V, f, E)$ and let $F_i = \{e \in E : f(e) \subseteq V_i\}$. Let $s \in V_i$ and $t \in V_j$ with $i \neq j$. Suppose there exists an $st$-path. Then by the definition of a path, there exist alternating vertices and blocks connecting $s$ and $t$. But since blocks of $F_i$ only involve vertices from $V_i$, and blocks of $F_j$ only involve vertices from $V_j$, any path from $V_i$ to $V_j$ would require a block incident with vertices from both $V_i$ and $V_j$, which cannot exist in a direct sum decomposition. Hence $s \not\sim t$.

Conversely, if $s, t \in V_i$ for the same component, then by the connectedness of $\Lambda_{V_i}$, there is a path from $s$ to $t$ entirely within $V_i \cup F_i$. Therefore the equivalence classes of $\sim$ restricted to $V$ are exactly the vertex sets of the components.
