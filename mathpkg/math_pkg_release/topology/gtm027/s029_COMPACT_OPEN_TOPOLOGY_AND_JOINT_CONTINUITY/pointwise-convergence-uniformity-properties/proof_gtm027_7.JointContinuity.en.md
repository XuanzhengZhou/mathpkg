---
role: proof
locale: en
of_concept: pointwise-convergence-uniformity-properties
source_book: gtm027
source_chapter: "7"
source_section: "Compact Open Topology and Joint Continuity"
---

# Proof of Theorem 7.3 — Properties of the Uniformity of Pointwise Convergence

The uniformity $\sigma_A$ of pointwise convergence on $A \subset X$ is defined by taking as a subbase the family of all sets of the form

$$\{(f, g) : (f(x), g(x)) \in V\}$$

for $V \in \mathcal{V}$ and $x \in A$. This is precisely the definition of the product uniformity for the product space $Y^A$ restricted to $F$, so properties (a) through (d) follow from the general theory of product uniformities (Theorem 6.4).

**(a)** By definition, the family of all sets $\{(f, g) : (f(x), g(x)) \in V\}$ for $V \in \mathcal{V}$ and $x \in A$ forms a subbase for the $\sigma_A$ uniformity.

**(b)** The topology induced by the product uniformity on $Y^A$ is the product topology, which is precisely the topology of pointwise convergence on $A$. Hence the topology of $\sigma_A$ is the topology of pointwise convergence on $A$.

**(c)** A net $\{f_n, n \in D\}$ is Cauchy relative to the product uniformity if and only if each coordinate net $\{f_n(x), n \in D\}$ is Cauchy in $(Y, \mathcal{V})$. This follows because a net is Cauchy in a product uniformity exactly when each projection is Cauchy.

**(d)** If $(Y, \mathcal{V})$ is complete, then $Y^A$ is complete in the product uniformity. The set of all functions $F$ is a subset of $Y^A$. If the pointwise closure $R[F]$ of $F$ in $Y^A$ is closed, then $F$ is a closed subset of a complete uniform space and is therefore complete relative to the $\sigma_A$ uniformity.
