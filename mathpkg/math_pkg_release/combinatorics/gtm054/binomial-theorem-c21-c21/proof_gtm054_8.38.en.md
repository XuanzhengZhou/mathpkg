---
role: proof
locale: en
of_concept: binomial-theorem-c21-c21
source_book: gtm054
source_chapter: "8"
source_section: "VIIID"
---

We proceed by induction on $m$. If $m = 1$, then in fact equality holds by C8a and B3.

As induction hypothesis, suppose that the given inequality holds for some $m \geq 1$. Let $p = (m+1)[n(3^{(m)}) - 1] + 2$, and let $V$ be a $p$-set. Arbitrarily choose $h: \mathcal{P}_2(V) \rightarrow \{1, \ldots, m+1\}$.

Let $x \in V$, and define for each $i = 1, \ldots, m+1$,

$$Q_i = \{y \in V + \{x\}: h(\{x, y\}) = i\}.$$

Noting that $(p-1)/(m+1) = n(3^{(m)}) - 1 + 1/(m+1)$, we infer that $|Q_i| \geq n(3^{(m)})$ for some $i = 1, \ldots, m+1$.

If $h(\{y, z\}) = i$ for some $y, z \in Q_i$, then $U = \{x, y, z\}$ is a 3-subset such that $\mathcal{P}_2(U) \subseteq h^{-1}[i]$. Otherwise, consider the restriction $h_1$ of $h$, namely $h_1: \mathcal{P}_2(Q_i) \rightarrow \{1, \ldots, m+1\} + \{i\}$. But since $|Q_i| \geq n(3^{(m)})$, there exists a subset $T \in \mathcal{P}_3(Q_i)$ such that $\mathcal{P}_2(T) \subseteq h^{-1}[j]$ for some $j \in \{1, \ldots, m+1\} + \{i\}$. Hence $n(3^{(m+1)}) \leq p$.

Greenwood

VIIID Perfect Graphs

A graph $\Gamma = (V, \mathcal{E})$ is said to be color-perfect if $\omega(\Gamma_s) = \chi_0(\Gamma_s)$ for all $S \in \mathcal{P}(V)$. By A2 and A3, $\Gamma'$ is color-perfect if and only if $\alpha_0(\Gamma_s) = \theta(\Gamma_s)$ for all $S \in \mathcal{P}(V)$. A graph $\Gamma$ is said to be perfect if both $\Gamma$ and $\Gamma'$ are color-perfect In 1961, C. Berge first published [b.4] the following conjecture:
