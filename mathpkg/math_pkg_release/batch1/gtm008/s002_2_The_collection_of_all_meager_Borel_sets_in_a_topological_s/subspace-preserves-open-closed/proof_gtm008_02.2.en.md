---
role: proof
locale: en
of_concept: subspace-preserves-open-closed
source_book: gtm008
source_chapter: "Chapter 2: Topological Spaces"
source_section: "2. The Collection of All Meager Borel Sets in a Topological Space"
---

1. If $A$ is open in $T$ then
   $$(\forall a \in A \cap X') (\exists N(a) \in T) [N(a) \subseteq A].$$
   Then $N(a) \cap X' \in T'$ and $a \in N(a) \cap X' \subseteq A \cap X'$. Thus $A \cap X'$ is open in $T'$.

2. If $a \in X'$ and $(\forall N(a) \in T') [N(a) \cap (A \cap X') \neq 0]$, then
   $$(\forall N(a) \in T) [N(a) \cap X' \cap A \neq 0].$$
   Thus $(\forall N(a) \in T) [N(a) \cap A \neq 0]$. Since $A$ is closed, $a \in A$ and hence $a \in A \cap X'$, i.e., $A \cap X'$ is closed in $T'$.

3. If $A$ is both open and closed in $T$, then by (1) and (2) above, $A \cap X'$ is both open and closed in $T'$.
