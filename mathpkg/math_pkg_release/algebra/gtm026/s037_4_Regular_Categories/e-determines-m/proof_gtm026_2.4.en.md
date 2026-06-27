---
role: proof
locale: en
of_concept: e-determines-m
source_book: gtm026
source_chapter: "2"
source_section: "4"
---

Let $(e, m)$ be the $E$-$M$ factorization of $t$, so that $t = e \circ m$ with $e \in E$, $m \in M$, and $e: C \to \mathrm{Im}(t)$, $m: \mathrm{Im}(t) \to D$.

By the assumed property of $t$, applied to the commutative square
$$
\begin{array}{ccc}
C & \xrightarrow{e} & \mathrm{Im}(t) \\
{\scriptstyle \mathrm{id}_C}\downarrow & & \downarrow{\scriptstyle m} \\
C & \xrightarrow{t} & D
\end{array}
$$
where the left edge $e \in E$ and the bottom edge is $t$, there exists a diagonal morphism
$$
h: \mathrm{Im}(t) \longrightarrow C
$$
such that $e \circ h = \mathrm{id}_C$.

Since $e$ is an epimorphism (axiom 4.3), the equation $e \circ h = \mathrm{id}_C$ implies $h \circ e \circ h = h$, and from $e \circ h = \mathrm{id}_C$ we also obtain $h \circ t = m$. Indeed, composing $t = e \circ m$ with $h$ on the left gives $h \circ t = h \circ e \circ m = \mathrm{id}_C \circ m = m$? No — careful: $e \circ h = \mathrm{id}_C$, not $h \circ e = \mathrm{id}_C$.

The correct computation from the diagram: the square commutes, so $e \circ m = t \circ \mathrm{id}_C = t$, which is just the factorization. The diagonal condition gives $e \circ h = \mathrm{id}_C$. From the commutativity of the lower triangle we need $h \circ t = m$, which follows from the fact that $e \circ h \circ t = t$ (using $e \circ h = \mathrm{id}_C$), and since $e$ is epi, $h \circ t = m$.

Now, since $m$ is a monomorphism (axiom 4.3) and
$$
h \circ e \circ m = h \circ t = m = \mathrm{id}_{\mathrm{Im}(t)} \circ m,
$$
we have $h \circ e \circ m = m$, whence $h \circ e = \mathrm{id}_{\mathrm{Im}(t)}$ (since $m$ is mono and $h \circ e \circ m = m$ gives $(h \circ e) \circ m = \mathrm{id} \circ m$, so $h \circ e = \mathrm{id}$).

Thus $h$ is an isomorphism with inverse $e$. Using axioms 4.4 and 4.2, $e$ is an isomorphism (being the inverse of $h$), and therefore
$$
t = e \circ m = h^{-1} \circ m \in M
$$
since $M$ is a subcategory (axiom 4.2) and contains all isomorphisms (axiom 4.4), so the composite of an isomorphism ($h^{-1}$) with a morphism in $M$ ($m$) remains in $M$.

[Note: the source text reaches the same conclusion via a slightly different computation using the diagrammatic order convention. The essential point is that the diagonal fill-in hypothesis forces the $E$-part of the factorization of $t$ to be an isomorphism, so $t \in M$.]
