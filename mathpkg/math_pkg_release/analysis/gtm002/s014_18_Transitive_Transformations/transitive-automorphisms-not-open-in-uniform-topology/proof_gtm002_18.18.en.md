---
role: proof
locale: en
of_concept: transitive-automorphisms-not-open-in-uniform-topology
source_book: gtm002
source_chapter: "18"
source_section: "18"
---

Let $H$ be the space of all automorphisms of the unit square $X$ with the uniform metric $\varrho(S, T) = \sup_{x \in X} |Sx - Tx|$. $H$ is topologically complete.

Suppose $T \in H$ is transitive and let $x$ be a point whose positive semiorbit is dense. Let $\varepsilon > 0$ be small enough so that the disk with radius $\varepsilon$ and center $x$ is contained in $X$. Let $n$ be the least positive integer such that $|x - T^n x| < \varepsilon$.

Choose an open disk $U$ with center $x$ and radius less than $\varepsilon$ such that $T^n x$ is interior to $U$ and $Tx, T^2x, \ldots, T^{n-1}x$ belong to $X \setminus \overline{U}$.

Then we can find a closed disk $D$ with center $x$ such that:
- $D$ and $T^n(D)$ are contained in $U$,
- $T(D), T^2(D), \ldots, T^{n-1}(D)$ are contained in $X \setminus U$.

Let $S$ be an automorphism of $X$ equal to the identity outside $U$, and inside $U$ equal to a radial contraction that maps $T^n(D)$ onto a subset of the interior of $D$.

Then $S \circ T$ is an automorphism of $X$ such that $(S \circ T)^n$ maps $D$ onto a subset of its interior. Consequently, $S \circ T$ is not transitive — any point starting in $D$ will have its forward orbit trapped within $D$, never reaching points outside $D$.

By making the contraction sufficiently mild (choosing $U$ small and $D$ appropriately), we can make $\varrho(S \circ T, T)$ arbitrarily small. Hence every neighborhood of a transitive automorphism contains a non-transitive one. Therefore the set of transitive automorphisms is not open in $H$.
