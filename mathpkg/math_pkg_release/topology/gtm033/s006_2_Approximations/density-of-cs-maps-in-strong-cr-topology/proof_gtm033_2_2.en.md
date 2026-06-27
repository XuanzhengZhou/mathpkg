---
role: proof
locale: en
of_concept: density-of-cs-maps-in-strong-cr-topology
source_book: gtm033
source_chapter: "2"
source_section: "2"
---

# Proof of Theorem 2.6 (Density of $C^s$ maps in the strong $C^r$ topology)

Let $f: M \to N$ be $C^r$. Let $\Phi = \{\varphi_i, U_i\}_{i \in \Lambda}$ be a locally finite atlas for $M$ and $\Psi = \{\psi_i, V_i\}_{i \in \Lambda}$ a family of charts for $N$ such that for all $i \in \Lambda$, $f(U_i) \subset V_i$. Let $L = \{L_i\}_{i \in \Lambda}$ be a closed cover of $M$, $L_i \subset U_i$. Let $\varepsilon = \{\varepsilon_i\}_{i \in \Lambda}$ be a family of positive numbers, and put $\mathcal{N} = \mathcal{N}^r(f; \Phi, \Psi, L, \varepsilon) \subset C^r(M,N)$.

We look for a $g \in \mathcal{N}$ which is $C^s$. The set $\Lambda$ is countable; we therefore assume that $\Lambda = \mathbb{Z}_+$ or, if $M$ is compact, $\Lambda = \{1, \ldots, p\}$. (We denote the integers by $\mathbb{Z}$, the positive integers by $\mathbb{Z}_+$, and the natural numbers by $\mathbb{N} = \mathbb{Z}_+ \cup \{0\}$.)

Let $\{W_i\}_{i \in \Lambda}$ be a family of open sets in $M$ such that $L_i \subset W_i \subset \overline{W_i} \subset U_i$. Then by the Relative Approximation Theorem (Theorem 2.5) applied in charts, one constructs by induction a sequence of maps $g_0, g_1, \ldots$ such that $g_k \in \mathcal{N}$ and $g_k$ is $C^s$ on a neighborhood of $\bigcup_{i=1}^k L_i$. In the case $\Lambda$ is finite (e.g., $M$ compact) the construction terminates at $g_p$, yielding the desired $C^s$ map. In the countably infinite case, the maps $g_k$ converge in the strong $C^r$ topology to a limit map $g \in \mathcal{N}$ which is $C^s$ on all of $M$.

Thus $C^s(M,N)$ is dense in $C^r_S(M,N)$, $0 \leqslant r < s$.

QED
