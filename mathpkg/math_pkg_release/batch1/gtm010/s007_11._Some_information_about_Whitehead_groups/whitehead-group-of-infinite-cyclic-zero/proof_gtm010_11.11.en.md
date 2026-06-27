---
role: proof
locale: en
of_concept: whitehead-group-of-infinite-cyclic-zero
source_book: gtm010
source_chapter: "11"
source_section: "11"
---

Think of Z as {t^i | i = 0, +/-1, +/-2, ...} so that Z(Z) is the set of all finite sums sum n_i t^i. Z(Z) has only trivial units because (at^alpha + ... + bt^beta)(ct^gamma + ... dt^delta) = 1 implies alpha+gamma = beta+delta = 0, hence alpha=beta and gamma=delta.

Given a matrix (a_ij(t)) representing an element W of Wh(Z), multiply each row by a suitably high power of t to eliminate negative powers. Let q be the highest power of t. If q > 1, apply operations to reduce q. Eventually get a matrix with linear entries. Using integral row/column operations, the matrix can be reduced to a 1x1 matrix (a) where a is a trivial unit, so W = 0.
