---
role: proof
locale: en
of_concept: jensens-inequality
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof of Jensen's Inequality for Expectations

**Jensen's Inequality.** Let the Borel function $g = g(x)$ defined on $\mathbb{R}$ be convex downward and $\xi$ a random variable such that $E|\xi| < \infty$. Then

$$g(E\xi) \leq Eg(\xi). \tag{25}$$

*Proof.* If $g = g(x)$ is convex downward, then for every $x_0$ there exists a number $\lambda = \lambda(x_0)$ such that

$$g(x) \geq g(x_0) + \lambda(x_0)(x - x_0)$$

for all $x$. (This is the supporting line property of convex functions.) Taking $x_0 = E\xi$ and $x = \xi(\omega)$, we obtain

$$g(\xi(\omega)) \geq g(E\xi) + \lambda(E\xi)(\xi(\omega) - E\xi).$$

Taking expectations of both sides (all quantities are well-defined since convex functions are continuous and hence Borel measurable),

$$Eg(\xi) \geq g(E\xi) + \lambda(E\xi)(E\xi - E\xi) = g(E\xi),$$

which is precisely Jensen's inequality. $\square$
