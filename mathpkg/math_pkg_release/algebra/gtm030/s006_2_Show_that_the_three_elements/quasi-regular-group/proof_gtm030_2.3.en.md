---
role: proof
locale: en
of_concept: quasi-regular-group
source_book: gtm030
source_chapter: "2"
source_section: "3"
---

Let $\mathfrak{A}$ be a ring and define the circle composition by $a \circ b = a + b - ab$.

**Associativity:** One verifies directly that the circle composition is associative. For any $a, b, c \in \mathfrak{A}$:
\begin{align*}
(a \circ b) \circ c &= (a + b - ab) \circ c \\
&= (a + b - ab) + c - (a + b - ab)c \\
&= a + b - ab + c - ac - bc + abc,
\end{align*}
and
\begin{align*}
a \circ (b \circ c) &= a \circ (b + c - bc) \\
&= a + (b + c - bc) - a(b + c - bc) \\
&= a + b + c - bc - ab - ac + abc.
\end{align*}
Both expressions are equal because addition is associative and commutative. Hence $(\mathfrak{A}, \circ)$ is a semi-group.

**Identity:** For any $a \in \mathfrak{A}$:
$$a \circ 0 = a + 0 - a \cdot 0 = a,$$
$$0 \circ a = 0 + a - 0 \cdot a = a.$$
Thus $0$ acts as the identity element in $(\mathfrak{A}, \circ)$.

**Definition of $\mathfrak{Q}$:** An element $a$ is quasi-regular if there exist $b, c \in \mathfrak{A}$ such that $a \circ b = 0$ and $c \circ a = 0$ (it has both left and right quasi-inverses). In a semi-group, if an element has both a left inverse and a right inverse, they coincide. Therefore the set $\mathfrak{Q}$ of quasi-regular elements is exactly the set of units of the semi-group $(\mathfrak{A}, \circ)$. Since the set of units of any semi-group with identity forms a group, $(\mathfrak{Q}, \circ)$ is a group.
