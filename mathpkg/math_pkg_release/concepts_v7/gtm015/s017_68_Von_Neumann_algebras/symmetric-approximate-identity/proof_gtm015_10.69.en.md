---
role: proof
locale: en
of_concept: symmetric-approximate-identity
source_book: gtm015
source_chapter: "10"
source_section: "69"
---

# Proof of Symmetric approximate identity approximation in L^1(G)

Proof. As noted in the proof of (69.13), $f * g \in \mathcal{L}^1(G)$ for every $g \in \mathcal{F}$. Applying (69.13) to $f$ and to $\tilde{f}$, we may choose a neighborhood $V$ of $e$ such that

$$\| f * g - f \|_1 \leq \varepsilon \quad \text{and} \quad \| \tilde{f} * g - \tilde{f} \|_1 \leq \varepsilon$$

whenever $g \in \mathcal{F}_V$. We can suppose that $V$ is compact and symmetric; then $g \in \mathcal{F}_V$ implies $\tilde{g} \in \mathcal{F}_V$. {The point is that $\tilde{g}(t) = \Delta(t)g(t^{-1})$ is essentially bounded because $\Delta$ is continuous and $g$ vanishes outside the compact set $V^{-1} = V$.} Thus if $g \in \mathcal{F}_V$ we may replace $g$ by $\tilde{g}$ in the second inequality of (*); the proof is concluded by the observation that $\tilde{f} * \tilde{g} = (g * f)^{\sim}$, hence $\|g * f - f\|_1 = \|(g * f)^{\sim} - \tilde{f}\|_1 = \|\tilde{f} * \tilde{g} - \tilde{f}\|_1 \leq \varepsilon$.
