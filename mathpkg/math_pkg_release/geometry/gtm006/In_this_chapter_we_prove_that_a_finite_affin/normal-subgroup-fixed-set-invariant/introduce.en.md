---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Result 14.5 is an elementary but frequently used fact in permutation group theory: the set of points fixed by a normal subgroup is invariant under the action of the whole group. That is, if $\Sigma \trianglelefteq \Gamma$, then any element of $\Gamma$ maps a point fixed by $\Sigma$ to another point fixed by $\Sigma$. This follows directly from the normality condition: for $\sigma \in \Sigma$, $\gamma \in \Gamma$, and $t \in \mathcal{T}$ (so $t^\sigma = t$), we have $(t^\gamma)^\sigma = t^{\gamma\sigma} = t^{\sigma'\gamma} = t^\gamma$, showing $t^\gamma$ is also fixed by $\Sigma$. This result is used repeatedly throughout the proof of Wagner's Theorem.
