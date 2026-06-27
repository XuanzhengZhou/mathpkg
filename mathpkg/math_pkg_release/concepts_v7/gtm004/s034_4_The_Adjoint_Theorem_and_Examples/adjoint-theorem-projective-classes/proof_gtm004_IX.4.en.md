---
role: proof
locale: en
of_concept: adjoint-theorem-projective-classes
source_book: gtm004
source_chapter: "IX"
source_section: "4. The Adjoint Theorem and Examples"
---

# Proof of Adjoint Theorem for Projective Classes of Epimorphisms

**Theorem 4.1.** Let $\mathcal{E}$ be a projective class in the abelian category $\mathfrak{A}$ and let $F: \mathfrak{A} \rightarrow \mathfrak{A}'$, $U: \mathfrak{A}' \rightarrow \mathfrak{A}$, where $\mathfrak{A}'$ is also abelian, be a pair of adjoint functors with $U$ faithful. Set $\mathcal{E}' = U^{-1}\mathcal{E}$. Then $\mathcal{E}'$ is a projective class of epimorphisms in $\mathfrak{A}'$. The objects $FP$ where $P$ is $\mathcal{E}$-projective in $\mathfrak{A}$ are $\mathcal{E}'$-projective and are sufficient for $\mathcal{E}'$-presenting objects of $\mathfrak{A}'$, so that the $\mathcal{E}'$-projectives are precisely the direct summands of objects $FP$.

**Proof.** First observe that $F$ sends $\mathcal{E}$-projectives to $\mathcal{E}'$-projectives. For if $P$ is $\mathcal{E}$-projective and $\varepsilon': A_1' \rightarrow A_2'$ is in $\mathcal{E}'$, then $U\varepsilon'$ is in $\mathcal{E}$ by definition of $\mathcal{E}' = U^{-1}\mathcal{E}$. Since $P$ is $\mathcal{E}$-projective, the induced map

$$\operatorname{Hom}_{\mathfrak{A}}(P, U\varepsilon'): \operatorname{Hom}_{\mathfrak{A}}(P, UA_1') \rightarrow \operatorname{Hom}_{\mathfrak{A}}(P, UA_2')$$

is surjective. By the adjunction isomorphism $\operatorname{Hom}_{\mathfrak{A}}(P, U(-)) \cong \operatorname{Hom}_{\mathfrak{A}'}(FP, -)$, it follows that

$$\operatorname{Hom}_{\mathfrak{A}'}(FP, A_1') \rightarrow \operatorname{Hom}_{\mathfrak{A}'}(FP, A_2')$$

is surjective. Hence $FP$ is $\mathcal{E}'$-projective.

Next we show that the objects $FP$, with $P$ $\mathcal{E}$-projective, are sufficient for $\mathcal{E}'$-presentation. Let $A'$ be an arbitrary object of $\mathfrak{A}'$. Consider the counit of the adjunction $\varepsilon_{A'}: FUA' \rightarrow A'$. Since $U$ is faithful, $\varepsilon_{A'}$ is an epimorphism. Moreover, we claim that $\varepsilon_{A'} \in \mathcal{E}'$. Indeed, applying $U$ to $\varepsilon_{A'}$ yields a morphism which, by the triangle identities of the adjunction, has a right inverse (namely the unit $\eta_{UA'}$), hence is a split epimorphism; in particular $U\varepsilon_{A'} \in \mathcal{E}$. Thus $\varepsilon_{A'} \in \mathcal{E}'$. Now choose an $\mathcal{E}$-projective $P$ and an $\mathcal{E}$-epimorphism $\sigma: P \rightarrow UA'$. Then the composite

$$FP \xrightarrow{F\sigma} FUA' \xrightarrow{\varepsilon_{A'}} A'$$

is an epimorphism in $\mathcal{E}'$ from $FP$ to $A'$, showing that objects of the form $FP$ (with $P$ $\mathcal{E}$-projective) are sufficient for $\mathcal{E}'$-presentation.

Finally, if $Q$ is any $\mathcal{E}'$-projective, then by the previous paragraph there exists an $\mathcal{E}'$-epimorphism $FP \rightarrow Q$ with $P$ $\mathcal{E}$-projective. Since $Q$ is $\mathcal{E}'$-projective, this epimorphism splits, so $Q$ is a direct summand of $FP$. Conversely, any direct summand of an $\mathcal{E}'$-projective is $\mathcal{E}'$-projective. Hence the $\mathcal{E}'$-projectives are precisely the direct summands of objects $FP$ where $P$ is $\mathcal{E}$-projective. $\square$
