---
role: proof
locale: en
of_concept: yoneda-embedding
source_book: gtm005
source_chapter: "III"
source_section: "2"
---

The Yoneda embedding $Y: D \to \mathbf{Set}^{D^{\mathrm{op}}}$ sends $r \mapsto D(-, r)$ on objects and $f \mapsto D(-, f)$ (post-composition) on morphisms. The Yoneda Lemma with $K = D(-, s)$ gives
$$\operatorname{Nat}(Y(r), Y(s)) = \operatorname{Nat}(D(-, r), D(-, s)) \cong D(r, s).$$
This bijection is exactly the action of $Y$ on hom-sets (sending $f$ to $Y(f) = D(-, f)$), proving $Y$ is fully faithful.

Consequently, $Y$ reflects isomorphisms: if $Y(f)$ is an isomorphism, then $f$ is an isomorphism. Also, for any small category $D$, $Y$ embeds $D$ as a full subcategory of the presheaf category $\mathbf{Set}^{D^{\mathrm{op}}}$.
