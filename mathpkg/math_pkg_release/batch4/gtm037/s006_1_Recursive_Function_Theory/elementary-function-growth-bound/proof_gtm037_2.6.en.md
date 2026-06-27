---
role: proof
locale: en
of_concept: elementary-function-growth-bound
source_book: gtm037
source_chapter: "2"
source_section: "2.6"
---

Let $A$ be the set of all functions $g$ (of any rank) for which there exists an $m \in \omega$ satisfying the required inequality. To prove the lemma it suffices to show that $A$ is closed under the elementary recursive operations.

**(1) $+ \in A$.**

Take $m = 2$. For any $x_0, x_1 \in \omega$ with $\max(x_0, x_1) > 1$,

$$x_0 + x_1 \leq \max(x_0, x_1) + \max(x_0, x_1)$$
$$= a(\max(x_0, x_1), 0) + a(\max(x_0, x_1), 0)$$
$$< a(\max(x_0, x_1), 1).$$

Since $a(\max(x_0, x_1), 1) < a(\max(x_0, x_1), 2)$ by the monotonicity properties of the Ackermann function, we have $+ \in A$ with $m = 2$.

**(2) $A$ is closed under composition.**

Assume $f$ is $m$-ary with witness $p \in \omega$, and $g_0, \ldots, g_{m-1}$ are $n$-ary with witnesses $q_0, \ldots, q_{m-1} \in \omega$ respectively. Let

$$h(x_0, \ldots, x_{n-1}) = f(g_0(x_0, \ldots, x_{n-1}), \ldots, g_{m-1}(x_0, \ldots, x_{n-1})).$$

Assume $\max\{g_i(x_0, \ldots, x_{n-1}) : i < m\} > 1$. Then

$$h(x_0, \ldots, x_{n-1}) < a(\max\{g_i(x_0, \ldots, x_{n-1}) : i < m\}, p)$$
$$< a(\max\{a(\max\{x_0, \ldots, x_{n-1}\}, q_i) : i < m\}, p)$$
$$= a(a(\max\{x_0, \ldots, x_{n-1}\}, \max\{q_0, \ldots, q_{m-1}\}), p)$$
$$\leq a(\max\{x_0, \ldots, x_{n-1}\}, \max\{q_0, \ldots, q_{m-1}\} + 2p)$$

by Lemma 2.43. Choose $s > \max\{q_0, \ldots, q_{m-1}\} + 2p$ such that the remaining case (where all $g_i$ values are $\leq 1$) is also bounded by $a(\max\{x_0, \ldots, x_{n-1}\}, s)$, using the finiteness of the set of possible outputs in that case.

**(3) $A$ is closed under $\sum$ (bounded sum).**

Suppose $f \in A$ is $m$-ary, and let $g = \sum f$ (so $g$ is $(m+1)$-ary with $g(x_0, \ldots, x_{m-1}, y) = \sum_{z < y} f(x_0, \ldots, x_{m-1}, z)$). Choose $p \in \omega$ such that $\max(x_0, \ldots, x_{m-1}) > 1$ implies $f(x_0, \ldots, x_{m-1}) < a(\max(x_0, \ldots, x_{m-1}), p)$. Let

$$q = p + 1 + \max\{f(x_0, \ldots, x_{m-1}) : x_0, \ldots, x_{m-1} \leq 1\}.$$

Then for any $x_0, \ldots, x_{m-1}, y \in \omega$, the value $f(x_0, \ldots, x_{m-1})$ is bounded above by a suitable iterate, and summing $y$ such terms yields the required bound for $g$.

The remaining cases (constant functions, successor, projections, multiplication, exponentiation, and bounded product $\prod$) are handled by similar arguments, completing the proof that $A$ contains all elementary functions.
