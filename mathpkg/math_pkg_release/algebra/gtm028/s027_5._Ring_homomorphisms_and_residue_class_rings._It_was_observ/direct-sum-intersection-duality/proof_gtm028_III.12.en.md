---
role: proof
locale: en
of_concept: direct-sum-intersection-duality
source_book: gtm028
source_chapter: "III"
source_section: "§12"
---

For the forward direction: $M = M_1 \oplus \cdots \oplus M_r$. Define $N_i$ as stated. Then $N_1 \cap \cdots \cap N_r = (0)$ is clear from independence. For the second condition, note $M_i \subset N_j$ for $i \neq j$, so $N_1 \cap \cdots \cap N_{i-1} \cap N_{i+1} \cap \cdots \cap N_r$ contains $M_i$, and $M_i + N_i = M$. For the third condition: clearly $M_i \subset \bigcap_{j \neq i} N_j$.

Conversely, given $N_i$ satisfying $(0) = \cap N_j$ and the second condition, define $M_i$ as the intersection of all $N_j$ with $j \neq i$. Then any $x \in M$ can be written as $x = \sum x_i$ with $x_i \in M_i$. Since $x - x_j = y_j \in N_j$, we have $x - \sum x_i \in \cap N_j = (0)$, so the sum spans $M$. Independence follows from $M_i \cap \sum_{j \neq i} M_j \subset M_i \cap N_i = (0)$. That $N_i = \sum_{j \neq i} M_j$ follows from the modular law:
$$N_i = N_i \cap (\sum_{j \neq i} M_j + M_i) = \sum_{j \neq i} M_j + (N_i \cap M_i) = \sum_{j \neq i} M_j.$$
