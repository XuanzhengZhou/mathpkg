---
role: proof
locale: en
of_concept: characterization-theorem-for-algebraic-structure-on-sets
source_book: gtm026
source_chapter: "1"
source_section: "1.13"
---

**Proof of necessity.** This follows immediately from 1.4.12, 2.1.11, 2.1.14, 2.1.22, 1.5, and 1.9.

**Proof of sufficiency.** By 1.9, it is enough to prove that $U$ creates co-equalizers of $U$-contractible pairs. To this end, suppose given a pair $f, g: A \longrightarrow B$ of morphisms in $\mathcal{A}$ and functions $h: BU \longrightarrow K$, $d: BU \longrightarrow AU$ and $d': K \longrightarrow BU$ such that $(fU, gU, h; d, d')$ is a contractible co-equalizer in $\mathbf{Set}$.

**Claim:** It is sufficient to find a congruence $R$ on $B$, with coordinate projections $p, q: R \longrightarrow BU$, such that $h = \text{coeq}(p, q)$ in $\mathbf{Set}$.

For suppose such $R$ exists. Since the canonical projection $\theta: BU \longrightarrow BU/R$ is also a coequalizer of $(p, q)$, there exists an isomorphism $\Gamma: BU/R \longrightarrow K$ such that $\theta.\Gamma = h$.

To complete the proof we must demonstrate that $R$ is a congruence. To prove this we will have to appeal once again to the fact that $U$ creates quotients of congruences.

As kernel pairs are separators, the kernel pair $(E, a, b)$ of $g$ exists in $\mathcal{A}$. Because $aU.fU.d.gU = aU.gU.d.gU = bU.gU.d.gU = bU.fU.d.gU$, there exists a unique function $\gamma: EU \longrightarrow R$ such that $\gamma.p = aU.fU$ and $\gamma.q = bU.fU$. Define $R_1$ to be the separator of $aU.fU$ and $bU.fU$ in $\mathbf{Set}$. Clearly, $R_1$ is an equivalence relation on $EU$. In fact, $R_1$ is a congruence (proof: the separator $(C, p_1, q_1)$ of $a.f$ and $b.f$ exists in $\mathcal{A}$ by hypothesis; since $U$ preserves limits (2.2.22) $(CU, p_1U, q_1U)$ is a separator of $aU.fU$ and $bU.fU$, so is isomorphic to $R_1$ with its coordinate projections; but then, since $(\mathcal{A}, U)$ is in $\text{Struct}(\mathbf{Set})$, we may transport the isomorphism $CU \cong R_1$ or, even better, assume that $(C, p_1, q_1)$ was over $R_1$ to begin with).

**Claim:** It is sufficient to prove that $\gamma = \text{coeq}(p_1U, q_1U)$ in $\mathbf{Set}$.

For then, arguing as in the previous claim, $\gamma$ admits a co-optimal lift $\bar{\gamma}: E \longrightarrow \bar{R}$; but then, since $\gamma.p = a.f$ and $\gamma.q = b.f$ are admissible, so are $p$ and $q$. This supports the second claim.

Our method will be to show that $(p_1U, q_1U)$ is the kernel pair of $\gamma$ and that $\gamma$ is split epi (and hence a coequalizer) so that, by 2.1.53, $\gamma = \text{coeq}(p_1U, q_1U)$.

**$(p_1U, q_1U)$ is the kernel pair of $\gamma$:** Since $p_1U$ and $q_1U$ compose equally with $aU.fU$, $p_1U.\gamma$ and $q_1U.\gamma$ compose equally with $p$. Similarly, $p_1U.\gamma$ and $q_1U.\gamma$ compose equally with $q$. Therefore (cf. 1.20) $p_1U.\gamma = q_1U.\gamma$. Suppose that $t.\gamma = u.\gamma$. Then, clearly, $t$ and $u$ compose equally with $aU.fU$ and $bU.fU$, inducing the desired unique map $T \longrightarrow CU$.

**$\gamma$ is split epi:** As $(EU, aU, bU)$ is the kernel pair of $gU$ (2.2.22) and $p.d.gU = q.d.gU$ there exists a unique function $\delta: R \longrightarrow EU$ such that $\delta.aU = p.d$ and $\delta.bU = q.d$. Since $d.fU = \text{id}_{BU}$ (1.3) $\delta.\gamma.p = p$ and $\delta.\gamma.q = q$ so $\delta.\gamma = \text{id}_R$. The proof is complete.
