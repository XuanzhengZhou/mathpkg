---
role: proof
locale: en
of_concept: projective-limit-is-closed-subspace-of-product
source_book: gtm003
source_chapter: "II"
source_section: "5"
---

For each pair $(\alpha, \beta) \in \mathbf{A} \times \mathbf{A}$ with $\alpha \leq \beta$, define
$$V_{\alpha \beta} = \{x = (x_\gamma)_{\gamma \in \mathbf{A}} \in F : x_\alpha - g_{\alpha \beta}(x_\beta) = 0\}.$$
The map $\varphi_{\alpha \beta} = p_\alpha - g_{\alpha \beta} \circ p_\beta: F \to E_\alpha$ is continuous and linear, since $p_\alpha, p_\beta$ are continuous projections and $g_{\alpha \beta}$ is continuous. The set $V_{\alpha \beta} = \varphi_{\alpha \beta}^{-1}(\{0\})$ is the kernel (null space) of this continuous map. Since $E_\alpha$ is Hausdorff, the singleton $\{0\}$ is closed, and therefore $V_{\alpha \beta}$ is closed in $F$.

The projective limit is $E = \bigcap_{\alpha \leq \beta} V_{\alpha \beta}$. As an intersection of closed sets, $E$ is closed in $F$.
