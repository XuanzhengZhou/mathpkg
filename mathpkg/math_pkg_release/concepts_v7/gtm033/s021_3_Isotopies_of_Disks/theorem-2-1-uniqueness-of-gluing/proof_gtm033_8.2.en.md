---
role: proof
locale: en
of_concept: theorem-2-1-uniqueness-of-gluing
source_book: gtm033
source_chapter: "8"
source_section: "2"
---

# Proof of Theorem 8.2.1 (Uniqueness of Differential Structure on Glued Manifolds)

Let $P, Q$ be manifolds with boundary and let $f: \partial Q \to \partial P$ be a diffeomorphism. Then the adjunction space $P \cup_f Q$ admits a differential structure, unique up to diffeomorphism, which induces the original structures on $P$ and $Q$ (after smoothing corners).

**Proof.** This theorem is proved in Section 8.2 of the book (Gluing Manifolds). The proof constructs a smooth structure on $P \cup_f Q$ by using collar neighborhoods of $\partial P$ and $\partial Q$ to extend $f$ to a diffeomorphism of tubular neighborhoods, then applying the fact that any two such extensions are isotopic, and isotopic gluing maps yield diffeomorphic adjunction spaces (Theorem 2.3). The full proof appears in the preceding section file (s020) of the stitched sections.

The uniqueness argument relies on the fact that collar neighborhoods are unique up to isotopy, and different choices of smoothing the corner along $\partial P = \partial Q$ in $P \cup_f Q$ lead to diffeomorphic manifolds by a standard argument using the existence and uniqueness of collars (Section 6). $\square$
