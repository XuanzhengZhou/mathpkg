---
role: proof
locale: en
of_concept: duality-of-category-axioms
source_book: gtm005
source_chapter: "II. Constructions on Categories"
source_section: "1. Duality"
---

The axioms for a category (as given in §I.1) are:

1. **Identity**: For each object $a$, there exists an identity arrow $1_a : a \to a$ such that $f \circ 1_a = f$ and $1_b \circ f = f$ for all $f : a \to b$.
2. **Associativity**: $(h \circ g) \circ f = h \circ (g \circ f)$ whenever the composites are defined.
3. **Domain/Codomain**: For each arrow $f$ there exist objects $a = \operatorname{dom} f$ and $b = \operatorname{cod} f$ with $f : a \to b$.

Taking the dual of axiom (1): the identity arrow $1_a : a \to a$ is self-dual (there is no arrow to reverse), so the dual statement is identical to the original --- it is still an axiom. Taking the dual of axiom (2): reversing the order of composition yields $f^{*} \circ (g^{*} \circ h^{*}) = (f^{*} \circ g^{*}) \circ h^{*}$, which is again the associativity axiom. Taking the dual of axiom (3): $f^{*} : b \to a$ has $b$ as domain and $a$ as codomain, which is still an instance of the domain/codomain axiom. Thus every axiom dualizes to another axiom.
