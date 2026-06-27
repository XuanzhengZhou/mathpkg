---
role: proof
locale: en
of_concept: pseudonorm-characterization-of-weak-continuity
source_book: gtm055
source_chapter: "15"
source_section: "1"
---

The verification that $\sigma_f$ is a pseudonorm is routine (cf. Example 11M). Suppose that $f$ is continuous with respect to $\mathcal{T}$. Then for any $x_0 \in \mathcal{E}$ and $\varepsilon > 0$, there exists a neighborhood $V$ of $x_0$ with respect to $\mathcal{T}$ such that $x \in V$ implies $|f(x) - f(x_0)| < \varepsilon$. But then
$$|\sigma_f(x) - \sigma_f(x_0)| = ||f(x)| - |f(x_0)|| \leq |f(x) - f(x_0)| < \varepsilon,$$
so $\sigma_f$ is also continuous with respect to $\mathcal{T}$ (this part does not require $\mathcal{T}$ to be linear). Conversely, suppose $\sigma_f$ is continuous with respect to $\mathcal{T}$. Then for $\varepsilon > 0$ there exists a neighborhood $V$ of $0$ such that $|\sigma_f(x) - \sigma_f(0)| = |f(x)| < \varepsilon$ for $x \in V$. Thus $f$ is continuous at $0$, and since $\mathcal{T}$ is a linear topology, $f$ is continuous on $\mathcal{E}$ (Prob. 12U). Hence the weak topology on $\mathcal{E}$ coincides with the supremum of the linear topologies induced by the pseudonorms $\sigma_f$, i.e., with the topology induced by $\{\sigma_f\}_{f \in \mathcal{E}^*}$.
