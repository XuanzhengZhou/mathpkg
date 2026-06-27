---
role: proof
locale: en
of_concept: associator-subgroup-auxiliary
source_book: gtm006
source_chapter: "6"
source_section: "7. The Skornyakov-San Soucie Theorem"
---

Let $x \in A(a, b)$. Then $[x, a, b] = x[b, a]$, so $(xa)b - x(ab) = x(ba) - x(ab)$, hence $(xa)b = x(ba)$. The converse is clear.

We have $[0, a, b] = 0 = 0[b, a]$, so $0 \in A(a, b)$.

Let $x, y \in A(a, b)$. Then
$$[x - y, a, b] = [x, a, b] - [y, a, b] = x[b, a] - y[b, a] = (x - y)[b, a].$$
Hence $x - y \in A(a, b)$, so $A(a, b)$ is a subgroup.

Finally,
$$x \in A(a, b) \iff [x, a, b] = x[b, a] \iff -[x, b, a] = -x[a, b] \iff [x, b, a] = x[a, b] \iff x \in A(b, a).$$
Thus $A(a, b) = A(b, a)$. $\square$
