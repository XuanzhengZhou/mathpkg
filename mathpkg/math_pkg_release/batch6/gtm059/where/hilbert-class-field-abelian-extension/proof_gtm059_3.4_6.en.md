---
role: proof
locale: en
of_concept: hilbert-class-field-abelian-extension
source_book: gtm059
source_chapter: "3"
source_section: "4.6"
---

*Proof.* For any ideal class $c \in C_K$, let $\mathfrak{a}$ be an integral ideal representing $c$. The Artin symbol $(\mathfrak{a}, K/F)$ is an element of $\operatorname{Gal}(K/F)$. When restricted to the Hilbert class field $H$ of $F$, the restriction map

$$
\operatorname{Gal}(K/F) \longrightarrow \operatorname{Gal}(H/F)
$$

sends $(\mathfrak{a}, K/F)$ to $(N_{K/F}(\mathfrak{a}), H/F)$, by the functorial properties of the Artin symbol with respect to norm maps. This establishes the first identity.

For the isomorphism $C_F \cong \operatorname{Gal}(H/F)$, this is the fundamental theorem of class field theory: the Artin symbol provides a canonical isomorphism between the ideal class group of $F$ and the Galois group of its Hilbert class field. The surjectivity of the norm map $N_{K/F}$ then follows because the restriction map $\operatorname{Gal}(K/F) \to \operatorname{Gal}(H/F)$ is surjective when $K \cap H = F$, and the image of $C_K$ under $N_{K/F}$ corresponds to the subgroup $\operatorname{Gal}(H/K \cap H)$ of $\operatorname{Gal}(H/F)$. This proves the lemma.
