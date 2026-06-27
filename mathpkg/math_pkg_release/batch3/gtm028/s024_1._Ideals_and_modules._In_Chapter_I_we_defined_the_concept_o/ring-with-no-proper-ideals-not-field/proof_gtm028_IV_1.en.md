---
role: proof
locale: en
of_concept: ring-with-no-proper-ideals-not-field
source_book: gtm028
source_chapter: "IV"
source_section: "1"
---

Consider the set $\mathfrak{A}$ of all elements $a$ of $R$ such that $Ra$ is the zero ideal. In other words, $\mathfrak{A}$ is the set of all absolute zero divisors of $R$. Since we have assumed that $R$ is not a field, there exist elements $a$ in $R$, different from zero, such that $Ra = (0)$. Thus $\mathfrak{A} \neq (0)$.

It is clear that $\mathfrak{A}$ is an ideal: if $a_1, a_2 \in \mathfrak{A}$, then for any $x \in R$, $x(a_1 - a_2) = xa_1 - xa_2 = 0 - 0 = 0$, so $a_1 - a_2 \in \mathfrak{A}$; and if $a \in \mathfrak{A}$, $b \in R$, then $x(ba) = (xb)a = 0$ for all $x$, so $ba \in \mathfrak{A}$. Since $R$ has no proper ideals, $\mathfrak{A} = R$.

Thus $ab = 0$ for all $a, b \in R$, i.e., the multiplication is trivial. Now every subgroup of the additive group of $R$ is an ideal (since all products are zero). Since $R$ has no proper ideals, the additive group has no proper subgroups, hence it is cyclic of prime order.
