---
role: proof
locale: en
of_concept: ring-no-proper-ideals-not-field-cyclic-prime-order
source_book: gtm028
source_chapter: "II"
source_section: "§1. Ideals and modules"
---

Let $\mathfrak{A}$ be the set of all elements $a \in R$ such that $Ra = (0)$, i.e., the set of absolute zero divisors of $R$. Since $R$ is not a field, there exist nonzero elements in $\mathfrak{A}$. The set $\mathfrak{A}$ is an ideal: if $a_1, a_2 \in \mathfrak{A}$, then for any $x \in R$, $x(a_1 - a_2) = xa_1 - xa_2 = 0 - 0 = 0$, so $a_1 - a_2 \in \mathfrak{A}$; and if $a \in \mathfrak{A}$, $b \in R$, then $x(ab) = (xa)b = 0 \cdot b = 0$, so $ab \in \mathfrak{A}$. Since $R$ has no proper ideals and $\mathfrak{A} \neq (0)$, we must have $\mathfrak{A} = R$. Thus $ab = 0$ for all $a, b \in R$.

Now any subgroup of the additive group of $R$ is an ideal (since all products are zero). Since $R$ has no proper ideals, the additive group has no proper subgroups, hence is cyclic of prime order.
