---
role: proof
locale: en
of_concept: contractible-implies-absolute-coequalizer
source_book: gtm026
source_chapter: "3"
source_section: "1"
---

Let $H: \mathcal{K} \to \mathcal{L}$ be any functor. It is obvious that $(fH, gH, hH; dH, d'H)$ is again a contractible coequalizer in $\mathcal{L}$, so it suffices to prove that $h = \operatorname{coeq}(f, g)$.

Suppose $f \cdot h' = g \cdot h'$ as shown below. Then
$$h \cdot d' \cdot h' = d \cdot g \cdot h' = d \cdot f \cdot h' = h'.$$
The uniqueness of $d' \cdot h'$ is secure since $h$ is (split) epi: indeed $h \cdot d' = \mathrm{id}_C$ shows $h$ is a split epimorphism, hence an epimorphism.
