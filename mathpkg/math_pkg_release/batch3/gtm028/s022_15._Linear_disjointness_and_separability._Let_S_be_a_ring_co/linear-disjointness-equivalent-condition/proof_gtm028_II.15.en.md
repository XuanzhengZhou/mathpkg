---
role: proof
locale: en
of_concept: linear-disjointness-equivalent-condition
source_book: gtm028
source_chapter: "II"
source_section: "§15. Linear disjointness and separability"
---

**Proof.** Assume that $L$ and $L'$ are linearly disjoint over $k$ and let $u'_1 x_1 + u'_2 x_2 + \cdots + u'_n x_n = 0$, where the $u'_i$ are in $L'$ and $x_1, x_2, \dots, x_n$ are elements of $L$ which are linearly independent over $k$. Let $\{x'_1, x'_2, \dots, x'_m\}$ be a basis of the vector space $k u'_1 + k u'_2 + \cdots + k u'_n$ over $k$ and let $u'_i = \sum_{j} a_{ij} x'_j$, where $a_{ij} \in k$. Then

$$\sum_{i,j} a_{ij} x'_j x_i = 0.$$

Since the $x_i$ are linearly independent over $k$ and the $x'_j$ are linearly independent over $k$, the linear disjointness implies that the $mn$ products $x_i x'_j$ are linearly independent over $k$. Hence all $a_{ij} = 0$, so all $u'_i = 0$. This shows that the $x_i$ are linearly independent over $L'$, establishing condition (LD).

Conversely, assume condition (LD) holds. Let $x_1, \dots, x_n \in L$ be linearly independent over $k$ and $x'_1, \dots, x'_m \in L'$ be linearly independent over $k$. Suppose $\sum_{i,j} c_{ij} x_i x'_j = 0$ with $c_{ij} \in k$. Then $\sum_i (\sum_j c_{ij} x'_j) x_i = 0$. Since each $\sum_j c_{ij} x'_j \in L'$ and the $x_i$ are linearly independent over $L'$ by (LD), we have $\sum_j c_{ij} x'_j = 0$ for each $i$. By linear independence of the $x'_j$ over $k$, all $c_{ij} = 0$. Hence the $mn$ products $x_i x'_j$ are linearly independent over $k$, proving linear disjointness.
