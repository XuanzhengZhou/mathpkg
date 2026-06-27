---
role: proof
locale: en
of_concept: subcontraction-circuit-lemma
source_book: gtm054
source_chapter: "III"
source_section: "14 (III.G)"
---

Let $V = \{y_1, y_2, x_1, \ldots, x_k\}$, and suppose $\{y_1, y_2\}, \{x_i, x_{i+1}\} \in \mathcal{E}$, the indices being read modulo $k$, and that there are no other edges of the form $\{x_i, x_j\}$.

**Case 1:** Three or more of the vertices $x_1, \ldots, x_k$ have valence $4$ (i.e., are incident with both $y_1$ and $y_2$). Say $x_1$, $x_p$, and $x_q$ all have valence $4$ ($1 < p < q \leq k$). Then the contraction defined by the partition

$$\{\{x_1, \ldots, x_{p-1}\}, \{x_p, \ldots, x_{q-1}\}, \{x_q, \ldots, x_k\}, \{y_1\}, \{y_2\}\}$$

of $V$ contains $K_5$ as a subgraph. We conclude $\Gamma$ is $K_5$.

**Case 2:** At most two of the vertices in $\{x_1, \ldots, x_k\}$ have valence $4$. Since $|V| > 4$ by E19b, and since each vertex of $\Gamma$ has valence at least $3$ by G7a, we may assume $x_1$ is incident with $y_1$ and not with $y_2$ and that $x_k$ is incident with $y_2$. Now let $p$ be the least index such that $x_p$ is incident with $y_2$, and let $q$ be the largest index such that $x_q$ is incident with $y_1$. One can show that contracting the sets $\{x_1, \ldots, x_p\}$, $\{x_p, \ldots, x_q\}$, $\{x_q, \ldots, x_k\}$ together with $\{y_1\}$ and $\{y_2\}$ yields $K_{3,3}$ as a subgraph of the contraction, implying $\Gamma$ is $K_{3,3}$.
