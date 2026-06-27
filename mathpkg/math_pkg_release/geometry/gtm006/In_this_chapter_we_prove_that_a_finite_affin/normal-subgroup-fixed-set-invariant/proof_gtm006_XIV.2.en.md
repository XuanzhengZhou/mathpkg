---
role: proof
locale: en
of_concept: normal-subgroup-fixed-set-invariant
source_book: gtm006
source_chapter: "XIV"
source_section: "2"
---

Let $t \in \mathcal{T}$ and $\gamma \in \Gamma$. For any $\sigma \in \Sigma$, we have:
$$(t^\gamma)^\sigma = t^{\gamma\sigma}.$$
Since $\Sigma \trianglelefteq \Gamma$, there exists $\sigma' \in \Sigma$ such that $\gamma\sigma = \sigma'\gamma$. Hence
$$t^{\gamma\sigma} = t^{\sigma'\gamma} = (t^{\sigma'})^\gamma.$$
Since $t \in \mathcal{T}$ is fixed by every element of $\Sigma$, $t^{\sigma'} = t$. Therefore $(t^{\sigma'})^\gamma = t^\gamma$. Thus $(t^\gamma)^\sigma = t^\gamma$ for all $\sigma \in \Sigma$, which means $t^\gamma \in \mathcal{T}$. Since $\gamma \in \Gamma$ was arbitrary, $\Gamma$ leaves $\mathcal{T}$ invariant.
