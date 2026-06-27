---
role: proof
locale: en
of_concept: projections-and-injections
source_book: gtm036
source_chapter: "1"
source_section: "1.5"
---

*Projection.* For each $s \in A$, the projection $P_s$ is defined on the product $\prod \{E_t : t \in A\}$ by $P_s(x) = x(s)$. Linearity follows from the pointwise definition of the linear operations in the product: for $x, y$ in the product and scalar $a$,
$$
P_s(x + y) = (x + y)(s) = x(s) + y(s) = P_s(x) + P_s(y),
$$
$$
P_s(a x) = (a x)(s) = a \, x(s) = a P_s(x).
$$
Since any element $z \in E_s$ can be realized as $P_s(x)$ by choosing $x$ with $x(s) = z$, the map $P_s$ is surjective onto $E_s$.

*Injection.* The injection $I_s : E_s \to \sum \{E_t : t \in A\}$ is defined for each $x \in E_s$ by
$$
I_s(x)(t) = \begin{cases} x & \text{if } t = s, \\ 0 & \text{if } t \neq s. \end{cases}
$$
Additivity: for $x, y \in E_s$,
$$
I_s(x + y)(t) = \begin{cases} x + y & (t = s) \\ 0 & (t \neq s) \end{cases} = I_s(x)(t) + I_s(y)(t),
$$
so $I_s(x + y) = I_s(x) + I_s(y)$. Scalar multiplication: similarly $I_s(a x) = a I_s(x)$. Hence $I_s$ is linear. It is injective because $I_s(x) = I_s(y)$ implies $x = I_s(x)(s) = I_s(y)(s) = y$. Its image is precisely $\{x \in \sum E_t : x(t) = 0 \text{ for } t \neq s\}$, i.e., those members of the direct sum supported only at $s$. On this subspace the inverse is given by the restriction of $P_s$, so $I_s$ is a linear isomorphism onto its image.
