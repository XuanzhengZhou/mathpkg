---
role: proof
locale: en
of_concept: empty-set-boolean-valued
source_book: gtm008
source_chapter: "13"
source_section: "13. Boolean-Valued Set Theory"
---

For $x \in V^{(B)}$:
$$[\![x \in \check{0}]\!] = \sum_{v \in \mathcal{D}(\check{0})} [\![x = \check{v}]\!] = 0$$
since $\mathcal{D}(\check{0}) = \emptyset$ (the empty set in $V$, because $0 = \emptyset$ has no elements).

Therefore:
$$[\![(\forall x)[x \notin \check{0}]]\!] = \prod_{x \in V^{(B)}} [\![x \notin \check{0}]\!] = \prod_{x \in V^{(B)}} (-[\![x \in \check{0}]\!]) = \prod_{x \in V^{(B)}} 1 = 1.$$

The formula $(\forall x)[x \notin a]$ is the defining property of the empty set in $ZF$. Thus the empty set of $V^{(B)}$ (denoted by $0$) satisfies this property with value $1$, and hence $[\![0 = \check{0}]\!] = 1$.
