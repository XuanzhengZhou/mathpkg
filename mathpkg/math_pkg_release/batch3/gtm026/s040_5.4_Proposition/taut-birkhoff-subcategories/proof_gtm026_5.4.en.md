---
role: proof
locale: en
of_concept: taut-birkhoff-subcategories
source_book: gtm026
source_chapter: "5"
source_section: "5.4"
---

In the context of 5.1, let $\mathcal{C}$ be an abstract Birkhoff subcategory of $\mathcal{P}$ with the taut property. For each $(K, s)$ in $\mathcal{A}$, let $\mathcal{C}(K, s)$ denote the subclass of $\mathcal{F}(K, s)$ of all $(f, L, \xi, t)$ such that $(L, t, \xi) \in \mathcal{C}$. Define $(K, s)\hat{T} = (KT, \hat{s})$ where $\hat{s}$ is the cartesian lift of the family

$$\{f^\#: KT \longrightarrow (L, t) \mid (f, L, \xi, t) \in \mathcal{C}(K, s)\},$$

setting $f = K\eta \circ g$, $g = f^\# = fT \circ \xi$, with $(f, L, \xi, t) \in \mathcal{C}(K, s)$.

Therefore $\mathrm{id}_{KT}: (KT, \bar{s}, K\mu) \longrightarrow (KT, \hat{s}, K\mu)$ is the reflection $(K, s)\lambda$ of $((K, s)\bar{T}, (K, s)\bar{\mu})$ in $\mathcal{C}$. It follows from the constructions in 3.2 and 3.3 that $\hat{T}$ is the algebraic theory for $V$, with $\eta$, $\circ$, $T$ as a functor, and $\mu$ all at the level of $T$ (just as for $\bar{T}$ in 5.2). $\square$
