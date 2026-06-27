---
role: proof
locale: en
of_concept: theorem-krull-domain
source_book: gtm029
source_chapter: "VI"
source_section: "13"
---

Let $v \in (F)$, and let $p(v)$ denote its center on $R$. Since the quotient ring $R_{p(v)}$ is the valuation ring $(E_4)$ of a discrete, rank 1 valuation $(E_1)$, $p(v)R_{p(v)}$ is its unique proper prime ideal. Thus, taking into account the relations between prime ideals in $R$ and in $R_{p(v)}$ (Vol. I, Ch. IV, § 11, Theorem 19), $p(v)$ is a minimal prime ideal in $R$.

Conversely we have to show that every minimal prime ideal $p$ in $R$ is the center of some valuation $v$ in $(F)$. More generally we shall prove that every proper prime ideal $p$ in $R$ contains the center $p(v)$ of some valuation $v$ in $(F)$. Suppose this is not so. Take an element $x \neq 0$ in $p$. Since $p \neq R$, $x$ is not a unit in $R$. Hence $v\left(\frac{1}{x}\right) < 0$ for at least one valuation $v$ in $(F)(E_2)$. Denote by $v_1, \dots, v_n$ the valuations $v$ in $(F)$ such that $v(x) > 0$ $(E_3)$

PROOF. For the necessity we observe that if $v$ is the $a$-adic valuation of a UFD $R$ (a being an irreducible element in $R$), we have $v(a) = 1$, and $w(a) = 0$ for every other $b$-adic valuation $w$ of $R$ such that $w \neq v$. Conversely, suppose the existence of the elements $a_v$ in $R$. These elements are irreducible, since, from $a_v = xy$ with $x$ and $y$ in $R$, we deduce $v(x) + v(y) = 1$ and $w(x) + w(y) = 0$ for every $w \neq v$ in $(F)$, whence $w(x) = w(y) = 0$ and either $v(x) = 0$ and $v(y) = 1$ or $v(x) = 1$ and $v(y) = 0$; therefore either $x$ or $y$ is a unit in $R$ since it has values 0 for all valuations in $(F)$ (use $(E_2)$). Secondly, for every element $x$ in $R$ we can write $x = u \cdot \prod_v a_v^{v(x)}$; from this we deduce that $v(u) = 0$ for all $v$ in $(F)$, i.e., that $u$ is a unit in $R$ (since $u$ and $1/u$ belong to $R$ by $(E_2)$). Lastly such a representation $x = u \cdot \prod_v a_v^{n(v)}$ (u: unit in $R$; the $n(v)$ almost all zero) is necessarily unique, since $v(x) = v(u) + n(v)v(a_v) + \sum_{w \neq v} n(w)v(a_w)$ and since therefore $v(x)$ is equal to $n(v)$ by the hypothesis made on the elements $a_v$. These facts show that $R$ is a UFD.
