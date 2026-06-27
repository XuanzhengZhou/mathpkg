---
role: proof
locale: en
of_concept: ambient-tubular-neighborhood-theorem
source_book: gtm033
source_chapter: "8"
source_section: "1. Isotopy"
---

# Proof of Ambient Tubular Neighborhood Theorem

**Theorem 1.8.** Let $A \subset M$ be a closed neat submanifold and let $U \subset M$ be a neighborhood of $A$. Then the $A$-germ of any isotopy of tubular neighborhoods of $A$ extends to a diffeotopy of $M$ having support in $U$.

*Proof.* Since an isotopy of tubular neighborhoods leaves $A$ pointwise fixed, in some neighborhood of $A$ it has bounded velocity. Indeed, near $A$ the isotopy moves points along the fibers of the tubular neighborhood by linear maps, which can be arranged to have bounded derivatives. Therefore, we can apply Theorem 1.7 with the open neighborhood being the tubular neighborhood and the closed set being $A$ itself (which is neat, hence closed). Theorem 1.7 provides a diffeotopy $G$ of $M$ having bounded velocity, which agrees with the given isotopy on a neighborhood of $A$, and whose support is contained in the image of the isotopy (hence in $U$). $\square$
