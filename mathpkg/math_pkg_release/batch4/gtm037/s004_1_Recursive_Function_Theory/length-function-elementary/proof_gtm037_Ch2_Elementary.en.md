---
role: proof
locale: en
of_concept: length-function-elementary
source_book: gtm037
source_chapter: "2"
source_section: "Elementary and Primitive Recursive Functions"
---

The length function can be expressed using the bounded minimum operator:
$$l(a) = \mu i < a \; [\, p_i \mid a \text{ and } \forall j \leq a \; (i < j \Rightarrow p_j \nmid a) \,].$$
This states that $l(a)$ is the least $i < a$ such that $p_i$ divides $a$ and for all $j$ with $i < j \leq a$, $p_j$ does not divide $a$. The bounded universal quantifier preserves elementarity by Proposition 2.15, and the prime function $p_k$ is elementary by Proposition 2.23. Therefore $l(a)$ is elementary.
