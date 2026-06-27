---
role: proof
locale: en
of_concept: projective-limit-intersection-closed
source_book: gtm003
source_chapter: "II"
source_section: "5"
---

By definition, the projective limit $E = \varprojlim g_{\alpha\beta} E_\beta$ consists of all threads $x = (x_\alpha)_{\alpha \in \mathbf{A}} \in F$ satisfying $x_\alpha = g_{\alpha\beta}(x_\beta)$ whenever $\alpha \leq \beta$. This condition is equivalent to $p_\alpha(x) - g_{\alpha\beta}(p_\beta(x)) = 0$, i.e., $x \in V_{\alpha\beta}$. Thus $E = \bigcap_{\alpha \leq \beta} V_{\alpha\beta}$ as sets. Each map $p_\alpha - g_{\alpha\beta} \circ p_\beta$ is a continuous linear map from $F$ into the Hausdorff space $E_\alpha$, so its null space $V_{\alpha\beta}$ is closed. An arbitrary intersection of closed sets is closed, so $E$ is closed in $F$.
