---
role: proof
locale: en
of_concept: model-surface-classification
source_book: gtm033
source_chapter: "9"
source_section: "1"
---

# Proof of Theorem 1.9 (Classification of Model Surfaces)

Two model surfaces are diffeomorphic if and only if they have the same genus, the same Euler characteristic, and the same orientability (both orientable or both nonorientable), and the same number of boundary components.

**Proof.** Let $M, N$ be model surfaces. If they are diffeomorphic, then clearly they have the same genus, orientability, and number of boundary components; their Euler characteristics are equal because the Euler characteristic is a diffeomorphism invariant.

Conversely, suppose $M$ and $N$ have the same genus $g$, the same number $b$ of boundary components, and both are orientable or both are nonorientable.

If both are orientable, then $\chi(M) = 2 - 2g - b = \chi(N)$. Induction on $p$ and Theorem 1.4(c) shows that two orientable surfaces of the same genus (with the same number of boundary disks removed) are diffeomorphic.

If both are nonorientable, then $\chi(M) = 2 - g - b = \chi(N)$. Theorem 1.6 (applied to the surfaces without boundary obtained by capping off the boundary circles) implies that $M \approx N$.

Thus in all cases, $M$ and $N$ are diffeomorphic. $\square$
