---
role: proof
locale: en
of_concept: periodic-automorphisms-first-category
source_book: gtm002
source_chapter: "18"
source_section: "Transitive Transformations"
---

Let $M$ be the space of measure-preserving automorphisms of the unit square with the uniform metric. For positive integers $i$ and $j$, define $P_{ij}$ as the set of $T \in M$ for which there exists a closed disk $D$ of radius at most $1/i$ such that for some positive integer $k$ dividing $j$, the sets $D, T(D), \ldots, T^{k-1}(D)$ are pairwise disjoint and $T^k$ is the identity on $D$.

**Step 1: Each $P_{ij}$ is nowhere dense.**

Let $T \in P_{ij}$ with associated disk $D$ and integer $k \mid j$. We construct an automorphism $S$ arbitrarily close to $T$ such that $S \notin P_{ij}$. Let $S$ be a measure-preserving automorphism of the square that rotates some annulus concentric with $D$ through an irrational multiple of $\pi$ and equals the identity outside $D$. Then no point of this annulus is periodic under $S \circ T$, since an irrational rotation composed with a map that is identity on $D$ cannot produce periodic behavior on the annulus. Hence $S \circ T \notin P_{ij}$, and $\varrho(S \circ T, T)$ can be made arbitrarily small by taking the annulus sufficiently thin. This shows that no open neighborhood of $T$ is contained in $P_{ij}$, hence $P_{ij}$ is nowhere dense.

**Step 2: $P = \bigcup_{i,j} P_{ij}$ is of first category.**

Since each $P_{ij}$ is nowhere dense, their countable union $P$ is of first category in $M$.

**Step 3: Characterization of $M \setminus P$.**

The complement $M \setminus P$ is residual in $M$. If $T \in M \setminus P$, then $T \notin P_{ij}$ for all $i, j$. This means that for every non-empty open set $U$ in the square, $T$ does not have periodic behavior on all points of any small disk within $U$. Equivalently, $T$ has nonperiodic points in every non-empty open subset of the square.
