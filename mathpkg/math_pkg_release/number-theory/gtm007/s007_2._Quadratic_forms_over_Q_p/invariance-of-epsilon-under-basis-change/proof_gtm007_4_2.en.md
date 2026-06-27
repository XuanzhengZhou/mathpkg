---
role: proof
locale: en
of_concept: invariance-of-epsilon-under-basis-change
source_book: gtm007
source_chapter: "4"
source_section: "2"
---

Let $e = (e_1, \ldots, e_n)$ and $e' = (e'_1, \ldots, e'_n)$ be two orthogonal bases of $V$. Set $a_i = e_i \cdot e_i$ and $a'_i = e'_i \cdot e'_i$. We prove $\varepsilon(e) = \varepsilon(e')$ by induction on $n$, the rank of $V$.

The case $n = 1$ is trivial since there are no pairs $i < j$ and $\varepsilon(e) = 1$ for any basis.

Assume $n \geq 2$. By the properties of orthogonal bases over a field, there exists a basis element, say $e_1$, that can be replaced by an element of the other basis. More precisely, we can pass from $e$ to $e'$ by a sequence of elementary transformations where only one basis vector is changed at a time, so it suffices to consider the case where $e$ and $e'$ differ only in the first vector: $e_1 \neq e'_1$ but $e_i = e'_i$ for $i \geq 2$, up to reordering.

Let $d(Q) = a_1 a_2 \cdots a_n$ in $k^*/k^{*2}$ be the discriminant. Using the properties of the Hilbert symbol, specifically the bilinearity $(ab, c) = (a, c)(b, c)$, we have:

$$\varepsilon(e') = (a'_1, a_2 a_3 \cdots a_n) \prod_{2 \leq i < j} (a'_i, a'_j).$$

Since $d(Q) = a'_1 a_2 \cdots a_n$ (the discriminant is unchanged by change of basis), we have $a'_1 = d(Q) / (a_2 \cdots a_n)$ in $k^*/k^{*2}$, which gives:

$$\varepsilon(e') = (a_1, d(Q)a_1) \prod_{2 \leq i < j} (a'_i, a'_j)$$

after using the relation between $a_1$ and $a'_1$ and the properties $(a, a) = (-1, a)$ and $(a, b)(a, c) = (a, bc)$.

Now, by the induction hypothesis applied to the orthogonal complement of $e_1$ (which has rank $n-1$), we have:

$$\prod_{2 \leq i < j} (a_i, a_j) = \prod_{2 \leq i < j} (a'_i, a'_j).$$

It remains to check that $(a_1, a_2 \cdots a_n) = (a_1, d(Q)a_1)$. Since $d(Q) = a_1 \cdots a_n$, we have $a_2 \cdots a_n = d(Q)/a_1 = d(Q)a_1$ in $k^*/k^{*2}$ (because $a_1^{-1} = a_1$ modulo squares). Therefore:

$$(a_1, a_2 \cdots a_n) = (a_1, d(Q)a_1).$$

Combining these equalities yields $\varepsilon(e) = \varepsilon(e')$, completing the induction.
