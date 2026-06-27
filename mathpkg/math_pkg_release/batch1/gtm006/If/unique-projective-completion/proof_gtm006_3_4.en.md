---
role: proof
locale: en
of_concept: unique-projective-completion
source_book: gtm006
source_chapter: "3"
source_section: "4"
---

We construct a projective plane $\mathcal{P}$ with a line $l_\infty$ such that $\mathcal{A} = \mathcal{P}^{l_\infty}$.

Let the points of $\mathcal{P}$ be the points of $\mathcal{A}$ together with one new point for each parallel class of lines of $\mathcal{A}$ (the "points at infinity"). Let the lines of $\mathcal{P}$ be the lines of $\mathcal{A}$ together with one new line $l_\infty$ (the "line at infinity"). Incidence is defined as follows: a point of $\mathcal{A}$ is on a line of $\mathcal{A}$ in $\mathcal{P}$ exactly when it is in $\mathcal{A}$; a point at infinity corresponding to a parallel class $\Pi$ is on every line of $\mathcal{A}$ belonging to $\Pi$; and every point at infinity is on $l_\infty$.

We verify the projective plane axioms. Any two distinct points of $\mathcal{A}$ are joined by their unique line in $\mathcal{A}$, which is also a line of $\mathcal{P}$. A point $A$ of $\mathcal{A}$ and a point at infinity $\Pi^*$: the unique line through $A$ parallel to the class $\Pi^*$ (axiom (ii) of affine planes) is the joining line. Two distinct points at infinity $\Pi_1^*, \Pi_2^*$ are joined by $l_\infty$.

For lines, any two lines of $\mathcal{A}$ that intersect in $\mathcal{A}$ do so uniquely in $\mathcal{P}$. If they are parallel in $\mathcal{A}$, they belong to the same parallel class $\Pi^*$, and intersect at the point $\Pi^*$ in $\mathcal{P}$. A line of $\mathcal{A}$ and $l_\infty$ intersect at the point at infinity corresponding to the parallel class of that line.

Since $\mathcal{A}$ contains three non-collinear points $X, Y, Z$, let $XY \cap l_\infty = A^*$ and $YZ \cap l_\infty = B^*$ in $\mathcal{P}$. As $XY$ is not parallel to $YZ$, $A^* \neq B^*$, and $X, Z, A^*, B^*$ form a quadrangle, proving $\mathcal{P}$ is a projective plane.

For uniqueness, suppose $\mathcal{A} = \mathcal{P}^l = \mathcal{P}'^{l'}$. Then by Lemma 3.11, since the identity is an isomorphism from $\mathcal{P}^l$ to $\mathcal{P}'^{l'}$ (both equal to $\mathcal{A}$), there exists an isomorphism from $\mathcal{P}$ to $\mathcal{P}'$ mapping $l$ to $l'$.
