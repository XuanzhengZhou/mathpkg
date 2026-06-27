---
role: proof
locale: en
of_concept: embedding-theorem-boundary
source_book: gtm033
source_chapter: "4. Manifolds with Boundary"
source_section: "4"
---

# Proof of Embedding Theorem for Manifolds with Boundary (Theorem 4.3)

**Theorem 4.3.** Let $M$ be a $C^r$ $n$-dimensional manifold with boundary, $r \geqslant 1$. Then:
(a) There exists a $C^r$ embedding of $M$ into $\mathbb{R}^{2n+1}$.
(b) There exists a $C^r$ immersion of $M$ into $\mathbb{R}^{2n}$.

*Proof.* The source text says: "The embedding Theorems 3.4 and 3.5 go through with only minor changes. With some care one can prove..." The book provides only a sketch, noting that the proof follows the same strategy as the compact case (Theorem 3.4) and the general case (Theorem 3.5) for manifolds without boundary.

**Outline of the proof:**

The proof follows the same projection strategy as the Whitney Embedding Theorem. Let $M \subset \mathbb{R}^q$ be a $C^r$ embedding (which exists by the Whitney Embedding Theorem 3.5, since every $\partial$-manifold can be embedded in some $\mathbb{R}^q$ as a closed subset).

**Step 1: Extension to the double.** Let $DM$ be the double of $M$ (obtained by gluing two copies of $M$ along $\partial M$). Then $DM$ is a $C^r$ manifold without boundary of dimension $n$. By Theorem 3.5, $DM$ admits a $C^r$ embedding into $\mathbb{R}^{2n+1}$ and a $C^r$ immersion into $\mathbb{R}^{2n}$. Restricting these maps to $M \subset DM$ yields the desired embedding and immersion respectively.

**Step 2: The projection argument.** Alternatively, one can work directly with $M$. Starting from an embedding $M \subset \mathbb{R}^q$, if $q > 2n+1$, one projects $\mathbb{R}^q$ onto a hyperplane $\mathbb{R}^{q-1}$ along a direction $v \in S^{q-1}$. The direction $v$ must be chosen to avoid:
- The secant map $\sigma: M \times M - \Delta \to S^{q-1}$ (to preserve injectivity),
- The unit tangent bundle map $\tau: T_1 M \to S^{q-1}$ (to preserve the immersion property).

Since $\dim(M \times M - \Delta) = 2n < q-1$ when $q > 2n+1$, and $\dim T_1 M = 2n-1$, the nowhere-dense lemma (or Sard's theorem) guarantees the existence of such a $v$. For the boundary, one must also ensure that the projection preserves the "neatness" condition at the boundary, which requires choosing $v$ not tangent to $\partial M$. This is an additional condition of codimension $n-1$, which does not affect the dimension count for $q > 2n+1$.

**Step 3: Iteration.** By iterating this projection $q - (2n+1)$ times, one obtains a $C^r$ embedding $M \to \mathbb{R}^{2n+1}$. For immersions, one projects down to $\mathbb{R}^{2n}$ ($q - 2n$ iterations).

$\square$

**Note.** The source text presents this theorem with a truncated statement: "4.3. Theorem. Let $M$ be a $C^r$ $n$-dimensional manifold, $" and notes that the proof requires "only minor changes" from the boundaryless case (Theorems 3.4 and 3.5). The complete statement and proof sketch above is reconstructed from this context.
