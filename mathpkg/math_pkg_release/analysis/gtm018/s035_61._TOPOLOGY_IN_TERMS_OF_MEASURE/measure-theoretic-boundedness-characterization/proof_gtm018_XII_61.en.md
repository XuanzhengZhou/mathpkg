---
role: proof
locale: en
of_concept: measure-theoretic-boundedness-characterization
source_book: gtm018
source_chapter: "XII"
source_section: "61"
---

**Sufficiency.** If $0 \leq \epsilon < 2\mu(E)$, then the set $\{x: \rho(xE, E) \leq \epsilon\}$ is bounded. Let $\delta$ be a positive number such that $4\delta < 2\mu(E) - \epsilon$, and let $C$ be a compact subset of $E$ such that $\mu(E) - \delta < \mu(C)$. It follows that

$$\rho(xC, C) \leq \rho(xC, xE) + \rho(xE, E) + \rho(E, C) < 2\delta + \rho(xE, E)$$

and hence that

$$\{x: \rho(xE, E) \leq \epsilon\} \subset \{x: \rho(xC, C) \leq \epsilon + 2\delta\}.$$

Since $\epsilon + 2\delta < 2\mu(C)$, it follows that

$$\{x: \rho(xE, E) \leq \epsilon\} \subset \{x: \mu(xC \cap C) \neq 0\} \subset CC^{-1}.$$

**Necessity.** Let $C$ be a compact set such that $A \subset C$ and let $D$ be a compact set of positive measure. Suppose that a Baire set $E$ of positive, finite measure is selected so that $E \supset C^{-1}D \cup D$. Since $D \subset E$, and since, for $x$ in $C$, $D \subset xC^{-1}D \subset xE$, it follows that, for $x$ in $C$, $D \subset xE \cap E$. This implies that

$$A \subset C \subset \{x: D \subset xE \cap E\} \subset \{x: \rho(xE, E) \leq \epsilon\},$$

where $\epsilon = 2(\mu(E) - \mu(D))$.
