---
role: proof
locale: en
of_concept: banach-space-finite-complex-measures
source_book: gtm036
source_chapter: "4"
source_section: "I (Complex Measures)"
---
The set $M(X, \mathcal{S})$ of all finite complex measures on $(X, \mathcal{S})$ is clearly a complex vector space under pointwise addition and scalar multiplication. The total variation norm $\|\mu\| = |\mu|(X) = \sup_{A \in \mathcal{S}} |\mu|(A)$ satisfies the triangle inequality since $|\mu + \nu|(A) \leq |\mu|(A) + |\nu|(A)$ for all $A \in \mathcal{S}$, giving $\|\mu + \nu\| \leq \|\mu\| + \|\nu\|$. Positive homogeneity follows from $|\alpha \mu| = |\alpha| |\mu|$.

For completeness, let $\{\mu_n\}$ be a Cauchy sequence in $M(X, \mathcal{S})$. For each $A \in \mathcal{S}$, the sequence $\{\mu_n(A)\}$ is Cauchy in $\mathbb{C}$, hence convergent; define $\mu(A) = \lim_n \mu_n(A)$. The limit $\mu$ is a finitely additive set function, and using the Nikodym convergence theorem (or standard measure-theoretic arguments) one verifies that $\mu$ is countably additive and finite, hence a complex measure. The convergence $\|\mu_n - \mu\| \to 0$ follows from the uniform bound on total variations given by the Cauchy condition.
