---
role: proof
locale: en
of_concept: closed-graph-theorem
source_book: gtm015
source_chapter: "V"
source_section: "48"
---

# Proof of the Closed Graph Theorem

Equipped with the product vector space structure and the product topology (11.9), $E \times F$ is also a metrizable, complete TVS. (If $E$ and $F$ are metrized by the additively invariant metrics $d, \delta$, then the metric $D((x, y), (x', y')) = d(x, x') + \delta(y, y')$ induces the product topology on $E \times F$ and is clearly invariant; since $d$ and $\delta$ are complete metrics, so is $D$, thus $E \times F$ is complete (7.8).)

Clearly $G_T = \{(x, Tx) : x \in E\}$ is a linear subspace of $E \times F$, and the mapping $S: G_T \to E$ defined by $S(x, Tx) = x$ is a vector space isomorphism. It is trivial that $S$ is continuous (it is the restriction of the projection onto $E$, which is continuous).

($\Rightarrow$) If $G_T$ is closed in $E \times F$, then $G_T$ is also a metrizable, complete TVS (12.1), therefore $S$ is bicontinuous by Corollary 48.4 (bicontinuous isomorphism for bijective continuous linear maps between metrizable, complete TVS). Composing with the projection of $E \times F$ onto $F$, we see that $x \mapsto S^{-1}x = (x, Tx) \mapsto Tx$ is continuous. Hence $T$ is continuous.

($\Leftarrow$) If, conversely, $T$ is continuous, then $G_T$ is closed in $E \times F$ by elementary general topology: if $(x_n, Tx_n) \to (x, y)$ in $E \times F$, then $x_n \to x$ and $Tx_n \to y$; by continuity of $T$, $Tx_n \to Tx$, so $y = Tx$ and $(x, y) = (x, Tx) \in G_T$. (No linear or metric structure is needed for this direction; it is sufficient that $E$ and $F$ be separated topological spaces.) $\square$
