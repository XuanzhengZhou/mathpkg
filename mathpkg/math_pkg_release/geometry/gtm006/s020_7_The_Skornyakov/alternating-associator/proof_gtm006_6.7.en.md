---
role: proof
locale: en
of_concept: associator-alternating-under-permutation
source_book: gtm006
source_chapter: "6"
source_section: "7. The Skornyakov-San Soucie Theorem"
---

Consider the permutation $\alpha$ given by $x^\alpha = y$, $y^\alpha = z$, $z^\alpha = x$. In an alternative ring,
$$0 = [x + y, x + y, z] = [x, x, z] + [x, y, z] + [y, x, z] + [y, y, z].$$
Since $[x, x, z] = [y, y, z] = 0$ (by the right alternative law),
$$[x, y, z] = -[y, x, z] = \operatorname{sgn} \alpha [x^\alpha, y^\alpha, z^\alpha].$$

Now consider the permutation $\beta$ given by $x^\beta = y$, $y^\beta = x$, $z^\beta = z$. Then since $D$ is alternative,
$$0 = [x + y, x + y, z] = [x, x, z] + [x, y, z] + [y, x, z] + [y, y, z]$$
and since the first and last terms on the right are zero,
$$[x, y, z] = -[y, x, z] = \operatorname{sgn} \beta [x^\beta, y^\beta, z^\beta].$$

Since $\alpha$ and $\beta$ generate the full symmetric group on $\{x, y, z\}$, the alternating property holds for all permutations. $\square$
