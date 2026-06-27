---
role: proof
locale: en
of_concept: transitivity-of-von-neumann-hierarchy
source_book: gtm053
source_chapter: ""
source_section: "Each of the sets V_α is transitive"
---

Suppose that this were not true. Then there would exist a least ordinal $\alpha$ with $V_{\alpha} \not\subset V_{\alpha+1}$, where $\alpha \geqslant 2$.

**Successor case.** If $\alpha$ is not a limit ordinal, write $\alpha = \beta + 1$. Take $Y \in X \in V_{\alpha}$ with $Y \notin V_{\alpha}$. Then:
$$X \in V_{\beta+1} = \mathcal{P}(V_{\beta}) \implies X \subset V_{\beta} \implies Y \in V_{\beta} \implies Y \in V_{\beta+1} = V_{\alpha},$$
since by the minimality of $\alpha$, we have $V_{\beta} \subset V_{\beta+1}$. This contradicts $Y \notin V_{\alpha}$.

**Limit case.** If $\alpha$ is a limit ordinal, the argument is analogous: find $\gamma < \alpha$ with $Y \in X \in V_{\gamma}$ and $Y \notin V_{\alpha}$, and derive a contradiction using the definition $V_{\alpha} = \bigcup_{\beta < \alpha} V_{\beta}$ along with the induction hypothesis that $V_{\gamma} \subset V_{\gamma+1}$ for all $\gamma < \alpha$.
