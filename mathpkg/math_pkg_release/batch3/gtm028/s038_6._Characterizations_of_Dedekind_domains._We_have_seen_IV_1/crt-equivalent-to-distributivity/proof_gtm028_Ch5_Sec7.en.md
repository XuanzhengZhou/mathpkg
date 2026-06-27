---
role: proof
locale: en
of_concept: crt-equivalent-to-distributivity
source_book: gtm028
source_chapter: "V"
source_section: "7"
---

We first consider the case $n = 2$. If $x_1 \equiv x_2 \pmod{\mathfrak{a}_1 + \mathfrak{a}_2}$, we have $x_1 - x_2 = a_1 - a_2$ with $a_i \in \mathfrak{a}_i$. We may then take $x = x_1 - a_1 = x_2 - a_2$ as a solution of the congruences $x \equiv x_i \pmod{\mathfrak{a}_i}$. The condition $x_1 \equiv x_2 \pmod{\mathfrak{a}_1 + \mathfrak{a}_2}$ is thus necessary and sufficient for the solvability of two simultaneous congruences.

For the general case, assuming $(D_1)$, we prove by induction on $n$ that the congruences $x \equiv x_i \pmod{\mathfrak{a}_i}$ ($i = 1, \cdots, n$) admit a solution if and only if $x_i \equiv x_j \pmod{\mathfrak{a}_i + \mathfrak{a}_j}$ for all $i, j$. The induction step uses $(D_1)$ to verify solvability conditions.

Conversely, we prove that both distributive laws follow from the validity of (CRT) for $n = 3$. For $(D_1)$, the left-hand side is obviously contained in the right-hand side, and we show any element $d \in (\mathfrak{a} + \mathfrak{b}) \cap (\mathfrak{a} + \mathfrak{b}')$ belongs to $\mathfrak{a} + (\mathfrak{b} \cap \mathfrak{b}')$ by solving three compatible congruences. For $(D_2)$ the argument is similar.

From the equivalence of $(D_1)$ and (CRT) for $n = 2$, we immediately deduce that (CRT) holds for every $n$.
