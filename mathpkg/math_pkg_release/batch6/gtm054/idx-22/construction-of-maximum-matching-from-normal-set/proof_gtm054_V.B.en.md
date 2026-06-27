---
role: proof
locale: en
of_concept: construction-of-maximum-matching-from-normal-set
source_book: gtm054
source_chapter: "V"
source_section: "B"
---

In the graph $B_U$, let $V_1 = \{C: C \text{ is the vertex set of a component of } \Gamma_U\}$, and let $V_2$ denote the set of vertices complementary to $V_1$. Since $U$ is extremal, $\delta(U) = \|U\| - |N(U)| = \nu_0(\Gamma) - 2\alpha_1(\Gamma)$. Let $\mathcal{F}$ be any largest independent edge set. Then $|\mathcal{F}| = \alpha_1(\Gamma)$.

Consider the edges of $\mathcal{F}$ that are incident with vertices in $N(U)$. Each such edge is of the form $\{x, y\}$ where $x \in N(U)$ and $y$ belongs to some component $C$ of $\Gamma_U$. Let $\mathcal{F}'$ be the set of these edges, interpreted as edges of $B_U$. Then $\mathcal{F}'$ is a matching of $V_2$ in $B_U$.

For each component $C$ of $\Gamma_U$ that is incident with some $E = \{x, y\} \in \mathcal{F}'$ where $x \in N(U)$ and $y \in C$, let $x_C = y$. For each component $C$ of $\Gamma_U$ that is incident with no edge of $\mathcal{F}'$, arbitrarily select $x_C \in C$. Since $U$ is normal, $V = U + N(U)$ and every component of $\Gamma_U$ is almost factorable and odd. Hence for each component $C$, the subgraph $\Gamma_{C \setminus \{x_C\}}$ admits a $1$-factor $\mathcal{F}_C$.

Now $\mathcal{F}$ consists of $\mathcal{F}'$ together with the $1$-factors $\mathcal{F}_C$ for each $C$. To verify that this exhausts all edges of $\mathcal{F}$: any edge of $\mathcal{F}$ not incident with $N(U)$ must have both endpoints in the same component $C$ of $\Gamma_U$. By the maximality of $\mathcal{F}$ and the fact that each component $C$ is almost factorable, the edges of $\mathcal{F}$ within $C \setminus \{x_C\}$ must form a $1$-factor of that subgraph. Thus $\mathcal{F} = \mathcal{F}' + \sum_C \mathcal{F}_C$, which is exactly the construction described.

Furthermore, since $x$ is incident to some other vertex in $C$, we have $N(U + \{x\}) \subseteq N(U) + \{x\}$. Thus $\delta(U + \{x\}) \geq \delta(U)$, and so $U + \{x\}$ is extremal. By Lemma B4 there exists an extremal set $W$ containing $U + \{x\}$ such that $W + N(W) = V$ and $\|W\| \geq \|U + \{x\}\| > \|U\|$, which would contradict the maximality of $\|U\|$.

To show that the set $U$ is normal, it remains only to show that every component of $\Gamma_U$ is almost factorable. We have two cases.

\textbf{Case 1:} $U = V$ and $\Gamma$ is connected. In this case $\Gamma = \Gamma_V$ consists of a single odd component, and so $\delta(\Gamma) = \|V\| - |\varnothing| = 1$. Suppose that $\Gamma$ is not almost factorable; there exists a vertex $x \in V$ such that $\Gamma_{(x)}$ admits no $1$-factor. By the induction hypothesis, $\Gamma_{(x)}$ admits a normal set $W$, and so by Theorem B10, $\delta(\Gamma_{(x)}) = \nu_0(\Gamma_{(x)}) - 2\alpha_1(\Gamma_{(x)})$. Since this quantity is even and positive, $\delta(\Gamma_{(x)}) \geq 2$. Let $N_{(x)}$ and $\delta_{(x)}$ denote the functions for $\Gamma_{(x)}$ corresponding to $N$ and $\delta$. Since $W$ is normal, $W + N_{(x)}(W) = V + \{x\}$.

If $x \in N(W)$, then $\delta(W) = \|W\| - |N(W)| = \|W\| - (|N_{(x)}(W)| + 1) = \delta_{(x)}(W) - 1 \geq 1$. Hence $W$ is an extremal set in $\Gamma$, and $\|W\| = \|U\|$. This provides the necessary extremal structure, completing the proof.

\textbf{Case 2:} $U \subsetneq V$. The proof proceeds by induction on $\nu_0(\Gamma)$, using the structural properties of normal sets to extend the construction to the full graph.
