---
role: proof
locale: en
of_concept: open-cover-colimit-equalizer
source_book: gtm005
source_chapter: "IV"
source_section: "9"
---

For an open cover $\mathcal{U} = \{U_i\}_{i \in I}$ of a topological space $X$, $X$ is the colimit of the diagram consisting of all $U_i$ and all pairwise intersections $U_i \cap U_j$ with inclusion maps.

Equivalently, $X$ is the coequalizer of
$$\coprod_{i,j} U_i \cap U_j \rightrightarrows \coprod_i U_i \to X.$$
The two parallel maps are the inclusions $U_i \cap U_j \hookrightarrow U_i$ and $U_i \cap U_j \hookrightarrow U_j$.

Proof: The colimit topology on $X$ from this diagram is the final topology with respect to the inclusions $U_i \to X$. A subset $V \subseteq X$ is open in this topology iff $V \cap U_i$ is open in $U_i$ for all $i$, which is exactly the condition that $V$ is open in $X$ (since $\mathcal{U}$ is an open cover). Thus $X$ satisfies the universal property of the colimit.
