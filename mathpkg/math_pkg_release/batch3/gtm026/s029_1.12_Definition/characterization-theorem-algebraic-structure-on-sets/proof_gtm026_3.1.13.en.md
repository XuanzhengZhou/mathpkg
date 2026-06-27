---
role: proof
locale: en
of_concept: characterization-theorem-algebraic-structure-on-sets
source_book: gtm026
source_chapter: "3"
source_section: "1.13"
---

Necessity follows from 1.4.12, 2.1.11, 2.1.14, 2.1.22, 1.5, and 1.9.

For sufficiency, by 1.9 it suffices to prove that $U$ creates coequalizers of $U$-contractible pairs. Suppose given $f, g: A \longrightarrow B$ in $\mathcal{A}$ and functions $h: BU \longrightarrow K$, $d: BU \longrightarrow AU$, $d': K \longrightarrow BU$ such that $(fU, gU, h; d, d')$ is a contractible coequalizer in $\mathbf{Set}$.

The strategy is to find a congruence $R$ on $B$ with coordinate projections $p, q: R \longrightarrow BU$ such that $h = \mathrm{coeq}(p, q)$ in $\mathbf{Set}$. Then since $U$ creates quotients of congruences, the canonical projection $\theta: BU \longrightarrow BU/R$ has a unique co-optimal lift, and composing with the isomorphism $BU/R \cong K$ yields the required lift of $h$.

The congruence $R$ is constructed as follows. Let $(E, a, b)$ be the kernel pair of $g$ in $\mathcal{A}$ (which exists because kernel pairs are separators). Since $aU.fU.d.gU = bU.fU.d.gU$, there exists a unique $\gamma: EU \longrightarrow R$ such that $\gamma.p = aU.fU$ and $\gamma.q = bU.fU$, where $R$ is the separator (in $\mathbf{Set}$) of $aU.fU$ and $bU.fU$. The separator $(C, p_1, q_1)$ of $a.f$ and $b.f$ exists in $\mathcal{A}$ by hypothesis, and since $U$ preserves limits, $(CU, p_1U, q_1U)$ is isomorphic to $R_1$, the separator in $\mathbf{Set}$, which is an equivalence relation on $EU$ and indeed a congruence.

One then shows that $(p_1U, q_1U)$ is the kernel pair of $\gamma$, that $\gamma$ is split epi, and hence $\gamma = \mathrm{coeq}(p_1U, q_1U)$ by 2.1.53. This implies $\gamma$ lifts to a co-optimal map, making $p$ and $q$ admissible, so $R$ is indeed a congruence on $B$.
