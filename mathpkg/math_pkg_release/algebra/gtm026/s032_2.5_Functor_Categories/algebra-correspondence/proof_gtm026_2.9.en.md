---
role: proof
locale: en
of_concept: algebra-correspondence
source_book: gtm026
source_chapter: "2"
source_section: "2.9"
---

Given a theory map $\lambda: T \to T'$, define a functor $V: \mathcal{K}^{T'} \to \mathcal{K}^T$ as follows. For a $T'$-algebra $(X, \xi': XT' \to X)$, set $(X, \xi')V = (X, X\lambda \cdot \xi')$, which is a $T$-algebra since:
$$
X\eta \cdot X\lambda \cdot \xi' = X\eta' \cdot \xi' = \mathrm{id}_X,
$$
and the $T$-associativity condition follows from the multiplication compatibility of the theory map.

For a $T'$-homomorphism $f: (X, \xi') \to (Y, \theta')$, we have $fT' \cdot \theta' = \xi' \cdot f$, and applying $V$ gives a $T$-homomorphism since $fT \cdot Y\lambda \cdot \theta' = X\lambda \cdot fT' \cdot \theta' = X\lambda \cdot \xi' \cdot f$.

Conversely, define a functor $\bar{V}: \mathcal{K}^T \to \mathcal{K}^{T'}$ sending a $T$-algebra $(X, \xi: XT \to X)$ to $(X, X\eta'T \cdot \xi_X, \xi')$, where appropriate structure maps are constructed using the theory map.

The two constructions are shown to be well-defined and to establish the correspondence. The verification that $V$ followed by $\bar{V}$ returns the original algebra, and vice versa, proceeds by diagram chase using the commuting diagrams displayed in the text.
