---
role: proof
locale: en
of_concept: uniform-space-embedding-into-product
source_book: gtm027
source_chapter: "6"
source_section: "Metrization"
---

# Proof of Uniform Space Embedding into a Product of Metric Spaces (Theorem 6.16)

**Theorem 6.16 (Weil).** Each uniform space is uniformly isomorphic to a subspace of the product of pseudo-metric spaces and each uniform Hausdorff space is uniformly isomorphic to a subspace of the product of metric spaces.

**Proof.** Let $(X, \mathcal{U})$ be a uniform space and let $P$ be the gage of $\mathcal{U}$ (the family of all uniformly continuous pseudo-metrics). The uniformity $\mathcal{U}$ is the smallest which makes the identity map of $X$ into the pseudo-metric space $(X,p)$ uniformly continuous for each $p \in P$.

For each $p \in P$, the pseudo-metric space $(X,p)$ is isometric under a map $h_p$ to a metric space $(X_p, p^*)$ obtained by identifying points at pseudo-distance zero (Theorem 4.15). Thus $\mathcal{U}$ is the smallest uniformity making each $h_p$ uniformly continuous.

Define a map $h : X \to \prod_{p \in P} X_p$ by $h(x)_p = h_p(x)$. By Theorem 6.10, $\mathcal{U}$ is the smallest uniformity making $h$ uniformly continuous. This means $h$ is a uniform embedding: $X$ is uniformly isomorphic to $h(X)$ with the relative uniformity from the product.

If $(X, \mathcal{U})$ is Hausdorff, then pseudo-metrics in $P$ separate points, so each $h_p$ is injective on the quotient, and $h$ is injective. Thus $h$ is a uniform isomorphism onto its image, giving an embedding into a product of metric spaces.
