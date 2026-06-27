---
role: proof
locale: en
of_concept: existence-of-large-residue-class-field
source_book: gtm043
source_chapter: "12"
source_section: "12.7"
---
Since $X$ is infinite, it is equipotent with the set of all finite subsets of a well-ordered index set. Let these finite sets be denoted $F_x$ for each $x \in X$.

Given any subset $B$ of $C(X)$ of cardinality $\leq \mathfrak{m}$, index it as $(g_y)_{y \in X}$ (with duplicates if $|B| < |X|$). Define
$$f(x) = 1 + \max_{y \in F_x} g_y(x) \quad (x \in X).$$
Since $F_x$ is finite and nonempty, $f$ is well-defined and continuous on the discrete space $X$.

For any $g_y \in B$ and $x \in Z_y$ (where $Z_y$ is a specific zero-set of a maximal ideal $M$ containing the ultrafilter of those finite-intersection-property sets), we have $y \in F_x$, so
$$g_y(x) \leq \max_{z \in F_x} g_z(x) < f(x).$$
Thus $f - g_y$ is positive on $Z_y \in Z[M]$. By 5.4(b), $M(f) > M(g_y)$. Hence no set of cardinality $\leq \mathfrak{m}$ is cofinal in $C/M$, implying $|C/M| > \mathfrak{m}$.