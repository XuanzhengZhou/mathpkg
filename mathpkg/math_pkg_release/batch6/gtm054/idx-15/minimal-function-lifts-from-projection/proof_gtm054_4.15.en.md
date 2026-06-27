---
role: proof
locale: en
of_concept: minimal-function-lifts-from-projection
source_book: gtm054
source_chapter: "IV"
source_section: "15"
---

Since $g \in \pi_Y[L]$, we have $g = h'c_Y$ for some $h' \in L$. Apply Proposition A6 to obtain an $\mathcal{M}$-decomposition $\{h_1, \ldots, h_m\}$ of $h'$. Then

$$g = h'c_Y = \sum_{i=1}^{m} h_i c_Y,$$

and $\sigma(h_i c_Y) \subseteq \sigma(g)$ for each $i$. Since $g$ is a minimal function of $\pi_Y[L]$, Proposition A2 implies that for each $i$, there exists $\eta_i \in \mathbb{Q}$ such that $h_i c_Y = \eta_i g$. Since $g \neq 0$, there exists some index with $\eta_i \neq 0$; say $\eta_1 \neq 0$. Set $h = \eta_1^{-1} h_1$. Then $h$ is a minimal function of $L$ and $g = h c_Y = \pi_Y(h)$.
