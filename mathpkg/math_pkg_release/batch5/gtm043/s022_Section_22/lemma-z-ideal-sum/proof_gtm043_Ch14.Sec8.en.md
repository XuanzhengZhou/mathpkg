---
role: proof
locale: en
of_concept: lemma-z-ideal-sum
source_book: gtm043
source_chapter: "14"
source_section: "8"
---

We prove that if $Z(h) \supset Z(g_1 + g_2)$, where $g_1 \in I$ and $g_2 \in J$, then $h \in (I, J)$. Without loss of generality, assume $h$ is bounded.

Let $Z_1 = Z(g_1)$ and $Z_2 = Z(g_2)$. Then $Z(h) \supset Z_1 \cap Z_2$. By (IV) of the compactification theorem (6.5),
$$\operatorname{cl}_{\beta X} Z(h) \supset \operatorname{cl} Z_1 \cap \operatorname{cl} Z_2.$$

Define $\varphi$ on $\operatorname{cl} Z_1 \cup \operatorname{cl} Z_2$ by:
$$\varphi(p) = 0 \text{ for } p \in \operatorname{cl} Z_1,$$
$$\varphi(p) = h^\beta(p) \text{ for } p \in \operatorname{cl} Z_2.$$

This is continuous, hence extends to $f^\beta \in C(\beta X)$, with $f \in C^*(X)$. Since $Z(f) \supset Z_1 \in Z[I]$, $f \in I$. Likewise $Z(h-f) \supset Z_2$, so $h-f \in J$. Therefore $h = f + (h-f) \in (I,J)$.
