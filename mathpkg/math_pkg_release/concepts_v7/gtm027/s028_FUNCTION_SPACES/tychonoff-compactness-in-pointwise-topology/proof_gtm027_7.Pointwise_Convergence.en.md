---
role: proof
locale: en
of_concept: tychonoff-compactness-in-pointwise-topology
source_book: gtm027
source_chapter: "7"
source_section: "Pointwise Convergence"
---

# Proof of Compactness Criterion for Pointwise Topology

**Theorem 1.** Let $F$ be a family of functions, each on a set $X$ to a topological space $Y$. Then $F$ is compact relative to the topology of pointwise convergence if and only if:

(a) $F$ is pointwise closed; that is, $F$ is a closed subset of the product space $Y^X$;

(b) for each $x \in X$, the closure of $F[x] = \{f(x) : f \in F\}$ in $Y$ is compact.

If $Y$ is a Hausdorff space and $F$ is compact relative to the pointwise topology, then $F[x]$ is compact (and closed) for each $x \in X$, because the evaluation map $e_x$ is continuous and maps the compact space $F$ into the Hausdorff space $Y$.

*Proof.* This is an immediate consequence of the Tychonoff theorem (5.13) on the product of compact spaces.

*Sufficiency.* Assume that $F$ is pointwise closed and that for each $x \in X$, the closure $\overline{F[x]}$ in $Y$ is compact. By the Tychonoff theorem, the product space

\[
K = \prod_{x \in X} \overline{F[x]}
\]

is compact. Since $f(x) \in F[x] \subset \overline{F[x]}$ for every $f \in F$ and $x \in X$, we have $F \subset K$. The hypothesis that $F$ is pointwise closed means that $F$ is closed in $Y^X$; a fortiori $F$ is closed in the relative topology of $K$. A closed subset of a compact space is compact, hence $F$ is compact in the pointwise topology.

*Necessity.* Suppose $F$ is compact in the pointwise topology. Then $F$ is compact as a subset of $Y^X$. If $Y$ is Hausdorff, then the product $Y^X$ is Hausdorff, so by Theorem 5.7 the compact subset $F$ is closed in $Y^X$; this establishes condition (a). For each $x \in X$, the evaluation map $e_x : F \to Y$, defined by $e_x(f) = f(x)$, is continuous relative to the pointwise topology (Theorem 3.2). The continuous image of a compact space is compact, so $F[x] = e_x(F)$ is compact. In a Hausdorff space $Y$, a compact subset is necessarily closed, hence $F[x]$ is closed as well. This establishes condition (b).

In the general case where $Y$ is not necessarily Hausdorff, the closure $\overline{F[x]}$ (taken in $Y$) of the continuous image of a compact set is also compact, which gives the required form of condition (b). $\square$