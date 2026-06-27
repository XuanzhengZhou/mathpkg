---
role: proof
locale: en
of_concept: infinite-r.e.-set-recursive-subset
source_book: gtm037
source_chapter: "6"
source_section: "6.3"
---

Let $A$ be infinite r.e., say $A = \operatorname{Rng} f$, $f$ recursive. We define $g$ by induction:

$$g0 = f0,$$
$$g(x + 1) = f\mu y (fy > gx).$$

Thus $gx < g(x + 1)$ for all $x \in \omega$, and hence, by 6.7, $\operatorname{Rng} g$ is infinite and recursive. Obviously $\operatorname{Rng} g \subseteq A$. $\square$
