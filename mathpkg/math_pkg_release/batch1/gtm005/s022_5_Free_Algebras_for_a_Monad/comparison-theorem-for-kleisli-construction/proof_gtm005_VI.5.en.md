---
role: proof
locale: en
of_concept: comparison-theorem-for-kleisli-construction
source_book: gtm005
source_chapter: "VI. Monads and Algebras"
source_section: "5. Free Algebras for a Monad"
---

The proof is left to the reader in the text, with the note that the uniqueness of $L$ requires an application of Proposition IV.7.1 on maps of adjunctions.

**Construction of $L$.** On objects, define $L(x_T) = Fx$ for each $x \in X$. On arrows, for $f^\flat : x_T \to y_T$ (where $f : x \to Ty = GFy$ in $X$), define

$$L(f^\flat) = \varepsilon_{Fy} \circ F(f) : Fx \to Fy.$$

**Verification of $LF_T = F$.** For a morphism $h : x \to y$ in $X$, we have $F_T(h) = (\eta_y \circ h)^\flat : x_T \to y_T$. Then

$$L(F_T(h)) = L((\eta_y \circ h)^\flat) = \varepsilon_{Fy} \circ F(\eta_y \circ h) = \varepsilon_{Fy} \circ F\eta_y \circ Fh = 1_{Fy} \circ Fh = Fh,$$

using the triangular identity $\varepsilon_{Fy} \circ F\eta_y = 1_{Fy}$.

**Verification of $GL = G_T$.** On objects: $GL(x_T) = G(Fx) = Tx = G_T(x_T)$. On arrows $f^\flat : x_T \to y_T$:

$$GL(f^\flat) = G(\varepsilon_{Fy} \circ Ff) = G\varepsilon_{Fy} \circ GFf = \mu_y \circ Tf = G_T(f^\flat),$$

since the monad multiplication is $\mu = G\varepsilon F$.

**Uniqueness.** The uniqueness of $L$ follows from the fact that the condition $LF_T = F$ forces $L(x_T) = Fx$ on objects, and the condition $GL = G_T$ together with the definition of composition in $X_T$ forces the action on morphisms. A formal proof using Proposition IV.7.1 (on maps of adjunctions) shows that any two such functors must coincide.
