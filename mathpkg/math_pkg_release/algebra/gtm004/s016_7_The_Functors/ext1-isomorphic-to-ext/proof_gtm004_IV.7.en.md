---
role: proof
locale: en
of_concept: ext1-isomorphic-to-ext
source_book: gtm004
source_chapter: "IV. Derived Functors"
source_section: "7. The Functors Ext^n_A Using Projectives"
---

# Proof of Proposition 7.1: Isomorphism Between Ext^1 and the Classical Ext Group

**Proposition 7.1.** $\operatorname{Ext}_A^1(A, B) \cong \operatorname{Ext}_A(A, B)$.

*Proof.* We consider the projective presentation $R_1 \xrightarrow{\mu} P_0 \xrightarrow{\varepsilon} A$ of $A$ and apply Proposition 5.8 (the contravariant analog of Proposition 5.5). We obtain the exact sequence

$$\operatorname{Hom}_A(P_0, B) \xrightarrow{\mu^*} \operatorname{Hom}_A(R_1, B) \to \operatorname{Ext}_A^1(A, B) \to 0.$$

Thus $\operatorname{Ext}_A^1(A, B)$ can be identified with the cokernel of $\mu^*$:

$$\operatorname{Ext}_A^1(A, B) \cong \operatorname{Coker}\big(\operatorname{Hom}_A(P_0, B) \xrightarrow{\mu^*} \operatorname{Hom}_A(R_1, B)\big).$$

On the other hand, by the definition of the classical Ext group $\operatorname{Ext}_A(A, B)$ (Section III.2), an element of $\operatorname{Ext}_A(A, B)$ is represented by an equivalence class of short exact sequences $B \rightarrowtail E \twoheadrightarrow A$, and there is a natural isomorphism

$$\operatorname{Ext}_A(A, B) \cong \operatorname{Coker}\big(\operatorname{Hom}_A(P_0, B) \to \operatorname{Hom}_A(R_1, B)\big)$$

obtained by pulling back the projective presentation along morphisms $\varphi: R_1 \to B$. Comparing the two descriptions yields the isomorphism

$$\operatorname{Ext}_A^1(A, B) \cong \operatorname{Ext}_A(A, B).$$

$\square$
