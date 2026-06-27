---
role: exercise
locale: en
chapter: "2"
section: "5"
exercise_number: 18
---

: Continuing this notation, find the component partition of $\Lambda^*$.

Let $\Lambda = (V, f, E)$ be a system, and let $s, t \in V \cup E$. An $st$-path is a sequence $s = s_0, s_1, \ldots, s_n = t$ of elements of $V \cup E$ such that:
(a) any three consecutive terms of the sequence are distinct;
(b) $\{s_{j-1}, s_j\}$ is an edge of the bipartite graph of $\Lambda$ for $j = 1, \ldots, n$.

For example, if $x, y \in V$, an $xy$-path is an alternating sequence $x = x_0, e_1, x_2, e_3, \ldots, e_{n-1}, x_n = y$ of vertices and blocks such that $\{x_i, x_{i+2}\} \subseteq f(e_{i+1})$ for $i = 0, 2, \ldots, n-2$. Note that a single vertex or block is itself a path; such a path is said to be trivial. A path is said to be elementary if all of its terms are distinct.
