---
role: proof
locale: en
of_concept: bipartite-deficiency-sum
source_book: gtm054
source_chapter: "V"
source_section: "B"
---

Let $B = \{V_1, V_2\}, \mathcal{E}$ be a bipartite graph. We first show that if $U \subseteq V_1 \cup V_2$ is a smallest extremal set in $B$, then $U$ is independent. Let $W$ be the vertex set of a component of $B_U$ with an odd number of vertices.

[First part of proof truncated in source text.]

To prove the reverse inequality, let $U_1$ and $U_2$ be critical subsets of $V_1$ and $V_2$, respectively, and let $W = (U_1 \cap N(U_2)) \cup (U_2 \cap N(U_1))$. Then

$$\begin{aligned}
\delta_1(\mathbf{B}) + \delta_2(\mathbf{B}) &= |U_1| + |U_2| - (|N(U_1)| + |N(U_2)|) \\
&= |U_1| + |U_2| - (|N(U_1 \cup U_2)| + |W|) \\
&\leq \|U_1 \cup U_2\| + |W| - |N(U_1 \cup U_2)| - |W| \\
&= \delta(U_1 \cup U_2) \leq \delta(\mathbf{B}).
\end{aligned}$$

The first direction showing $\delta(\mathbf{B}) \leq \delta_1 + \delta_2$ uses the fact that a smallest extremal set is independent, from which the bipartite sub-deficiencies can be bounded.
