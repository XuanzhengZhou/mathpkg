---
role: proof
locale: en
of_concept: multiplication-is-primitive-recursive
source_book: gtm037
source_chapter: "1"
source_section: "Recursive Function Theory"
---

The function $\cdot$ is defined by primitive recursion. The base function is $C_0^1 x = 0$, which is primitive recursive (constant function). The step function is

$$h(x, y, z) = +(U_2^3(x, y, z), U_0^3(x, y, z)) = z + x,$$

which is a composition of the already-established primitive recursive function $+$ with projections. Then $\cdot$ satisfies:

$$x \cdot 0 = C_0^1 x = 0,$$
$$x \cdot \delta y = h(x, y, x \cdot y) = (x \cdot y) + x.$$

Since $C_0^1$ and $h$ are primitive recursive, $\cdot$ is primitive recursive.
