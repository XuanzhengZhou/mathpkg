---
role: proof
locale: en
of_concept: lemma-15-1
source_book: gtm055
source_chapter: "15"
source_section: "Section 16_Section_16"
---

Proof. The verification that $\sigma_f$ is a pseudonorm is routine and is left to the reader (cf. Example 11M). Suppose that $f$ is continuous

there exists a neighborhood $V$ of $x_0$ with respect to $\mathcal{T}$ such that $x \in V$ implies $|f(x) - f(x_0)| < \varepsilon$. But then

$$|\sigma_f(x) - \sigma_f(x_0)| = ||f(x)| - |f(x_0)|| \leq |f(x) - f(x_0)| < \varepsilon,$$

and it follows that $\sigma_f$ is also continuous with respect to $\mathcal{T}$. (Observe that this part of the argument does not even require that the topology $\mathcal{T}$ be linear.)

Suppose next that $\sigma_f$ is continuous with respect to a topology $\mathcal{T}$ on $\mathcal{E}$. Then for any given $\varepsilon > 0$ there exists a neighborhood $V$ of the origin in $\mathcal{E}$ with respect to $\mathcal{T}$ such that $|\sigma_f(x) - \sigma_f(0)| = |f(x)| < \varepsilon$ for every $x$ in $V$. Thus $f$ is continuous at the origin, and if $\mathcal{T}$ is a linear topology on $\mathcal{E}$, this implies that $f$ is continuous on $\mathcal{E}$ with respect to $\mathcal{T}$ (Prob. 12U). Hence the weak topology on $\mathcal{E}$ coincides with the supremum of the linear topologies induced by the various pseudonorms $\sigma_f, f \in \mathcal{E}^*$, or, in other words, with the topology induced by the family $\{\sigma_f\}_{f \in \mathcal{E}^*}$ (Ch. 11, p. 234).
