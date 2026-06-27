---
role: proof
locale: en
of_concept: generators-contain-basis
source_book: gtm031
source_chapter: "II"
source_section: "2"
---

Suppose the vectors $f_1, f_2, \ldots, f_m$ are generators for the $n$-dimensional vector space $\Re$. Select from this set a maximal linearly independent subset, and assume without loss of generality that $f_1, f_2, \ldots, f_r$ is such a subset. Then for any $i > r$, the set $(f_1, f_2, \ldots, f_r, f_i)$ is linearly dependent. By Lemma 1 (if $x_1, \ldots, x_r$ are linearly independent and $x_1, \ldots, x_r, x_{r+1}$ are linearly dependent, then $x_{r+1}$ is linearly dependent on $x_1, \ldots, x_r$), each $f_i$ (and consequently every $x \in \Re$) is linearly dependent on $f_1, f_2, \ldots, f_r$.

Thus $f_1, f_2, \ldots, f_r$ spans $\Re$ and, being linearly independent, is a basis. By Theorem 3 (invariance of dimension), $r = n$. Hence the original set of generators contains at least $n$ elements and contains a subset of $n$ elements that forms a basis.
