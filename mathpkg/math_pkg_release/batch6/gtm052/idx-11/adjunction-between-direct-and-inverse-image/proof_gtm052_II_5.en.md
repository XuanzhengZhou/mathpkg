---
role: proof
locale: en
of_concept: adjunction-between-direct-and-inverse-image
source_book: gtm052
source_chapter: "II"
source_section: "5"
---

By definition, $f^*\mathcal{G} = f^{-1}\mathcal{G} \otimes_{f^{-1}\mathcal{O}_Y} \mathcal{O}_X$. The adjunction between tensor product and Hom gives:
$$\operatorname{Hom}_{\mathcal{O}_X}(f^{-1}\mathcal{G} \otimes_{f^{-1}\mathcal{O}_Y} \mathcal{O}_X, \mathcal{F}) \cong \operatorname{Hom}_{f^{-1}\mathcal{O}_Y}(f^{-1}\mathcal{G}, \mathcal{F}).$$
Now the adjunction between $f^{-1}$ and $f_*$ at the level of sheaves of abelian groups (Ex. 1.18) yields:
$$\operatorname{Hom}_{f^{-1}\mathcal{O}_Y}(f^{-1}\mathcal{G}, \mathcal{F}) \cong \operatorname{Hom}_{\mathcal{O}_Y}(\mathcal{G}, f_*\mathcal{F}),$$
where the $\mathcal{O}_Y$-module structure on $f_*\mathcal{F}$ comes from the morphism $\mathcal{O}_Y \to f_*\mathcal{O}_X$. Composing these isomorphisms gives the desired adjunction.
