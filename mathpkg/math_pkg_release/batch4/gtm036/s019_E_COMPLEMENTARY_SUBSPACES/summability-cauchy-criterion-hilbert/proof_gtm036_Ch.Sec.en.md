---
role: proof
locale: en
of_concept: summability-cauchy-criterion-hilbert
source_book: gtm036
source_chapter: ""
source_section: ""
---

The family $\{x_\alpha\}$ is summable if and only if the net of finite partial sums $\{\sum_{\alpha \in F} x_\alpha : F \subset A \text{ finite}\}$ is Cauchy in $H$, directed by inclusion. A net $\{S_F\}$ is Cauchy if for every $e > 0$ there exists a finite $B \subset A$ such that for all finite $F, G \supset B$, $\|S_F - S_G\| < e$. Taking $F = B \cup C$ and $G = B$ where $C \cap B = \emptyset$ gives $\|\sum_{\alpha \in C} x_\alpha\| < e$. Conversely, if the condition holds, then for $F, G \supset B$, the symmetric difference $(F \setminus G) \cup (G \setminus F) \subset A \setminus B$, and $\|S_F - S_G\| \leq \|\sum_{\alpha \in F \setminus G} x_\alpha\| + \|\sum_{\alpha \in G \setminus F} x_\alpha\| < 2e$, so the net is Cauchy and hence summable (by completeness of $H$).
