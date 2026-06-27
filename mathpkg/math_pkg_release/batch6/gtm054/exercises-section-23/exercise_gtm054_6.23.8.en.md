---
role: exercise
locale: en
chapter: "6"
section: "23"
exercise_number: 8
---

(a) Let $\Theta$ be a spanning subgraph of $\Gamma$. Show that if $\Theta$ is almost factorable, then so is $\Gamma$.
(b) Find all “edge-minimal” almost factorable graphs on $\leq 5$ vertices.

Corresponding to any

set $\{\{x\}: x \in N(U)\}$. Finally, each largest independent set $\mathcal{F}$ of edges of $\Gamma$ can be constructed as follows:

(a) Let $\mathcal{F}'$ be a matching of $\{\{x\}: x \in N(U)\}$ in $B_U$.

(b) Let $C$ be the vertex set of a component of $\Gamma_U$. Regarding $C$ as a vertex of $B_U$,

(i) if $C$ is incident with an edge $E \in \mathcal{F}'$, then let $x_C$ be the vertex in $C$ incident with $E$ in $\Gamma$.

(ii) if $C$ is incident with no edge in $\mathcal{F}'$, then arbitrarily select $x_C \in C$.

(c) Since $U$ is normal, there exists a 1-factor $\mathcal{F}_C$ in the component of $\Gamma_U$ with vertex set $C$.

(d) Let $\mathcal{F} = \mathcal{F}' + \sum_C \mathcal{F}_C$.

Before proving this theorem, let us first illustrate how the construction of $\mathcal{F}$ works for the graph $\Gamma$ and set $U$ of Example B6. First we must consider the graph $B_U$ of Figure B9. Let $\mathcal{F}' = \{E_1, E_5\}$. Then $x_{C_1} = b$ and $x_{C_2} = d$. Let us arbitrarily choose $x_{C_3} = f$. Then $\mathcal{F}_{C_1} = \{\{a, c\}\}, \mathcal{F}_{C_2} = \varnothing$, and $\mathcal{F}_{C_3} = \{\{e, g\}\}$. Hence $\mathcal{F} = \{E_1, E_5, \{a, c\}, \{e, g\}\}$.

PROOF OF THEOREM B10. In the graph $B_U$, let $V_1 = \{C: C$ is the vertex set of a component of $\Gamma_U\}$, and let $V_2$ denote the set of vertices complementary to $V_1$. Since $U$ is extremal, $\

since $x$ is incident to some other vertex in $C$, we have $N(U + \{x\}) \subseteq N(U) + \{x\}$. Thus $\delta(U + \{x\}) \geq \delta(U)$, and so $U + \{x\}$ is extremal. By B4 there exists an extremal set $W$ containing $U + \{x\}$ such that $W + N(W) = V$ and $\|W\| \geq \|U + \{x\}\| > \|U\|$, contrary to the maximality of $\|U\|$.

To show that the set $U$ is normal, it remains only to show that every component of $\Gamma_U$ is almost factorable. We have two cases.

Case 1: $U = V$ and $\Gamma$ is connected. In this case $\Gamma = \Gamma_V$ consists of a single odd component, and so $\delta(\Gamma) = \|V\| - |\varnothing| = 1$. Suppose that $\Gamma$ is not almost factorable; there exists a vertex $x \in V$ such that $\Gamma_{(x)}$ admits no 1-factor. By the induction hypothesis, $\Gamma_{(x)}$ admits a normal set $W$, and so by Theorem B10, $\delta(\Gamma_{(x)}) = \nu_0(\Gamma_{(x)}) - 2\alpha_1(\Gamma_{(x)})$. Since this quantity is even and positive, $\delta(\Gamma_{(x)}) \geq 2$. Let $N_{(x)}$ and $\delta_{(x)}$ denote the functions for $\Gamma_{(x)}$ corresponding to $N$ and $\delta$. Since $W$ is normal, $W + N_{(x)}(W) = V + \{x\}$.

If $x \in N(W)$, then $\delta(W) = \|W\| - |N(W)| = \|W\| - (|N_{(x)}(W)| + 1) = \delta_{(x)}(W) - 1 \geq 1$. Hence $W$ is an extremal set in $\Gamma$, and $\|W\| = \

Note in particular how Tutte’s result generalizes Corollary A6 from bipartite graphs to all graphs.
