---
role: proof
locale: en
of_concept: closed-convex-hull-equals-closure-of-convex-hull
source_book: gtm015
source_chapter: "3"
source_section: "25"
---

# Proof of Closed convex hull equals closure of convex hull

Let $A = \operatorname{conv} S$ and let $B$ be the closed convex hull of $S$. Since $B$ is a convex superset of $S$, we have $A \subset B$ and therefore $\overline{A} \subset \overline{B} = B$.

On the other hand, $\overline{A}$ is a closed convex superset of $S$ by (25.17), therefore $B \subset \overline{A}$.

Thus $B = \overline{A}$.
