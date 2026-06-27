---
role: proof
locale: en
of_concept: idempotent-self-adjoint-implies-projection
source_book: gtm036
source_chapter: ""
source_section: "I"
---

Define $F = \{x \in H : P(x) = x\}$. Since $P$ is continuous and linear, $F$ is a closed linear subspace. For any $x \in H$, write $x = Px + (x - Px)$. By idempotence, $P(Px) = Px$, so $Px \in F$. For any $y \in F$ (so $Py = y$), self-adjointness gives:
$$(x - Px, y) = (x, y) - (Px, y) = (x, y) - (x, Py) = (x, y) - (x, y) = 0.$$
Thus $x - Px \in F^\perp$, and the decomposition $x = Px + (x - Px)$ is the unique orthogonal decomposition. Hence $Px$ is the orthogonal projection of $x$ onto $F$, and since orthogonal projection coincides with the metric projection for linear subspaces, $P$ is the projection onto $F$.
