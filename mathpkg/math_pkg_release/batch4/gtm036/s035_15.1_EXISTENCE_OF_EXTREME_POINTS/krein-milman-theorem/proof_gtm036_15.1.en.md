---
role: proof
locale: en
of_concept: krein-milman-theorem
source_book: gtm036
source_chapter: "15"
source_section: "15.1"
---
Let $R$ be any closed (hence compact) support of $A$; then by the maximal principle there exists a family $\mathcal{A}$ of closed supports of $A$ which is maximal with respect to the following properties: (i) $R \in \mathcal{A}$; and (ii) $\mathcal{A}$ has the finite intersection property. Let $S = \bigcap \{B : B \in \mathcal{A}\}$. Then $S$ is a non-void closed support of $A$ since $\mathcal{A}$ is compact. Furthermore, $S$ is a minimal closed support of $A$ in the sense that it contains as a proper subset no closed support of $A$. Hence each closed support of $A$ contains a minimal closed support of $A$.

Let $S$ be any minimal closed support of $A$, and assume that a line segment $[x:y]$, where $x \neq y$, is contained in $S$. Then there exists a continuous linear functional $f$ on the real restriction of $E$ such that $f(x) \neq f(y)$. Since $S$ is compact, $f$ is bounded on $S$, and
$$C = \{z : z \in S, f(z) = \sup \{f(y) : y \in S\}\}$$
is a non-void proper closed subset of $S$. Moreover, $C$ is a support of $S$ (and hence a support of $A$), contradicting the minimality of $S$. Therefore, a minimal closed support of $A$ contains no line segment with distinct endpoints; consequently it is a single point, which is an extreme point of $A$. Thus every closed support of $A$ contains an extreme point.

Finally, let $B$ be the closed convex extension of the set of all extreme points of $A$. Clearly $B \subset A$. If $B \neq A$, then by the Hahn-Banach theorem there exists a continuous linear functional $f$ and a real number $\alpha$ such that $\sup \{f(x) : x \in B\} < \alpha \leq \sup \{f(x) : x \in A\}$. The set $\{x : x \in A, f(x) \geq \alpha\}$ is a non-void closed support of $A$, and by the first part of the proof it contains an extreme point, which is a contradiction. Hence $A = B$, and $A$ is the closed convex extension of the set of all its extreme points.
