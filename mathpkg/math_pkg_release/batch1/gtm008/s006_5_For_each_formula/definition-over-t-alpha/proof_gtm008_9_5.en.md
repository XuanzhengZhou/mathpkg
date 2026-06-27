---
role: proof
locale: en
of_concept: definition-over-t-alpha
source_book: gtm008
source_chapter: "9"
source_section: "5"
---

The proof follows from the construction of $T_{\alpha+1}$. Any $t \in T_{\alpha+1}$ is either a constant $\underline{k}$ with $\rho(k) \leq \alpha+1$, or of the form $\hat{x}^{\beta}\varphi(x^{\beta})$ for some $\beta \leq \alpha+1$.

For constants $\underline{k}$ with $\rho(k) \leq \alpha+1$, the earlier analysis (following Theorem 9.30) shows that $\underline{k}$ is defined over $T_{\rho(k)}$, and in particular, if $\rho(k) \leq \alpha$, then $\underline{k}$ is defined over $T_{\alpha}$.

For terms of the form $\hat{x}^{\beta}\varphi(x^{\beta})$ with $\beta \leq \alpha$, they are defined over $T_{\beta}$ by construction. Since $T_{\beta} \subseteq T_{\alpha}$ for $\beta \leq \alpha$, these terms are also defined over $T_{\alpha}$.

The only remaining case is a term $\hat{x}^{\alpha+1}\varphi(x^{\alpha+1})$, which is defined over $T_{\alpha}$ by the definition of the term-forming operation $\hat{x}^{\beta}$.
