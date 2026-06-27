---
role: proof
locale: en
of_concept: compact-jointly-continuous-implies-evenly-continuous
source_book: gtm027
source_chapter: "7"
source_section: "Even Continuity"
---

# Proof of Theorem 7.20 — Compactness under Jointly Continuous Topology Implies Even Continuity

Let $F$ be a family of continuous functions on $X$ to a regular Hausdorff space $Y$, compact relative to a jointly continuous topology.

First, the identity map from $(F, \text{compact topology})$ to $(F, \wp)$ is continuous (since the given topology contains $\wp$). As a continuous bijection from a compact space to a Hausdorff space, it is a homeomorphism. Hence the given topology coincides with $\wp$, and $\wp$ is jointly continuous.

Now let $x \in X$, $y \in Y$, and let $U$ be an open neighborhood of $y$. Choose a closed neighborhood $W$ of $y$ with $W \subset U$ (using regularity of $Y$). Define

$$K = \{f \in F : f(x) \in W\},$$

which is $\wp$-closed (hence $\wp$-compact since $F$ is $\wp$-compact). Let $P(f, x) = f(x)$. The compact set $K \times \{x\}$ is contained in $P^{-1}[U]$ because for $f \in K$, $P(f, x) = f(x) \in W \subset U$. Since $P$ is continuous, by Theorem 5.12 (tube lemma for compact sets), there exists a neighborhood $V$ of $x$ such that $K \times V \subset P^{-1}[U]$.

Thus: if $f(x) \in W$ and $v \in V$, then $f(v) \in U$. This is precisely the definition of even continuity for $F$.
