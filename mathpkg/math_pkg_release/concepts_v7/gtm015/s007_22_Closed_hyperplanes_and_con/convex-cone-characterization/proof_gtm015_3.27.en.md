---
role: proof
locale: en
of_concept: convex-cone-characterization
source_book: gtm015
source_chapter: "3"
source_section: "27"
---

# Proof of Characterization of convex cones

A subset $A$ of $E$ is a convex cone if and only if (i) $\alpha A \subset A$ for all $\alpha > 0$, and (ii) $A + A \subset A$.

Condition (i) is the definition of a cone. If, moreover, $A$ is convex, then condition (ii) is a consequence of condition (i): citing (25.10),

$$A + A = 1A + 1A = (1 + 1)A = 2A \subset A.$$

Conversely, assuming $A$ satisfies (i) and (ii), it is to be shown that $A$ is convex. Indeed, if $0 < \alpha < 1$ then

$$\alpha A + (1 - \alpha)A \subset A + A \subset A.$$

Thus $A$ is convex.
