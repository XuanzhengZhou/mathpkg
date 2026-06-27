---
role: proof
locale: en
of_concept: sublattice-approximation-pair-of-points
source_book: gtm043
source_chapter: "16"
source_section: "3"
---
Fix $\epsilon > 0$. For each pair of points $p, q \in X$, let $g_{pq}$ be a function in $A$ such that
$$|f(p) - g_{pq}(p)| < \epsilon \quad \text{and} \quad |f(q) - g_{pq}(q)| < \epsilon.$$
For each fixed $q$, the union over $p$ of the open sets
$$\{x: g_{pq}(x) - f(x) < \epsilon\}$$
is all of $X$, and hence a finite number of them, say for $p_1, \dots, p_s$, cover $X$. Let
$$g_q = g_{p_1q} \wedge \dots \wedge g_{p_sq}.$$
Then $g_q \in A$, $g_q \leq f + \epsilon$, and $g_q(x) > f(x) - \epsilon$ for all $x \in V_q$, where
$$V_q = \bigcap_{k \leq s} \{x: g_{p_kq}(x) > f(x) - \epsilon\}.$$
Each set $V_q$ is open; and $\bigcup_{q \in X} V_q = X$, since $q \in V_q$. Hence, a finite number of these sets cover $X$; let $g$ denote the supremum of the corresponding functions $g_q$. Then $g \in A$, and $|f - g| \leq \epsilon$, i.e., $d(f, g) \leq \epsilon$.
