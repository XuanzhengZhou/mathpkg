---
role: proof
locale: en
of_concept: yoneda-correspondence-for-natural-transformations
source_book: gtm005
source_chapter: "III"
source_section: "2"
---

Given functors $F, G: C \to D$, the Yoneda Lemma establishes a bijection between natural transformations $F \Rightarrow G$ and certain families of morphisms.

Specifically, applying the Yoneda embedding $Y: D \to \mathbf{Set}^{D^{\mathrm{op}}}$, we obtain representable presheaves $D(-, F(c))$ and $D(-, G(c))$ for each $c \in C$. A natural transformation $\tau: F \Rightarrow G$ induces maps $D(-, \tau_c): D(-, F(c)) \Rightarrow D(-, G(c))$.

The Yoneda Lemma identifies $\operatorname{Nat}(D(-, F(c)), D(-, G(c))) \cong D(F(c), G(c))$, and the collection of these identifications, as $c$ varies, reconstructs the original natural transformation $\tau$. This establishes the correspondence between natural transformations and their actions on representable presheaves.
