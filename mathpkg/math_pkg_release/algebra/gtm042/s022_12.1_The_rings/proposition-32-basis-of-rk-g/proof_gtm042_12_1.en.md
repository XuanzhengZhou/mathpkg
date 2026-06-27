---
role: proof
locale: en
of_concept: proposition-32-basis-of-rk-g
source_book: gtm042
source_chapter: "12"
source_section: "12.1"
---

It is clear that the $\chi_i$ generate $R_K(G)$. On the other hand, if $i \neq j$ we have $\operatorname{Hom}^G(V_i, V_j) = 0$. In general, if $V$ and $W$ have characters $\chi_V$ and $\chi_W$, then

$$\dim_K \operatorname{Hom}^G(V, W) = \dim_{\mathbb{C}} \operatorname{Hom}^G(V_{\mathbb{C}}, W_{\mathbb{C}}) = \langle \chi_V, \chi_W \rangle,$$

cf. 7.2, Lemma 2. It follows that $\langle \chi_i, \chi_j \rangle = 0$ for $i \neq j$, and

$$\langle \chi_i, \chi_i \rangle = \dim_K \operatorname{End}^G(V_i)$$

is an integer $\geqslant 1$ (equal to $1$ iff $V_{\mathbb{C}}$ is irreducible, i.e., $V_i$ is absolutely irreducible; cf. Bourbaki [8], SS13, no. 4). In particular, the $\chi_i$ are linearly independent, proving both (a) and (b).
