---
role: proof
locale: en
of_concept: uniqueness-of-direct-sum-representation
source_book: gtm031
source_chapter: "II: Finite Dimensional Vector Spaces"
source_section: "10: Direct Sums and Independence"
---

Let $\mathfrak{R} = \mathfrak{R}_1 \oplus \cdots \oplus \mathfrak{R}_r$ be a direct sum, so the $\mathfrak{R}_i$ are independent and their sum is $\mathfrak{R}$. By definition, any $y \in \mathfrak{R}$ can be written as $y = y_1 + \cdots + y_r$ with $y_i \in \mathfrak{R}_i$.

To prove uniqueness, suppose $y = y_1 + \cdots + y_r = y_1' + \cdots + y_r'$ with $y_i, y_i' \in \mathfrak{R}_i$. Set $z_i = y_i - y_i' \in \mathfrak{R}_i$. Then $\sum_{i=1}^r z_i = 0$. For each $i$, we have
$$
-z_i = \sum_{j \neq i} z_j \in \mathfrak{R}_i \cap \left(\sum_{j \neq i} \mathfrak{R}_j\right).
$$
Since the $\mathfrak{R}_i$ are independent, $\mathfrak{R}_i \cap (\sum_{j \neq i} \mathfrak{R}_j) = 0$ by Theorem 10. Hence $z_i = 0$ for all $i$, so $y_i = y_i'$ for all $i$.

Conversely, if uniqueness of representation holds, suppose there exists a nonzero $z_i \in \mathfrak{R}_i \cap (\sum_{j \neq i} \mathfrak{R}_j)$. Then $z_i = \sum_{j \neq i} z_j$ with $z_j \in \mathfrak{R}_j$. This gives two distinct representations of $z_i$: $z_i = z_i$ (as an element of $\mathfrak{R}_i$) and $z_i = \sum_{j \neq i} z_j$ (as a sum from the other subspaces), contradicting uniqueness. Therefore the intersection must be zero, and the subspaces are independent.
