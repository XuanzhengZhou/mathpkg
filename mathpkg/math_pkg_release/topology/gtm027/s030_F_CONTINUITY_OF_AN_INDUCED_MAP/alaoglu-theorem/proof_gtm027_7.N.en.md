---
role: proof
locale: en
of_concept: alaoglu-theorem
source_book: gtm027
source_chapter: "7"
source_section: "N"
---

# Proof of Alaoglu Theorem on Weak-Star Compactness of the Unit Sphere

Let $X$ be a normed linear space and $X^*$ its dual. The unit sphere $S^* = \{f \in X^* : \|f\| \leq 1\}$ is compact relative to the $w^*$-topology (the topology of pointwise convergence on $X$).

**Proof.** For each $x \in X$, let $I_x = [-\|x\|, \|x\|] \subseteq \mathbb{R}$. Consider the product space

$$P = \prod_{x \in X} I_x$$

with the product topology. By Tychonoff's theorem, $P$ is compact.

Define the map $\phi : S^* \to P$ by $\phi(f) = (f(x))_{x \in X}$. This is an embedding: the $w^*$-topology on $S^*$ is exactly the topology of pointwise convergence, which is the relativization of the product topology on $P$.

The image $\phi(S^*)$ is a closed subset of $P$. To see this, suppose $\{f_\alpha\}$ is a net in $S^*$ such that $\phi(f_\alpha) \to \xi \in P$. Then for each $x$, $f_\alpha(x) \to \xi_x$. The pointwise limit of linear functionals of norm $\leq 1$ is again linear (by continuity of addition and scalar multiplication) and has norm $\leq 1$. Thus $\xi$ corresponds to an element of $S^*$.

Since $P$ is compact and $\phi(S^*)$ is closed in $P$, $\phi(S^*)$ is compact. As $\phi$ is a homeomorphism onto its image, $S^*$ is compact.

Consequently, each norm-bounded $w^*$-closed subset of $X^*$ is $w^*$-compact (as a closed subset of a sufficiently large scalar multiple of the unit sphere).
