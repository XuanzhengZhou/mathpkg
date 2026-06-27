---
role: proof
locale: en
of_concept: properties-of-tilde-functor
source_book: gtm052
source_chapter: "II"
source_section: "5"
---

The map $M \to \widetilde{M}$ is clearly functorial. It is exact because localization is exact, and exactness of sheaves can be measured at the stalks (use Ex. 1.2 and (5.1b)). It commutes with direct sum and tensor product because these operations commute with localization.

To say it is fully faithful means $\operatorname{Hom}_A(M, N) = \operatorname{Hom}_{\mathcal{O}_X}(\widetilde{M}, \widetilde{N})$ for any $A$-modules $M$ and $N$. The functor $\sim$ gives a natural map $\operatorname{Hom}_A(M, N) \to \operatorname{Hom}_{\mathcal{O}_X}(\widetilde{M}, \widetilde{N})$. Applying the global sections functor $\Gamma$ and using (5.1d) gives a map the other way. These two maps are clearly inverse to each other, hence isomorphisms.

The statements about $f_*$ and $f^*$ follow directly from the definitions: for a $B$-module $N$, $f_*(\widetilde{N})$ evaluated on a distinguished open $D(g) \subseteq \operatorname{Spec} A$ is $\widetilde{N}(f^{-1}(D(g))) = N_{g}$, which equals $({}_{A}N)_g$, so $f_*(\widetilde{N}) \cong ({}_{A}N)^{\sim}$. For $f^*(\widetilde{M})$, we have $f^*(\widetilde{M}) = f^{-1}(\widetilde{M}) \otimes_{f^{-1}\mathcal{O}_{\operatorname{Spec} A}} \mathcal{O}_{\operatorname{Spec} B}$, which localizes to $(M \otimes_A B)^{\sim}$.
