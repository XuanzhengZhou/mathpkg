---
role: proof
locale: en
of_concept: first-category-sets-nowhere-dense
source_book: gtm002
source_chapter: "22"
source_section: "22. Category Measure Spaces"
---

Let $P = \bigcup_{i=1}^{\infty} N_i$ be any set of first category, where each $N_i$ is nowhere dense. Since $N_i$ is nowhere dense, its closure $\overline{N}_i$ has empty interior, and therefore $\mu(\overline{N}_i) = 0$ (by the defining property of a category measure, sets of first category have measure zero, and closed nowhere dense sets are of first category).

Apply Theorem 22.1 to each $\overline{N}_i$ and $\varepsilon = 1/2^{i+j}$: for each pair of positive integers $i$ and $j$, there exists an open set $G_{ij}$ such that
$$\overline{N}_i \subset G_{ij} \quad \text{and} \quad \mu(G_{ij}) < \frac{1}{2^{i+j}}.$$

Define $H_j = \bigcup_{i=1}^{\infty} G_{ij}$ for each $j$. Then each $H_j$ is open, $P \subset H_j$, and
$$\mu(H_j) \leq \sum_{i=1}^{\infty} \mu(G_{ij}) < \sum_{i=1}^{\infty} \frac{1}{2^{i+j}} = \frac{1}{2^j}.$$

Since $\mu$ is a category measure, $\mu(\overline{H}_j) = \mu(H_j) < 1/2^j$. Now set
$$F = \bigcap_{j=1}^{\infty} \overline{H}_j.$$
Then $F$ is closed as an intersection of closed sets, and $P \subset F$. Moreover,
$$\mu(F) \leq \mu(\overline{H}_j) < \frac{1}{2^j} \quad \text{for every } j,$$
so $\mu(F) = 0$. Since $\mu$ is a category measure, $F$ is of first category. A closed set of first category must have empty interior (otherwise it would contain an open set of second category, since $X$ is a Baire space). Thus $\operatorname{int}(F) = \emptyset$, meaning $F$ is nowhere dense. Since $P \subset F$, $P$ is also nowhere dense.
