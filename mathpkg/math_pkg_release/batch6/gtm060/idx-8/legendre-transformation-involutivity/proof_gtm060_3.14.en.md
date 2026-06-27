---
role: proof
locale: en
of_concept: legendre-transformation-involutivity
source_book: gtm060
source_chapter: "3"
source_section: "14"
---

To apply the Legendre transform to $g$, with variable $p$, we introduce a new independent variable $x$ and construct the function

$$G(x, p) = xp - g(p).$$

The point $p(x)$ at which $G$ attains its maximum satisfies $\partial G / \partial p = 0$, i.e., $g'(p) = x$. Then the Legendre transform of $g(p)$ is the function of $x$ equal to $G(x, p(x))$.

We show that $G(x, p(x)) = f(x)$. The function $G(x, p) = xp - g(p)$ has a geometric interpretation: it is the ordinate of the point with abscissa $x$ on the line tangent to the graph of $f(x)$ with slope $p$. For fixed $p$, $G(x, p)$ is a linear function of $x$ with $\partial G / \partial x = p$, and for $x = x(p)$ we have $G(x, p) = xp - g(p) = f(x)$ by the definition of $g(p)$.

Now fix $x = x_0$ and vary $p$. The values of $G(x_0, p)$ are the ordinates of the intersection points of the vertical line $x = x_0$ with the tangent lines to the graph of $f(x)$ having various slopes $p$. By convexity of the graph, all these tangents lie below the curve, so the maximum of $G(x_0, p)$ over $p$ is attained at the tangent point, where $G(x_0, p(x_0)) = f(x_0)$. Therefore $G(x, p(x)) = f(x)$, proving the involutivity.
