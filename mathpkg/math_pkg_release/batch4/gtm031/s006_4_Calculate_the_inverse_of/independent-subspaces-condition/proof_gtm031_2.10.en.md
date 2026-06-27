---
role: proof
locale: en
of_concept: independent-subspaces-condition
source_book: gtm031
source_chapter: "II: Finite Dimensional Vector Spaces"
source_section: "10: Direct Sums and Independence"
---

**Necessity:** Assume the subspaces $\mathfrak{S}_1, \mathfrak{S}_2, \cdots, \mathfrak{S}_r$ are independent. Suppose $x \in \mathfrak{S}_i \cap (\mathfrak{S}_1 + \cdots + \mathfrak{S}_{i-1} + \mathfrak{S}_{i+1} + \cdots + \mathfrak{S}_r)$. Then $x \in \mathfrak{S}_i$ and $x = \sum_{j \neq i} x_j$ with $x_j \in \mathfrak{S}_j$. Thus $0 = -x + \sum_{j \neq i} x_j$ gives two representations of $0$ as a sum of elements from the $\mathfrak{S}_k$: one is $0 = 0 + \cdots + 0$, and the other uses $-x \in \mathfrak{S}_i$ and $x_j \in \mathfrak{S}_j$ for $j \neq i$. By uniqueness of representation (independence), we must have $x = 0$ and all $x_j = 0$. Hence the intersection is $\{0\}$.

**Sufficiency:** Assume $\mathfrak{S}_i \cap (\sum_{j \neq i} \mathfrak{S}_j) = 0$ for all $i$. To show independence, suppose $y = \sum y_i = \sum y_i'$ with $y_i, y_i' \in \mathfrak{S}_i$. Then $\sum (y_i - y_i') = 0$. Set $z_i = y_i - y_i' \in \mathfrak{S}_i$. From $\sum z_i = 0$ we have $-z_i = \sum_{j \neq i} z_j$, so $-z_i \in \mathfrak{S}_i \cap (\sum_{j \neq i} \mathfrak{S}_j) = 0$. Thus $z_i = 0$ and $y_i = y_i'$ for all $i$, proving uniqueness.

Conversely, if uniqueness fails for some $i$, then there exists a nonzero $z_i \in \mathfrak{S}_i \cap (\sum_{j \neq i} \mathfrak{S}_j)$, demonstrating that the intersection condition is both necessary and sufficient.
