---
role: proof
locale: en
of_concept: associates-in-integral-domain
source_book: gtm028
source_chapter: "I"
source_section: "14"
---

Assume $b \mid a$ and $a \mid b$ in an integral domain $R$. Then there exist $c, c' \in R$ such that $a = bc$ and $b = ac'$. Substituting, we obtain $a = ac'c$. Since $R$ is an integral domain and $a$ may be zero (if $a = 0$, then $b = 0$ trivially and they are associates via the unit $1$), we consider the non-zero case. Cancelling $a$ from $a = a(c'c)$ yields $c'c = 1$. Thus $c$ and $c'$ are units in $R$, and $a = bc$ with $\epsilon = c$ a unit, so $a$ and $b$ are associates. Conversely, if $a = b\epsilon$ with $\epsilon$ a unit, then $b \mid a$ trivially, and $b = a\epsilon^{-1}$ shows $a \mid b$.
