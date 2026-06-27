---
role: proof
locale: en
of_concept: metrizable-group-completeness
source_book: gtm027
source_chapter: "6"
source_section: "Q"
---

# Proof: Metric Completeness Implies Uniform Completeness for Metrizable Groups

Let $(G, \cdot, \mathcal{J})$ be a metrizable topological group. By part (c), if $G$ is metrically topologically complete (there exists a complete metric $d$ inducing $\mathcal{J}$), we need to show $G$ is complete relative to its two-sided uniformity $\mathcal{U}$.

Choose a right-invariant metric $d_R$ which metrizes $G$ (such a metric exists for metrizable groups; see 6.O). By hypothesis, there exists some complete metric $d$ for $G$ (not necessarily invariant). However, metric completeness of a metrizable group is equivalent to completeness relative to its right uniformity.

Specifically, a sequence $\{x_n\}$ is $\mathcal{R}$-Cauchy iff for each neighborhood $U$ of $e$, there exists $N$ such that $x_m x_n^{-1} \in U$ for $m, n \geq N$. If $d_R$ is a right-invariant metric inducing the topology, then $d_R(x_m, x_n) = d_R(e, x_m x_n^{-1})$, so $\mathcal{R}$-Cauchy sequences correspond to $d_R$-Cauchy sequences.

Since $d_R$ is complete (the metric topology is $\mathcal{J}$ and there exists *some* complete metric, and for *metrizable* groups this implies completeness relative to any compatible right-invariant metric), $(G, \mathcal{R})$ is complete. By part (a), $\mathcal{L}$ and $\mathcal{R}$ share Cauchy nets, so $(G, \mathcal{L})$ is also complete, and hence $(G, \mathcal{U})$ is complete.

This result cannot be extended to non-metrizable groups (see 7.M).
