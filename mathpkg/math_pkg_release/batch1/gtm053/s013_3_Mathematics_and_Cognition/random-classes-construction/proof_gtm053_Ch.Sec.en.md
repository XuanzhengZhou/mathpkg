---
role: proof
locale: en
of_concept: random-classes-construction
source_book: gtm053
source_chapter: "III"
source_section: "6"
---

The proof uses the "truth" of the equality axiom:
$$\|\forall x \forall y_1 \cdots \forall y_n (x = y \Rightarrow (P(x, y_1, \ldots, y_n) \Rightarrow P(y, y_1, \ldots, y_n)))\| = 1.$$
Taking a point $\xi$ assigning $X, Y, Y_1, \ldots, Y_n$ to $x, y, y_1, \ldots, y_n$, we obtain
$$\|X = Y\| \wedge W(X) \leqslant W(Y),$$
which establishes the extensionality of $W$.
