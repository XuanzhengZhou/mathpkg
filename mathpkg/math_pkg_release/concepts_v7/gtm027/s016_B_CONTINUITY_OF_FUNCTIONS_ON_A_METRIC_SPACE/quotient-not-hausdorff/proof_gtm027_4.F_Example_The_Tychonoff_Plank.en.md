---
role: proof
locale: en
of_concept: quotient-not-hausdorff
source_book: gtm027
source_chapter: "4"
source_section: "F. Example (The Tychonoff Plank) on Subspaces of Normal Spaces"
---

# Proof: A Quotient Space That Is Not Hausdorff

**Statement (b)**: Let $X$ be a topological space, let $A, B \subset X$ be disjoint subsets. Define
$$S = \Delta \cup (A \times A) \cup (B \times B) \subset X \times X,$$
where $\Delta = \{(x, x) : x \in X\}$ is the diagonal. Regard $S$ as an equivalence relation on $X$ (identifying points of $A$ with each other and points of $B$ with each other). Then $S$ is closed in $X \times X$, but the quotient space $X/S$ is not Hausdorff. The members of $X/S$ are the equivalence classes $[A]$, $[B]$, and $\{x\}$ for each $x \in X \setminus (A \cup B)$.

**Proof**:

**$S$ is closed in $X \times X$**:

The diagonal $\Delta$ is closed in $X \times X$ if and only if $X$ is Hausdorff. Assuming $X$ is Hausdorff (as is the case for the Tychonoff Plank $X$), $\Delta$ is closed.

The sets $A \times A$ and $B \times B$ are products of subsets. In the context of the Tychonoff Plank, take $A = \Omega_0 \times \{\Omega\}$ (the "top edge") and $B = \{(x, x) : x \in \Omega_0\}$ (the diagonal). Both $A$ and $B$ are closed subsets of $X$. Then $A \times A$ and $B \times B$ are closed in $X \times X$ (products of closed sets in a product of $T_1$ spaces).

Thus $S = \Delta \cup (A \times A) \cup (B \times B)$ is the union of three closed sets, hence closed in $X \times X$.

**$X/S$ is not Hausdorff**:

In the quotient space $X/S$, consider the two distinct points $[A]$ and $[B]$. We claim that these two points cannot be separated by disjoint open sets.

Let $\pi: X \to X/S$ be the quotient map. Suppose $U$ and $V$ are disjoint open neighborhoods of $[A]$ and $[B]$ respectively in $X/S$. Then $\pi^{-1}(U)$ and $\pi^{-1}(V)$ are disjoint saturated open sets in $X$, with $A \subset \pi^{-1}(U)$ and $B \subset \pi^{-1}(V)$.

Since $A = \Omega_0 \times \{\Omega\}$ consists of points with second coordinate $\Omega$, any neighborhood $\pi^{-1}(U)$ of $A$ must contain points of the form $(x, y)$ with $y$ arbitrarily close to $\Omega$. In particular, for countably many $x$, these neighborhoods intersect the diagonal region.

Similarly, $B = \{(x, x) : x \in \Omega_0\}$ is the diagonal, and any neighborhood $\pi^{-1}(V)$ of $B$ contains open rectangles around each $(x, x)$.

Using the same argument as in parts (d) and (e) of the ordinal space problems: define $f(x)$ as the smallest ordinal larger than $x$ such that $(x, f(x)) \notin \pi^{-1}(U)$. Then $f(x) \geq x$ for all $x$, and by the fixed-point-like theorem (part (d)), there exists $\xi$ such that $(\xi, \xi)$ is an accumulation point of the graph of $f$. This leads to the conclusion that $\pi^{-1}(U)$ and $\pi^{-1}(V)$ must intersect, contradicting disjointness.

Therefore $[A]$ and $[B]$ cannot be separated by disjoint open sets in $X/S$, so $X/S$ is not Hausdorff, even though $S$ is a closed equivalence relation on $X$.
