---
role: proof
locale: en
of_concept: left-kan-extension-as-coend
source_book: gtm005
source_chapter: "X"
source_section: "4. Kan Extensions as Coends"
---

**Proof.** By the parameter theorem, we regard the coend $Lc = \int^m C(Km, c) \cdot Tm$ as a functor of $c$. Let $S: C \to A$ be any functor. Then we compute:

$$\begin{aligned}
\mathrm{Nat}(L, S) &\cong \int_c A(Lc, Sc) \quad \text{(end formula for Nat)}\\
&\cong \int_c A\left(\int^m C(Km, c) \cdot Tm,\; Sc\right) \quad \text{(definition of } L\text{)}\\
&\cong \int_c \int_m A\big(C(Km, c) \cdot Tm,\; Sc\big) \quad \text{(continuity of } A(-, Sc) \text{ as a coend)}\\
&\cong \int_c \int_m \mathrm{Ens}\big(C(Km, c),\; A(Tm, Sc)\big) \quad \text{(definition of copower)}\\
&\cong \int_m \int_c \mathrm{Ens}\big(C(Km, c),\; A(Tm, Sc)\big) \quad \text{(Fubini theorem for ends)}\\
&\cong \int_m A(Tm, SKm) \quad \text{(Yoneda lemma and end formula)}\\
&\cong \mathrm{Nat}(T, SK) \quad \text{(end formula for Nat)}.
\end{aligned}$$

Each isomorphism is natural in $S$, and the composite gives the bijection $\mathrm{Nat}(L, S) \cong \mathrm{Nat}(T, SK)$ required for $L$ to be the left Kan extension. The Fubini theorem (interchange of ends) applies because both indicated ends exist, while $\mathrm{Ens}$ must be a sufficiently large category of sets containing all relevant hom-sets and natural transformation sets.
