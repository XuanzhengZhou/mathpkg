---
role: proof
locale: en
of_concept: successive-approximations-lemma
source_book: gtm015
source_chapter: "V"
source_section: "48"
---

# Proof of the Successive Approximations Lemma

**(i)** Suppose $r$ and $\rho$ satisfy $(*)$: $B_\rho(Tx) \subset \overline{T(B_r(x))}$ for all $x \in E$, and let $a > r$. Write $a = \sum_{1}^{\infty} r_n$ with $r_n > 0$ for all $n$, and $r_1 = r$. (For example, let $r_{n+1} = 2^{-n}(a - r)$ for $n = 1, 2, 3, \ldots$.) For each $n$ there exists, by hypothesis, a $\rho_n > 0$ such that
$$B_{\rho_n}(Tx) \subset \overline{T(B_{r_n}(x))} \quad \text{for all } x \in E. \qquad (*)_n$$
We can suppose $\rho_1 = \rho$ and $\rho_n \to 0$.

Given any $x_0 \in E$ and $y \in B_\rho(Tx_0)$, the problem is to show that $y \in T(B_a(x_0))$; thus, we seek $x \in B_a(x_0)$ with $y = Tx$. The desired point $x$ will be obtained as the limit of a suitable sequence $x_n$.

We construct a sequence $x_1, x_2, x_3, \ldots$ in $E$ such that
$$x_n \in B_{r_n}(x_{n-1}) \quad \text{and} \quad y \in B_{\rho_n}(Tx_n)$$
for all $n \geq 1$. Having chosen $x_{n-1}$ and given that $y \in B_{\rho_{n-1}}(Tx_{n-1}) \subset \overline{T(B_{r_{n-1}}(x_{n-1}))}$, we can select $x_n$ such that $x_n \in B_{r_{n-1}}(x_{n-1})$ and $y \in B_{\rho_{n-1}}(Tx_n)$. Renaming indices yields the desired properties.

The sequence $(x_n)$ is Cauchy: for $n < m$,
$$d(x_n, x_m) \leq \sum_{k=n}^{m-1} d(x_k, x_{k+1}) \leq \sum_{k=n}^{\infty} r_k,$$
which tends to $0$ as $n \to \infty$ since $\sum r_n = a < \infty$. By completeness of $E$, $x_n \to x$ for some $x \in E$. Moreover,
$$d(x_0, x) \leq \sum_{n=1}^{\infty} d(x_{n-1}, x_n) \leq \sum_{n=1}^{\infty} r_n = a,$$
so $x \in B_a(x_0)$. By continuity of $T$, $Tx = \lim Tx_n = y$, proving $(**)$.

**(ii)** To show $T$ is an open mapping, let $U$ be an open set in $E$ and let $x_0 \in U$. Choose $r > 0$ such that $B_r(x_0) \subset U$. By hypothesis, there exists $\rho > 0$ such that $B_\rho(Tx_0) \subset \overline{T(B_{r/2}(x_0))}$. By part (i) with $a = r$, we obtain $B_\rho(Tx_0) \subset T(B_r(x_0)) \subset T(U)$. Since $x_0$ was arbitrary in $U$, $T(U)$ is open in $F$. $\square$
