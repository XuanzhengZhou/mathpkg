---
role: proof
locale: en
of_concept: embedding-density-weak-topology
source_book: gtm033
source_chapter: "2. Function Spaces"
source_section: "2.1"
---

# Proof of Density of Embeddings in the Weak Topology (Proposition 1.0)

**Proposition 1.0.** Let $M$ be a compact $C^r$ manifold, $2 \leqslant r \leqslant \infty$. Then embeddings are dense in $C^r_W(M, \mathbb{R}^q)$ if $q > 2 \dim M$, while immersions are dense if $q \geqslant 2 \dim M$.

*Proof.* This proposition is an immediate consequence of the Easy Whitney Embedding Theorem (Theorem 1.3.5) together with the approximation argument given in the proof of that theorem. Let us reexamine the proof.

Theorem 1.3.5 states that every compact $C^r$ $n$-manifold $M$ can be $C^r$ embedded in $\mathbb{R}^{2n+1}$, and immersed in $\mathbb{R}^{2n}$. The proof of that theorem proceeds by taking an arbitrary $C^r$ map $f: M \to \mathbb{R}^q$ (with $q > 2n$ or $q \geqslant 2n$ respectively) and showing that it can be approximated by an embedding (or immersion) by projecting along a suitably chosen direction $v \in S^{q-1}$.

Specifically, given any $C^r$ map $f: M \to \mathbb{R}^q$, a projection $\pi_v: \mathbb{R}^q \to \mathbb{R}^{q-1}$ (orthogonal projection along $v$) is chosen such that $\pi_v \circ f$ is an embedding (or immersion). The direction $v$ is chosen to avoid:
1. The secant map $\sigma: M \times M - \Delta \to S^{q-1}$ (for injectivity),
2. The unit tangent bundle map $\tau: T_1M \to S^{q-1}$ (for immersion).

Both conditions are satisfied for almost every $v \in S^{q-1}$ by Sard's theorem (or the nowhere-dense lemma), since $\dim(M \times M - \Delta) = 2n < q-1$ and $\dim T_1M = 2n-1 < q-1$ when $q > 2n$ (or $q \geqslant 2n$ for immersions).

Since one can also make the projection $\pi_v$ arbitrarily close to the identity by choosing $v$ close to a coordinate axis, the composition $\pi_v \circ f$ is $C^r_W$-close to $f$. As this construction works starting from any $f$, embeddings (respectively immersions) are dense in $C^r_W(M, \mathbb{R}^q)$ under the stated dimension conditions.

$\square$

**Remark.** The restriction $r \geqslant 2$ in the statement comes from the need for the map $\tau: T_1M \to S^{q-1}$ to be at least $C^1$, so that Sard's theorem applies. The secant map $\sigma$ requires $M$ to be at least $C^2$ as well.
