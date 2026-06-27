---
role: proof
locale: en
of_concept: normal-subgroup-fixed-set-invariance
source_book: gtm006
source_chapter: "XIV"
source_section: "1"
---

**Proof.** (Result 14.5) Let $\Gamma$ be a permutation group on a set $\mathcal{S}$. If $\Sigma$ is a normal subgroup of $\Gamma$ and if $\mathcal{T}$ is the subset of all elements fixed by $\Sigma$ then $\Gamma$ leaves $\mathcal{T}$ invariant.

Let $t \in \mathcal{T}$ and $\gamma \in \Gamma$. We must show $t^\gamma \in \mathcal{T}$, i.e., that $\Sigma$ fixes $t^\gamma$. For any $\sigma \in \Sigma$, we need $(t^\gamma)^\sigma = t^\gamma$. Since $\Sigma \trianglelefteq \Gamma$, there exists $\sigma' \in \Sigma$ such that $\gamma\sigma = \sigma'\gamma$, i.e., $\sigma' = \gamma\sigma\gamma^{-1}$. Then

$$(t^\gamma)^\sigma = t^{\gamma\sigma} = t^{\sigma'\gamma} = (t^{\sigma'})^\gamma = t^\gamma,$$

where $t^{\sigma'} = t$ because $t \in \mathcal{T}$ is fixed by every element of $\Sigma$. Thus $t^\gamma \in \mathcal{T}$ and $\mathcal{T}$ is $\Gamma$-invariant.
