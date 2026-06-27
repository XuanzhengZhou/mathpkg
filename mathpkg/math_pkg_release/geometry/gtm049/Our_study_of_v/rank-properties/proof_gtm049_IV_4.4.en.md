---
role: proof
locale: en
of_concept: rank-properties
source_book: gtm049
source_chapter: "IV"
source_section: "4.4"
---
Let $$f: V \to V'$$ be a linear mapping. The rank of $$f$$ is $$\dim \operatorname{im} f$$.

(1) $$\operatorname{rank} f \leq \min(\dim V, \dim V')$$: Since $$\operatorname{im} f$$ is a subspace of $$V'$$, its dimension cannot exceed $$\dim V'$$. By the isomorphism theorem, $$\operatorname{im} f \cong V / \ker f$$, so $$\dim \operatorname{im} f = \dim V - \dim \ker f \leq \dim V$$.

(2) For the matrix rank: the row rank is the dimension of the subspace of $$F^n$$ spanned by the rows; the column rank is the dimension of the subspace of $$F^m$$ spanned by the columns. Using the correspondence between matrices and linear mappings, both equal $$\operatorname{rank} f$$.
