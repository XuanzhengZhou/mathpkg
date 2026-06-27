---
role: proof
locale: en
of_concept: right-kan-extension-via-powers
source_book: gtm005
source_chapter: "X"
source_section: "4. Kan Extensions as Coends"
---

**Proof.** This is dual to the coend formula for left Kan extensions (Theorem 1 of this section). Using the defining property of powers, the Yoneda lemma, and the end formula for natural transformations, one establishes:

$$\begin{aligned}
\mathrm{Nat}(S, R) &\cong \int_c A(Sc, Rc) \\
&\cong \int_c A\left(Sc,\; \int_m Tm^{C(c, Km)}\right) \\
&\cong \int_c \int_m A\big(Sc,\; Tm^{C(c, Km)}\big) \\
&\cong \int_c \int_m \mathrm{Ens}\big(C(c, Km),\; A(Sc, Tm)\big) \\
&\cong \int_m A(SKm, Tm) \cong \mathrm{Nat}(SK, T),
\end{aligned}$$

which exhibits $R$ as $\mathrm{Ran}_K T$. For the additive case, the ordinary power is replaced by the cotensor defined by the adjunction $A(b, c^C) \cong \mathrm{Ab}(C, A(b, c))$.
