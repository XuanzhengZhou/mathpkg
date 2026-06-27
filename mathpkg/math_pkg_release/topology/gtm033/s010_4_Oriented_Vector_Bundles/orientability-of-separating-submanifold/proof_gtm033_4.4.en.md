---
role: proof
locale: en
of_concept: orientability-of-separating-submanifold
source_book: gtm033
source_chapter: "4"
source_section: "4. Oriented Vector Bundles"
---

# Proof of Theorem 4.5 (Orientability of Separating Codimension-1 Submanifold)

Let $N$ be a simply connected manifold and let $M \subset N$ be a closed connected submanifold of codimension $1$, with $\partial M = \partial N = \varnothing$. Assume that $M$ separates $N$. If $N$ is orientable, then $M$ is orientable.

**Proof.** Since $M$ separates the connected manifold $N$, Lemma 4.4 implies that the normal bundle $\nu$ of $M$ in $N$ is trivial. A trivial vector bundle is always orientable (it admits the constant standard orientation in any global trivialization).

Restrict the tangent bundle of $N$ to $M$. There is a natural short exact sequence of vector bundles over $M$:

$$0 \longrightarrow TM \longrightarrow TN|_M \longrightarrow \nu \longrightarrow 0.$$

Here the first map is the inclusion of the tangent bundle of the submanifold, and the second map is the quotient projection onto the algebraic normal bundle $\nu = TN|_M / TM$.

Now we apply Lemma 4.1 (the short exact sequence lemma for orientations):

- $TN|_M$, the restriction of the tangent bundle of $N$ to $M$, is orientable because $N$ is orientable (an orientation of $TN$ restricts to an orientation of $TN|_M$).
- $\nu$ is orientable because it is trivial (Theorem 4.2 via Lemma 4.4).

Since $TN|_M$ and $\nu$ are both orientable, Lemma 4.1 implies that the third term $TM$ in the short exact sequence is also orientable. Therefore $M$ is an orientable manifold.

**Remark.** The hypothesis that $N$ is simply connected is not used in the proof given above; orientability of $N$ suffices. In Hirsch's text, the "simply connected" hypothesis appears because any simply connected manifold is automatically orientable, so the theorem is stated with the stronger hypothesis for convenience in applications. The proof is exactly as written, using only that $N$ is orientable.

QED
