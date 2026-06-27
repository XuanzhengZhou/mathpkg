---
role: proof
locale: en
of_concept: strongly-isovalent-graph-k3
source_book: gtm054
source_chapter: "IX"
source_section: "46"
---

By E11 we have
$$n_1 p_{21}^1 = n_2 p_{11}^2 \quad\text{and}\quad n_2 p_{12}^2 = n_1 p_{21}^1.$$

Given $p_{11}^1 = p_{11}^2 = 1$, by E10 we have
$$p_{11}^1 + p_{12}^1 = n_1 - 1 \quad\text{and}\quad p_{11}^2 + p_{12}^2 = n_1,$$
which yield $p_{12}^1 = n_1 - 2$ and $p_{12}^2 = n_1 - 1$.

From E11, $n_1 p_{21}^1 = n_2 \cdot 1$, so $p_{21}^1 = n_2 / n_1$.
Substituting into the second E11 identity:
$$n_2 (n_1 - 1) = n_1 \cdot \frac{n_2}{n_1} = n_2.$$

If $n_2 > 0$, this gives $n_1 - 1 = 1$, hence $n_1 = 2$.
Since $v = 1 + n_1 + n_2$, we have $p_{21}^1 = n_2 / 2$, which must be a nonnegative integer.
From the remaining association scheme identities, all $p_{jk}^i$ must be nonnegative integers, forcing $n_2 = 0$.
Thus $v = 1 + 2 + 0 = 3$, $n_1 = 2$, and the graph is $K_3$.
