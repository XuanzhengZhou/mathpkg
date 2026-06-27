---
role: proof
locale: en
of_concept: boundedness-compactness-equicontinuity
source_book: gtm036
source_chapter: "18"
source_section: "18.5"
---

Recall that a subset of $E^*$ is equicontinuous if and only if its polar in $E$ is a neighborhood of $0$.

For (i): Assume $B$ is equicontinuous. Let $B_0$ denote the polar of $B$ in $E$, so $B_0$ is a neighborhood of $0$ in $E$. The weak* closed convex circled extension of $B$ is precisely the bipolar $B_0^0$, and the polar of $B_0^0$ is $B_0$ (by the computation rules for polars, 16.3). Since $B_0^0$ has $B_0$, a neighborhood of $0$, as its polar, $B_0^0$ is equicontinuous. Moreover, $B_0^0$ is weak* compact by the Banach-Alaoglu theorem (17.4), because $B_0$ is a neighborhood of $0$ and therefore the polar of a neighborhood is weak* compact. This establishes (i).

For (ii): Suppose $B$ is weak* compact and convex, and let $U$ be a strong neighborhood of $0$ in $E^*$. Without loss of generality, we may assume that $U$ is a (weak*) barrel, since the family of weak* barrels forms a local base for the strong topology. Since $B$ is weak* compact and convex, and $U$ is a weak* barrel (hence a weak* closed, circled, convex, absorbing set), the absorption corollary (10.2) implies that $U$ absorbs $B$. That is, there exists $\lambda > 0$ such that $B \subset \lambda U$. Since this holds for every strong neighborhood $U$ of $0$, $B$ is strongly bounded. This establishes (ii).

For (iii): If $B$ is strongly bounded, then for each weak* neighborhood $V$ of $0$ in $E^*$, there exists $\lambda > 0$ with $B \subset \lambda V$, because every weak* neighborhood is also a strong neighborhood (the strong topology is finer than the weak* topology). Thus $B$ is weak* bounded. Conversely, if $B$ is weak* bounded and $E$ is sequentially complete, then $B$ is strongly bounded: this follows directly from the uniform boundedness theorem (applied to the family $B$ as linear functionals on the sequentially complete locally convex space $E$), which states that a pointwise bounded family of continuous linear functionals on a sequentially complete locally convex space is equicontinuous, hence uniformly bounded on bounded sets, which is precisely strong boundedness.
