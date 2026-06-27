---
role: proof
locale: en
of_concept: strong-separation-theorem-for-convex-sets
source_book: gtm036
source_chapter: "14"
source_section: "14.3"
---

This is a variant of theorem 3.9 on strong separation. If $f$ strongly separates $A$ and $B$, then $f$ is bounded away from $0$ on the set $B - A$ because $\sup \{r(x): x \in A\} < \inf \{r(y): y \in B\}$ where $r$ is the real part of $f$. Hence, if $f$ is continuous, then $0$ does not belong to $(B - A)^-$. To show the converse, suppose that $0 \notin (B - A)^-$ and that $E$ is locally convex. Then there is a convex circled open neighborhood $U$ of $0$ such that $0 \notin B - A + U$ and the preceding theorem shows that there is a continuous linear functional $f$ separating $B - A + U$ and $\{0\}$. If $r$ is the real part of $f$, then $\sup \{r(x): x \in A\} \leq \inf \{r(y): y \in B\} + \inf \{r(z): z \in U\}$. It follows that $f$ is a continuous functional which strongly separates $A$ and $B$.
