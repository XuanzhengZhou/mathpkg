---
role: proof
locale: en
of_concept: wiener-hopf-equation-unique-solution
source_book: gtm034
source_chapter: "27"
source_section: "APPLICATIONS TO ANALYSIS"
---

Set $S = [0,\infty)$ and let $Q(x,y)$ be the restriction of $P(x,y)$ to $S \times S$. Then $Q$ is a transient kernel whose Green function is, by P19.3,
$$g(x,y) = \sum_{n=0}^{\min(x,y)} u(x-n)v(y-n), \quad x \geq 0, \ y \geq 0.$$
Taking $\xi = 0$, we compute the Martin kernel for $y \geq x$:
$$\frac{g(x,y)}{g(0,y)} = \frac{1}{u(0)v(y)} \sum_{k=0}^{x} u(x-k)v(y-k).$$

To evaluate $\lim_{y \to +\infty} g(x,y)/g(0,y)$, it suffices to prove $\lim_{y \to +\infty} v(y-k)/v(y) = 1$ for each fixed $k$. This follows from a probabilistic argument (due to H. Kesten): denote by $J(x,y)$ the probability that the random walk starting at $x$ first visits $y$ before entering $(-\infty, -1]$. Then $g(0,x) = u(0)v(x) = J(0,x)g(x,x)$ and $v(x+1)/v(x) = [J(0,x+1)/J(0,x)] \cdot [g(x+1,x+1)/g(x,x)]$. Recurrence forces both ratios to tend to $1$ as $x \to +\infty$, giving the required limit.

Hence the limit in P3 evaluates to
$$f(x) = \lim_{y \to +\infty} \frac{g(x,y)}{g(0,y)} = \frac{u(0) + u(1) + \cdots + u(x)}{u(0)}, \quad x \geq 0.$$
By P19.5, this function is $Q$-regular. P3 then implies any non-negative solution is a positive multiple of $f(x)$, establishing both existence and uniqueness.
