---
role: proof
locale: en
of_concept: complete-nuclear-space-projective-limit
source_book: gtm003
source_chapter: "III"
source_section: "7. Nuclear Mappings and Spaces"
---

We prove the second assertion concerning Fréchet spaces.

**Necessity.** Suppose $E$ is a nuclear (F)-space. By Corollary 2 there exists a decreasing base $\{V_n : n \in \mathbb{N}\}$ at $0$ such that each $\tilde{E}_{V_n}$ is a Hilbert space. Set $H_n = \tilde{E}_{V_n}$. By Theorem 7.2(c) we can further ensure (by passing to a subsequence of neighborhoods if necessary) that each of the canonical maps $\phi_{V_n, V_{n+1}}: H_{n+1} \to H_n$ is nuclear. Define $g_{mn} = \phi_{V_m, V_n}$ for $m \leq n$; then $g_{mn}$ is nuclear whenever $m < n$ by Corollary 2 of (7.1) (as a composition of nuclear maps). Since $E$ is complete, we have $E = \varprojlim_n H_n$ with connecting maps $g_{mn}$.

**Sufficiency.** Conversely, suppose $E = \varprojlim_n H_n$ is the projective limit of a sequence of Hilbert spaces with nuclear connecting maps $g_{mn}$ for $m < n$. Let $V$ be a convex, circled $0$-neighborhood chosen from a suitable base in $E$. Then the canonical map $E \to \tilde{E}_V$ can be identified with the projection $p$ of $E$ onto a finite product of the spaces $H_n$, say $\prod_{k=1}^m H_k$. Denoting by $p_n$ the projection of $E$ into $H_n$, we have $p = (p_1, \ldots, p_m)$. For any $n > m$, we have $p_k = g_{kn} \circ p_n$ for each $k$, hence
$$p = (g_{1n} \circ p_n, \ldots, g_{mn} \circ p_n).$$
Since each $g_{kn}$ ($k \leq m < n$) is nuclear by hypothesis and $p_n$ is continuous, each component $g_{kn} \circ p_n$ is nuclear by Corollary 2 of (7.1). Therefore $p$ is nuclear as a finite tuple of nuclear maps, proving that $E$ is nuclear.
