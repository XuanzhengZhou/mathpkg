---
role: proof
locale: en
of_concept: semi-nuclei-automorphisms-from-autotopism
source_book: gtm006
source_chapter: "VIII"
source_section: "5"
---
We shall prove the case $i = r$; the other two cases are similar.

If $n_1, n_2$ are any two elements of $N_r$, then by definition $lpha_r(n_1 + n_2) = (ba(n_1 + n_2))R$. The left distributive law of $D$ together with the additive property of $R$ now gives $(n_1 + n_2)^{lpha_r} = (ban_1 + ban_2)R = (ban_1)R + (ban_2)R = n_1^{lpha_r} + n_2^{lpha_r}$.

In order to establish that $lpha_r$ is multiplicative on $N_r$, we first show that for any $x \in D$ and any $n \in N_r$,
$$(xn)R = xR \cdot (ban)R = xR \cdot n^{lpha_r}. 	ag{1}$$

Clearly $(xn)R = [((xR_a^{-1})a)n]R$ and thus, using the fact that $n$ associates on the right and the equation $(xy)R = (xP)(yQ)$, we have $(xn)R = [((xR_a^{-1})a)n]R = (xR_a^{-1})P \cdot (an)Q = ((xR_a^{-1})a)R \cdot (ban)R = xR \cdot (ban)R$.

For any $n_1, n_2 \in N_r$, $(n_1 n_2)^{lpha_r} = (ba(n_1 n_2))R = ((ban_1)n_2)R = n_1^{lpha_r} n_2^{lpha_r}$ as required. Thus $lpha_r$ is an automorphism of $N_r$. The proofs for $lpha_l$ and $lpha_m$ follow by symmetric arguments. $\square$
