---
role: proof
locale: en
of_concept: vanishing-singular-trpr-theorem
source_book: gtm046
source_chapter: "X"
source_section: "33-35"
---

Fix $x \in [\bar{P}_s(x, R) = 0]$. For $m < n$ and arbitrary $S$, we have the Ces\`{a}ro decomposition and taking limits yields the convergence. If $S_0$ is a $\bar{P}$-null set, then $\bar{P}(x, S_0) \leq \lim \frac{1}{n} \sum_{k=1}^{n} P_s^k(x, R) = 0$, so $\bar{P}(x, S)$ is $\bar{P}$-continuous. Moreover, by letting $n \to \infty$ in $\frac{1}{n} \sum_{k=m+1}^{m+n} P^k(x, S) = \int \{ \frac{1}{n} \sum_{k=1}^{n} P^k(x, dy) P^m(y, S) \}$, we obtain $\bar{P}(x, S) = \int \bar{P}(x, dy) P^m(y, S)$. Hence $\bar{P}(x, S) = \int \bar{P}(x, dy) \{ \frac{1}{n} \sum_{k=1}^{n} P^k(y, S) \}$. Under the null-set condition, dominated convergence yields idempotency.
