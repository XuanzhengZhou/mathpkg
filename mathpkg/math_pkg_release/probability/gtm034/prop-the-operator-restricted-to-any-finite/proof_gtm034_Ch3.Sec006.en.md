---
role: proof
locale: en
of_concept: prop-the-operator-restricted-to-any-finite
source_book: gtm034
source_chapter: "3"
source_section: "006"
---

Proof: If P8 were false, there would be a function $v(x)$, $x \in B$, such that

$$\sum_{s \in B} v(s) A(s,y) = 0 \text{ for } y \in B,$$

and such that $v(x)$ does not vanish identically on $B$. We shall assume this to be so and operate by $v$ on the left in P4 (i.e., we multiply P4 by $v(x)$ and sum $x$ over $B$), obtaining

$$v(y) = \mu_B(y) \sum_{z \in B} v(x), \quad y \in B.$$

As $\mu_B(y) \geq 0$ on $B$, we have either $v(y) \geq 0$ on $B$ or $v(y) \leq 0$ on $B$. But we know that $A(x,y) \geq 0$ since it is the limit of the sequence of functions $A_n(x,y) = G_n(0,0) - G_n(x,y)$, which are non-negative by P1.3. The situation is further improved by P7 which adds the information that $A(x,y) > 0$ unless $x = y$. Therefore the operator $A$, with $x,y$ restricted to the set $B$, represents a matrix, with zeros on the diagonal, and with all other elements positive. Now this matrix $A$ has the property that $vA = 0$ where $v$ is a nonzero vector, all of whose components are of the same sign. This
