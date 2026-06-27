---
role: proof
locale: en
of_concept: lindelof-with-open-and-closed-base-separation
source_book: gtm043
source_chapter: "16"
source_section: "16"
---
Let $H$ and $K$ be disjoint closed sets. For each point $x$, let $U(x)$ be an open-and-closed neighborhood of $x$ that fails to meet at least one of these sets. Since $X$ is a Lindelöf space, the family of all sets $U(x)$ has a countable subfamily $\{U_k\}_{k \in \mathbb{N}}$ whose union is $X$. Define
$$V_k = U_k - \bigcup_{i < k} U_i;$$
then $\{V_k\}_{k \in \mathbb{N}}$ is a family of disjoint, open-and-closed sets whose union is $X$. Moreover, for each $k$, either $V_k \cap H = \emptyset$ or $V_k \cap K = \emptyset$. Let
$$W = \bigcup \{V_k: V_k \cap H = \emptyset\};$$
then $\{W, X - W\}$ is a partition of $X$ separating $H$ and $K$.
