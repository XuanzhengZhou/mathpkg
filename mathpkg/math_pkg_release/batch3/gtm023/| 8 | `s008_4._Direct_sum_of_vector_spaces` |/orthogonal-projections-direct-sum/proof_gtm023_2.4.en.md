---
role: proof
locale: en
of_concept: orthogonal-projections-direct-sum
source_book: gtm023
source_chapter: "2"
source_section: "4"
---

Let $x \in E$ be arbitrary. Then the relation

$$
x = \sum_{i=1}^{r} \varrho_i x \in \sum_{i=1}^{r} \operatorname{Im} \varrho_i
$$

shows that

$$
E = \sum_{i=1}^{r} \operatorname{Im} \varrho_i. \tag{2.32}
$$

To prove that the sum (2.32) is direct, suppose that

$$
x \in \operatorname{Im} \varrho_i \cap \sum_{j \neq i} \operatorname{Im} \varrho_j.
$$

Then $x = \varrho_i y$ for some $y \in E$, so that

$$
\varrho_i x = \varrho_i^2 y = \varrho_i y = x. \tag{2.33}
$$

On the other hand, we have that for some vectors $y_j \in E$,

$$
x = \sum_{j \neq i} \varrho_j y_j
$$

whence, in view of $\varrho_i \circ \varrho_j = 0$ for $i \neq j$,

$$
\varrho_i x = \sum_{j \neq i} \varrho_i \varrho_j y_j = 0. \tag{2.34}
$$

Relations (2.33) and (2.34) yield $x = 0$, and hence the decomposition (2.32) is direct.
