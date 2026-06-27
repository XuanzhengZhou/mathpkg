---
role: proof
locale: en
of_concept: associated-primes-characterization-via-quotient
source_book: gtm028
source_chapter: "IV"
source_section: "§5. Uniqueness theorems"
---

Given an index $i$, there exists $c \in \bigcap_{j \neq i} \mathfrak{q}_j$, $c \notin \mathfrak{q}_i$, since the representation is irredundant. The ideal $\mathfrak{a} : (c)$ contains $\mathfrak{q}_i$ and is contained in $\mathfrak{p}_i$. If $xy \in \mathfrak{a} : (c)$ and $x \notin \mathfrak{p}_i$, then $xyc \in \mathfrak{a} \subset \mathfrak{q}_i$, whence $yc \in \mathfrak{q}_i$ (since $x \notin \mathfrak{p}_i$), and $yc \in \mathfrak{a}$ since $yc \in (c) \subset \bigcap_{j \neq i} \mathfrak{q}_j$. This shows $y \in \mathfrak{a} : (c)$. By Theorem 13 of III, §9, $\mathfrak{a} : (c)$ is primary for $\mathfrak{p}_i$.

Conversely, if $\mathfrak{a} : (c)$ is primary for a prime $\mathfrak{p}$ with $c \notin \mathfrak{a}$, then writing $\mathfrak{a} : (c) = \bigcap_i (\mathfrak{q}_i : (c))$ and taking radicals gives $\mathfrak{p} = \bigcap_i \sqrt{\mathfrak{q}_i : (c)}$. The radical $\sqrt{\mathfrak{q}_i : (c)}$ is $\mathfrak{p}_i$ if $c \notin \mathfrak{q}_i$, and $R$ otherwise. Hence $\mathfrak{p}$ is an intersection of some $\mathfrak{p}_i$, so by Property B it equals one of them.
