---
role: proof
locale: en
of_concept: lemma-determinant-index
source_book: gtm059
source_chapter: "2"
source_section: "11"
---

First, we verify the sign convention making the right-hand side positive. Multiplication by $r'$ gives an endomorphism of $QR'$, which decomposes into $d$ one-dimensional algebras corresponding to the eigenspaces of the Galois action. Composing, we obtain
$$\det(r^* m^n) = \prod_{i=1}^{n} \det(r' m^n) = m^n \prod_{i=1}^{n} R_{i,i}.$$
On the other hand, $r^* m^n$ maps $R$ into itself, and by standard elementary linear algebra over $\mathbb{Z}$, the index is given by the absolute value of the determinant. The sign is determined in Chapter 3, where it is shown to equal $(-1)^{n-1}$ times the order of the minus part of the ideal class group in the cyclotomic field, corresponding to the product of sign factors $(-1)^{n-1}$ of the differences $d - R_{i,i}$.
