---
role: proof
locale: en
of_concept: max-flow-min-cut-theorem
source_book: gtm054
source_chapter: "IV"
source_section: "18"
---

Let $n$ be the least positive integer such that $nk$ is integral. Consider the set of all feasible flows $h'$ such that for all $e \in W$,

$$h'(e) \in \{0, 1/n, 2/n, \ldots, k(e)\}.$$

Moreover (C7):
(a) $h'(e) > 0 \Rightarrow h'(e) \geq 1/n$;
(b) $h'(e) < k(e) \Rightarrow h'(e) \leq k(e) - 1/n$.

Clearly there exists a flow $h$ in this set such that $h(e_0) \geq h'(e_0)$ for all such $h'$. If $k$ is integral, then $n = 1$ and $h$ is already integral. If $h(e_0) = k(e_0)$, then $h$ is a maximum flow through $e_0$ and the theorem holds.

Hence suppose $h(e_0) < k(e_0)$ (C8).

An $x_0x$-path $x_0, e_1, x_1, \ldots, e_m, x$ is called \textit{unsaturated with respect to $h$} if:
$$e_i \neq e_0 \text{ for } i = 1, \ldots, m;$$
$$e_i = (x_{i-1}, x_i) \Rightarrow h(e_i) < k(e_i);$$
$$e_i = (x_i, x_{i-1}) \Rightarrow h(e_i) > 0.$$

Define $U = \{x \in V : \text{there exists an unsaturated } x_0x\text{-path}\}$. Clearly $x_0 \in U$.

\textbf{Case 1:} $y_0 \in U$. Let $x_0, e_1, x_1, \ldots, e_m, y_0$ be an unsaturated $x_0y_0$-path. Then the circuit $D = x_0, e_1, x_1, \ldots, e_m, y_0, e_0, x_0$ has the property that $h_D$ satisfies $h_D(e_0) = 1$ and $h + (1/n)h_D$ is feasible with $h(e_0) + 1/n > h(e_0)$, contradicting the maximality of $h$ among flows with denominators $n$.

\textbf{Case 2:} $y_0 \notin U$. Let $C$ be the cut determined by $U$. Then $C$ is a cut through $e_0$ (since $x_0 \in U$ and $y_0 \notin U$). For every edge $e = (x, y)$:
- If $x \in U$ and $y \notin U$ (forward across cut), then the path cannot be extended, so $h(e) = k(e)$ (otherwise we could extend to $y$).
- If $y \in U$ and $x \notin U$ (backward across cut), then the path cannot be reversed, so $h(e) = 0$.

Now $h(e_0) = \sum_{g_U(e) = -1} h(e)$ and $k(C; e_0) = \sum_{g_U(e) = 1} k(e)$. By the orthogonality relation $h \cdot g_U = 0$ and the observations above,
$$h(e_0) = \sum_{g_U(e) = 1} h(e) = \sum_{g_U(e) = 1} k(e) = k(C; e_0).$$

Thus $h(e_0) = k(C; e_0)$, and $h$ is a maximum flow through $e_0$ with value equal to the minimum cut capacity. The result follows.
