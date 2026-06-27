---
role: proof
locale: en
of_concept: diagonal-fill-in
source_book: gtm026
source_chapter: "2"
source_section: "4"
---

Uniqueness is immediate: since $e \in E$ is an epimorphism (axiom 4.3), the equation $e \circ h = f$ uniquely determines $h$. (Equivalently, since $m \in M$ is a monomorphism, $h \circ m = g$ uniquely determines $h$.)

For existence, let $g = e_1 \circ m_1$ and $f = e_2 \circ m_2$ be the $E$-$M$ factorizations of $g$ and $f$, respectively. Here $e_1, e_2 \in E$ and $m_1, m_2 \in M$, and we write composition in diagrammatic order ($x; y$ means apply $x$ then $y$).

The commutativity $f; m = e; g$ yields two $E$-$M$ factorizations of the same morphism:
$$
(e_2, \; m_2; m) \quad \text{and} \quad (e; e_1, \; m_1).
$$
Both factor the morphism $A \to D$ obtained by traversing the square.

By the uniqueness clause of axiom 4.5, there exists an isomorphism
$$
\psi: \mathrm{Im}(g) \longrightarrow \mathrm{Im}(f)
$$
satisfying the two relations encoded in the comparison diagram:
$$
e_2; \psi^{-1} = e; e_1, \qquad \psi^{-1}; m_2; m = m_1
$$
or equivalently (renaming $\psi \leftrightarrow \psi^{-1}$ as needed),
$$
e_2; \psi = e; e_1, \qquad \psi; m_1 = m_2; m.
$$
The direction of $\psi$ is fixed by the requirement that these equations type-check. Define
$$
h = e_1; \psi; m_2: B \longrightarrow C.
$$

To verify $e; h = f$, compute:
$$
e; h = e; e_1; \psi; m_2 = e_2; \psi^{-1}; \psi; m_2 = e_2; m_2 = f,
$$
using the relation connecting the two factorizations. Similarly, $h; m = g$ follows from the second relation.

The construction is the standard diagonal fill-in argument for any factorization system: the two $E$-$M$ factorizations of the composite along the square are compared via the unique isomorphism provided by 4.5, and the diagonal morphism is assembled from the constituent parts.
