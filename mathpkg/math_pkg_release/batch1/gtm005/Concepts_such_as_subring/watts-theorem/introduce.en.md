---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Watt's Theorem characterizes representable contravariant additive functors on module categories. The key observation is that a ring $R$, as an $R$-module, is a generator in $R\text{-}\mathbf{Mod}$, and therefore a cogenerator in the opposite category. Applying the Special Adjoint Functor Theorem to the functor $T : (R\text{-}\mathbf{Mod})^{\mathrm{op}} \to \mathbf{Ab}$ (which preserves limits by hypothesis on colimits) yields a left adjoint $F$. By additivity, the adjunction $\mathbf{Ab}(G, T A) \cong \mathrm{Hom}_R(A, F G)$ for $G \in \mathbf{Ab}$ implies that $T \cong \mathrm{Hom}_R(-, F\mathbb{Z})$, giving the representing module $C = F\mathbb{Z}$.
