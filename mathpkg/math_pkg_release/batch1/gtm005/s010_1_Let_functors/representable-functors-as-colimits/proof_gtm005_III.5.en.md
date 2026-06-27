---
role: proof
locale: en
of_concept: representable-functors-as-colimits
source_book: gtm005
source_chapter: "III"
source_section: "5"
---

Every presheaf $K: D^{\mathrm{op}} \to \mathbf{Set}$ is a colimit of representable presheaves. Consider the category of elements $\int_D K$: objects are pairs $(d, x)$ with $x \in K(d)$, morphisms $f: (d, x) \to (d', x')$ are maps $f: d \to d'$ with $K(f)(x') = x$.

The projection $\pi: \int_D K \to D$ sends $(d, x) \mapsto d$. Then
$$K \cong \varinjlim_{(d, x) \in \int_D K} D(-, d) = \varinjlim (Y \circ \pi).$$
The cocone components $D(-, d) \Rightarrow K$ correspond via Yoneda to the elements $x \in K(d)$, sending $f \in D(c, d)$ to $K(f)(x) \in K(c)$. The colimit universal property: any cocone from the $D(-, d)$ to a presheaf $P$ factors uniquely through $K$, establishing the isomorphism.

This is the co-Yoneda Lemma (or density of the Yoneda embedding).
