---
role: proof
locale: en
of_concept: series-representation-of-completed-tensor-product
source_book: gtm003
source_chapter: "III"
source_section: "6.4"
---

Let $\{p_n\}, \{q_n\}$ be increasing sequences of semi-norms generating the topologies of $E, F$, and let $r_n = p_n \otimes q_n$ with extension $\bar{r}_n$. Given $u \in E \tilde{\otimes} F$, there exists $\{u_n\}$ in $E \otimes F$ with $\bar{r}_n(u - u_n) < n^{-2} 2^{-(n+1)}$. Set $v_n = u_{n+1} - u_n$. Then $r_n(v_n) \leq \bar{r}_n(u-u_n) + \bar{r}_n(u-u_{n+1}) \leq \bar{r}_n(u-u_n) + \bar{r}_{n+1}(u-u_{n+1}) < n^{-2}2^{-n}$. By (6.3), each $v_n$ admits a representation $\sum_{i=i_n+1}^{i_{n+1}} \lambda_i x_i \otimes y_i$ with $p_n(x_i) \leq n^{-1}$, $q_n(y_i) \leq n^{-1}$, and $\sum |\lambda_i| \leq 2^{-n}$. Then $u = u_1 + \sum v_n = \sum \lambda_i x_i \otimes y_i$ satisfies the required conditions.
