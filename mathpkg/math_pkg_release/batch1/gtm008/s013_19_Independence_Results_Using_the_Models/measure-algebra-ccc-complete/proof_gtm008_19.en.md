---
role: proof
locale: en
of_concept: measure-algebra-ccc-complete
source_book: gtm008
source_chapter: "19"
source_section: "19"
---

Let $S \subseteq B$ be a set of mutually disjoint elements. We must show $\overline{S} \leq \omega$. Assume $0 \notin S$. For each $n \in \omega$, let $S_n = \{b \in S \mid m(b) \geq 1/n\}$. Since $m(1) = 1$ and elements of $S$ are mutually disjoint, each $S_n$ is finite (otherwise the sum of measures would exceed 1). Hence $S = \bigcup_{n \in \omega} S_n$ is countable.

Since $B$ satisfies the c.c.c., every set of pairwise disjoint elements is at most countable. A $\sigma$-algebra with the c.c.c. is complete: given any set $A \subseteq B$, by the c.c.c. the set of all possible disjoint refinements is bounded, so $\sum A$ exists as a countable supremum.
