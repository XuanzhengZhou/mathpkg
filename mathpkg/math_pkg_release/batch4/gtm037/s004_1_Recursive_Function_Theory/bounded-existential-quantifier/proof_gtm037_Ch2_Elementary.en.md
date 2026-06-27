---
role: proof
locale: en
of_concept: bounded-existential-quantifier
source_book: gtm037
source_chapter: "2"
source_section: "Elementary and Primitive Recursive Functions"
---

The characteristic function of $S$ is given by
$$\chi_S(x_0, \ldots, x_{m-1}) = \operatorname{sg} \sum \{\chi_R(x_0, \ldots, x_{m-2}, y) : y < x_{m-1}\}.$$
The sum over the finite set $\{y : y < x_{m-1}\}$ of values of $\chi_R$ is an $A$-function because $A$ is closed under the elementary recursive operations (in particular, bounded sum). Then applying the sign function $\operatorname{sg}$ preserves membership in $A$. Hence $\chi_S$ is an $A$-function, so $S$ is an $A$-relation.
