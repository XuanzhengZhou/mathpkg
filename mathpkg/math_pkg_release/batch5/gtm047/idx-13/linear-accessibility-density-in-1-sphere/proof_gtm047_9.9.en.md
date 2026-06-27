---
role: proof
locale: en
of_concept: linear-accessibility-density-in-1-sphere
source_book: gtm047
source_chapter: "9"
source_section: "9"
---

Take $w \in \text{Int } A$, and let $B$ be a small disk centered at $w$ such that $B \cap J \subset \text{Int } A$. Since $I$ is open (by the Jordan curve theorem), $B \cap I$ is nonempty. Pick any point $x \in B \cap I$. The line segment $wx$ meets $J$ at $w$ and lies otherwise in $B$. Since $B \cap J \subset \text{Int } A$, the segment from $x$ toward $w$ must enter $I$ before hitting $J$. Let $v$ be the first point of this segment (starting from $x$) that lies in $J$. Then $v \in \text{Int } A$ (since $B \cap J \subset \text{Int } A$), and the subsegment from $v$ to $x$ lies entirely in $I$ except at $v$. Taking $v' = x$ gives the desired linear interval.

The proof of the density statement is incomplete in the source text; the argument above establishes existence of at least one linearly accessible point in any arc $A$, which implies density.
