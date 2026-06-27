---
role: proof
locale: en
of_concept: commutator-subgroup-lie-algebra
source_book: gtm021
source_chapter: "10"
source_section: "Differentials of Morphisms"
---
For fixed $x \in A$, the commutator map $\gamma_x(y) = yxy^{-1}x^{-1}$ maps $B$ into $C$, so its differential $(d\gamma_x)_e = 1 - \operatorname{Ad} x$ maps $\mathfrak{b}$ into $\mathfrak{c}$. Thus $Y - \operatorname{Ad} x(Y) \in \mathfrak{c}$ for all $Y \in \mathfrak{b}, x \in A$.

Similarly, for fixed $y \in B$, the map $x \mapsto xyx^{-1}y^{-1}$ has differential $1 - \operatorname{Ad} y$ at $e$, which maps $\mathfrak{a}$ into $\mathfrak{c}$, so $X - \operatorname{Ad} y(X) \in \mathfrak{c}$ for all $X \in \mathfrak{a}, y \in B$.

Now fix $Y \in \mathfrak{b}$ and consider the map $A \to \mathfrak{c}$ sending $x \mapsto Y - \operatorname{Ad} x(Y)$. Differentiating this at $e$: since $d(\operatorname{Ad})_e = \operatorname{ad}$, the differential sends $X \in \mathfrak{a}$ to $-\operatorname{ad} X(Y) = -[X, Y]$. Therefore $[X, Y] \in \mathfrak{c}$ for all $X \in \mathfrak{a}, Y \in \mathfrak{b}$.
