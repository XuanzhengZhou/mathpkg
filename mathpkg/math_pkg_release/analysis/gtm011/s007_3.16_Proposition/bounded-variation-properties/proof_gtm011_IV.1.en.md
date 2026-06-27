---
role: proof
locale: en
of_concept: bounded-variation-properties
source_book: gtm011
source_chapter: "IV"
source_section: "1"
---

(a) If $P \subset Q$, then each subinterval of $P$ is split into finitely many subintervals in $Q$. By the triangle inequality, the sum of absolute differences over the finer partition $Q$ is at least as large as over $P$. More precisely, for each $[t_{k-1}, t_k]$ in $P$, if $Q$ adds points $t_{k-1} = s_0 < s_1 < \cdots < s_r = t_k$, then

$$|\gamma(t_k) - \gamma(t_{k-1})| = \left|\sum_{j=1}^{r} (\gamma(s_j) - \gamma(s_{j-1}))\right| \leq \sum_{j=1}^{r} |\gamma(s_j) - \gamma(s_{j-1})|.$$

Summing over all subintervals of $P$ gives $v(\gamma; P) \leq v(\gamma; Q)$.

(b) For any partition $P = \{a = t_0 < \cdots < t_m = b\}$,

$$\begin{align*}
v(\alpha\gamma + \beta\sigma; P) &= \sum_{k=1}^{m} |(\alpha\gamma + \beta\sigma)(t_k) - (\alpha\gamma + \beta\sigma)(t_{k-1})| \\
&\leq \sum_{k=1}^{m} \left(|\alpha|\,|\gamma(t_k) - \gamma(t_{k-1})| + |\beta|\,|\sigma(t_k) - \sigma(t_{k-1})|\right) \\
&= |\alpha|\, v(\gamma; P) + |\beta|\, v(\sigma; P) \\
&\leq |\alpha|\, V(\gamma) + |\beta|\, V(\sigma).
\end{align*}$$

Taking the supremum over all partitions $P$ yields $V(\alpha\gamma + \beta\sigma) \leq |\alpha|\, V(\gamma) + |\beta|\, V(\sigma)$, which also shows $\alpha\gamma + \beta\sigma$ is of bounded variation.
