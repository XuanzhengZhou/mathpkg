---
role: proof
locale: en
of_concept: ordinals-belong-to-von-neumann-universe
source_book: gtm053
source_chapter: ""
source_section: "Each of the sets V_α is transitive"
---

The proof follows by transfinite induction on the ordinals. For the base case, $0 = \varnothing \in V_1 = \mathcal{P}(\varnothing)$. Assuming $\alpha \in V$, we show $\alpha+1 \in V$. If $\alpha \in V_{\beta}$ for some $\beta$, then $\alpha \subset V_{\beta}$ by transitivity of $V_{\beta}$, so $\alpha+1 = \alpha \cup \{\alpha\} \subset V_{\beta} \cup \{V_{\beta}\} \subset V_{\beta+1}$, hence $\alpha+1 \in V_{\beta+2}$. For a limit ordinal $\lambda$, if each $\alpha < \lambda$ belongs to some $V_{\beta_\alpha}$, then $\lambda = \bigcup_{\alpha<\lambda} \alpha \subset V_{\sup \beta_\alpha}$, so $\lambda \in V$.
