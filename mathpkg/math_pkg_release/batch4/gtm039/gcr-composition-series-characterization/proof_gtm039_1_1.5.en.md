---
role: proof
locale: en
of_concept: "gcr-composition-series-characterization"
source_book: gtm039
source_chapter: "1"
source_section: "1.5"
---
Define $J_0 = 0$. For successor ordinals, let $J_{\alpha+1}$ be the preimage in $A$ of $\text{CCR}(A/J_\alpha)$. For limit ordinals, take the norm closure of the union. By the GCR property, the process terminates at some $\alpha_0$ with $J_{\alpha_0} = A$. Uniqueness follows by transfinite induction: if $\{K_\beta\}$ is another such series, then $J_\alpha = K_\alpha$ for all $\alpha$. Conversely, if a CCR composition series exists, then for any ideal $K \neq A$, the first $\alpha$ with $J_\alpha \not\subseteq K$ yields a nonzero CCR ideal $J_\alpha/(J_\alpha \cap K) \cong (J_\alpha+K)/K$ in $A/K$. $\square$
