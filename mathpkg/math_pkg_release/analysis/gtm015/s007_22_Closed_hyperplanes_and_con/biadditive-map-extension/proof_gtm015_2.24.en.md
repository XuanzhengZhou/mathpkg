---
role: proof
locale: en
of_concept: biadditive-map-extension
source_book: gtm015
source_chapter: "2"
source_section: "24"
---

# Proof of Extension of bi-additive maps to completions

Let $A, B, C$ be complete, abelian, separated topological groups, let $A_0$ and $B_0$ be dense subgroups of $A$ and $B$, and suppose $f: A_0 \times B_0 \rightarrow C$ is bi-additive:

$$f(a + a', b) = f(a, b) + f(a', b), \quad f(a, b + b') = f(a, b) + f(a, b')$$

for all $a, a' \in A_0$, $b, b' \in B_0$.

First fix $b \in B_0$ and consider $f(\cdot, b): A_0 \rightarrow C$. This is a uniformly continuous homomorphism (since it is additive), hence by (24.2) it extends uniquely to a continuous homomorphism $\bar{f}(\cdot, b): A \rightarrow C$. Then for each $a \in A$, the map $b \mapsto \bar{f}(a, b)$ is additive on $B_0$ and uniformly continuous, so it extends uniquely to a continuous map on all of $B$. The resulting extension $\bar{f}: A \times B \rightarrow C$ is bi-additive and continuous.
