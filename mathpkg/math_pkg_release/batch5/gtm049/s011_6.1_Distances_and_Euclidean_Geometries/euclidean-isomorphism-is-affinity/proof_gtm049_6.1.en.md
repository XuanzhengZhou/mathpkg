---
role: proof
locale: en
of_concept: euclidean-isomorphism-is-affinity
source_book: gtm049
source_chapter: "VI"
source_section: "6.1"
---

Suppose $\dim S \geq 2$ and that $M, M'$ are the subspaces belonging to the cosets $S, S'$, respectively. By Theorem 5 of Chapter II, every distance-preserving bijection between Euclidean geometries is an affine map, hence an affinity. Its underlying linear map $f: M \to M'$ must preserve the bilinear form because, for any $a, b \in M$, the distance condition

$$d(a, b) = d'(af, bf)$$

implies $\sigma(a-b, a-b) = \sigma'((a-b)f, (a-b)f)$. By polarization (using the parallelogram law D.6), this extends to $\sigma(a, b) = \sigma'(af, bf)$ for all $a, b$. Hence $f$ is an isomorphism of the Euclidean spaces $(M, \sigma)$ and $(M', \sigma')$.
