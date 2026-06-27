---
role: proof
locale: en
of_concept: closed-compact-neighborhood-base
source_book: gtm027
source_chapter: "5"
source_section: "Locally Compact Spaces"
---

# Proof of Closed Compact Neighborhoods Form a Base (Theorem 17)

Let $X$ be a locally compact topological space which is either Hausdorff or regular.

Let $x$ be a point of $X$, let $C$ be a compact neighborhood of $x$, and let $U$ be an arbitrary neighborhood of $x$. We construct a closed compact neighborhood $V$ of $x$ such that $V \subset U$.

**Case 1: $X$ is regular.** Since $X$ is regular, there exists a closed neighborhood $V$ of $x$ which is a subset of the intersection $U \cap C^0$, where $C^0$ denotes the interior of $C$. Evidently $V$ is a closed subset of the compact set $C$, hence $V$ is compact. Thus $V$ is a closed compact neighborhood of $x$ contained in $U$.

**Case 2: $X$ is Hausdorff.** Let $W = (U \cap C)^0$ be the interior of $U \cap C$. Since $C$ is compact and $X$ is Hausdorff, $C$ is closed (by Theorem 5.4), and the closure $W^-$ is a subset of the compact set $C$. Hence $W^-$ is a compact Hausdorff space. By Theorem 5.9 (a compact Hausdorff space is regular), $W$ contains a closed compact set $V$ which is a neighborhood of $x$ in the subspace $W^-$. But $V$ is also a neighborhood of $x$ in $W$ (with respect to the relativized topology for $W$), and therefore $V$ is a neighborhood of $x$ in $X$.

In both cases, we have produced a closed compact neighborhood $V$ of $x$ contained in the given neighborhood $U$. Hence the family of closed compact neighborhoods of $x$ forms a base for the neighborhood system of $x$. $\square$
