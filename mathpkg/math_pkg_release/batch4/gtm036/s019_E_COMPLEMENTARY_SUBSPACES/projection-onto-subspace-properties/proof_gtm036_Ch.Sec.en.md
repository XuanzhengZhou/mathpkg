---
role: proof
locale: en
of_concept: projection-onto-subspace-properties
source_book: gtm036
source_chapter: ""
source_section: "I"
---

(i) For $x \in H$, $P(x) \in F$. Since $P$ restricted to $F$ is the identity (each point of $F$ is its own best approximation), $P(P(x)) = P(x)$.

(ii) Since $F$ is a linear subspace, the projection inequality gives $(x - Px, y) = 0$ for all $y \in F$. In particular, $(x - Px, Py) = 0$ and $(y - Py, Px) = 0$. Thus $(x, Py) = (Px, Py) = (Px, y)$.

(iii) If $x \in F$, then $x$ is the unique best approximation to itself, so $P(x) = x$. Conversely, if $P(x) = x$, then $x = P(x) \in F$.

Additivity: $(x + y) - (Px + Py) = (x - Px) + (y - Py)$ is orthogonal to $F$ (as both summands are), and $Px + Py \in F$, so $Px + Py$ is the projection of $x + y$. Similarly, $P(\lambda x) = \lambda P(x)$. Thus $P$ is linear.
