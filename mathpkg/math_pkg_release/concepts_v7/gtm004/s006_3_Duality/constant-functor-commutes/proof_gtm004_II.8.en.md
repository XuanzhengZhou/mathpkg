---
role: proof
locale: en
of_concept: constant-functor-commutes
source_book: gtm004
source_chapter: "II"
source_section: "8"
---

# Proof of Constant Functor Commutes with Any Functor

Let $P_{\mathfrak{C}}: \mathfrak{C} \to \mathfrak{C}^{\mathfrak{P}}$ and $P_{\mathfrak{D}}: \mathfrak{D} \to \mathfrak{D}^{\mathfrak{P}}$ be the constant functors (sending each object $X$ to the constant diagram at $X$, and each morphism to the constant natural transformation). Let $F: \mathfrak{C} \to \mathfrak{D}$ be any functor.

The diagram

commutes strictly: for any object $X \in \mathfrak{C}$,

$$F^{\mathfrak{P}} \circ P_{\mathfrak{C}}(X) = F^{\mathfrak{P}}(\text{const}_X) = F \circ \text{const}_X = \text{const}_{FX} = P_{\mathfrak{D}} \circ F(X).$$

Here $\text{const}_X: \mathfrak{P} \to \mathfrak{C}$ is the functor sending every object of $\mathfrak{P}$ to $X$ and every morphism to $1_X$. Post-composing with $F$ yields the functor sending every object to $FX$ and every morphism to $1_{FX}$, which is precisely $\text{const}_{FX} = P_{\mathfrak{D}}(FX)$. The equality on morphisms is equally straightforward.

Thus $F^{\mathfrak{P}} P_{\mathfrak{C}} = P_{\mathfrak{D}} F$, i.e., the constant functor commutes with any functor.
