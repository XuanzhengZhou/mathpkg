---
role: proof
locale: en
of_concept: envelop-compact-implies-partition-refinement
source_book: gtm043
source_chapter: "16"
source_section: "26"
---
By hypothesis, each component $F_\alpha$ of $F$ is contained in some member $U_\alpha$ of $\mathcal{U}$. Now, each $F_\alpha$ is an intersection of open-and-closed sets in the compact set $F$ (Theorem 16.15); hence some finite intersection is contained in the open set $U_\alpha$. Thus, there exists an open-and-closed set $H_\alpha$ in $F$, with $F_\alpha \subset H_\alpha \subset U_\alpha$. A finite collection of the sets $H_\alpha$ covers the compact set $F$; the required partition of $F$ is obtained from this collection by taking intersections and differences where necessary. The converse is obvious: if a partition of $F$ refines $\mathcal{U}$, then $\mathcal{U}$ envelops $F$.
