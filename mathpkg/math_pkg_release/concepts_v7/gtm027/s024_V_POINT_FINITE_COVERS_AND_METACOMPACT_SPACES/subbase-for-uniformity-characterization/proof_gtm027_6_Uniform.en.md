---
role: proof
locale: en
of_concept: subbase-for-uniformity-characterization
source_book: gtm027
source_chapter: "6"
source_section: "Uniform Spaces"
---

# Proof of Characterization of a Subbase for a Uniformity (Theorem 6.3)

**Theorem 6.3.** A family $\mathcal{S}$ of subsets of $X \times X$ is a subbase for some uniformity for $X$ if

(a) each member of $\mathcal{S}$ contains the diagonal $\Delta$,

(b) for each $U$ in $\mathcal{S}$ the set $U^{-1}$ contains a member of $\mathcal{S}$, and

(c) for each $U$ in $\mathcal{S}$ there is $V$ in $\mathcal{S}$ such that $V \circ V \subset U$.

In particular, the union of any collection of uniformities for $X$ is the subbase for a uniformity for $X$.

**Proof.** It must be shown that the family $\mathcal{B}$ of finite intersections of members of $\mathcal{S}$ satisfies the conditions of Theorem 6.2 (characterization of a base for a uniformity).

This follows from the following observation: if $U_1, \ldots, U_n$ and $V_1, \ldots, V_n$ are subsets of $X \times X$, if $U = \bigcap \{U_i : i = 1, \ldots, n\}$ and $V = \bigcap \{V_i : i = 1, \ldots, n\}$, then $V \subset U^{-1}$ (or $V \circ V \subset U$) whenever $V_i \subset U_i^{-1}$ (respectively, $V_i \circ V_i \subset U_i$) for each $i$.

Indeed, the diagonal is in each member of $\mathcal{S}$ so it is in each finite intersection. For inverses: given $U_i$ choose $V_i \in \mathcal{S}$ with $V_i \subset U_i^{-1}$, then $\bigcap V_i \subset (\bigcap U_i)^{-1}$. For composition: given $U_i$ choose $V_i \in \mathcal{S}$ with $V_i \circ V_i \subset U_i$, then $(\bigcap V_i) \circ (\bigcap V_i) \subset \bigcap (V_i \circ V_i) \subset \bigcap U_i$.

Thus $\mathcal{B}$ satisfies the conditions of Theorem 6.2 and hence is a base for a uniformity $\mathcal{U}$, making $\mathcal{S}$ a subbase for $\mathcal{U}$.
