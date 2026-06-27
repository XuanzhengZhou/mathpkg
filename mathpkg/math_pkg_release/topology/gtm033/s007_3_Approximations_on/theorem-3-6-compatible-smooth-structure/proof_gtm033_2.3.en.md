---
role: proof
locale: en
of_concept: theorem-3-6-compatible-smooth-structure
source_book: gtm033
source_chapter: "2"
source_section: "3. Approximations on ∂-Manifolds and Manifold Pairs"
---

# Proof of Theorem 3.6: Compatible Smooth Structure on Manifold Pairs

**Theorem 3.6.** Let $(M,M_0)$ be a $C^r$ manifold pair. If $0 < r < s \leqslant \infty$ then $(M,M_0)$ has a compatible $C^s$ structure (that is, $(M,M_0)$ is $C^r$ diffeomorphic to a $C^s$ manifold pair). If also $M_0$ is closed in $M$, and $M_0 \subset M - \partial M$ or $M_0 \subset \partial M$ or $M_0$ is neat, then the compatible $C^s$ structure is unique up to $C^r$ diffeomorphism of manifold pairs.

*Proof.* The proof follows by adapting the proofs of Theorems 2.12, 2.13, and 2.14 to $\partial$-manifolds. The key ingredients are:

1. **Existence** (adaptation of Theorem 2.12): The convolution-based approximation constructed in Lemma 3.2 provides a $C^\infty$ approximation to the identity on halfspaces. Using partitions of unity and the atlas of $(M,M_0)$, one constructs a $C^s$ atlas on $M$ compatible with the $C^r$ structure, such that $M_0$ remains a $C^s$ submanifold in the appropriate sense (closed, boundary, or neat).

2. **Uniqueness** (adaptation of Theorems 2.13, 2.14): Given two compatible $C^s$ structures on $(M,M_0)$, the identity map is $C^r$. One constructs a $C^s$ diffeomorphism between the two structures by smoothing the identity relative to $M_0$, using the density result of Lemma 3.2 and the relative approximation theorems for manifold pairs.

The key technical point is that the convolution kernel factorizes as $\theta(x,y) = \alpha(x)\beta(y)$, ensuring that the boundary condition ($M_0 \subset \partial M$ or $M_0$ is neat) is preserved by the smoothing process.

QED
