---
role: proof
locale: en
of_concept: watts-theorem
source_book: gtm005
source_chapter: "V"
source_section: "7. Subobjects and Generators"
---

Since $R$ is a generator in $R\text{-}\mathbf{Mod}$, it is a cogenerator in $(R\text{-}\mathbf{Mod})^{\mathrm{op}}$. The category $(R\text{-}\mathbf{Mod})^{\mathrm{op}}$ is small-complete (since $R\text{-}\mathbf{Mod}$ is small-cocomplete) and has small hom-sets. The functor $T : (R\text{-}\mathbf{Mod})^{\mathrm{op}} \to \mathbf{Ab}$ takes small limits to limits by hypothesis (colimits in $R\text{-}\mathbf{Mod}$ become limits in the opposite category).

Apply the Special Adjoint Functor Theorem to $T$: the category $(R\text{-}\mathbf{Mod})^{\mathrm{op}}$ is small-complete, has small hom-sets, and $R$ is a small cogenerating set. Hence $T$ has a left adjoint $F : \mathbf{Ab} \to (R\text{-}\mathbf{Mod})^{\mathrm{op}}$, giving a natural isomorphism
\[
\mathbf{Ab}(G, T A) \cong \mathrm{Hom}_{R\text{-}\mathbf{Mod}}(A, F G)
\]
for $A \in R\text{-}\mathbf{Mod}$ and $G \in \mathbf{Ab}$.

Taking $G = \mathbb{Z}$, we have $T A \cong \mathbf{Ab}(\mathbb{Z}, T A) \cong \mathrm{Hom}_R(A, F \mathbb{Z})$. Setting $C = F \mathbb{Z}$ yields the desired representation
\[
T \cong \mathrm{Hom}_R(-, C).
\]
