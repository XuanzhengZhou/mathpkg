---
role: proof
locale: en
of_concept: completion-via-outer-measure
source_book: gtm018
source_chapter: "III. Extension of Measures"
source_section: "§13. Extension, Completion, and Approximation"
---

Denote the $\mu^*$-measurable sets by $\mathbf{S}^*$ and the completion domain by $\bar{\mathbf{S}}$. Since $\mu^*$ on $\mathbf{S}^*$ is a complete measure, $\bar{\mathbf{S}} \subset \mathbf{S}^*$ and $\bar{\mu} = \mu^*$ on $\bar{\mathbf{S}}$. To prove $\mathbf{S}^* \subset \bar{\mathbf{S}}$: by $\sigma$-finiteness of $\mu^*$ on $\mathbf{S}^*$ (12.E), consider $E \in \mathbf{S}^*$ with $\mu^*(E) < \infty$.

By 12.C, $E$ has a measurable cover $F$. Since $\mu^*(F) = \mu(F) = \mu^*(E)$, we have $\mu^*(F - E) = 0$. Let $G$ be a measurable cover of $F - E$; then $\mu(G) = \mu^*(F - E) = 0$. The relation

$$E = (F - G) \cup (E \cap G)$$

exhibits $E$ as a union of a set in $\mathbf{S}(\mathbf{R})$ and a subset of a null set in $\mathbf{S}(\mathbf{R})$, so $E \in \bar{\mathbf{S}}$.
