---
role: proof
locale: en
of_concept: existence-of-base-theorem
source_book: gtm009
source_chapter: "10"
source_section: "10.1"
---
The proof will in fact yield a concrete method for constructing all possible bases. For each vector $\gamma \in E$, define $\Phi^+(\gamma) = \{ \alpha \in \Phi \mid (\gamma, \alpha) > 0 \}$ = the set of roots lying on the "positive" side of the hyperplane orthogonal to $\gamma$. Call $\gamma \in E$ regular if $\gamma \in E - \bigcup_{\alpha \in \Phi} P_\alpha$.

Call $\alpha \in \Phi^+(\gamma)$ decomposable if $\alpha = \beta_1 + \beta_2$ for some $\beta_i \in \Phi^+(\gamma)$, indecomposable otherwise. Then Theorem 10.1 follows from Theorem 10.1: Let $\gamma \in E$ be regular. Then the set $\Delta(\gamma)$ of all indecomposable roots in $\Phi^+(\gamma)$ is a base of $\Phi$, and every base is obtainable in this manner. The proof proceeds in several steps:

(1) Each root in $\Phi^+(\gamma)$ is a nonnegative $\mathbb{Z}$-linear combination of $\Delta(\gamma)$.
(2) $(\alpha, \beta) \leq 0$ for all $\alpha \neq \beta \in \Delta(\gamma)$.
(3) $\Delta(\gamma)$ is linearly independent.
(4) $\Delta(\gamma)$ is a base.
(5) Every base arises this way: given a base $\Delta$, pick $\gamma$ with $(\gamma, \alpha) > 0$ for all $\alpha \in \Delta$, then $\Delta = \Delta(\gamma)$.