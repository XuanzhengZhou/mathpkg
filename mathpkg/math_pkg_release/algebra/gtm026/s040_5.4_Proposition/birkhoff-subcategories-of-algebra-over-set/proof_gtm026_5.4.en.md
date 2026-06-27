---
role: proof
locale: en
of_concept: birkhoff-subcategories-of-algebra-over-set
source_book: gtm026
source_chapter: "5"
source_section: "5.4"
---

Let $\bar{T}$ be the canonical lift of $T$ to $\mathcal{A}$ (5.3). $(\mathbf{Set}, \text{surjections}, \text{injections})$ is a regular category. It follows from 4.16 that $(\mathcal{A}, E, M)$ is a regular category with $E =$ admissible surjections and $M =$ optimal injections. Since $T$ preserves surjections (1.4.29), $\bar{T}$ preserves $E$ (as remarked in the proof of 5.2, $f\bar{T}$ is the function $fT$). Since $\mathcal{C}$ is a full replete subcategory of $\mathcal{A}^{\bar{T}}$, it suffices to show that $\mathcal{C}$ is closed under products, "optimal injective $T$-homomorphisms into" and "$T$-homomorphisms which are split epimorphisms in $\mathcal{A}$ out of," since then $\mathcal{C}$ is an $E$-Birkhoff subcategory of $\mathcal{A}^{\bar{T}}$ (use 4.23(2) noting that, by 2.3.29, the optimal injective maps are exactly the equalizers in $\mathcal{A}$) and algebraic over $\mathcal{A}$ in particular (3.3).

**(5.7) $\mathcal{C}$ is closed under products.** Given $(X_i, s_i, \xi_i)$ in $\mathcal{C}$ with product $p_i: (X, s, \xi) \longrightarrow (X_i, s_i, \xi_i)$ in $\mathcal{A}^{\bar{T}}$, we have, for each $\alpha: (U^{\bar{T}})^n \longrightarrow U^{\bar{T}}$, the commutative diagram:

$$
\begin{array}{ccc}
X^n & \xrightarrow{(p_i)^n} & (X_i)^n \\[4pt]
{\scriptstyle (X,\xi)\alpha}\ \downarrow & & \downarrow\ {\scriptstyle (X_i,s_i,\xi_i)\alpha} \\[4pt]
X & \xrightarrow{p_i} & X_i
\end{array}
$$

Since $f^n: (K^n, s^n) \longrightarrow (L^n, t^n)$ is admissible whenever $f: (K, s) \longrightarrow (L, t)$ is admissible, $(p_i)^n$ is admissible. Thus $(X, \xi)\alpha$ is admissible as the composite of admissible maps. Hence $(X, s, \xi) \in \mathcal{C}$.

**(5.9) $\mathcal{C}$ is closed under $U^{\bar{T}}$-split epimorphisms.** Let $(X, s, \xi) \in \mathcal{C}$ and let $f: (X, s, \xi) \longrightarrow (Y, t, \theta) \in \mathcal{A}^{\bar{T}}$ and $d: (Y, t) \longrightarrow (X, s) \in \mathcal{A}$ satisfy $d \circ f = \mathrm{id}_Y$. Consider the diagram induced by the semantic operation $\alpha: (U^{\bar{T}})^n \longrightarrow U^{\bar{T}}$. Then $(Y, \theta)\alpha = d^n \circ (X, \xi)\alpha \circ f: (Y^n, t^n) \longrightarrow (Y, t)$ is admissible, being a composite of admissible maps. $\square$
