---
role: proof
locale: en
of_concept: fixed-point-free-disconnected-structure
source_book: gtm054
source_chapter: "II"
source_section: "E"
---

Let $\Lambda = \bigoplus_{i=1}^{k} \Lambda_i$, where $\Lambda_i = (V_i, f_i, E_i)$ for $i = 1, \ldots, k$ are the components of $\Lambda$, and $V_i \neq \varnothing$ for at least two components (since $\Lambda$ is not connected). By hypothesis, $\Lambda$ is fixed-point free, so $G_0(\Lambda) \neq \{1_V\}$ and every non-identity element of $G_0(\Lambda)$ is a derangement.

Suppose there exist at least three components with nonempty vertex sets, say $\Lambda_1, \Lambda_2, \Lambda_3$ with $V_1, V_2, V_3 \neq \varnothing$. Then one can construct a non-identity automorphism $(p, q) \in G(\Lambda)$ that fixes some $x \in V_3$ while $q \neq 1_V$, contradicting the fixed-point free hypothesis. The construction uses the fact that components can be permuted and the restrictions give system-isomorphisms (by Proposition E9).

Therefore at most two components have nonempty vertex sets. Moreover, if $\Lambda_1$ were not asymmetric, there would exist a non-identity $q \in G_0(\Lambda_1)$ fixing some vertex, which would extend to an automorphism of $\Lambda$ fixing that same vertex, again contradicting fixed-point free. Hence $\Lambda_1$ and $\Lambda_2$ are asymmetric.
