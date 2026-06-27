---
role: proof
locale: en
of_concept: periodic-points-first-category
source_book: gtm002
source_chapter: "18"
source_section: "18"
---
Let $\{U_i\}$ be a countable base for the square. For positive integers $i$ and $j$, define $P_{ij}$ as the set of all $T \in M$ such that every point of $U_i$ is periodic under $T$ and has period dividing $j$.

To show $P_{ij}$ is nowhere dense, we prove that for any $T \in P_{ij}$ and any $\varepsilon > 0$, there exists $S \in M \setminus P_{ij}$ with $\varrho(S \circ T, T) < \varepsilon$.

Given $T \in P_{ij}$, choose a closed disk $D \subset U_i$ with arbitrarily small radius such that for some positive integer $k$ (a divisor of $j$), the sets $D, T(D), \ldots, T^{k-1}(D)$ are disjoint and $T^k$ is equal to the identity on $D$. (This is possible because all points of $U_i$ have period dividing $j$.)

Let $S$ be a measure-preserving automorphism of $X$ that rotates some annulus concentric with $D$ through an irrational multiple of $\pi$ and is equal to the identity outside $D$. (Such a measure-preserving rotation exists: take polar coordinates about the center of $D$ and rotate the angular coordinate by an irrational multiple of $\pi$ within a small annulus.)

Then no point of this annulus is periodic under $S \circ T$. Indeed, the composition of $T$ (which is periodic with period $k$ on $D$) with the irrational rotation $S$ yields a transformation whose restriction to the annulus has no periodic points, since the rotation angle is an irrational multiple of $\pi$.

Hence $S \circ T \in M \setminus P_{ij}$ and $\varrho(S \circ T, T)$ can be made arbitrarily small by taking the annulus sufficiently thin. This shows that $P_{ij}$ contains no open set, i.e., $P_{ij}$ is nowhere dense in $M$.

Therefore the countable union
$$P = \bigcup_{i,j=1}^{\infty} P_{ij}$$
is of first category in $M$. The complement $M \setminus P$ consists of all measure-preserving automorphisms that have nonperiodic points in every nonempty open subset of the square, since if any open set consisted entirely of periodic points, the automorphism would belong to some $P_{ij}$.
