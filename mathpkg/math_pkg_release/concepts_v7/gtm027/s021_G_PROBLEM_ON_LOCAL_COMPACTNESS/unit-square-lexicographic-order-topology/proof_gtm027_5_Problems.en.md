---
role: proof
locale: en
of_concept: unit-square-lexicographic-order-topology
source_book: gtm027
source_chapter: "5"
source_section: "Problems"
---

# Proof of Properties of the Unit Square with Lexicographic Order Topology

Let $Q = [0,1]$ be the closed unit interval. Let $X = Q \times Q$ be ordered by the dictionary (lexicographic) order: $(a,b) < (c,d)$ if and only if $a < c$ or ($a = c$ and $b < d$). Endow $X$ with the order topology.

**Proposition.** The space $X$ is compact, connected, Hausdorff, satisfies the first axiom of countability, but is not separable and is hence not metrizable.

**Proof.**

1. *Hausdorff.* Every order topology is Hausdorff: for $(a,b) < (c,d)$, if $a < c$, choose $a < r < c$; then the open intervals $[0, (r,0))$ and $((r,1), (1,1)]$ separate the two points. If $a = c$ and $b < d$, choose $b < s < d$; then the intervals $[0, (a,s))$ and $((a,s), (1,1)]$ separate them.

2. *Compact.* $X$ is a linearly ordered set. A linearly ordered set with the order topology is compact if and only if it is complete (every subset has a supremum and infimum) and has both a least and greatest element. $X$ has least element $(0,0)$ and greatest element $(1,1)$. For completeness: any nonempty subset $S \subset X$ has $a_0 = \sup\{a : \exists b, (a,b) \in S\}$ in $[0,1]$. If $S$ has points with first coordinate $a_0$, let $b_0 = \sup\{b : (a_0,b) \in S\}$; then $\sup S = (a_0, b_0)$. Otherwise $\sup S = (a_0, 0)$. Thus $X$ is complete and hence compact.

3. *Connected.* As a complete linearly ordered set with the order topology, $X$ is a linear continuum (it is dense in itself and complete). Every linear continuum is connected in the order topology.

4. *First countable.* For a point $(a,b) \in X$, a local basis is given by the intervals $((a, b - 1/n), (a, b + 1/n))$ for points not of the form $(a,0)$ or $(a,1)$, and by endpoints-appropriate variants. Each basis is countable, so $X$ satisfies the first axiom of countability.

5. *Not separable.* For each $x \in [0,1]$, the vertical "line" $\{(x, y) : y \in [0,1]\}$ contains uncountably many disjoint open intervals (e.g., the intervals between $(x, y)$ and $(x, y')$ for $y < y'$). Any dense subset must intersect each such open interval, hence must be uncountable. Therefore $X$ is not separable. Since every metrizable space is first-countable and separable (for compact metric spaces, separability is automatic), $X$ cannot be metrizable.
