---
role: proof
locale: en
of_concept: category-measure-regularity
source_book: gtm002
source_chapter: "22"
source_section: "22"
---

Let $\mathcal{F}$ be a maximal family of pairwise disjoint open subsets of $G$ whose closures are contained in $G$. Such a family exists by Zorn's Lemma; by regularity of $X$, every point of $G$ has an open neighborhood whose closure is contained in $G$, so $\mathcal{F}$ is nonempty. Let $U = \bigcup \{V : V \in \mathcal{F}\}$. By maximality of $\mathcal{F}$, we have $G \subset \bar{U}$. Hence $G - U \subset \bar{U} - U$, which is nowhere dense. Since $\mu$ is a category measure, every nowhere dense set has measure zero, so $\mu(G - U) = 0$. Therefore

$$\mu(G) = \mu(U) = \sum_{V \in \mathcal{F}} \mu(V).$$

Choose $n$ so that $\sum_{i=1}^n \mu(V_i) > \mu(G) - \varepsilon$, where $V_1, \dots, V_n$ are the first $n$ members of $\mathcal{F}$. Then $F = \bigcup_{i=1}^n \bar{V}_i$ is a finite union of closed sets, hence closed, and $F \subset G$ since each $\bar{V}_i \subset G$. Moreover,

$$\mu(F) \ge \mu\left(\bigcup_{i=1}^n V_i\right) = \sum_{i=1}^n \mu(V_i) > \mu(G) - \varepsilon.$$

This proves the first assertion. The second follows by complementation: given a closed set $F$, apply the first assertion to the open set $X - F$ to obtain a closed set $C \subset X - F$ with $\mu(C) > \mu(X - F) - \varepsilon$. Then $G = X - C$ is an open superset of $F$ and

$$\mu(G) = \mu(X) - \mu(C) < \mu(X) - [\mu(X - F) - \varepsilon] = \mu(F) + \varepsilon.$$
