---
role: proof
locale: en
of_concept: if-varphi-abs-a-if-a-1-ldots-a-m-b-1-ldots-b-n-is-a-list-of-distinct-variables-c
source_book: gtm001
source_chapter: "11"
source_section: ""
---

** Since

$$b_1, \ldots, b_n \in A \land \varphi(a_1, \ldots, a_m, b_1, \ldots, b_n) \rightarrow a_1, \ldots, a_m \in A$$

we have that

$$b_1, \ldots, b_n \in A \rightarrow [(\exists x_1, \ldots, x_m) \varphi \leftrightarrow (\exists x_1, \ldots, x_m \in A) \varphi].$$

Since $\varphi$ is absolute w.r.t. $A$

$$b_1, \ldots, b_n \in A \land a_1, \ldots, a_m \in A \rightarrow [\varphi \leftrightarrow \varphi^A].$$

Therefore if $b_1, \ldots, b_n \in A$ then

$$[(\exists x_1, \ldots, x_m \in A) \varphi \leftrightarrow (\exists x_1, \ldots, x_m \in A) \varphi^A]$$

and hence

$$[(\exists x_1, \ldots, x_m) \varphi \leftrightarrow (\exists x_1, \ldots, x_m \in A) \varphi^A].$$
