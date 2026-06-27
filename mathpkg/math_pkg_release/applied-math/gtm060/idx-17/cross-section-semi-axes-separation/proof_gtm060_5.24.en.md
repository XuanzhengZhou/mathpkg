---
role: proof
locale: en
of_concept: cross-section-semi-axes-separation
source_book: gtm060
source_chapter: "5"
source_section: "24"
---

The inequality $a'_k \leq a_k$ follows from Theorem 5, since in the calculation of $a_k$ the maximum is taken over a larger set (all $k$-dimensional subspaces of $\mathbb{R}^n$, while $a'_k$ is the maximum only over $k$-dimensional subspaces contained in $\mathbb{R}^{n-1}$).

To prove the inequality $a'_k \geq a_{k+1}$, intersect $\mathbb{R}^{n-1}$ with any $(k+1)$-dimensional subspace $\mathbb{R}^{k+1} \subset \mathbb{R}^n$. The intersection has dimension at least $k$. The smallest semi-axis of the ellipsoid $E' \cap \mathbb{R}^{k+1}$ is greater than or equal to the smallest semi-axis of $E \cap \mathbb{R}^{k+1}$. By Theorem 5,

$$a'_k = \max_{\{\mathbb{R}^k \subset \mathbb{R}^{n-1}\}} \min_{\mathbf{x} \in \mathbb{R}^k \cap E'} \|\mathbf{x}\| \geq \max_{\{\mathbb{R}^{k+1} \subset \mathbb{R}^{n}\}} \min_{\mathbf{x} \in \mathbb{R}^{k+1} \cap E'} \|\mathbf{x}\| = a_{k+1}.$$

Thus $a_1 \geq a'_1 \geq a_2 \geq a'_2 \geq \cdots \geq a_{n-1} \geq a'_{n-1} \geq a_n$. $\square$
