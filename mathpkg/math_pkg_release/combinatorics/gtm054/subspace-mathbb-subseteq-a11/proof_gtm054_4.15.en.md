---
role: proof
locale: en
of_concept: subspace-mathbb-subseteq-a11
source_book: gtm054
source_chapter: "4"
source_section: "Section 15"
---

Since $g \in \pi_Y[L]$, $g = h'c_Y$ for some function $h' \in L$. Applying the proposition, let $\{h_1, \ldots, h_m\}$ be an $\mathcal{M}$-decomposition of $h'$. Clearly,

$$g = h'c_Y = \sum_{i=1}^{m} h_i c_Y,$$

and $\sigma(h_i c_Y) \subseteq \sigma(g)$. By Proposition A2, there exists $\eta_i \in \mathbb{Q}$ such that $h_i c_Y = \eta_i g$ ($i = 1, \ldots, m$). Since $g \neq 0$, $\eta_i \neq 0$ for some index $i$; say $\eta_1 \neq 0$. Let

$$h = \frac{1}{\eta_1} h_1.$$

Then $h$ is a minimal function of $L$ and $g = hc_Y = \pi_Y(h)$.

If $L$ is a subspace of $\mathbb{Q}^x$ and if $h$ is a minimal function of $L$, then there exists a smallest positive number $\theta \in \mathbb{Q}$

where $\eta_i$ is a positive rational number, $g_i$ is an elementary function of $L$, and $g_i(x)h(x) \geq 0$ for all $x \in X$ and all $i = 1, \ldots, m$.

Proof. Apply the proposition to $h$. By A2 and A13, each minimal function $h_i$ may be replaced by $\eta_i g_i$ where $\eta_i > 0$ and $g_i$ is an elementary function $(i = 1, \ldots, m)$.

A subspace $L$ of $\mathbb{Q}^X$ is unimodular if $g[X] \subseteq \{0, 1, -1\}$ for every elementary function $g$ of $L$.
