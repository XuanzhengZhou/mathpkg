---
role: proof
locale: en
of_concept: compact-net-cluster-point
source_book: gtm036
source_chapter: "2"
source_section: "4"
---
This equivalence is a standard theorem in general topology, stated here without proof.

If $X$ is compact but some net $\{x_\alpha\}_{\alpha \in A}$ has no cluster point, then each point $x \in X$ has an open neighborhood $U_x$ visited by the net only finitely often (i.e., there exists $\alpha_x$ such that for all $\beta \geq \alpha_x$, $x_\beta \notin U_x$). The family $\{U_x : x \in X\}$ covers $X$; by compactness there is a finite subcover $\{U_{x_1}, \ldots, U_{x_n}\}$. Taking an index $\gamma$ larger than all $\alpha_{x_i}$ (possible since $A$ is directed), the net must lie outside all $U_{x_i}$ for $\beta \geq \gamma$, contradicting the cover property.

Conversely, if every net has a cluster point but there exists an open cover $\{U_i\}$ with no finite subcover, consider the directed set of finite subsets of the index set ordered by inclusion. For each finite $F$, choose $x_F$ not in $\bigcup_{i \in F} U_i$ (possible by the no-finite-subcover assumption). This net has a cluster point $x$, which lies in some $U_{i_0}$. But then the net must cofinally visit $U_{i_0}$, yet for any $F$ containing $i_0$, $x_F \notin U_{i_0}$, a contradiction.
