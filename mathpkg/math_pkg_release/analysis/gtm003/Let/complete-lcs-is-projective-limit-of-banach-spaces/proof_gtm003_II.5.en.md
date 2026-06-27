---
role: proof
locale: en
of_concept: complete-lcs-is-projective-limit-of-banach-spaces
source_book: gtm003
source_chapter: "II"
source_section: "5"
---

Let $E$ be a complete l.c.s. For each continuous semi-norm $p$ on $E$, denote by $E_p$ the Banach space associated with $p$ and by $g_p$ the canonical map $E \to E_p$. Set $F = \prod_p E_p$ and let $g$ be the map $x \mapsto (g_p(x))$ of $E$ into $F$. The map $g$ is an isomorphism (into $F$) for the projective topology on $E$ with respect to the family $\{(E_p, g_p)\}$. For each pair $(\alpha, \beta) \in \mathbf{A} \times \mathbf{A}$ such that $\alpha \leq \beta$, denote by $V_{\alpha\beta}$ the subspace $\{x: x_\alpha - g_{\alpha\beta}(x_\beta) = 0\}$ of $F$. Since $E_\alpha$ is Hausdorff and $V_{\alpha\beta}$ is the null space of the continuous linear map $p_\alpha - g_{\alpha\beta} \circ p_\beta$ of $F$ into $E_\alpha$, $V_{\alpha\beta}$ is closed; thus $E = \bigcap_{\alpha \leq \beta} V_{\alpha\beta}$ is closed in $F$. The completion $\tilde{E}$ is then the projective limit $\varprojlim \tilde{E}_p$ of the Banach spaces $\tilde{E}_p$.
