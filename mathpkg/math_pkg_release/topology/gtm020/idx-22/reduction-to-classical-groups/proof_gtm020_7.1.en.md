---
role: proof
locale: en
of_concept: reduction-to-classical-groups
source_book: gtm020
source_chapter: "7"
source_section: "1"
---

**Proof.** Let $\{(V_i, h_i)\}$ be an atlas of $\xi$. Then there are cross sections $h_i(b, e_j) = s_j(b)$ for $1 \leq j \leq n$ of $\xi$ over $V_i$ which form a basis of the fibre over each $b \in V_i$.

By Proposition (7.3), there are $n$ cross sections $s_1^*, \ldots, s_n^*$ of $\xi$ over $V_i$ such that $\beta(s_i^*, s_j^*)$ equals $1$ for $i = j$ and $0$ for $i \neq j$ at each $b \in V_i$.

We define $h_i^* \colon V_i \times F^n \to \xi|_{V_i}$ by
$$h_i^*(b, a_1, \ldots, a_n) = a_1 s_1^*(b) + \cdots + a_n s_n^*(b).$$
Then $h_i^*$ is a chart of $\xi$ over $V_i$, and $\{(V_i, h_i^*)\}$ is an atlas. By construction, $h_i^*$ is metric-preserving in the sense that
$$\beta(h_i^*(b, x), h_i^*(b, y)) = (x \mid y)$$
for all $x, y \in F^n$.

For the last statement, we recall that $h_i(b, g_{i,j}(b)x) = h_j(b, x)$ for $b \in V_i \cap V_j$ and $x \in F^n$. For $b \in V_i \cap V_j$, we have
$$(x \mid y) = \beta(h_j^*(b, x), h_j^*(b, y)) = \beta(h_i^*(b, g_{i,j}(b)x), h_i^*(b, g_{i,j}(b)y)) = (g_{i,j}(b)x \mid g_{i,j}(b)y).$$

Consequently, $g_{i,j}(b)$ preserves the inner product on $F^n$, and therefore $g_{i,j}(b)$ belongs to $O(n)$ for $F = \mathbf{R}$, $U(n)$ for $F = \mathbf{C}$, or $Sp(n)$ for $F = \mathbf{H}$. $\square$
