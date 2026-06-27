---
role: proof
locale: en
of_concept: chinese-remainder-for-ideals
source_book: gtm077
source_chapter: "II"
source_section: "27"
---
# Proof of the Chinese Remainder Theorem for Ideals

Let $\mathfrak{a}_1, \ldots, \mathfrak{a}_r$ be pairwise coprime ideals of the
ring of integers $\mathfrak{o}_K$ of an algebraic number field $K$. For any
integers $\alpha_1, \ldots, \alpha_r \in \mathfrak{o}_K$, there exists an
integer $\xi \in \mathfrak{o}_K$ such that

$$\xi \equiv \alpha_i \pmod{\mathfrak{a}_i} \qquad (i = 1, \ldots, r).$$

**Proof.** Since the congruences modulo ideals satisfy the same formal rules as
congruences in the rational number field (as stated at the beginning of §27),
the proof carries over directly from the rational case.

Set $\mathfrak{A} = \mathfrak{a}_1 \cdots \mathfrak{a}_r$ and
$\mathfrak{A}_i = \mathfrak{A} / \mathfrak{a}_i$. Because the $\mathfrak{a}_i$
are pairwise coprime, we have $(\mathfrak{A}_i, \mathfrak{a}_i) = 1$. By
Theorem 78 (solvability of linear congruences modulo an ideal), there exists
an integer $\mu_i$ such that

$$\mathfrak{A}_i \mu_i \equiv 1 \pmod{\mathfrak{a}_i}.$$

Now define

$$\xi = \sum_{i=1}^r \alpha_i \mathfrak{A}_i \mu_i.$$

For each $j$, we have $\mathfrak{A}_i \equiv 0 \pmod{\mathfrak{a}_j}$ whenever
$i \neq j$, while $\mathfrak{A}_j \mu_j \equiv 1 \pmod{\mathfrak{a}_j}$.
Therefore

$$\xi \equiv \alpha_j \cdot 1 + \sum_{i \neq j} \alpha_i \cdot 0 \equiv \alpha_j \pmod{\mathfrak{a}_j},$$

as required. The solution is uniquely determined modulo $\mathfrak{A}$.
