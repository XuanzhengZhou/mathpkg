---
role: proof
locale: en
of_concept: category-measure-approximation
source_book: gtm002
source_chapter: "22"
source_section: "Category Measure Spaces"
---

Let $G$ be an arbitrary open set. There exists a maximal family $\{U_i\}$ of disjoint open sets whose closures $\overline{U}_i$ are contained in $G$ (by the Hausdorff maximal principle). The maximality of $\mathcal{F} = \{U_i\}$ implies that $G \subset \overline{U}$, where $U = \bigcup_i U_i$. Hence $G - U$ is contained in $\overline{U} - U$, which is nowhere dense. Therefore $\mu(G - U) = 0$ and consequently

$$\mu(G) = \mu(U) = \sum_i \mu(U_i).$$

Choose $n$ so that $\sum_{i=1}^n \mu(U_i) > \mu(G) - \varepsilon$. Then $F = \bigcup_{i=1}^n \overline{U}_i$ is a closed subset of $G$, and $\mu(F) > \mu(G) - \varepsilon$. This proves the first assertion.

The second assertion follows by complementation: apply the first assertion to the open set $X - F$ and then take complements.
