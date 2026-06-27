---
role: proof
locale: en
of_concept: matrix-normal-form-admissible-operations
source_book: gtm059
source_chapter: "5"
source_section: "5"
---
The proof is by induction on the number of rows/columns, using the notion of $r$-normal form and the admissible operations. Define $\deg^0(R)$ as the minimum Weierstrass degree among entries after applying admissible transformations. By the lemma (induction step), if $R$ is in $(r-1)$-normal form with rank $r-1$ diagonalized, one can transform it into $r$-normal form with the same rank. The Euclidean algorithm property (using the Weierstrass Division Theorem) ensures that all off-diagonal entries in the $r$-th row/column can be eliminated. The process terminates when all rows are in normal form, and the diagonal entries are distinguished polynomials (or powers of $p$) ordered by Weierstrass degree.

Returning to the module interpretation, the diagonal matrix corresponds to the quasi-isomorphism $M \sim \bigoplus \Lambda/(f_i)$ stated in Theorem 3.1. If $f, g$ are relatively prime distinguished polynomials, the map $\Lambda/(fg) \to \Lambda/(f) \oplus \Lambda/(g)$ is an embedding with finite cokernel, allowing further decomposition into irreducible factors.
