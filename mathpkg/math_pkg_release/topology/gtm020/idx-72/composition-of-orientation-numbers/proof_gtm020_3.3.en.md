---
role: proof
locale: en
of_concept: composition-of-orientation-numbers
source_book: gtm020
source_chapter: "3"
source_section: "3.3"
---

For the first statement, we observe that
$$\det[D(g \circ f)(x)] = \det[D(g)(f(x))] \cdot \det[D(f)(x)]$$
by the chain rule. Thus
$$O(g \circ f) = \operatorname{sgn}(\det[D(g \circ f)(x)]) = \operatorname{sgn}(\det[D(g)(f(x))]) \cdot \operatorname{sgn}(\det[D(f)(x)]) = O(g)\,O(f).$$
The second statement is immediate from the definition: since $f|_{U'}$ agrees with $f$ on $U'$, its Jacobian determinant has the same sign at every point of $U'$ as the Jacobian determinant of $f$ itself.
