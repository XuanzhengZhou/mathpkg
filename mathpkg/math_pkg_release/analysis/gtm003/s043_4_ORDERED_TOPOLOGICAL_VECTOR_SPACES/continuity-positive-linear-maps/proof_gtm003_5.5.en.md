---
role: proof
locale: en
of_concept: continuity-positive-linear-maps
source_book: gtm003
source_chapter: "V"
source_section: "5"
---

Let $u$ be a linear map of $E$ into $F$ such that $u(C) \subset D$, and consider the algebraic adjoint $u^*$ of $u$ (Chapter IV, Section 2). For each $y' \in D'$, the map $x \to \langle x, u^* y' \rangle = \langle u(x), y' \rangle$ is a positive linear form on $E$, hence continuous by assumption. Since $F' = D' - D'$ by (3.3), Corollary 3 (weak normality of $D$), it follows that $u^*(F') \subset E'$; hence $u$ is weakly continuous by (IV, 2). Since $E$ is a Mackey space, every weakly continuous linear map from $E$ into a locally convex space is continuous; therefore $u$ is continuous.
