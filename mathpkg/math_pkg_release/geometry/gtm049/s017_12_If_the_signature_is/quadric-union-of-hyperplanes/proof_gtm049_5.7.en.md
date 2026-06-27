---
role: proof
locale: en
of_concept: quadric-union-of-hyperplanes
source_book: gtm049
source_chapter: "5"
source_section: "7"
---

Since $Q$ is non-empty and non-degenerate, $Q \not\subseteq H$ and $Q \not\subseteq K$ by Exercise 3. We may assume $\operatorname{pdim} V > 1$, so $H \cap K$ contains points.

(i) Suppose $P \in Q \cap H \cap K$. Take any point $R$ not in $H$ or $K$. The line $PR$ meets $Q$ only at $P$, so the restriction $\sigma_{PR}$ is degenerate, implying $R \subseteq P^\perp$. Since the points $R$ not in $H \cup K$ span $V$, we would have $P \in V^\perp$, contradicting non-degeneracy of $Q$ (which would imply $\sigma$ is degenerate). Hence $Q \cap H \cap K = \emptyset$.

(ii) Since $Q \subseteq H \cup K$ and $Q$ is a quadric (defined by a single quadratic equation), the restriction of the quadratic form to $H$ (respectively $K$) defines a quadric in the hyperplane. The condition $Q \cap H \cap K = \emptyset$ forces the decomposition: either $Q = H \cup K$ (when the quadratic form factors as a product of two linear forms, each defining one hyperplane), or $Q$ is the union of four subspaces — the two components of $Q \cap H$ (hyperplanes in $H$) and the two components of $Q \cap K$ (hyperplanes in $K$). This follows from the fact that a quadratic form on $V$ whose zero set lies in $H \cup K$ must factor as the product of two linear forms, up to a scalar.
