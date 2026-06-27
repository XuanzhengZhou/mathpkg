---
role: proof
locale: en
of_concept: localization-of-continuity-linear
source_book: gtm036
source_chapter: "5"
source_section: "3"
---

Recall that a function $T$ on a topological space $E$ to a topological space $F$ is continuous at a point $x$ if for each neighborhood $W$ of $T(x)$ there is a neighborhood of $x$ whose image under $T$ is a subset of $W$. If $T$ is linear, if $E$ is a linear topological space with local base $\mathcal{U}$, and if $F$ is a linear topological space with local base $\mathcal{V}$, then $T$ is continuous at $x$ if and only if for each $V$ in $\mathcal{V}$ there is $U$ in $\mathcal{U}$ such that $T[U + x] \subset V + T(x)$; that is, if and only if $T[U] \subset V$. Thus a linear function is continuous at some point $x$ of its domain if and only if it is continuous at $0$, and this is the case if and only if it is continuous at every point.
