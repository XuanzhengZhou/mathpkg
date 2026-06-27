---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Every matrix can be reduced to a canonical block-diagonal form consisting of an identity block of size equal to the rank and zeros elsewhere, using only elementary row and column operations plus non-zero scaling. This is the matrix-level counterpart to the basis-change argument that defines the normal form of a linear map. The reduction algorithm proceeds by moving a nonzero entry to the top-left corner, normalizing it, then clearing the rest of the first row and column, and iterating on the remaining submatrix.
