---
role: proof
locale: en
of_concept: first-category-nowhere-dense
source_book: gtm002
source_chapter: "22"
source_section: "Category Measure Spaces"
---

Let $P = \bigcup_{i=1}^{\infty} N_i$, with each $N_i$ nowhere dense, be any set of first category. Since $\mu(\overline{N}_i) = 0$, Theorem 22.1 implies that for any two positive integers $i$ and $j$ there is an open set $G_{ij}$ such that $\overline{N}_i \subset G_{ij}$ and $\mu(G_{ij}) < 1/2^{i+j}$.

Put $H_j = \bigcup_{i=1}^{\infty} G_{ij}$. Then $H_j$ is open, $P \subset H_j$, and

$$\mu(\overline{H}_j) = \mu(H_j) < \frac{1}{2^j}.$$

Put $F = \bigcap_{j=1}^{\infty} \overline{H}_j$. Then $F$ is closed and $P \subset F$. Since $\mu(F) = 0$, the interior of $F$ must be empty. Hence $F$, and therefore $P$, is nowhere dense.
