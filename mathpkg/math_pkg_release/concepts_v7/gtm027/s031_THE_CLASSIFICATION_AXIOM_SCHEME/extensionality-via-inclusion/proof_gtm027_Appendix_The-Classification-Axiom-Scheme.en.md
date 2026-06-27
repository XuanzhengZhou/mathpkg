---
role: proof
locale: en
of_concept: extensionality-via-inclusion
source_book: gtm027
source_chapter: "Appendix"
source_section: "The Classification Axiom Scheme"
---

# Proof of Extensionality via Inclusion

**Theorem 27.** $x = y$ iff $x \subset y$ and $y \subset x$.

*Proof.* By definition (Definition 25), $x \subset y$ means for each $z$, if $z \in x$ then $z \in y$. Similarly $y \subset x$ means for each $z$, if $z \in y$ then $z \in x$. Together these are equivalent to: for each $z$, $z \in x$ iff $z \in y$. By the axiom of extent (I), this is exactly the condition for $x = y$.
