---
role: proof
locale: en
of_concept: oscillation-bound-implies-integral-bound
source_book: gtm002
source_chapter: "7"
source_section: "Functions of First Class"
---

For a given function $f$, bounded on $I$, let $F(I)$ be the greatest lower bound of all sums of the form
$$\sum_{i=1}^{n} \omega(I_i) |I_i|,$$
where $\{I_1, \ldots, I_n\}$ is any subdivision of $I$ (any finite set of non-overlapping closed intervals whose union is $I$). $F(I)$ is the difference between the upper and lower integrals of $f$ on $I$; the equation $F(I) = 0$ expresses the condition that $f$ be Riemann-integrable on $I$. It is easy to verify that if $\{I_1, \ldots, I_n\}$ is any subdivision of $I$, then $F(I) = \sum_{i=1}^{n} F(I_i)$.

Now suppose $\omega(x) < \varepsilon$ for each $x \in I$, but contrary to the lemma, $F(I) \geq \varepsilon|I|$. Then $F(I_1) \geq \varepsilon|I|/2$ for at least one of the intervals $I_1$ obtained by bisecting $I$. Similarly, $F(I_2) \geq \varepsilon|I|/2^2$ for at least one of the intervals $I_2$ obtained by bisecting $I_1$. By repeated bisection we obtain a nested sequence of closed intervals $I_n$ such that $F(I_n) \geq \varepsilon|I|/2^n$ for $n = 1, 2, \ldots$.

These intervals intersect in a point $x \in I$. By hypothesis, $\omega(x) < \varepsilon$, and therefore $\omega(J) < \varepsilon$ for some open interval $J$ containing $x$. Choose $n$ so that $I_n \subset J$. Then
$$F(I_n) \leq \omega(I_n) |I_n| \leq \omega(J) |I|/2^n < \varepsilon|I|/2^n,$$
contradicting $F(I_n) \geq \varepsilon|I|/2^n$. Hence $F(I) < \varepsilon|I|$.
