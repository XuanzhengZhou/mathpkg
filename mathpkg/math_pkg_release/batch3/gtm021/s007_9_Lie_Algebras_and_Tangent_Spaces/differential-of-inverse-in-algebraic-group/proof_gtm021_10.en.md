---
role: proof
locale: en
of_concept: differential-of-inverse-in-algebraic-group
source_book: gtm021
source_chapter: "10"
source_section: "Differentials of Morphisms"
---
Consider the composite map
$$G \xrightarrow{(1, \iota)} G \times G \xrightarrow{\mu} G,$$
which sends $x \mapsto x x^{-1} = e$. This is the constant map, so its differential at $e$ is the zero map.

Differentiating using the chain rule and Proposition 10.1(a):
$$0 = d(\mu \circ (1, \iota))_e = d\mu_{(e,e)} \circ d(1, \iota)_e = d\mu_{(e,e)}(d(1)_e(X), d\iota_e(X)) = d\mu_{(e,e)}(X, d\iota_e(X)) = X + d\iota_e(X).$$

Therefore $d\iota_e(X) = -X$.
