---
role: proof
locale: en
of_concept: open-set-decomposition-into-intervals
source_book: gtm055
source_chapter: "3"
source_section: "General topology"
---

Since $U$ is open, every nonopen interval contained in $U$ is contained in an open interval contained in $U$. It follows that the connected components of $U$ are all open intervals. That no disjoint collection of nonempty open intervals can be uncountable follows from the fact that $\mathbb{R}$ satisfies the second axiom of countability (each such interval contains a distinct rational number). To complete the proof it suffices to observe that if $\{I_n\}$ is a disjoint (countable) collection of nonempty open intervals such that $U = \bigcup_n I_n$, and if $V$ is a connected component of $U$ that meets some one $I_n$, then neither endpoint of $I_n$ can belong to $V$, and therefore $V = I_n$ (by Proposition 3.6).
