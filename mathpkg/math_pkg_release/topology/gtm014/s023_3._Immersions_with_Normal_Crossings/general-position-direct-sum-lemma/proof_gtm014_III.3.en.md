---
role: proof
locale: en
of_concept: general-position-direct-sum-lemma
source_book: gtm014
source_chapter: "III"
source_section: "§3. Immersions with Normal Crossings"
---

First note that $\dim F_i = \operatorname{codim} H_i$, since
$$\dim F_i = \dim D_i - \dim D$$
$$= \dim V - \operatorname{codim}\bigl(\bigcap_{j \neq i} H_j\bigr) - \dim V + \operatorname{codim}(H_1 \cap \cdots \cap H_r)$$
$$= \operatorname{codim}(H_i)$$
because the $H_i$ are in general position.

So
$$\dim D + \dim F_1 + \cdots + \dim F_r = \dim D + \operatorname{codim} H_1 + \cdots + \operatorname{codim} H_r$$
$$= \dim D + \operatorname{codim}(H_1 \cap \cdots \cap H_r) \quad \text{(by general position)}$$
$$= \dim V \quad (\text{since } D = H_1 \cap \cdots \cap H_r).$$

To show (a), we need only show the sum $D + F_1 + \cdots + F_r$ is direct. Suppose $d + f_2 + \cdots + f_r \in F_1$ where $f_j \in F_j$ for $2 \leq j \leq r$. Each $f_j$ is in $D_j - D$, so $f_j \in H_i$ for $i \neq j$. Hence $d + f_2 + \cdots + f_r \in H_1$. Now $F_1 \subset D_1 - D = H_2 \cap \cdots \cap H_r - H_1 \cap \cdots \cap H_r$, so $F_1 \cap H_1 = 0$. Thus $d + f_2 + \cdots + f_r = 0$.

By symmetry, each $F_i$ intersects the sum of the remaining subspaces trivially, so the sum is direct.
