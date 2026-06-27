---
role: proof
locale: en
of_concept: krein-milman-theorem
source_book: gtm036
source_chapter: "15"
source_section: "15.1"
---

Let $R$ be any closed (hence compact) support of $A$; then by the maximal principle there exists a family $\mathcal{A}$ of closed supports of $A$ which is maximal with respect to the following properties: (i) $R \in \mathcal{A}$; and (ii) $\mathcal{A}$ has the finite intersection property. Let $S = \bigcap \{B : B \in \mathcal{A}\}$. Then $S$ is a non-void closed support of $A$ since $A$ is compact. Furthermore, $S$ is a minimal closed support of $A$ in the sense that it contains as a proper subset no closed support of $A$. Hence each closed support of $A$ contains a minimal closed support of $A$.

Let $S$ be any minimal closed support of $A$, and assume that a line segment $[x:y]$, where $x \neq y$, is contained in $S$. Then there exists a continuous linear functional $f$ on the real restriction of $E$ such that $f(x) \neq f(y)$. Since $S$ is compact, $f$ is bounded on $S$, and $C = \{z : z \in S, f(z) = \sup \{f(y) : y \in S\}\}$ is a non-void closed proper subset of $S$. It can be shown that $C$ is a support of $A$, contradicting the minimality of $S$. Hence no such non-trivial line segment exists in $S$, which means $S$ consists of a single point, namely an extreme point of $A$. Therefore each closed support of $A$ contains an extreme point.

To show that $A$ is the closed convex extension of its extreme points: let $B$ be the closed convex extension of the set of all extreme points of $A$. If $A \neq B$, then by the separation theorem there exists a continuous linear functional separating a point of $A \setminus B$ from $B$, and the supporting hyperplane would define a closed support of $A$ containing no extreme point, a contradiction. Hence $A = B$.
