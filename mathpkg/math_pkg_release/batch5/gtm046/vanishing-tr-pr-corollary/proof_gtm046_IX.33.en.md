---
role: proof
locale: en
of_concept: vanishing-tr-pr-corollary
source_book: gtm046
source_chapter: "IX"
source_section: "33"
---

This follows from the limit assertion in the Vanishing Singular Transition Probability Theorem upon letting $n \to \infty$ in

$$\frac{1}{n} \sum_{k=1+m}^{n+m} P^k(x, S) = \int P^m(x, dy) \left\{ \frac{1}{n} \sum_{k=1}^{n} P^k(y, S) \right\}.$$

By stationarity, the left-hand side converges to $\bar{P}(x, S)$, and the Cesàro average inside the integral converges to $\bar{P}(y, S)$. By the dominated convergence theorem, the right-hand side converges to $\int P^m(x, dy) \bar{P}(y, S)$, yielding the asserted identity.
