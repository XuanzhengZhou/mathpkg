---
role: proof
locale: en
of_concept: locally-compact-regular-completely-regular
source_book: gtm027
source_chapter: "5"
source_section: "Locally Compact Spaces"
---

# Proof that Locally Compact Regular Spaces are Completely Regular

This follows directly from Theorem 18. Let $X$ be a locally compact regular topological space. To show $X$ is completely regular, we must verify that for any closed subset $A$ of $X$ and any point $x \notin A$, there exists a continuous function $f: X \to [0,1]$ such that $f(x) = 0$ and $f = 1$ on $A$.

First, since $X$ is locally compact and regular, by Theorem 17 each point has a base of closed compact neighborhoods. Let $C$ be a closed compact neighborhood of $x$ disjoint from $A$ (such a neighborhood exists because $X$ is regular and $A$ is closed). Then $C$ is a closed compact set, and $U = X \setminus A$ is an open neighborhood of $C$. By Theorem 18, there exists a closed compact neighborhood $V$ of $C$ contained in $U$, and a continuous function $f: X \to [0,1]$ such that $f = 0$ on $C$ and $f = 1$ on $X \setminus V$. In particular, $f(x) = 0$ and $f = 1$ on $A \subset X \setminus V$. Hence $X$ is completely regular.

For the special case: if $X$ is a locally compact Hausdorff space, then by the corollary to Theorem 17, $X$ is regular. Applying the above, $X$ is completely regular, and since it is Hausdorff, it is a Tychonoff space. $\square$
