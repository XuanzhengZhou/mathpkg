---
role: proof
locale: en
of_concept: extremal-property-of-eigenvalues
source_book: gtm060
source_chapter: "5"
source_section: "24"
---

Consider the subspace $\mathbb{R}^{n-k+1}$ spanned by the axes $a_k \geq a_{k+1} \geq \cdots \geq a_n$. The intersection of any $k$-dimensional subspace $\mathbb{R}^k$ with $\mathbb{R}^{n-k+1}$ contains a non-zero vector $\mathbf{x}$ (since $\dim \mathbb{R}^k + \dim \mathbb{R}^{n-k+1} = k + (n-k+1) = n+1 > n$). Since $\|\mathbf{x}\|$ in the ellipsoid $E$ is at most the length $\ell$ of the smallest semi-axis of $E \cap \mathbb{R}^k$, and since $\mathbf{x}$ belongs to the subspace spanned by the $n-k+1$ smallest axes, its norm satisfies $\|\mathbf{x}\| \leq a_k$. Therefore $\ell \leq a_k$. The maximum is attained when $\mathbb{R}^k$ is the subspace spanned by the $k$ largest semi-axes $a_1 \geq a_2 \geq \cdots \geq a_k$, for which the minimum norm on the intersection is exactly $a_k$. $\square$
