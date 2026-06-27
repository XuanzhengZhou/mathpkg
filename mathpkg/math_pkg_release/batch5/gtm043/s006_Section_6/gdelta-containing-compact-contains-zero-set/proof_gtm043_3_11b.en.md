---
role: proof
locale: en
of_concept: gdelta-containing-compact-contains-zero-set
source_book: gtm043
source_chapter: "3"
source_section: "3.11"
---

A $G_{\delta}$-set $A$ has the form $\bigcap_{n \in \mathbb{N}} U_n$, where each $U_n$ is open. If $A \supset S$, then $S$ is completely separated from $X - U_n$ (by Theorem 3.11(a), since $\{x\}$ is compact for each $x \notin U_n$, and using compactness of $S$), and so there is a zero-set $F_n$ satisfying $S \subset F_n \subset U_n$. Then
$$S \subset \bigcap_n F_n \subset A;$$
and $\bigcap_n F_n$, as a countable intersection of zero-sets, is a zero-set.

In particular, every compact $G_{\delta}$ in a completely regular space is a zero-set. Special case: every $G_{\delta}$-point is a zero-set.
