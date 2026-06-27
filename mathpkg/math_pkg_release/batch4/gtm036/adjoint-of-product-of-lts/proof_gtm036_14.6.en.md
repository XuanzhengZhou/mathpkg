---
role: proof
locale: en
of_concept: adjoint-of-product-of-lts
source_book: gtm036
source_chapter: "14"
source_section: "14.6"
---

Recall that a local base for the product topology is the family of sets $U$ of the following form: $U$ is the set of all $x$ in the product such that, for each $t$ in a fixed finite set $B$, $x_t$ belongs to a prescribed neighborhood in $E_t$. A linear functional $\phi$ on the product $\times \{E_t: t \in A\}$ is continuous if and only if it is bounded on some such $U$, which means $\phi$ annihilates all but finitely many coordinate axes. Hence $\phi$ can be written as a finite sum: $\phi(x) = \sum \{g_t(x_t): t \in B\}$ where $g_t \in E_t^*$ for each $t \in B$, and $B$ is a finite subset of $A$. This representation is unique, establishing that $(\times E_t)^* \cong \sum E_t^*$, the direct sum of the adjoints.
