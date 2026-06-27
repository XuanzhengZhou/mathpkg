---
role: proof
locale: en
of_concept: comparison-theorem-for-kleisli-construction
source_book: gtm005
source_chapter: "VI"
source_section: "5. Free Algebras for a Monad"
---

**Proof sketch.** Define the functor $L : X_T \to A$ on objects by $L(x_T) = Fx$ for each $x \in X$, and on an arrow $f^\flat : x_T \to y_T$ (corresponding to $f : x \to Ty = GFy$ in $X$) by

$$L(f^\flat) = \varepsilon_{Fy} \circ F(f) : Fx \to FGFy \to Fy.$$

This definition is forced by the conditions $LF_T = F$ (which requires $L(x_T) = Fx$) and $GL = G_T$ (which determines the action on morphisms). One verifies that $L$ preserves identities and composition using the properties of the adjunction and the monad $T$. The uniqueness of $L$ follows from an application of Proposition IV.7.1 on maps of adjunctions, using a somewhat different argument than the one for the Eilenberg-Moore comparison theorem. (The proof is left to the reader in the original text.)
