---
role: proof
locale: en
of_concept: unit-iff-principal-ideal-equals-ring
source_book: gtm028
source_chapter: "IV"
source_section: "1"
---

If $a$ is a unit, then $a^{-1} \in R$. For any $x \in R$, we have $x = x \cdot 1 = x(a^{-1}a) = (xa^{-1})a \in Ra$. Thus $R \subseteq Ra$, and obviously $Ra \subseteq R$, so $Ra = R$.

Conversely, if $Ra = R$, then $1 \in Ra$ (since $R$ has identity), so $1 = xa$ for some $x \in R$. As $R$ is commutative, $x = a^{-1}$, so $a$ is a unit.
