---
role: proof
locale: en
of_concept: complete-cone-metrizable-tvs
source_book: gtm003
source_chapter: "V"
source_section: "3"
---

It is clear that each set $V_n = (U_n \cap C) - (U_n \cap C)$ is radial and circled in $E_1 = C - C$, and obviously
$$V_{n+1} + V_{n+1} \subset V_n \quad \text{for all } n \in \mathbb{N}.$$
It follows from (I, 1.2) that $\{V_n : n \in \mathbb{N}\}$ is a $0$-neighborhood base for a (unique translation invariant) topology $\mathfrak{T}_1$ on $E_1$ under which $E_1$ is a topological vector space. Clearly $(E_1, \mathfrak{T}_1)$ is metrizable, and it remains to prove completeness.

Given a Cauchy sequence in $(E_1, \mathfrak{T}_1)$, we can extract a subsequence $\{z_n\}$ such that
$$z_{n+1} - z_n \in V_n \quad (n \in \mathbb{N}).$$
Consequently, we can write
$$z_{n+1} - z_n = x_n - y_n,$$
where $x_n, y_n \in U_n \cap C$. It is evident that the series $\sum x_n$ and $\sum y_n$ converge in $E$: since $U_{n+1} + U_{n+1} \subset U_n$ and each $U_n$ is closed and circled, the partial sums form Cauchy sequences in the complete cone $C \subset E$. By the completeness of $C$, there exist $x, y \in C$ such that
$$x = \sum_{n=1}^{\infty} x_n, \qquad y = \sum_{n=1}^{\infty} y_n$$
(with convergence in $E$). Then for each $N \in \mathbb{N}$,
$$z_{N+1} - z_1 = \sum_{n=1}^{N} (x_n - y_n) = \sum_{n=1}^{N} x_n - \sum_{n=1}^{N} y_n.$$
Thus the subsequence $\{z_n\}$ converges to $z_1 + x - y \in E_1 = C - C$ in the topology of $E$, and one verifies that this convergence also holds with respect to $\mathfrak{T}_1$. Since a Cauchy sequence with a convergent subsequence converges, $(E_1, \mathfrak{T}_1)$ is complete.
