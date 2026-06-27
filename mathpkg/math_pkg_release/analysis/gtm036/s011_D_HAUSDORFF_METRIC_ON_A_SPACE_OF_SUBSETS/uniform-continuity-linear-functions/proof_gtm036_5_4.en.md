---
role: proof
locale: en
of_concept: uniform-continuity-linear-functions
source_book: gtm036
source_chapter: "5"
source_section: "4"
---

Let $T$ be continuous at $0$. By Proposition 5.3 (localization of continuity), $T$ is continuous everywhere. For each neighborhood $V$ of $0$ in $F$, continuity at $0$ gives a neighborhood $U$ of $0$ in $E$ such that $T[U] \subset V$. Then for any $x, y \in E$ with $x - y \in U$, we have $T(x) - T(y) = T(x - y) \in V$ by linearity. This establishes the stated uniform continuity property.

The extension property follows from the general principle for uniformly continuous functions: if $T$ is uniformly continuous and the codomain is complete, then $T$ extends uniquely to a continuous linear map on the completion of its domain. (The text notes this as "a form of a well-known principle applying to arbitrary uniformly continuous functions.")
