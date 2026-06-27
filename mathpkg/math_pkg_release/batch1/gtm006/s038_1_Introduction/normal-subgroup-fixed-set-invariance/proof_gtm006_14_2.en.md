---
role: proof
locale: en
of_concept: normal-subgroup-fixed-set-invariance
source_book: gtm006
source_chapter: "XIV"
source_section: "2"
---
**Proof of Result 14.5.** Let $\mathcal{T}$ be the set of points in $\mathcal{S}$ fixed by $\Sigma$. Take any $x \in \mathcal{T}$ and any $\gamma \in \Gamma$. We need to show that $\gamma(x) \in \mathcal{T}$, i.e., $\gamma(x)$ is also fixed by every $\sigma \in \Sigma$.

For any $\sigma \in \Sigma$, since $\Sigma \trianglelefteq \Gamma$, there exists $\sigma' \in \Sigma$ such that $\sigma\gamma = \gamma\sigma'$. Then:

$$\sigma(\gamma(x)) = (\sigma\gamma)(x) = (\gamma\sigma')(x) = \gamma(\sigma'(x)) = \gamma(x),$$

where the last equality uses that $x \in \mathcal{T}$ (so $\sigma'(x) = x$). Thus $\gamma(x)$ is fixed by $\sigma$ for all $\sigma \in \Sigma$, proving $\gamma(x) \in \mathcal{T}$. Hence $\Gamma$ leaves $\mathcal{T}$ invariant. $\square$
