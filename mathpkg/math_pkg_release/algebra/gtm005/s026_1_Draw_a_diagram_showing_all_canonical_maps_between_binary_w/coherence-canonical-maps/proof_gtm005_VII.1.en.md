---
role: proof
locale: en
of_concept: coherence-canonical-maps
source_book: gtm005
source_chapter: "VII"
source_section: "1"
---

Mac Lane's Coherence Theorem: Any two canonical maps in a monoidal category between the same two tensor product expressions (built from $\alpha$, $\lambda$, $\rho$, identities, $\otimes$, and composition) are equal.

Proof strategy: Every monoidal category is monoidally equivalent to a strict monoidal category (where $\alpha$, $\lambda$, $\rho$ are identities). In a strict monoidal category, there is exactly one canonical map between any two expressions (since all bracketings are literally equal). The monoidal equivalence transports this uniqueness back to the original category.

The strictification is achieved by constructing the category of "formal words" where objects are finite sequences of objects of the original category, and associativity/unit maps become identities. The equivalence shows any diagram of canonical maps commutes.
