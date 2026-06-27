---
role: proof
locale: en
of_concept: uncountable-gdelta-contains-perfect-set
source_book: gtm002
source_chapter: "5"
source_section: "5. Non-Measurable Sets"
---
Let $E = \bigcap G_n$, $G_n$ open, be an uncountable $G_{\delta}$ set. Let $F$ denote the set of all condensation points of $E$ that belong to $E$, that is, all points $x$ in $E$ such that every neighborhood of $x$ contains uncountably many points of $E$. $F$ is non-empty; otherwise, the family of intervals that have rational endpoints and contain only countably many points of $E$ would cover $E$, and $E$ would be countable. Similar reasoning shows that $F$ has no isolated points.

Let $I(0)$ and $I(1)$ be two disjoint closed intervals of length at most $1/3$ whose interiors meet $F$ and whose union is contained in $G_1$. Proceeding inductively, if $2^n$ disjoint closed intervals $I(i_1, \ldots, i_n)$ ($i_k = 0$ or $1$) whose interiors all meet $F$ and whose union is contained in $G_n$ have been defined, let $I(i_1, \ldots, i_{n+1})$ ($i_{n+1} = 0$ or $1$) be disjoint closed intervals of length at most $1/3^{n+1}$ contained in $G_{n+1} \cap I(i_1, \ldots, i_n)$ whose interiors meet $F$.

From the fact that $F$ has no isolated points and that $E \subset G_{n+1}$ it is clear that such intervals exist. Thus a family of intervals $I(i_1, \ldots, i_n)$ having the stated properties can be defined for all finite sequences of $0$'s and $1$'s. Let
$$C = \bigcap_{n=1}^{\infty} \bigcup_{i_1,\ldots,i_n} I(i_1, \ldots, i_n).$$
Then $C \subset E$, $C$ is closed, $C$ is nowhere dense, and $C$ has measure zero. The mapping that sends each point of $C$ to the real number whose binary expansion is determined by the sequence of intervals containing it maps $C$ continuously onto $[0, 1]$.
