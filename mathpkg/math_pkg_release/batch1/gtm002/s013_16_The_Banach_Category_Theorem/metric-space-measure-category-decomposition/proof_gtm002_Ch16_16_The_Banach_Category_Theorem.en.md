---
role: proof
locale: en
of_concept: metric-space-measure-category-decomposition
source_book: gtm002
source_chapter: "16"
source_section: "16. The Banach Category Theorem"
---

By selecting a point from each member of the given base, we obtain a dense set $S$ of at most the same cardinality. For each positive integer $n$, let $F_n$ be a maximal subset of $S$ with the property that $\varrho(x, y) \geq 1/n$ for any two distinct points of $F_n$. Put $D = \bigcup_{n=1}^{\infty} F_n$. Then $D$ is dense in $X$, and since every subset of $F_n$ is closed, every subset of $D$ is an $F_\sigma$. Hence $\mu$ is defined for all subsets of $D$. Because $\mu$ is zero for points and $\operatorname{card} D$ has measure zero, it follows that no subset of $D$ has positive finite measure. Therefore, by (i) and (ii), $\mu(D) = 0$ and $D$ is contained in a $G_\delta$ set of measure zero. The complement is then a set of first category.

