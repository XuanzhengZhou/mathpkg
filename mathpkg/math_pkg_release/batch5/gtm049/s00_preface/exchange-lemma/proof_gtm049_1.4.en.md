---
role: proof
locale: en
of_concept: exchange-lemma
source_book: gtm049
source_chapter: "I"
source_section: "1.4"
---

We use induction on $k$ to prove that $b_1, \ldots, b_k, a_{k+1}, \ldots, a_r$ span $V$ (so long as $k \leq s$). When $k=0$ this is given. Assume the statement for $k=h-1$ and consider the case $k=h$. Then $b_h = y_1b_1 + \cdots + y_{h-1}b_{h-1} + x_h a_h + \cdots + x_r a_r$, and the linear independence of the $b_i$'s ensures that at least one $x_i$ is non-zero. By renumbering the vectors $a_h, \ldots, a_r$, if necessary, we may suppose that $x_h \neq 0$. Now we can solve for $a_h$ as an element of

$$[b_1, \ldots, b_h, a_{h+1}, \ldots, a_r] = M,$$

where $M$ contains $b_1, \ldots, b_{h-1}, a_{h+1}, \ldots, a_r$ and also $a_h$. Hence $M=V$, by the induction hypothesis. The result now follows by induction.
