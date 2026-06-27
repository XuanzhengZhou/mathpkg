---
role: proof
locale: en
of_concept: first-category-sets-nowhere-dense
source_book: gtm002
source_chapter: "22"
source_section: "22"
---

Let $P = \bigcup_{i=1}^{\infty} N_i$, where each $N_i$ is nowhere dense, be any set of first category. Since $\mu(\bar{N}_i) = 0$ (each $\bar{N}_i$ is closed and nowhere dense, hence of first category, so has measure zero), Theorem 22.1 implies that for any two positive integers $i$ and $j$, there is an open set $G_{ij}$ such that $\bar{N}_i \subset G_{ij}$ and $\mu(G_{ij}) < 1/2^{i+j}$. Put

$$H_j = \bigcup_{i=1}^{\infty} G_{ij}.$$

Then $H_j$ is open, $P \subset H_j$, and

$$\mu(\bar{H}_j) = \mu(H_j) \le \sum_{i=1}^{\infty} \mu(G_{ij}) < \sum_{i=1}^{\infty} \frac{1}{2^{i+j}} = \frac{1}{2^j}.$$

Now put $F = \bigcap_{j=1}^{\infty} \bar{H}_j$. Then $F$ is closed and $P \subset F$. Moreover,

$$\mu(F) \le \mu(\bar{H}_j) < \frac{1}{2^j}$$

for every $j$, so $\mu(F) = 0$. Since $\mu$ is a category measure, $\mu(F) = 0$ implies $F$ is of first category, hence $F$ has empty interior. Thus $F$ is a closed set with empty interior, i.e., $F$ is nowhere dense. Since $P \subset F$, $P$ is also nowhere dense.
