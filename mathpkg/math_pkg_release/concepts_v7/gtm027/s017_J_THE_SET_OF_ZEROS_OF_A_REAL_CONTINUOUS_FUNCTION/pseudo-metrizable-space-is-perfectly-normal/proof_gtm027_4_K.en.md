---
role: proof
locale: en
of_concept: pseudo-metrizable-space-is-perfectly-normal
source_book: gtm027
source_chapter: "4"
source_section: "K"
---

# Proof of Theorem K(a): Every pseudo-metrizable space is perfectly normal

**Theorem.** Each pseudo-metrizable topological space is perfectly normal.

**Proof.** Let $d$ be a pseudo-metric on $X$ that induces the topology. Recall that in a pseudo-metric space, the distance from a point $x$ to a set $B$ is defined by

$$d(x, B) = \inf\{d(x, b) : b \in B\},$$

and $x \mapsto d(x, B)$ is continuous for any non-empty $B \subset X$. Moreover, if $B$ is closed, then $d(x, B) = 0$ if and only if $x \in B$.

**Step 1: $X$ is normal.** Let $A$ and $B$ be disjoint closed subsets of $X$. Define $f: X \to \mathbb{R}$ by

$$f(x) = \frac{d(x, A)}{d(x, A) + d(x, B)}.$$

The denominator is never zero: if $d(x, A) + d(x, B) = 0$, then $d(x, A) = d(x, B) = 0$, which would imply $x \in A \cap B$ (since $A$ and $B$ are closed), contradicting $A \cap B = \varnothing$. Since $x \mapsto d(x, A)$ and $x \mapsto d(x, B)$ are continuous, $f$ is continuous as a quotient of continuous functions with a non-vanishing denominator.

For $x \in A$, $d(x, A) = 0$, so $f(x) = 0$. For $x \in B$, $d(x, B) = 0$, so $f(x) = 1$. The sets $U = f^{-1}[(-\infty, 1/2)]$ and $V = f^{-1}[(1/2, \infty)]$ are disjoint open neighborhoods of $A$ and $B$ respectively. Thus $X$ is normal.

**Step 2: Every closed set is a $G_\delta$.** Let $C$ be a closed subset of $X$. For each positive integer $n$, define

$$U_n = \{x \in X : d(x, C) < 1/n\}.$$

The function $x \mapsto d(x, C)$ is continuous, so each $U_n = d(\cdot, C)^{-1}[(-\infty, 1/n)]$ is open. Clearly $C \subset U_n$ for all $n$, so

$$C \subset \bigcap_{n=1}^{\infty} U_n.$$

Conversely, if $x \in \bigcap_{n=1}^{\infty} U_n$, then $d(x, C) < 1/n$ for all $n$, so $d(x, C) = 0$. Since $C$ is closed, this implies $x \in C$. Hence

$$C = \bigcap_{n=1}^{\infty} U_n,$$

which expresses $C$ as a countable intersection of open sets, i.e., a $G_\delta$ set.

Since $X$ is normal and every closed subset is a $G_\delta$, $X$ is perfectly normal by definition. $\square$
