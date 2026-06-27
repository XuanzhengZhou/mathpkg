---
role: proof
locale: en
of_concept: line-decomposition
source_book: gtm002
source_chapter: "1"
source_section: "1"
---
Let $\{a_i\}$ be an enumeration of the rational numbers. For each $i$ and $j$, let $I_{ij}$ be an open interval with center $a_i$ and length $1/2^{i+j}$. Define
$$G_j = \bigcup_{i=1}^{\infty} I_{ij} \quad (j = 1, 2, \dots)$$
and let
$$B = \bigcap_{j=1}^{\infty} G_j, \qquad A = \mathbb{R} \setminus B.$$

\textbf{$B$ is a nullset:} For any $\varepsilon > 0$, choose $j$ large enough so that $1/2^j < \varepsilon$. Then $B \subset G_j = \bigcup_i I_{ij}$, and
$$\sum_{i=1}^{\infty} |I_{ij}| = \sum_{i=1}^{\infty} \frac{1}{2^{i+j}} = \frac{1}{2^j} \sum_{i=1}^{\infty} \frac{1}{2^i} = \frac{1}{2^j} < \varepsilon.$$
Thus $B$ can be covered by intervals with arbitrarily small total length, so $B$ is a nullset.

\textbf{$A$ is of first category:} Each $G_j$ is a dense open subset of $\mathbb{R}$, since it is a union of open intervals and contains all rational points (each rational $a_i$ is the center of $I_{ij}$). Therefore, each complement $G_j' = \mathbb{R} \setminus G_j$ is nowhere dense. Since $B = \bigcap_j G_j$, we have
$$A = \mathbb{R} \setminus B = \bigcup_{j=1}^{\infty} (\mathbb{R} \setminus G_j) = \bigcup_{j=1}^{\infty} G_j',$$
a countable union of nowhere dense sets. Hence $A$ is of first category.
