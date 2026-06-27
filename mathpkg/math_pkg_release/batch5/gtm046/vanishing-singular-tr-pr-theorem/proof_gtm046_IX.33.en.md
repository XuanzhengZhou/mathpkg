---
role: proof
locale: en
of_concept: vanishing-singular-tr-pr-theorem
source_book: gtm046
source_chapter: "IX"
source_section: "33"
---

Fix $x \in [\bar{P}_s(x, R) = 0]$. For $m < n$ and arbitrary $S$,

$$\frac{1}{n} \sum_{k=1}^{n} P^k(x, S) = \frac{1}{n} \sum_{k=1}^{m-1} P^k(x, S) + \frac{1}{n} \sum_{k=m}^{n} P^k(x, S).$$

As $m \to \infty$, the limit assertion follows. If $S_0$ is a $\bar{P}$-null set, then

$$\bar{P}(x, S_0) = \lim \frac{1}{n} \sum_{k=1}^{n} P^k(x, S_0) \leq \lim \frac{1}{n} \sum_{k=1}^{n} P_s^k(x, R) = 0$$

so $\bar{P}(x, S)$ is $\bar{P}$-continuous. Moreover, by letting $n \to \infty$ in

$$\frac{1}{n} \sum_{k=m+1}^{m+n} P^k(x, S) = \int \left\{ \frac{1}{n} \sum_{k=1}^{n} P^k(x, dy) \, P^m(y, S) \right\}$$

we obtain $\bar{P}(x, S) = \int \bar{P}(x, dy) P^m(y, S)$, and consequently

$$\bar{P}(x, S) = \int \bar{P}(x, dy) \left\{ \frac{1}{n} \sum_{k=1}^{n} P^k(y, S) \right\}.$$

Now assume the set of points $x$ where this does not hold is a $\bar{P}$-null set. By $\bar{P}$-continuity of $\bar{P}(x, S)$ and the dominated convergence theorem, letting $n \to \infty$ yields idempotency.
