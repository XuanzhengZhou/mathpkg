---
role: proof
locale: en
of_concept: truth-functions-complete
source_book: gtm022
source_chapter: "II"
source_section: "3"
---

The constant functions $0, 1 \in L(X_n)$ since $0 = \bar{F}$ and $1 = \overline{F \Rightarrow F}$. Thus the result holds for $n = 0$.

If $f, g$ are truth functions $\mathbb{Z}_2^n \to \mathbb{Z}_2$, we define the truth function $f \Rightarrow g$ by $(f \Rightarrow g)(z_1, \ldots, z_n) = f(z_1, \ldots, z_n) \Rightarrow g(z_1, \ldots, z_n)$. The set of truth functions is closed under this operation. Since $L(X_n)$ contains the coordinate functions (the variables $x_1, \ldots, x_n$) and is closed under $\Rightarrow$ (and $F$), and every truth function can be built from coordinate functions using $\Rightarrow$ and $F$, it follows that $L(X_n)$ equals the set of all truth functions.
