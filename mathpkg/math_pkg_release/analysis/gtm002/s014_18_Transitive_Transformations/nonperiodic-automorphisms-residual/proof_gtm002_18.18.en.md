---
role: proof
locale: en
of_concept: nonperiodic-automorphisms-residual
source_book: gtm002
source_chapter: "18"
source_section: "18"
---

Let $M$ be the space of all measure-preserving automorphisms of the unit square $X = [0,1]^2$ with the uniform metric. For each pair of basic open sets $U_i, U_j$ (from a fixed countable base) and each positive integer $k$, let $P_{ij}^k$ be the set of all $T \in M$ for which there exists a closed disk $D \subseteq U_i$ such that the sets $D, T(D), \ldots, T^{k-1}(D)$ are disjoint and $T^k$ equals the identity on $D$. Define

$$P_{ij} = \bigcup_{k=1}^{\infty} P_{ij}^k, \qquad P = \bigcup_{i,j} P_{ij}.$$

The set $P$ consists of those measure-preserving automorphisms that have a periodic point in some nonempty open set.

To show $P_{ij}$ is nowhere dense in $M$, let $T \in M$ and $\varepsilon > 0$. Within $U_j$, select a closed disk $D$ with arbitrarily small radius and a positive integer $k$ dividing $j$ such that $D, T(D), \ldots, T^{k-1}(D)$ are disjoint and $T^k = \text{id}$ on $D$. Construct a measure-preserving automorphism $S$ that rotates some annulus concentric with $D$ through an irrational multiple of $\pi$ and equals the identity outside $D$. Then no point of this annulus is periodic under $S \circ T$. Hence $S \circ T \in M - P_{ij}$, while $\varrho(S \circ T, T)$ is arbitrarily small. Therefore $P_{ij}$ is nowhere dense in $M$, and consequently $P$ is of first category in $M$.

The complement $M - P$ is thus residual. Every $T \in M - P$ fails to belong to any $P_{ij}$, meaning that in every nonempty open subset $U$ of $X$, $T$ has no points that are periodic and belong to a set on which some iterate of $T$ acts as the identity. Equivalently, every $T \in M - P$ has nonperiodic points in every nonempty open subset of $X$. By Theorem 17.3 (Poincaré recurrence), the set of recurrent points under any $T \in M$ is residual in $X$; since nonperiodic points also form a residual set (being the complement of the countable union of fixed-point sets of iterates), the intersection of recurrent and nonperiodic points is residual in $X$ for each $T \in M - P$. Thus the automorphisms with nonperiodic points in every open set form a residual set in $M$.
