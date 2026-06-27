---
role: proof
locale: en
of_concept: convex-hull-finite-set-compact
source_book: gtm015
source_chapter: "35"
source_section: "Compact convex sets in a TVS"
---

# Proof of Convex hull of a finite set is compact

Let $E$ be a topological vector space over $\mathbb{K}$ and let $x_1, \ldots, x_n \in E$. Define the standard $(n-1)$-simplex

$$\Delta_{n-1} = \left\{ (\lambda_1, \ldots, \lambda_n) \in \mathbb{R}^n : \lambda_i \geq 0,\; \sum_{i=1}^n \lambda_i = 1 \right\}.$$

The simplex $\Delta_{n-1}$ is a closed bounded subset of $\mathbb{R}^n$, hence compact. Define the mapping $\varphi : \Delta_{n-1} \to E$ by

$$\varphi(\lambda_1, \ldots, \lambda_n) = \sum_{i=1}^n \lambda_i x_i.$$

Since addition and scalar multiplication are continuous operations in a TVS (1.3), the map $(\lambda_1, \ldots, \lambda_n) \mapsto \sum_i \lambda_i x_i$ is continuous. By definition,

$$\operatorname{conv}\{x_1, \ldots, x_n\} = \varphi(\Delta_{n-1}),$$

i.e., the convex hull is precisely the image of the compact simplex under the continuous map $\varphi$. The continuous image of a compact set is compact; therefore $\operatorname{conv}\{x_1, \ldots, x_n\}$ is compact.

This lemma is used in the proof of Theorem (35.1): in the argument, the set $A = \operatorname{conv}\{s_1, \ldots, s_n\}$ is compact precisely by this result.
