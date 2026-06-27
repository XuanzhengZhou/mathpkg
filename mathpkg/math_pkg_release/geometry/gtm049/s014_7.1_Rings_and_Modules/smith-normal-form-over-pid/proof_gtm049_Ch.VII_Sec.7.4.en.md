---
role: proof
locale: en
of_concept: smith-normal-form-over-pid
source_book: gtm049
source_chapter: "VII"
source_section: "7.4"
---
Let $(v_i), (v_j')$ be any ordered bases of $E, E'$, respectively, and suppose the matrix of $g$ is $C$. We restrict attention to ordered bases of $E$ and $E'$ that can be obtained from $(v_i)$ and $(v_j')$ by elementary moves.

An elementary move on $(v_i)$ changes $C$ by either an interchange of two rows or the addition of a multiple of one row to another. An elementary move on $(v_j')$ changes the columns of $C$ in a similar manner.

The proof essentially follows the algorithm implicit in the proof of Theorem 1. Among all matrices obtainable from $C$ by elementary row and column operations, choose one whose $(1,1)$-entry has minimal degree among all non-zero entries that can appear in the $(1,1)$-position. By using the division algorithm in $F[X]$ and elementary operations, all other entries in the first row and first column can be made divisible by this $(1,1)$-entry and subsequently reduced to zero.

Proceeding inductively on the remaining submatrix yields a diagonal matrix where each diagonal entry divides the next. The divisibility condition $d_i \mid d_{i+1}$ follows from the fact that if an entry $d_{i+1}$ were not divisible by $d_i$, further elementary operations could reduce its degree.

The invariant factors of $E'/Eg$ are precisely the non-unit diagonal entries. This follows because $d_1 e_1', \ldots, d_t e_t'$ generate the image $E g$, and the quotient $E'/Eg$ decomposes as the direct sum of cyclic modules with annihilators $[d_{s+1}], \ldots, [d_t]$, where $d_1, \ldots, d_s$ are non-zero constants (units in $F[X]$). These annihilators are independent of the choice of bases, establishing uniqueness.
