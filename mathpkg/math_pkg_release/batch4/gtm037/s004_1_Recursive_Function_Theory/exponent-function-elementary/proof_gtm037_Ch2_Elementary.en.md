---
role: proof
locale: en
of_concept: exponent-function-elementary
source_book: gtm037
source_chapter: "2"
source_section: "Elementary and Primitive Recursive Functions"
---

The exponent $(a)_i$ can be expressed using the bounded minimum operator:
$$(a)_i = \mu x < a \; (p_i^x \mid a \text{ and } p_i^{x+1} \nmid a).$$
Here $p_i^x \mid a$ means $p_i^x$ divides $a$, and $p_i^{x+1} \nmid a$ means $p_i^{x+1}$ does not divide $a$. The divisibility relation $x \mid y$ is elementary, the prime function $p_i$ is elementary by Proposition 2.23, and exponentiation $x^y$ and the bounded $\mu$-operator preserve elementarity. Hence $(a)_i$ is elementary.
