---
role: proof
locale: en
of_concept: nuclear-frechet-space-as-projective-limit-of-hilbert-spaces
source_book: gtm003
source_chapter: "III"
source_section: "7"
---

Let $E$ be a nuclear (F)-space. By Corollary 2, there exists a decreasing base $\{V_n : n \in \mathbb{N}\}$ at $0$ such that each $\tilde{E}_{V_n}$ is a Hilbert space. By (7.2)(c), we may refine so that each canonical map $\phi_{V_n, V_{n+1}}: \tilde{E}_{V_{n+1}} \to \tilde{E}_{V_n}$ is nuclear. The representation $E = \varprojlim_n H_n$ with $H_n = \tilde{E}_{V_n}$ and $g_{mn} = \phi_{V_m, V_n}$ ($m \leq n$) gives the desired projective limit with nuclear linking maps.

Conversely, if $E$ has such a representation and $V$ is a convex, circled $0$-neighborhood from a suitable base, then $E \to \tilde{E}_V$ can be identified with the projection $p$ of $E$ into a finite product $\prod_{k=1}^{m} H_k$. Denoting by $p_n$ the projection of $E$ into $H_n$, we have $p = (p_1, \ldots, p_m) = (g_{1n} \circ p_n, \ldots, g_{mn} \circ p_n)$ for any $n > m$, which shows $p$ is nuclear since each $g_{kn}$ is nuclear.
