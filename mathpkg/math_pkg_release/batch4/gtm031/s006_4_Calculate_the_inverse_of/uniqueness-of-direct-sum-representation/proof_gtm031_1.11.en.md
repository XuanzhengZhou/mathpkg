---
role: proof
locale: en
of_concept: uniqueness-of-direct-sum-representation
source_book: gtm031
source_chapter: "1"
source_section: "11"
---

Let $\mathfrak{S}_1, \mathfrak{S}_2, \ldots, \mathfrak{S}_r$ be independent subspaces and set $\mathfrak{S} = \mathfrak{S}_1 + \mathfrak{S}_2 + \cdots + \mathfrak{S}_r$. Suppose $y = y_1 + y_2 + \cdots + y_r = y_1' + y_2' + \cdots + y_r'$ where $y_i, y_i' \in \mathfrak{S}_i$. Set $z_i = y_i - y_i' \in \mathfrak{S}_i$. Then $\sum z_i = 0$, so
$$-z_i = \sum_{j \neq i} z_j \in \mathfrak{S}_i \cap (\mathfrak{S}_1 + \cdots + \mathfrak{S}_{i-1} + \mathfrak{S}_{i+1} + \cdots + \mathfrak{S}_r).$$
Since the $\mathfrak{S}_j$ are independent, this intersection is $\{0\}$; hence $z_i = 0$ and $y_i = y_i'$ for all $i$.

Conversely, if uniqueness of representation holds but the $\mathfrak{S}_i$ are not independent, then for some $i$ there exists a non-zero vector $z_i \in \mathfrak{S}_i \cap (\sum_{j \neq i} \mathfrak{S}_j)$. Thus $z_i = \sum_{j \neq i} z_j$ with $z_j \in \mathfrak{S}_j$, giving two distinct representations of $z_i$ as a sum of elements from the $\mathfrak{S}_k$, a contradiction.
