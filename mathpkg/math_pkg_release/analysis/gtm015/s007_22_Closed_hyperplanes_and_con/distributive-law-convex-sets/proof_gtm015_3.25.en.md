---
role: proof
locale: en
of_concept: distributive-law-convex-sets
source_book: gtm015
source_chapter: "3"
source_section: "25"
---

# Proof of Distributive law for convex sets with positive scalars

If $\alpha = 0$ or $\beta = 0$ the conclusion holds trivially; assume $\alpha > 0$, $\beta > 0$. The left side is obviously contained in the right side, since for any $z \in A$, $(\alpha + \beta)z = \alpha z + \beta z \in \alpha A + \beta A$.

On the other hand, if $x, y \in A$ then, setting $\alpha_1 = \alpha / (\alpha + \beta)$ and $\beta_1 = \beta / (\alpha + \beta)$, we have $\alpha_1 + \beta_1 = 1$ and $\alpha_1, \beta_1 \ge 0$, so by convexity

$$z = \alpha_1 x + \beta_1 y \in A.$$

Then

$$\alpha x + \beta y = (\alpha + \beta)(\alpha_1 x + \beta_1 y) = (\alpha + \beta)z \in (\alpha + \beta)A.$$

Thus $\alpha A + \beta A \subset (\alpha + \beta)A$.
