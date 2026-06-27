---
role: proof
locale: en
of_concept: helly-space-first-countability
source_book: gtm027
source_chapter: "5"
source_section: "Problems"
---

# Proof that the Helly Space Satisfies the First Axiom of Countability

Let $H$ be the Helly space of all non-decreasing functions $f : [0,1] \to [0,1]$ with the topology of pointwise convergence.

**Theorem.** $H$ satisfies the first axiom of countability and is hence sequentially compact.

**Proof.**

*First countability.* By definition, the product topology on $Q^Q$ has as a subbasis the sets
\[
S(x, U) = \{f \in Q^Q : f(x) \in U\}
\]
for $x \in Q$ and $U \subset Q$ open. A local basis at a point $f \in Q^Q$ in the product topology is given by restricting to basic open sets where finitely many coordinates are constrained.

For $f \in H$, consider the collection of neighborhoods obtained by restricting the function values at a countable dense subset of $Q$. Let $D \subset Q$ be the set of rational points in $[0,1]$, which is countable. For each finite subset $\{x_1, \ldots, x_n\} \subset D$ and each $\varepsilon \in \{\frac{1}{k} : k \in \mathbb{N}\}$, define
\[
U(f; x_1, \ldots, x_n; \varepsilon) = \{h \in H : |h(x_i) - f(x_i)| < \varepsilon \text{ for } i = 1, \ldots, n\}.
\]

This collection is countable (countably many choices of finite subsets of the countable set $D$, and countably many choices of $\varepsilon$). We claim it forms a local basis at $f$ in $H$.

Any basic open neighborhood of $f$ in $H$ has the form
\[
V = \{h \in H : |h(y_j) - f(y_j)| < \delta \text{ for } j = 1, \ldots, m\}
\]
for some finite set $\{y_1, \ldots, y_m\} \subset Q$ and $\delta > 0$. Since $D$ is dense in $Q$, for each $y_j$ we can choose rational points $r_j^-, r_j^+ \in D$ with $r_j^- \leq y_j \leq r_j^+$ and such that for any non-decreasing function $h$, the values $h(r_j^-)$ and $h(r_j^+)$ constrain $h(y_j)$.

Choose $\varepsilon > 0$ small enough and rational points close enough so that the conditions $|h(r_j^\pm) - f(r_j^\pm)| < \varepsilon$ imply $|h(y_j) - f(y_j)| < \delta$ for all $j$, using the monotonicity of $h$ and the continuity of $f$ at the rational approximations. Then the corresponding neighborhood from our countable family is contained in $V$.

Thus $H$ is first countable.

*Sequential compactness.* Since $H$ is compact Hausdorff (proved in Problem 5.M(a)) and first countable, it follows that $H$ is sequentially compact: in a first countable compact space, every sequence has a convergent subsequence. (Proof: If $H$ is compact and first countable, for any sequence $(f_n)$, consider the decreasing family of closed sets $F_k = \overline{\{f_n : n \geq k\}}$; the intersection $\bigcap_k F_k$ is nonempty by compactness, and any point in the intersection is a cluster point of the sequence; first countability then yields a convergent subsequence.)

Alternatively, one may construct the subsequence directly using the countable local basis at each point.
