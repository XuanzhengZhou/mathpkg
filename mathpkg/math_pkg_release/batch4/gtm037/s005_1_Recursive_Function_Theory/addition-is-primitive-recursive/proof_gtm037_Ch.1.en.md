---
role: proof
locale: en
of_concept: addition-is-primitive-recursive
source_book: gtm037
source_chapter: "1"
source_section: "Recursive Function Theory"
---

The function $+$ is defined by primitive recursion from the initial functions. Let $f(x) = U_0^1 x = x$ be the base function (a projection, hence primitive recursive). Let $h(x, y, z) = \delta(U_2^3(x, y, z))$ be the step function, which is primitive recursive since it is a composition of the successor function $\delta$ and the projection $U_2^3$. Then $+$ is defined by:

$$x + 0 = f(x) = U_0^1 x,$$
$$x + \delta y = h(x, y, x + y) = \delta U_2^3(x, y, x + y).$$

Since both $f$ and $h$ are primitive recursive, the function $+$ obtained by primitive recursion from them is primitive recursive.
