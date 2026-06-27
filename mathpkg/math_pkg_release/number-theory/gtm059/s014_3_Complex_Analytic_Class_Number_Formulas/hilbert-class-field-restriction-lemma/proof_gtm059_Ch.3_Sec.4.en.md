---
role: proof
locale: en
of_concept: hilbert-class-field-restriction-lemma
source_book: gtm059
source_chapter: "3"
source_section: "4.6 The (±1)-conjectures"
---

Let $F$ be a number field and $H$ its Hilbert class field. Let $K$ be an abelian extension of $F$.

By the definition of the Artin symbol, for an unramified prime ideal $\mathfrak{p}$ of $F$, the Artin symbol $(\mathfrak{p}, H/F)$ is the Frobenius automorphism at $\mathfrak{p}$ in $\operatorname{Gal}(H/F)$. The restriction map on Galois groups gives

$$
(\mathfrak{p}, K/F) \big|_H = (\mathfrak{p}, H/F),
$$

since the Frobenius automorphism in the larger extension restricts to the Frobenius in the smaller extension. This extends multiplicatively to all ideals, and hence to all ideal classes $c \in C_F$.

For an ideal class $c \in C_K$, we consider the norm $N_{K/F}(c) \in C_F$. By the functoriality of the Artin symbol under the norm map (a standard result in class field theory), we have

$$
(c, K/F) \big|_H = (N_{K/F}(c), H/F).
$$

This follows from the fact that for a prime ideal $\mathfrak{P}$ of $K$ lying above $\mathfrak{p}$ of $F$, the Frobenius $(\mathfrak{P}, K/F)$ restricts to $(\mathfrak{p}, H/F)^f$ where $f$ is the inertial degree, and the norm of $\mathfrak{P}$ is $\mathfrak{p}^f$.

The isomorphism $\operatorname{Gal}(K/F) \cong \operatorname{Gal}(H/F)$ when $K \cap H = F$ follows from the fact that $K$ and $H$ are linearly disjoint over $F$, and the compositum $KH$ has Galois group isomorphic to the direct product.
