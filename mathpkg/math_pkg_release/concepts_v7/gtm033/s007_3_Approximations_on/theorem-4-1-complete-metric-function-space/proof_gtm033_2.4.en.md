---
role: proof
locale: en
of_concept: theorem-4-1-complete-metric-function-space
source_book: gtm033
source_chapter: "2"
source_section: "4. Weak and Strong Topologies on Function Spaces"
---

# Proof of Theorem 4.1: Complete Metric on Weak Function Space

**Theorem 4.1.** Let each component of $X$ be locally compact with a countable base; let $Y$ be a complete metric space. Then $C_W(X, Y)$ has a complete metric.

*Proof.* It suffices to construct a complete metric on $C_W(X, Y)$ for each component $X_\alpha$ of $X$; therefore we assume $X$ is locally compact with a countable base. Then $X$ has a countable covering by compact sets $\{X_n\}$. Each space $C_W(X_n, Y)$ has a complete metric.

Define a map

$$\rho: C_W(X, Y) \rightarrow \prod_n C_W(X_n, Y),$$

$$\rho_n(f) = f|X_n.$$

Then $\rho$ is a homeomorphism onto a closed subspace. Since the product of a countable number of complete metric spaces has a complete metric, $C_W(X, Y)$ is homeomorphic to a closed subspace of a complete metric space and thus has a complete metric.

QED
