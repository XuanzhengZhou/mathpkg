---
role: proof
locale: en
of_concept: monoid-is-semigroup-with-identity
source_book: gtm005
source_chapter: "I"
source_section: "2"
---

Let $M$ be a monoid, i.e., a category with exactly one object $*$. Let $S = \hom(*, *)$ be the set of all arrows from $*$ to itself. Since there is only one object, any two arrows $f, g \in S$ are composable: $\operatorname{dom} g = * = \operatorname{cod} f$, so $\langle g, f \rangle \in A \times_O A$. Define a binary operation $\cdot : S \times S \to S$ by $g \cdot f = g \circ f$.

Associativity follows directly from the associativity axiom of categories: for all $f, g, h \in S$,
$$
h \cdot (g \cdot f) = h \circ (g \circ f) = (h \circ g) \circ f = (h \cdot g) \cdot f.
$$
Thus $(S, \cdot)$ is a semigroup.

The identity arrow $\operatorname{id}_* \in S$ serves as a two-sided identity element: for every $f \in S$, the unit axiom of categories gives
$$
f \cdot \operatorname{id}_* = f \circ \operatorname{id}_{\operatorname{dom} f} = f = \operatorname{id}_{\operatorname{cod} f} \circ f = \operatorname{id}_* \cdot f.
$$
Thus $(S, \cdot, \operatorname{id}_*)$ is a semigroup with identity.

Conversely, given a set $S$ with an associative binary operation $\cdot$ and a two-sided identity element $e \in S$, define a category with one object $*$, arrow set $S$, $\operatorname{dom}(f) = \operatorname{cod}(f) = *$ for all $f \in S$, $\operatorname{id}_* = e$, and $g \circ f = g \cdot f$. The associativity and unit axioms hold by the semigroup and identity properties. Hence a monoid is exactly a semigroup with identity element.
