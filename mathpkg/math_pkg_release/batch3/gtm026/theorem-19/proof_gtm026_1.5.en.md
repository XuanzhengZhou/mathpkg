---
role: proof
locale: en
of_concept: theorem-19
source_book: gtm026
source_chapter: "1"
source_section: "5.6"
---

Let $\bar{T}$ be the canonical lift of $T$ to $\mathcal{A}$ (5.3). (Set, surjections, injections) is a regular category. It follows from 4.16 that $(\mathcal{A}, E, M)$ is a regular category with $E =$ admissible surjections and $M =$ optimal injections. Since $T$ preserves surjections (1.4.29), $\bar{T}$ preserves $E$ (as remarked in the proof of 5.2, $f\bar{T}$ is the function $fT$). Since $\mathcal{C}$ is a full replete subcategory of $\mathcal{A}^{\bar{T}}$ it suffices to show that $\mathcal{C}$ is closed under products, "optimal injective $T$-homomorphisms into" and "$T$-homomorphisms which are split epimorphisms in $\mathcal{A}$ out of," since then $\mathcal{C}$ is an $E$-Birkhoff subcategory of $\mathcal{A}^{\bar{T}}$ (use 4.23(2) noting that, by 2.3.29, the optimal injective maps are exactly the equalizers in $\mathcal{A}$) and algebraic over $\mathcal{A}$ in particular (3.3).

(5.7) $\mathcal{C}$ is closed under products. Given $(X_i, s_i, \xi_i)$ in $\mathcal{C}$ with product $p_i:(X, s, \xi)$ $\longrightarrow (X_i, s_i, \xi_i)$ in $\mathcal{A}^{\bar{T}}$ we have, for each $\alpha:(U^{\bar{T}})^n \longrightarrow U^{\bar{T}}$ the commutative diagram

$$\begin{array}{cccc}
X^n & (p_i)^n & (X_i)^n \\
(X, \xi) \alpha & (X_i, s_i, \xi_i) \alpha \\
X & p_i & X_i
\end{array}$$

Since $f^n:(K^n, s^n) \longrightarrow (L^n, t^n)$ is admissible whenever $f:(K, s) \longrightarrow (L, t)$ is (it is categor

(5.9) $\mathcal{C}$ is closed under $U^{\mathbf{T}}$-split epimorphisms. Let $(X, s, \xi) \in \mathcal{C}$ and let $f: (X, s, \xi) \longrightarrow (Y, t, \theta) \in \mathcal{A}^{\mathbf{T}}$ and $d: (Y, t) \longrightarrow (X, s) \in \mathcal{A}$ satisfy $d.f = \mathrm{id}_Y$. Consider the diagram

induced by the semantic operation $\alpha: (U^{\mathbf{T}})^n \longrightarrow U^{\mathbf{T}}$. Then $(Y, \theta)\alpha = d^n.(X, \xi)\alpha.f: (Y^n, t^n) \longrightarrow (Y, t)$ is admissible.

The proof of 5.6 does not provide much information about the nature of the algebraic theory in $\mathcal{A}$ which gives rise to $V$. The following elementary observation greatly simplifies this problem.

5.10 Taut Birkhoff Subcategories. In the context of 5.1, let $\mathcal{C}$ be an abstract Birkhoff subcategory of $\mathcal{P}$ (of course, $U_1$ is known to be algebraic by 5.2) with the additional property that $\mathcal{C}$ is taut as in 2.3.37, that is, $\mathcal{C}$ has the property that whenever $f_i: P \longrightarrow C_i$ is a family of morphisms in $\mathcal{P}$ with each $C_i$ in $\mathcal{C}$ such that $f_i U_1$ constitutes an optimal family in $\mathcal{A}$, then $P$ is also in $\mathcal{C}$. Under these conditions, the algebraic theory in $\mathcal{A}$ giving rise to $V$ is very simple to describe in the style of the $\bar{T}$ of 5.2. For each $(K, s)$ in $\mathcal{A}$ let $\mathcal{C}(K, s)$ denote the subclass of $\mathcal{F}(K, s)$ of all $(f, L, \xi, t)$ such that $(L, t, \xi) \in \mathcal{C}$. Define $(

setting $f = K\eta.g$, $g = f^{\#} = fT.\xi$ with $(f, L, \xi, t) \in \mathcal{C}(K, s)$. Therefore $id_{KT} : (KT, \bar{s}, K\mu) \longrightarrow (KT, \hat{s}, K\mu)$ is the reflection $(K, s)\lambda$ of $(K, s)\bar{T}, (K, s)\bar{\mu})$ in $\mathcal{C}$. It follows from the constructions in 3.2 and 3.3 that $\hat{T}$ is the algebraic theory for $V$ with $\eta, \circ, T$ as a functor and $\mu$ all at the level of $T$ (just as for $\bar{T}$ in 5.2).

Returning to the context of 5.6, we have:

(5.11) The algebraic theory in $\mathcal{A}$ giving rise to $V:\mathcal{C} \longrightarrow \mathcal{A}$ is given by $(X, s)\hat{T} = (XT, \hat{s})$ where $\hat{s}$ is the cartesian lift of the family $(KT \xrightarrow{g}(L, t))$: there exists $\xi$ with $(L, t, \xi) \in \mathcal{C}$ and $g:(KT, K\mu) \longrightarrow (L, \xi)$ a $\mathbf{T}$-homomorphism. $K\eta:(K, s) \longrightarrow (K, s)\hat{T}$ is admissible and if $\alpha:(K_1, s_1) \longrightarrow (K_2, s_2)\hat{T}$ and $\beta:(K_2, s_2) \longrightarrow (K_3, s_3)\hat{T}$ are admissible then so is $\alpha \circ \beta:(K_1, s_1) \longrightarrow (K_3, s_3)\hat{T}$ thereby providing the $\eta$ and $\circ$ for the algebraic theory $\hat{T} = (\hat{T}, \eta, \circ)$. To prove this, we must only be sure that 5.10 applies. But this is clear
