---
role: proof
locale: en
of_concept: uncountable-gdelta-contains-nowhere-dense-closed-set
source_book: gtm002
source_chapter: "5"
source_section: "Non-Measurable Sets"
---

**Proof.** Let $E = \bigcap_{n=1}^{\infty} G_n$, where each $G_n$ is open. Let $F$ denote the set of all condensation points of $E$ that belong to $E$, i.e., points $x \in E$ such that every neighborhood of $x$ contains uncountably many points of $E$. Then $F$ is non-empty; otherwise, the family of intervals with rational endpoints that contain only countably many points of $E$ would cover $E$, making $E$ countable. Similarly, $F$ has no isolated points.

Let $I(0)$ and $I(1)$ be two disjoint closed intervals of length at most $1/3$ whose interiors meet $F$ and whose union is contained in $G_1$. Proceeding inductively, suppose $2^n$ disjoint closed intervals $I(i_1, \ldots, i_n)$ (with $i_k = 0$ or $1$) have been defined whose interiors all meet $F$ and whose union is contained in $G_n$. For each such interval, choose two disjoint closed subintervals $I(i_1, \ldots, i_n, 0)$ and $I(i_1, \ldots, i_n, 1)$ of length at most $1/3^{n+1}$, contained in $G_{n+1} \cap I(i_1, \ldots, i_n)$, whose interiors meet $F$. Since $F$ has no isolated points and $E \subset G_{n+1}$, such intervals exist.

Define
$$C = \bigcap_{n=1}^{\infty} \bigcup_{i_1, \ldots, i_n} I(i_1, \ldots, i_n).$$
Then $C$ is closed, nowhere dense (since it contains no interval of length exceeding $1/3^n$ for any $n$), and has measure zero (the total length at stage $n$ is $(2/3)^n$). The mapping that sends each point of $C$, represented by its sequence of dyadic indices $(i_1, i_2, \ldots)$, to the number with binary expansion $0.i_1 i_2 \ldots$ in $[0,1]$ is a continuous surjection onto $[0,1]$. $\square$
