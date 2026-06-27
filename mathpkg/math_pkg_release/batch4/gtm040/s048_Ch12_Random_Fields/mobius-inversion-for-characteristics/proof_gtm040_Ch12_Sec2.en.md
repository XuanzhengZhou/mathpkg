---
role: proof
locale: en
of_concept: mobius-inversion-for-characteristics
source_book: gtm040
source_chapter: "12"
source_section: "2. Gibbs fields"
---
Assume that the first condition holds. Then

$$\sum_{B \subset A} \Phi(B) = \sum_{B \subset A} \sum_{D \subset B} (-1)^{|B-D|} \Psi(D)$$

$$= \sum_{D \subset A} \Psi(D) \left[ \sum_{E \subset A-D} (-1)^{|E|} \right] \quad (E = B - D)$$

$$= \Psi(A),$$

since the bracketed sum above is $1$ if $D = A$ and $0$ otherwise. The opposite implication is verified by an analogous computation.
