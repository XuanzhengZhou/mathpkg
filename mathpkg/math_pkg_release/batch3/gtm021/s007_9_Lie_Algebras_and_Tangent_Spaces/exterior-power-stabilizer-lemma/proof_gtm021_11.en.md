---
role: proof
locale: en
of_concept: exterior-power-stabilizer-lemma
source_book: gtm021
source_chapter: "11"
source_section: "Construction of Certain Representations"
---
For (a): The "if" direction is clear. For the converse, choose a basis $(w_1, \ldots, w_n)$ of $W$ such that $M$ is spanned by $w_1, \ldots, w_d$ and $x(M)$ by $w_{l+1}, \ldots, w_{l+d}$ for some $l \geqslant 0$. We must show $l = 0$.

If $(\wedge^d x)L = L$, then $x(w_1) \wedge \cdots \wedge x(w_d)$ is a scalar multiple of $w_1 \wedge \cdots \wedge w_d$. Expanding in the wedge basis, each $x(w_i)$ is a linear combination of $w_1, \ldots, w_n$. If $l > 0$, some basis vector $w_j$ with $j > d$ would appear, contradicting that the wedge product remains proportional to $w_1 \wedge \cdots \wedge w_d$. Hence $l = 0$ and $x(M) = M$.

For (b): Again the "if" direction is clear. For the converse, suppose $(d\wedge^d)(X)L \subset L$. This means $(d\wedge^d)(X)(w_1 \wedge \cdots \wedge w_d) \in L$.

The action of $d\wedge^d(X)$ on a wedge product is:
$$(d\wedge^d)(X)(w_1 \wedge \cdots \wedge w_d) = \sum_{i=1}^d w_1 \wedge \cdots \wedge X(w_i) \wedge \cdots \wedge w_d.$$

For this to lie in $L = K(w_1 \wedge \cdots \wedge w_d)$, each term must be either a multiple of $w_1 \wedge \cdots \wedge w_d$ or zero. Since the vectors $w_1 \wedge \cdots \wedge X(w_i) \wedge \cdots \wedge w_d$ for different choices of the replaced factor are linearly independent (unless zero, which occurs when $X(w_i)$ lies in the span of $M$), and none can equal $w_1 \wedge \cdots \wedge w_d$ (since $X(w_i)$ would then need to be $w_i$, which is not generally true), we must have each term equal to zero. Hence $X(w_i) \in M$ for $1 \leq i \leq d$, so $X(M) \subset M$.
