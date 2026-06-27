---
role: proof
locale: en
of_concept: linear-endomorphism-algebra-of-direct-sum-equals-kronecker-product
source_book: gtm031
source_chapter: ""
source_section: "10. Alternative definition of an algebra"
---

The relation $\mathfrak{L}(\mathfrak{R} \times \mathfrak{S}, \mathfrak{R} \times \mathfrak{S}) \cong \mathfrak{L}(\mathfrak{R}, \mathfrak{R}) \times \mathfrak{L}(\mathfrak{S}, \mathfrak{S})$ holds at the vector space level by Theorem 4 (which established the isomorphism for the underlying vector spaces). To verify that this is an algebra isomorphism, we need to check that multiplication (composition of linear transformations) is preserved.

For $A_1, B_1 \in \mathfrak{L}(\mathfrak{R}, \mathfrak{R})$ and $A_2, B_2 \in \mathfrak{L}(\mathfrak{S}, \mathfrak{S})$, the corresponding transformations in $\mathfrak{L}(\mathfrak{R} \times \mathfrak{S}, \mathfrak{R} \times \mathfrak{S})$ are $A_1 \times A_2$ and $B_1 \times B_2$ respectively. Their composition is

$$(A_1 \times A_2)(B_1 \times B_2) = (A_1B_1) \times (A_2B_2),$$

which corresponds exactly to the product $(A_1 \times A_2)(B_1 \times B_2)$ in the Kronecker product algebra $\mathfrak{L}(\mathfrak{R}, \mathfrak{R}) \times \mathfrak{L}(\mathfrak{S}, \mathfrak{S})$ as defined by formula (38). Thus the vector space isomorphism respects the algebra multiplication, establishing the algebra isomorphism.
