---
role: proof
locale: en
of_concept: free-abelian-group-characterization
source_book: gtm057
source_chapter: "IV"
source_section: "5"
---

**Theorem (5.2):** An abelian group $G$ is free abelian iff it has a basis $E$ (a generating set such that any map $E \to H$ into an abelian group $H$ extends to a homomorphism).

*Proof.* ($\Rightarrow$) If $G$ is free abelian of rank $n$, then $G \cong F_n/[F_n, F_n]$ where $F_n$ is free of rank $n$. The images of the free generators of $F_n$ form a basis of $G$, since any function on them lifts to a homomorphism of $F_n$ and descends via the abelianizer (Theorem 4.4).

($\Leftarrow$) If $G$ has a basis $E$, construct a free abelian group $A$ on the set $E$. The inclusion $E \to A$ extends to a homomorphism $G \to A$, and the inclusion $E \to G$ extends to $A \to G$. These are mutual inverses, so $G \cong A$.
