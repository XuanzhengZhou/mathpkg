---
role: proof
locale: en
of_concept: identity-baire-implies-separable
source_book: gtm018
source_chapter: "64"
source_section: "Weil Topology"
---

**Theorem F.** Let $\{U_n\}$ be a sequence of bounded open sets such that $\{e\} = \bigcap_{n=1}^{\infty} U_n$; we may assume without loss of generality that

$$\overline{U}_{n+1} \subset U_n, \quad n = 1, 2, \dots.$$

There exists a sequence $\{C_i\}$ of compact sets such that $X = \bigcup_{i=1}^{\infty} C_i$; since each $C_i$ is compact, there exists, for each $i$ and $n$, a finite subset $\{x_{ij}^{(n)}\}$ of $C_i$ such that $C_i \subset \bigcup_j x_{ij}^{(n)} U_n$. We shall prove that the countable class $\{x_{ij}^{(n)} U_n\}$ is a base.

We prove first that if $U$ is any neighborhood of $e$, then there exists a positive integer $n$ such that $e \in U_n \subset U$. This follows from the fact that $\{e\} = \bigcap U_n$, the compactness argument using $\overline{U}_{n+1} \subset U_n$, and the finite intersection property. The countable class of translates $\{x_{ij}^{(n)} U_n\}$ then forms a countable base for the topology of $X$, proving that $X$ is separable. $\blacksquare$
