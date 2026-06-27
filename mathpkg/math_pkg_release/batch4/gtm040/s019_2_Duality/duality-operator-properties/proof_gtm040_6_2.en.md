---
role: proof
locale: en
of_concept: duality-operator-properties
source_book: gtm040
source_chapter: "6"
source_section: "2. Duality"
---

We prove (1) and (4); the rest of the proof is left to the reader.

For (1), we have

$$\text{dual dual } X = \text{dual}(D X^T D^{-1})$$
$$= D(D X^T D^{-1})^T D^{-1}$$
$$= D D^{-1} X^{TT} D D^{-1}$$
$$= X.$$

Associativity holds because all matrices involved are non-negative, so no convergence issues arise.

For (4), we compute

$$\text{dual}(XY) = D(XY)^T D^{-1} = D Y^T X^T D^{-1} = (D Y^T D^{-1})(D X^T D^{-1}) = \text{dual } Y \; \text{dual } X.$$

This uses $(XY)^T = Y^T X^T$ and the insertion of $D^{-1}D = I$ between $Y^T$ and $X^T$.
