---
role: proof
locale: en
of_concept: topology-of-group-uniformities
source_book: gtm027
source_chapter: "6"
source_section: "O"
---

# Proof: The Topology of a Topological Group Coincides with Its Uniform Topologies

Let $(G, \mathcal{J})$ be a topological group. For each neighborhood $U$ of the identity $e$, define

$$U_L = \{(x, y) : x^{-1}y \in U\}, \quad U_R = \{(x, y) : xy^{-1} \in U\}.$$

The left uniformity $\mathcal{L}$ has base $\{U_L : U \text{ a neighborhood of } e\}$, the right uniformity $\mathcal{R}$ has base $\{U_R\}$, and the two-sided uniformity $\mathcal{U}$ has $\mathcal{L} \cup \mathcal{R}$ as subbase.

For each neighborhood $U$ of $e$, the set $U_L[x] = \{y : x^{-1}y \in U\} = xU$ is a neighborhood of $x$ in $\mathcal{J}$. Conversely, every $\mathcal{J}$-neighborhood of $x$ is of the form $xV$ for some neighborhood $V$ of $e$, hence equals $V_L[x]$. Thus the topology of $\mathcal{L}$ equals $\mathcal{J}$.

Similarly, $U_R[x] = \{y : xy^{-1} \in U\} = Ux^{-1}$ is a neighborhood of $x$ in $\mathcal{J}$, and every $\mathcal{J}$-neighborhood of $x$ can be written as $V_R[x]$. Thus the topology of $\mathcal{R}$ equals $\mathcal{J}$.

Since $\mathcal{L} \cup \mathcal{R}$ is a subbase for $\mathcal{U}$, the topology of $\mathcal{U}$ is the supremum of the topologies of $\mathcal{L}$ and $\mathcal{R}$, which both equal $\mathcal{J}$. Hence the topology of $\mathcal{U}$ equals $\mathcal{J}$.
