---
role: proof
locale: en
of_concept: separating-set-contraction-planarity
source_book: gtm054
source_chapter: "III"
source_section: "13 (III.G Kuratowski's Theorem)"
---

If $\Gamma$ is planar, then so are $\Gamma_1$ and $\Gamma_2$ by E15.

The converse follows from E17 in the case $|W| = 1$. We prove the converse in the case $|W| = 3$, leaving the case $|W| = 2$ to the reader.

Let $W = \{x_1, x_2, x_3\}$, and let $\{x_0, e_1, e_2, e_3\}$ be a set of four distinct elements disjoint from all sets in question. For $j = 1, 2$, let $V_j = U_j \cup W \cup \{x_0\}$; let $F_1$ be the edge set of $\Gamma_{W \cup U_1}$; let $F_2 = E \setminus F_1$; let $E_j = F_j \cup \{e_1, e_2, e_3\}$; and finally let $\Theta_j = (V_j, f_j, E_j)$ where

$$f_j(e) = \begin{cases} \{x_0, x_i\} & \text{if } e = e_i \ (i = 1, 2, 3); \\ f(e) & \text{otherwise.} \end{cases}$$

One easily sees that $\Theta_j$ is a subcontraction of $\Gamma$. The graphs $\Gamma_j$ and $\Theta_j$ may differ only in that $\Gamma_j$ may admit additional multiple edges.

**Part 1:** The cycles in a certain set $\{Z_i^j\}$ (read from Figure G5) are all in $\mathcal{L}(\Gamma)$ and each edge of $\Gamma$ which is not an isthmus belongs to exactly two of these cycles.

For $i \geq 4$, $j = 1, 2$, $Z_i^j \subseteq F_j$ and hence is a cycle of $(\Theta_j)_{U_j \cup W} = \Gamma_{U_j \cup W}$. But any cycle of $\Gamma_{U_j \cup W}$ is a cycle of $\Gamma$. We observe that $Z_1^j \cup \{e_2, e_3\}$ is the edge set of an $x_2 x_3$-path in $\Gamma_{U_j \cup W}$. Thus, $Z_1^1 \oplus Z_1^2$ is the edge set of a circuit in $\Gamma$ passing through $x_2$ and $x_3$, and by A9, $Z_1^1 \oplus Z_1^2 \in \mathcal{L}(\Gamma)$. Similarly $Z_2^1 \oplus Z_2^2$ and $Z_3^1 \oplus Z_3^2$ are cycles of $\Gamma$.

Observe that $E$ is the disjoint union of $F_1$ and $F_2$, and that if $e \in F_j$ is an isthmus of $\Theta_j$, then it is an isthmus of $\Gamma$. Thus if $e \in F_j$ and is not an isthmus of $\Gamma$, it belongs to two of the cycles $Z_1^j, \ldots, Z_m^j$, and hence to two of the cycles in the constructed set.

**Part 2:** The set of cycles constructed spans $\mathcal{L}(\Gamma)$.

Since $Z_1^j, \ldots, Z_m^j$ is a simple imbedding of $\Theta_j$, we have by Euler's Formula:

$$m_j - \nu_1(\Theta_j) + \nu_0(\Theta_j) = 2, \quad \text{for } j = 1, 2.$$

Adding these two equations together yields

$$m_1 + m_2 - (\nu_1(\Gamma) + 6) + (\nu_0(\Gamma) + \ldots)$$

and the counting argument shows that the constructed cycles form a simple imbedding of $\Gamma$, establishing its planarity.
