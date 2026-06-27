---
role: proof
locale: en
of_concept: lemma-r-normal-form
source_book: gtm059
source_chapter: "5. Iwasawa Theory and Ideal Class Groups"
source_section: "3. Modules over Z_p[[T]]"
---

**Proof.** Using operation (O.1) with respect to each of the first $r-1$ rows, we may assume without loss of generality that any given power $p^k$ divides all elements of the matrix $R$, and that $R$ can be transformed into a matrix which has already been partially diagonalized.

Since $R$ is in $(r-1)$-normal form, the first $r-1$ diagonal entries $\lambda_1, \dots, \lambda_{r-1}$ are distinguished polynomials with $\deg^0(R) = \deg \lambda_i$ for $i = 1, \dots, r-1$. Among the entries in rows $r$ and below, consider those that are not divisible by $p$. Since the module is finitely generated and $A$ is Noetherian, there exists an entry $a$ among these with minimal Weierstrass degree, after applying admissible transformations that leave the first $r-1$ rows unchanged.

By applying row and column operations (which are admissible), we may move this entry to the $(r,r)$ position. If the resulting entry $a_{rr}$ is not a distinguished polynomial, we may apply operation (O.2) or (O.3) to adjust the module by pseudo-isomorphism so that it becomes distinguished. Furthermore, since $p^k$ divides all entries for arbitrarily large $k$, the off-diagonal entries in the $r$-th row and column can be eliminated by elementary row and column operations.

After these operations, the matrix takes the form where the $r$-th diagonal entry is a distinguished polynomial $\lambda_r$ with $\deg \lambda_r = \deg^0(R)$, and all other entries in the first $r$ rows and columns are zero. This is precisely the $r$-normal form, and the operations used are all admissible (or row/column operations). The dimension of the matrix is preserved throughout, completing the proof. $\square$
