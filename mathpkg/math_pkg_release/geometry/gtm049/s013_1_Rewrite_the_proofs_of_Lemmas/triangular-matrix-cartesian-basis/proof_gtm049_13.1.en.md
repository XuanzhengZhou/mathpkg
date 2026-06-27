---
role: proof
locale: en
of_concept: triangular-matrix-cartesian-basis
source_book: gtm049
source_chapter: "13"
source_section: "13.1"
---

By the previous proposition (Exercise 3, first part), there exists a linear mapping $f \colon W \to W$ such that $\sigma(af, b) = \tau(a, b)$ for all $a, b \in W$. Since $W$ is a finite dimensional complex vector space, $f$ admits an upper triangular matrix with respect to some basis of $W$. Applying the Gram–Schmidt process to this basis yields a cartesian (orthonormal) basis of $(W, \sigma)$. With respect to this cartesian basis, the matrix of $f$ remains triangular (the change-of-basis from a triangular to a cartesian basis via Gram–Schmidt preserves triangularity). The matrix of $\tau$ in this cartesian basis is then the matrix of $f$, which is triangular. (This is left as Exercise 3 in the source text.)
