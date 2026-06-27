---
role: proof
locale: en
of_concept: non-separably-generated-subfield
source_book: gtm028
source_chapter: "II"
source_section: "§13. Separably generated fields of algebraic functions"
---

\begin{proof}
Since $K$ is not separably generated over $k$, by Theorem 30 no subset of $\{x_1, \ldots, x_n\}$ can be a separating transcendence basis of $K/k$. Let $r = \operatorname{tr. deg.} K/k$. We select a transcendence basis from among the $x_i$; after relabeling, let $\{x_1, \ldots, x_r\}$ be such a transcendence basis. Since this set is not a separating transcendence basis, $K$ is not separable over $k(x_1, \ldots, x_r)$.

Now consider the elements $x_1, \ldots, x_r, x_{r+1}$ (where $x_{r+1}$ is any of the remaining generators). The field $L = k(x_1, \ldots, x_r, x_{r+1})$ has transcendence degree $r$ over $k$ (since $x_1, \ldots, x_r$ are algebraically independent and $x_{r+1}$ is algebraic over them). If $L$ were separably generated over $k$, then by Theorem 30 (applied to $L$ with generators $x_1, \ldots, x_r, x_{r+1}$), the set $\{x_1, \ldots, x_r, x_{r+1}\}$ would contain a separating transcendence basis of $L/k$. This separating transcendence basis would have $r$ elements.

If $\{x_1, \ldots, x_r\}$ is already a separating transcendence basis of $L/k$, then $L$ is separable over $k(x_1, \ldots, x_r)$. Since $K$ is an algebraic extension of $L$ (all remaining $x_i$ for $i > r+1$ are algebraic over $k(x_1, \ldots, x_{r+1})$), and $L$ is separable over $k(x_1, \ldots, x_r)$, the transitivity of separability would imply that $K$ is separable over $k(x_1, \ldots, x_r)$, contradicting the assumption.

If the separating transcendence basis of $L/k$ contained $x_{r+1}$ but not, say, $x_1$, then after relabeling we would obtain a different transcendence basis that is separating. But then by a standard exchange argument, one can show that $K$ would be separably generated after all, again a contradiction.

Thus, for a suitable choice of the $r+1$ elements among the $x_i$, the field $k(x_1, \ldots, x_{r+1})$ has transcendence degree $r$ and is not separably generated over $k$.
\end{proof}
