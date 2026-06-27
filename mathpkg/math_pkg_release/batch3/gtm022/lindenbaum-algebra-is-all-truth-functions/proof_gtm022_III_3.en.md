---
role: proof
locale: en
of_concept: "lindenbaum-algebra-is-all-truth-functions"
source_book: gtm022
source_chapter: "III"
source_section: "3"
---
Proof. The constant functions $0, 1 \in L(X_n)$ since $0 = \bar{F}$ and $1 = \overline{F \Rightarrow F}$. Thus the result holds for $n = 0$.

If $f, g$ are truth functions $\mathbb{Z}_2^n \to \mathbb{Z}_2$, define $f \Rightarrow g$ by $(f \Rightarrow g)(z_1, \ldots, z_n) = f(z_1, \ldots, z_n) \Rightarrow g(z_1, \ldots, z_n)$. The coordinate functions $u_i(z_1, \ldots, z_n) = z_i$ belong to $L(X_n)$ since $u_i = \bar{x}_i$. Since every truth function can be built from coordinate functions using the $\Rightarrow$ operation (as in the proof of functional completeness), all truth functions belong to $L(X_n)$. $\square$
