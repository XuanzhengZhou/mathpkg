---
role: proof
locale: en
of_concept: closure-under-products-in-birkhoff-subcategories
source_book: gtm026
source_chapter: "5"
source_section: "5.4"
---

Given $(X_i, s_i, \xi_i)$ in $\mathcal{C}$ with product $p_i: (X, s, \xi) \longrightarrow (X_i, s_i, \xi_i)$ in $\mathcal{A}^{\bar{T}}$, we have, for each $\alpha: (U^{\bar{T}})^n \longrightarrow U^{\bar{T}}$, the commutative diagram:

$$
\begin{array}{ccc}
X^n & \xrightarrow{(p_i)^n} & (X_i)^n \\[4pt]
{\scriptstyle (X,\xi)\alpha}\ \downarrow & & \downarrow\ {\scriptstyle (X_i,s_i,\xi_i)\alpha} \\[4pt]
X & \xrightarrow{p_i} & X_i
\end{array}
$$

Since $f^n: (K^n, s^n) \longrightarrow (L^n, t^n)$ is admissible whenever $f: (K, s) \longrightarrow (L, t)$ is admissible, $(p_i)^n$ is admissible. Thus $(X, \xi)\alpha$ is admissible as the composite of admissible maps. Hence $(X, s, \xi) \in \mathcal{C}$. $\square$
