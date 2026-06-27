---
role: proof
locale: en
of_concept: pi-cross-norm
source_book: gtm003
source_chapter: "III"
source_section: "6.3"
---

Let $M_0 = \{u: r(u) < 1\}$, $M_1 = \{u: r(u) \leq 1\}$. If $u \in \Gamma(U \otimes V)$, then $u = \sum \lambda_i(x_i \otimes y_i)$ with $x_i \in U$, $y_i \in V$, $\sum |\lambda_i| \leq 1$. Writing $\bar{x}_i = \lambda_i x_i$, we have $r(u) \leq \sum p(\bar{x}_i)q(y_i) = \sum |\lambda_i| p(x_i)q(y_i) \leq 1$. Conversely, if $r(u) < 1$, then $u = \sum x_i \otimes y_i$ with $\sum p(x_i)q(y_i) < 1$. Choosing $\varepsilon_i > 0$ such that $\sum [p(x_i)+\varepsilon_i][q(y_i)+\varepsilon_i] < 1$ and scaling appropriately gives $u \in \Gamma(U \otimes V)$.
