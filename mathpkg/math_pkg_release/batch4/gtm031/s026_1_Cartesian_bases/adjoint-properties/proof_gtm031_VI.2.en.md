---
role: proof
locale: en
of_concept: adjoint-properties
source_book: gtm031
source_chapter: "VI"
source_section: "2"
---

Using the defining property $(xA, y) = (x, yA')$ and the symmetry $(x, y) = (y, x)$ of the scalar product:

\textbf{(1)} For all $x, y$:
$$(x(A+B), y) = (xA + xB, y) = (xA, y) + (xB, y) = (x, yA') + (x, yB') = (x, yA' + yB') = (x, y(A' + B')).$$
By uniqueness of the adjoint, $(A+B)' = A' + B'$.

\textbf{(2)} For all $x, y$:
$$(x(AB), y) = ((xA)B, y) = (xA, yB') = (x, (yB')A') = (x, y(B'A')).$$
Thus $(AB)' = B'A'$.

\textbf{(3)} Using symmetry of $(x, y)$:
$$(xA', y) = (y, xA') = (yA, x) = (x, yA).$$
Since $(xA', y) = (x, yA'')$ by definition, we have $(x, yA'') = (x, yA)$ for all $x, y$, hence $A'' = A$.

Equivalently, with respect to a Cartesian basis, the matrix of $A'$ is the transpose of the matrix of $A$, and these properties reflect the well-known identities for matrix transposition.
