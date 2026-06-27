---
role: proof
locale: en
of_concept: nonorientable-submanifold-does-not-separate
source_book: gtm033
source_chapter: "4"
source_section: "4. Oriented Vector Bundles"
---

# Proof of Theorem 4.6 (Nonorientable Submanifold Does Not Separate)

Let $N$ be a simply connected manifold and let $M \subset N$ be a closed connected submanifold of codimension $1$, with $\partial M = \partial N = \varnothing$. Assume $M$ is nonorientable. Then $M$ does not separate $N$.

**Proof.** We prove the contrapositive: if $M$ separates $N$, then $M$ must be orientable.

Suppose $M$ separates $N$. Since $N$ is simply connected, $N$ is orientable. (Every simply connected manifold is orientable: the fundamental group acts trivially on the orientation double cover, so the double cover is disconnected, yielding a global section, i.e., an orientation.)

Now apply Theorem 4.5: $N$ is simply connected (hence orientable), $M$ is a closed connected submanifold of codimension $1$ with empty boundaries, and $M$ separates $N$. Theorem 4.5 then asserts that $M$ is orientable.

Thus the assumption that $M$ separates $N$ forces $M$ to be orientable. Consequently, a nonorientable $M$ cannot separate $N$.

**Remark.** This theorem is a fundamental obstruction result in the topology of manifolds: nonorientable hypersurfaces in simply connected manifolds never separate the ambient space. Together with Theorem 4.5, it shows that for codimension-1 closed connected submanifolds of simply connected manifolds, the properties "separating" and "orientable" are equivalent.

QED
