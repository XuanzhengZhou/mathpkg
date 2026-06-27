---
role: proof
locale: en
of_concept: pairwise-comaximal-ideals
source_book: gtm028
source_chapter: "III"
source_section: "§13"
---

If $\mathfrak{A}_1$ and $\mathfrak{A}_2$ are comaximal, obviously $\sqrt{\mathfrak{A}_1}$ and $\sqrt{\mathfrak{A}_2}$ are. Conversely suppose $\sqrt{\mathfrak{A}_1} + \sqrt{\mathfrak{A}_2} = R$. Then by the formulas on the radical,
$$R = \sqrt{R} = \sqrt{\sqrt{\mathfrak{A}_1} + \sqrt{\mathfrak{A}_2}} = \sqrt{\mathfrak{A}_1 + \mathfrak{A}_2},$$
hence $\mathfrak{A}_1 + \mathfrak{A}_2 = R$.

For the congruence solution: if $n = 2$, then $1 = a_1 + a_2$ with $a_i \in \mathfrak{A}_i$, so that $a_1 \equiv 0 \pmod{\mathfrak{A}_1}$, $a_2 \equiv 1 \pmod{\mathfrak{A}_1}$, $a_1 \equiv 1 \pmod{\mathfrak{A}_2}$, $a_2 \equiv 0 \pmod{\mathfrak{A}_2}$. Placing $b = b_1 a_2 + b_2 a_1$ we get $b \equiv b_i \pmod{\mathfrak{A}_i}$ for $i = 1, 2$.

For $n > 2$, by induction we have an element $b'$ such that $b' \equiv b_i \pmod{\mathfrak{A}_i}$ for $i = 1, \cdots, n-1$. Since $\mathfrak{A}_n$ and $\mathfrak{A}_1 \cap \cdots \cap \mathfrak{A}_{n-1}$ are comaximal (by the second statement), there is an element $b$ such that $b \equiv b' \pmod{\mathfrak{A}_1 \cap \cdots \cap \mathfrak{A}_{n-1}}$ and $b \equiv b_n \pmod{\mathfrak{A}_n}$. This yields $b \equiv b_i \pmod{\mathfrak{A}_i}$ for all $i$.
