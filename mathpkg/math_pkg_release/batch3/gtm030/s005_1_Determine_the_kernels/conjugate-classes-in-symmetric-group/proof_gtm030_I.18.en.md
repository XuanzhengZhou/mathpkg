---
role: proof
locale: en
of_concept: conjugate-classes-in-symmetric-group
source_book: gtm030
source_chapter: "I"
source_section: "18"
---

Write a permutation $\alpha$ in its cycle decomposition:

$$\alpha = (i_1 i_2 \cdots i_r)(j_1 j_2 \cdots j_s) \cdots (l_1 l_2 \cdots l_u)$$

Then for any $\beta \in S_n$,

$$\beta^{-1} \alpha \beta = (i_1 \beta \; i_2 \beta \; \cdots \; i_r \beta) \cdots (l_1 \beta \; l_2 \beta \; \cdots \; l_u \beta).$$

We may suppose that $r \geq s \geq \cdots \geq u$ and that all the numbers $1, \ldots, n$ are displayed in the cycle decomposition. Then $r + s + \cdots + u = n$. In this way we associate with $\alpha$ a set of positive integers $r, s, \cdots, u$ satisfying

$$r \geq s \geq \cdots \geq u, \qquad r + s + \cdots + u = n.$$

Equation (21) shows that $\alpha$ and $\alpha'$ are conjugates in $S_n$ if and only if the associated sets $r, s, \cdots, u$ are the same for these two permutations. Hence there is a 1-1 correspondence between the conjugate classes in $S_n$ and the partitions of $n$.
