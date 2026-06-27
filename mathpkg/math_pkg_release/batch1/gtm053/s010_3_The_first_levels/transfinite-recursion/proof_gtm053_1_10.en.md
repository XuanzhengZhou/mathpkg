---
role: proof
locale: en
of_concept: transfinite-recursion
source_book: gtm053
source_chapter: "1"
source_section: "10"
---

The function $F$ is defined by transfinite induction on $\alpha$. Assume that $F(\beta)$ has been defined for all $\beta < \alpha$. Then the set of values $\{F(\beta) \mid \beta < \alpha\}$ is determined, and we define

$$F(\alpha) = G(\{F(\beta) \mid \beta < \alpha\}).$$

For the base case $\alpha = 0$, the set of values on elements of $0 = \varnothing$ is empty, so $F(0) = G(\varnothing)$. This uniquely determines $F(0)$. Then $F(1) = G(\{F(0)\})$, and by induction the entire function $F$ on the class of ordinals is uniquely determined. The existence of such a function defined on a proper class follows from the axiom of replacement.
