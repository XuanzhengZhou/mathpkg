---
role: proof
locale: en
of_concept: banach-steinhaus-barrel-proof
source_book: gtm036
source_chapter: "12"
source_section: "12.1"
---

Let $V$ be a closed, convex, circled neighborhood of $0$ in $G$. Define $W = \bigcap\{f^{-1}[V] : f \in F\}$. Each $f$ is continuous and $V$ is closed, so each $f^{-1}[V]$ is closed; hence $W$ is closed. Since each $f$ is linear and $V$ is convex and circled, each $f^{-1}[V]$ is convex and circled; hence $W$ is convex and circled. By Theorem 12.1(iv), pointwise boundedness of $F$ on $A$ (where $A$ is of second category) implies that $W$ absorbs each point of $A$, hence absorbs each point of $E$ (since $A$ being of second category implies it is "large" and $W$ is a vector subspace-like set).

Thus $W$ is a barrel in $E$. Since $E$ is of second category (as it contains a second category set), every barrel in $E$ is a neighborhood of $0$. Therefore $W$ is a neighborhood of $0$ in $E$.

Since this holds for an arbitrary closed, convex, circled neighborhood $V$ of $0$ in $G$, and such neighborhoods form a base at $0$, the family $F$ is equicontinuous.
