---
role: proof
locale: en
of_concept: elementary-circuit-flow-augmentation
source_book: gtm054
source_chapter: "IV"
source_section: "18"
---

By the Max-Flow-Min-Cut Theorem (C6), there exists an integral maximum flow $h'$ through $e_0$. By A17, the integral flow $h' - h$ admits an $\mathcal{M}$-decomposition $\{g_1, \ldots, g_m\}$ where each $g_i$ is elementary, $\sigma(g_i) \subseteq \sigma(h' - h)$, and $(h' - h)(e)g_i(e) \geq 0$ for all $e \in W$ and all $i = 1, 2, \ldots, m$.

Since $h'(e_0) > h(e_0)$ by assumption (because $h$ is not a maximum flow), we have $g_j(e_0) = 1$ for some $j$. By B8, $g_j = h_D$ for some elementary circuit $D$ of $\Gamma$.

Now we verify $h + h_D$ is feasible. For any $e \in W$:
- If $h_D(e) = 1$, then $g_j(e) = 1$, so $(h' - h)(e) \geq g_j(e) = 1$ implies $h(e) + 1 \leq h'(e) \leq k(e)$.
- If $h_D(e) = -1$, then $g_j(e) = -1$, so $(h' - h)(e) \leq g_j(e) = -1$ implies $h(e) - 1 \geq h'(e) \geq 0$.
- If $h_D(e) = 0$, then $(h + h_D)(e) = h(e)$, which is already feasible.

Thus $h + h_D$ is feasible, $h_D(e_0) = 1$, and the proposition is proved.
