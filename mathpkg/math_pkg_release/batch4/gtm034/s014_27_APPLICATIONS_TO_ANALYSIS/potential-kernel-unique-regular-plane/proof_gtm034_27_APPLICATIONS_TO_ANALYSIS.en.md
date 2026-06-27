---
role: proof
locale: en
of_concept: potential-kernel-unique-regular-plane
source_book: gtm034
source_chapter: "27"
source_section: "APPLICATIONS TO ANALYSIS"
---

Take $S = R \setminus \{0\}$ and $Q(x,y) = P(x,y)$ for $x,y \in S$. By results of Chapter III, $g_{(0)}(x,y) = g(x,y) > 0$ for all $x,y \in S$.

From P13.3, $\sum_{y \in R} P(x,y)a(y) - a(x) = \delta(x,0)$. Since $a(0) = 0$, restricting to $x \in S$ gives $\sum_{y \in S} Q(x,y)a(y) = a(x)$, so $a(x)$ is $Q$-regular.

By P11.6 and P12.2, $g(x,y) = a(x) + a(-y) - a(x-y)$. For arbitrary $\xi \in S$,
$$\frac{g(x,y)}{g(\xi,y)} = \frac{a(x) + a(-y) - a(x-y)}{a(\xi) + a(-y) - a(\xi-y)}.$$
As $|y| \to \infty$, the asymptotic property $\lim_{|y| \to \infty} [a(x+y) - a(y)] = 0$ (from P12.2) yields
$$\lim_{|y| \to \infty} \frac{g(x,y)}{g(\xi,y)} = \frac{a(x)}{a(\xi)}, \quad x \in S.$$
Thus $f(x) = a(x)/a(\xi)$ satisfies the hypothesis of P3 and is $Q$-regular. By P3, the positive multiples of $a(x)$ are the only $Q$-regular functions on $S$.
