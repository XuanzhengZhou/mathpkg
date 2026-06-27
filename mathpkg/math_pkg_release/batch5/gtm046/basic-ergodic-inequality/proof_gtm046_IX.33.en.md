---
role: proof
locale: en
of_concept: basic-ergodic-inequality
source_book: gtm046
source_chapter: "IX"
source_section: "33"
---

Let $k = 1, 2, \ldots, n+m$, $k \leq l \leq \min(k+m-1, n+m)$, and let

$$B^{mk} = [X_k - b Y_k \text{ is } m\text{-positive}] = \left[ \sup_l \frac{X_k + \cdots + X_l}{Y_k + \cdots + Y_l} > b \right].$$

If $k \leq n$, then $l$ varies from $k$ to $k+m-1$ and $B^{mk} = B_k^m$, where $B_k^m$ is the translate by $k-1$ of $B^m$. By Riesz's lemma, the $m$-positive terms among $X_k - b Y_k$ for $k = 1, \ldots, n+m$ form disjoint stretches of positive sums. Hence, summing over all such stretches yields

$$\sum_{k=1}^{n} \left( \frac{X_k}{Z^n} - b \frac{Y_k}{Z^n} \right) I_{B_k^m C} + \sum_{k=n+1}^{n+m} \left( \frac{X_k}{Z^n} - b \frac{Y_k}{Z^n} \right)^+ I_C \geq 0.$$

Integrating preserves the inequality, giving the stated result.
