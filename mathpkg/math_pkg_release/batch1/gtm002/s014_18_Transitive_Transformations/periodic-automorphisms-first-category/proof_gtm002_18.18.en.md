---
role: proof
locale: en
of_concept: periodic-automorphisms-first-category
source_book: gtm002
source_chapter: "18"
source_section: "18"
---

Let $M$ be the space of all measure-preserving automorphisms of the unit square $X$. For each pair of positive integers $i$ and $j$, define
$$P_{ij} = \{ T \in M : \text{every point of } U_i \text{ is periodic under } T \text{ with period } j \}.$$
Then $P = \bigcup_{i,j} P_{ij}$ (everywhere-periodic automorphisms), so it suffices to show each $P_{ij}$ is nowhere dense in $M$.

Fix $i$, $j$ and $T \in P_{ij}$. Then each point of the basic open set $U_i$ is periodic of period $j$. A point $x \in U_i$ has a period $k$ dividing $j$, and the sets $D, T(D), \ldots, T^{k-1}(D)$ are disjoint for a sufficiently small closed disk $D$ centered at $x$; moreover $T^k$ equals the identity on $D$.

Let $S$ be a measure-preserving automorphism of $X$ that rotates some annulus concentric with $D$ through an irrational multiple of $\pi$ and equals the identity outside $D$. Choose the annulus with arbitrarily small radius so that $S$ is arbitrarily close to the identity in the uniform metric. Then no point of this annulus is periodic under $S \circ T$, because the composition of a periodic map with an irrational rotation on an invariant annulus produces non-periodic points. Hence $S \circ T \in M \setminus P_{ij}$ and $\varrho(S \circ T, T)$ is arbitrarily small.

Thus every neighborhood of any $T \in P_{ij}$ contains points of $M \setminus P_{ij}$, so $P_{ij}$ is nowhere dense. Therefore $P = \bigcup_{i,j} P_{ij}$ is a countable union of nowhere dense sets, i.e., of first category in $M$.
