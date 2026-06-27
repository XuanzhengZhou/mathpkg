---
role: proof
locale: en
of_concept: category-object-in-sets-is-small-category
source_book: gtm005
source_chapter: "XII"
source_section: "1. Internal Categories"
---

In $\mathbf{Set}$, the pullback $C_1 \times_{C_0} C_1$ is precisely the set of composable pairs $\{(f, g) \mid d_1 f = d_0 g\}$. The composition map $\gamma : C_1 \times_{C_0} C_1 \to C_1$ is then an ordinary function assigning a composite arrow to each composable pair. The commutativity conditions (3)-(6) translate as follows:

(3) $d_0 i = 1 = d_1 i$ means each object $c$ has an identity arrow $i(c)$ whose domain and codomain are both $c$.

(4) $i \times 1$ and $1 \times i$ with $\gamma$ assert that composing with an identity arrow on either side returns the original arrow: $\gamma(i(c), f) = f$ and $\gamma(g, i(c)) = g$.

(5) $d_0 \gamma = d_0 \pi_1$ and $d_1 \gamma = d_1 \pi_2$ assert that the domain of a composite $g \circ f$ is the domain of $f$ and the codomain is the codomain of $g$.

(6) The associativity diagram on $C_1 \times_{C_0} C_1 \times_{C_0} C_1$ asserts $\gamma(\gamma(f, g), h) = \gamma(f, \gamma(g, h))$ for composable triples.

Thus an internal category in $\mathbf{Set}$ is exactly a small category in the ordinary sense: $C_0$ is a set of objects, $C_1$ is a set of arrows, and the structure maps satisfy the standard category axioms.
