---
role: proof
locale: en
of_concept: existence-of-gauss-map
source_book: gtm020
source_chapter: "3. Vector Bundles"
source_section: "5"
---

Let $\{U_i\}$ be a countable or finite open covering of $B$ such that $\xi|U_i$ is trivial, let $h_i: U_i \times F^k \to \xi|U_i$ be $U_i$-isomorphisms, and let $\{\eta_i\}$ be a partition of unity with the closure of $\eta_i^{-1}((0,1]) \subset U_i$.

Define $g: E(\xi) \to \sum_i F^k$ as $g = \sum_i g_i$, where $g_i|E(\xi|U_i)$ is given by $(\eta_i p)(p_2 h_i^{-1})$ and $p_2: U_i \times F^k \to F^k$ is the projection. On the fibre over $b$, the map $g_i$ is the composition
$$p^{-1}(b) \xrightarrow{h_i^{-1}} \{b\} \times F^k \xrightarrow{p_2} F^k \xrightarrow{\eta_i(b)} F^k.$$
Thus each $g_i$ is linear on fibres, and the sum $g = \sum_i g_i$ is also linear on fibres. Since for each $b \in B$ there exists some $i$ with $\eta_i(b) > 0$, the map $g$ restricted to the fibre $p^{-1}(b)$ is a monomorphism, hence $g$ is a Gauss map into $\sum_i F^k \cong F^\infty$ (when the cover is countable) or into $F^{kn}$ (when the cover has $n$ sets).
