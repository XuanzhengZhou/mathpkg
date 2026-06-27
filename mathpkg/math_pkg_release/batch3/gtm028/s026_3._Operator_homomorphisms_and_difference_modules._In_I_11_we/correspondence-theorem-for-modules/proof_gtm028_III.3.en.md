---
role: proof
locale: en
of_concept: correspondence-theorem-for-modules
source_book: gtm028
source_chapter: "III"
source_section: "3"
---

If $L$ is a submodule of $M$ containing $N$, then $L' = LT$ is an $R$-submodule of $M'$ by Theorem 1. Distinct submodules $L$ give rise to distinct images $L'$, because $(LT)T^{-1} = L$. To prove this formula, first note $L \subset (LT)T^{-1}$ trivially. Conversely, if $x \in (LT)T^{-1}$, then $xT \in LT$, so $xT = yT$ with $y \in L$, hence $x - y \in N \subset L$, so $x \in L$, as required.

It remains to show that every submodule $L'$ of $M'$ arises in this way. By Theorem 1, $L'T^{-1}$ is a submodule of $M$, and $N \subset L'T^{-1}$ (obvious, since $NT = (0) \subset L'$). Moreover, $(L'T^{-1})T = L'$ because $T$ is onto. Thus the $(1,1)$ correspondence is established.

For the isomorphisms: $T$ induces an $R$-homomorphism of $L$ onto $L'$ with kernel $N$, so $L - N \cong L'$ by Theorem 3. To prove $M - L \cong M' - L'$, consider the natural homomorphism $M \to M' \to M' - L'$. Its kernel consists of those $x \in M$ with $xT \in L'$, i.e., $x \in L'T^{-1} = L$. By Theorem 3, $M - L \cong M' - L'$.
