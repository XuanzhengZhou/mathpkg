---
role: proof
locale: en
of_concept: positive-measure-difference-set
source_book: gtm002
source_chapter: "4"
source_section: "4"
---
(The proof in the source is truncated; the following is a standard proof.)

For the measure case: Since $m(A) > 0$, by Lebesgue's density theorem there exists a point $x \in A$ of density $1$. It follows that for sufficiently small $\delta > 0$, $m(A \cap (x - \delta, x + \delta)) > \frac{3}{2}\delta$. Then for any $|t| < \delta$, the sets $A \cap (x - \delta, x + \delta)$ and $(A \cap (x - \delta, x + \delta)) + t$ must intersect (otherwise their total measure would exceed $2\delta$), which gives $a - b = t$ for some $a, b \in A$.

For the category case: Since $A$ has the property of Baire and is of second category, by Theorem 4.4 we can write $A = G \triangle P$ where $G$ is a nonempty open set (otherwise $A$ would be of first category) and $P$ is of first category. Let $I \subset G$ be an open interval. Then for sufficiently small $\delta > 0$, the intersection $I \cap (I + t)$ is a nonempty open set (hence of second category) for all $|t| < \delta$. Since $P \cup (P + t)$ is of first category, there must exist points in $A \cap (A + t)$, giving $a - b = t$ for some $a, b \in A$.
