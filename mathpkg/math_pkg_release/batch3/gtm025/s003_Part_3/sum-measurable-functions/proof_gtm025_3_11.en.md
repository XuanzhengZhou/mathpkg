---
role: proof
locale: en
of_concept: sum-measurable-functions
source_book: gtm025
source_chapter: "3"
source_section: "11"
---

**Proof.** For $a \in \mathbb{R}$, let $A_\beta = A$ if $a < \beta$, $\emptyset$ otherwise. Then
$$h^{-1}(]a, \infty[) = \{x \notin A : f(x) + g(x) > a\} \cup A_\beta.$$
Now $\{x \notin A : f(x) > a - g(x)\} \in \mathcal{A}$ by (11.9), and $A_\beta \in \mathcal{A}$. Hence $h$ is measurable. $\square$
