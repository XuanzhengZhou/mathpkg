---
role: proof
locale: en
of_concept: helly-space-compact-hausdorff
source_book: gtm027
source_chapter: "5"
source_section: "Problems"
---

# Proof that the Helly Space is Compact Hausdorff

Let $Q = [0,1]$ be the closed unit interval. The *Helly space* $H$ is the set of all non-decreasing functions $f : Q \to Q$, i.e.,
\[
H = \{f \in Q^Q : f(a) \leq f(b) \text{ whenever } a \leq b\}.
\]
$H$ is endowed with the relative topology induced by the product topology on $Q^Q$ (which is the topology of pointwise convergence).

**Theorem.** $H$ is compact Hausdorff.

**Proof.**

*Hausdorff.* The product space $Q^Q = \prod_{x \in Q} Q$ is a product of Hausdorff spaces, hence Hausdorff. Any subspace of a Hausdorff space is Hausdorff. Therefore $H$ is Hausdorff.

*Compact.* We show that $H$ is closed in $Q^Q$. Since $Q^Q$ is compact by Tychonoff's theorem (product of compact spaces), any closed subspace is compact.

To see that $H$ is closed, consider the complement. If $g \in Q^Q \setminus H$, then $g$ is not non-decreasing, so there exist points $a, b \in Q$ with $a \leq b$ but $g(a) > g(b)$. Let $\varepsilon = g(a) - g(b) > 0$. Consider the basic open neighborhood of $g$:
\[
U = \{h \in Q^Q : |h(a) - g(a)| < \varepsilon/2 \text{ and } |h(b) - g(b)| < \varepsilon/2\}.
\]
For any $h \in U$, we have $h(a) > g(a) - \varepsilon/2$ and $h(b) < g(b) + \varepsilon/2$, so
\[
h(a) - h(b) > [g(a) - \varepsilon/2] - [g(b) + \varepsilon/2] = g(a) - g(b) - \varepsilon = 0.
\]
Thus $h(a) > h(b)$ for all $h \in U$, so $U$ is an open neighborhood of $g$ entirely disjoint from $H$. Hence $Q^Q \setminus H$ is open, and $H$ is closed.

Therefore $H$, being a closed subspace of the compact Hausdorff space $Q^Q$, is compact Hausdorff.
