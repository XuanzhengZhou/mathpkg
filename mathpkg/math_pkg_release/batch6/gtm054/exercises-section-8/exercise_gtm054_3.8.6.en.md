---
role: exercise
locale: en
chapter: "3"
section: "8"
exercise_number: 6
---

Prove:

(a) If $\rho(x) \geq 2$ for every vertex $x$ of the multigraph $\Gamma$, then $\Gamma$ contains a circuit.

(b) If $\rho(x) \geq 2$ for every vertex $x$ of the multigraph $\Gamma$, and if there exists a vertex of $\Gamma$ in no circuit, then $\Gamma$ contains two disjoint circuits.

(c) If $\rho(\Gamma) \geq 2$, then $\Gamma$ contains a circuit.

(d) Let $\Gamma$ be a connected multigraph. Then $\Gamma$ contains a circuit if and only if $\rho(\Gamma) \geq 2

include $f(e_{i+1})$ in order to “cancel out” $x_i$ (the indices being read modulo $k$). We conclude that $\{e_1, \ldots, e_k\}$ is elementary.

Conversely, assume that $Z$ is an elementary cycle of $\Gamma$. Since $\sum_{e \in Z} f(e) = \varnothing$, the vertices of $\Gamma_z$ all have valence 2 or more. By Exercise A6a, $\Gamma_z$ contains a circuit, the edges of which form a cycle $Z' \in \mathcal{L}(\Gamma_z) \subseteq \mathcal{L}(\Gamma)$. Clearly $Z' \subseteq Z$. Since $Z$ is elementary, $Z' = Z$, and $\Gamma_z$ is a circuit.

Note that the “converse” in this proposition is only a “partial converse.” It is not in fact true that every cycle is the set of edges of some circuit. For example, the edges of two disjoint circuits taken together form such a cycle. The strongest possible “converse” is given in the next proposition.
