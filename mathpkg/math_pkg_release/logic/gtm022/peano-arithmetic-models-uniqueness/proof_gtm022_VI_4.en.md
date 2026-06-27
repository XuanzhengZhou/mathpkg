---
role: proof
locale: en
of_concept: "peano-arithmetic-models-uniqueness"
source_book: gtm022
source_chapter: "VI"
source_section: "4"
---
Proof. Define $f(0) = 0'$ and, assuming $f(a) = a'$, define $f(s(a)) = s'(a')$. Use the induction axiom $P_5$ to show $f$ is a well-defined function from $A$ to $A'$. Construct $g: A' \to A$ symmetrically. Apply induction again to show $g \circ f = \operatorname{id}_A$ and $f \circ g = \operatorname{id}_{A'}$. Thus $f$ is an isomorphism. $\square$
