---
role: proof
locale: en
of_concept: tutte-normal-set-matching-construction
source_book: gtm054
source_chapter: "V"
source_section: "B"
---

In the graph $B_U$, let $V_1 = \{C: C \text{ is the vertex set of a component of } \Gamma_U\}$, and let $V_2$ denote the set of vertices complementary to $V_1$. Since $U$ is extremal,
$$\delta(U + \{x\}) \geq \delta(U)$$
since $x$ is incident to some other vertex in $C$, we have $N(U + \{x\}) \subseteq N(U) \cup \{x\}$. Thus $\delta(U + \{x\}) \geq \delta(U)$, and so $U + \{x\}$ is extremal. By B4 there exists an extremal set $W$ containing $U + \{x\}$ such that $W + N(W) = V$ and $|W| \geq |U + \{x\}| > |U|$, contrary to the maximality of $|U|$.

To show that the set $U$ is normal, it remains only to show that every component of $\Gamma_U$ is almost factorable. We have two cases.

\textbf{Case 1:} $U = V$ and $\Gamma$ is connected. In this case $\Gamma = \Gamma_V$ consists of a single odd component, and so $\delta(\Gamma) = |V| - |\varnothing| = 1$. Suppose that $\Gamma$ is not almost factorable; there exists a vertex $x \in V$ such that $\Gamma_{(x)}$ admits no 1-factor. By the induction hypothesis, $\Gamma_{(x)}$ admits a normal set $W$, and so by Theorem B10,
$$\delta(\Gamma_{(x)}) = \nu_0(\Gamma_{(x)}) - 2\alpha_1(\Gamma_{(x)}).$$
Since this quantity is even and positive, $\delta(\Gamma_{(x)}) \geq 2$. Let $N_{(x)}$ and $\delta_{(x)}$ denote the functions for $\Gamma_{(x)}$ corresponding to $N$ and $\delta$. Since $W$ is normal, $W + N_{(x)}(W) = V \setminus \{x\}$.

If $x \in N(W)$, then
$$\delta(W) = |W| - |N(W)| = |W| - (|N_{(x)}(W)| + 1) = \delta_{(x)}(W) - 1 \geq 1.$$
Hence $W$ is an extremal set in $\Gamma$, and $|W|$ satisfies the required conditions. This completes the proof of Case 1.

\textbf{Case 2:} $U \neq V$ or $\Gamma$ is disconnected. The proof proceeds by a similar argument, using the maximality of $U$ and the induction hypothesis applied to each component.

The construction procedure described in the theorem statement follows directly: each largest independent edge set $\mathcal{F}$ is built by taking a matching $\mathcal{F}'$ in the bipartite graph $B_U$, selecting representative vertices $x_C$ from each component, using the 1-factors guaranteed by the almost factorable property within each component, and combining these pieces.

Note in particular how this result generalizes Corollary A6 from bipartite graphs to all graphs.
