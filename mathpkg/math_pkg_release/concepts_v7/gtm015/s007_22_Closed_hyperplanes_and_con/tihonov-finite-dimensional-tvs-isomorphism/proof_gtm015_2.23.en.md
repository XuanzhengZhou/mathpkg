---
role: proof
locale: en
of_concept: tihonov-finite-dimensional-tvs-isomorphism
source_book: gtm015
source_chapter: "2"
source_section: "23"
---

# Proof of Tihonov theorem: finite-dimensional separated TVS is isomorphic to Euclidean space

The proof is by induction on $r$, the case $r = 1$ being covered by (22.1). Assume inductively that the theorem holds for $r - 1$.

Let $e_1, \ldots, e_r$ be the canonical basis of $\mathbb{K}^r$, that is, $e_k = (\delta_{jk})_{1 \le j \le r}$. Define $x_k = u(e_k)$ ($k = 1, \ldots, r$); then $x_1, \ldots, x_r$ is a basis of $E$, and, for any $(\lambda_k)$ in $\mathbb{K}^r$,

$$u((\lambda_k)) = u\left(\sum_1^r \lambda_k e_k\right) = \sum_1^r \lambda_k u(e_k) = \sum_1^r \lambda_k x_k.$$

Let $M$ be the linear subspace of $E$ spanned by $x_1, \ldots, x_{r-1}$; with the relative topology, $M$ is also a separated TVS. By induction, the vector space isomorphism $\mathbb{K}^{r-1} \rightarrow M$ defined by

$$(\lambda_1, \ldots, \lambda_{r-1}) \mapsto \sum_1^{r-1} \lambda_k x_k$$

is bicontinuous. Since $\mathbb{K}^{r-1}$ is a complete TVS (7.8), its isomorph $M$ is also complete (5.12); since $E$ is separated, it follows that $M$ is closed in $E$. Thus, $M$ is a closed, maximal linear subspace of $E$. Let $N = \mathbb{K}x_r$ be the one-dimensional subspace spanned by $x_r$; then $E$ is the topological direct sum of $M$ and $N$ (22.3), that is, the mapping $(y, z) \mapsto y + z$ is a bicontinuous isomorphism of the product TVS $M \times N$ onto $E$. Since $M \cong \mathbb{K}^{r-1}$ (by induction) and $N \cong \mathbb{K}$ (trivially), we have $E \cong \mathbb{K}^r$.
