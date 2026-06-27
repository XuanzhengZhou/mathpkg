---
role: proof
locale: en
of_concept: normal-crossings-implies-tangent-spaces-general-position
source_book: gtm014
source_chapter: "3"
source_section: "Immersions with Normal Crossings"
---

Let $D = H_1 \cap \cdots \cap H_r$ and let $D_i = \bigcap_{j \neq i} H_j$. Choose a complementary subspace $F_i$ to $D$ in $D_i$ for $1 \leq i \leq r$. First note that $\dim F_i = \operatorname{codim} H_i$, since

$$\dim F_i = \dim D_i - \dim D$$
$$= \dim V - \operatorname{codim}\left( \bigcap_{j \neq i} H_j \right) - \dim V + \operatorname{codim}\left( H_1 \cap \cdots \cap H_r \right)$$
$$= \operatorname{codim}\left( H_i \right)$$

since the $H_i$'s are in general position. So

$$\dim D + \dim F_1 + \cdots + \dim F_r = \dim D + \operatorname{codim} H_1 + \cdots + \operatorname{codim} H_r$$
$$= \dim D + \operatorname{codim}\left( H_1 \cap \cdots \cap H_r \right)\quad\text{(by general position)}$$
$$= \dim V\quad(\text{since } D = H_1 \cap \cdots \cap H_r).$$

Thus to show the result we need only show that the sum $D + F_1 + \cdots + F_r$ is direct. Suppose $d + f_2 + \cdots + f_r$ is in $F_1$ where $f_j \in F_j$ for $2 \leq j \leq r$. Note that each $f_j$ is in $D_j \setminus D$; so $f_j$ is in $H_i$ for $i \neq j$. Hence $d + f_2 + \cdots + f_r$ is in $H_1$. Now $F_1 \subset D_1 \setminus D = H_2 \cap \cdots \cap H_r \setminus H_1 \cap \cdots \cap H_r$. Hence $F_1 \cap H_1 = 0$ and thus $d + f_2 + \cdots + f_r = 0$.

Now suppose $d + f_1 + \cdots + f_r = 0$ with $d \in D$ and $f_i \in F_i$. Then for each $i$, $f_i \in D_i$ so $f_i \in H_j$ whenever $j \neq i$. It follows that each $f_i = 0$ (since otherwise the sum cannot vanish by the pairwise independence established above), and hence $d = 0$. Therefore the sum is direct and $\dim V = \dim D + \sum \dim F_i$, which establishes that the $H_i$ are in general position.
