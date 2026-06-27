---
role: proof
locale: en
of_concept: left-kan-extension-via-coends
source_book: gtm005
source_chapter: "X"
source_section: "4. Kan Extensions as Coends"
---

Define $Lc = \int^m C(Km, c) \cdot Tm$. By the parameter theorem, we regard this coend as a functor of $c$. Compare with any other functor $S: C \to A$. Then

$$\mathrm{Nat}(L, S) \cong \int_c A(Lc, Sc)$$
$$\cong \int_c A\!\left(\int^m C(Km, c) \cdot Tm, \; Sc\right)$$
$$\cong \int_c \int_m A\!\left(C(Km, c) \cdot Tm, \; Sc\right) \quad\text{(continuity of $A(-, Sc)$)}$$
$$\cong \int_c \int_m \mathbf{Ens}\!\left(C(Km, c), \; A(Tm, Sc)\right) \quad\text{(definition of copowers)}$$
$$\cong \int_m \int_c \mathbf{Ens}\!\left(C(Km, c), \; A(Tm, Sc)\right) \quad\text{(Fubini theorem for ends)}$$
$$\cong \int_m A(Tm, SKm) \quad\text{(Yoneda lemma + end formula for Nat)}$$
$$\cong \mathrm{Nat}(T, SK).$$

Here the Fubini theorem (interchange of ends) applies because both indicated ends exist. The step using the Yoneda lemma requires the identification $\mathrm{Nat}(C(Km, -), A(Tm, S-)) \cong A(Tm, SKm)$, which follows from the Yoneda lemma: the natural transformation is determined by its value at $1_{Km}$. Each step is natural in $S$, yielding a natural isomorphism $\mathrm{Nat}(L, S) \cong \mathrm{Nat}(T, SK)$, which characterizes $L$ as $\mathrm{Lan}_K T$.
