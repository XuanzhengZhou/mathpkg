---
role: proof
locale: en
of_concept: gl-connected-component-positive-determinant
source_book: gtm014
source_chapter: "IV"
source_section: "5"
---

The identity component of $\mathrm{GL}(n,\mathbb{R})$ contains $\mathrm{GL}^+(n,\mathbb{R})$, the set of matrices with positive determinant. To see this, let $A \in \mathrm{GL}^+(n,\mathbb{R})$. By the polar decomposition, $A = UP$ where $U$ is orthogonal and $P$ is positive definite symmetric. Since $\det A > 0$, we have $\det U = 1$, so $U \in \mathrm{SO}(n)$.

The set of positive definite symmetric matrices is convex (hence connected): if $P_1, P_2$ are positive definite, then $tP_1 + (1-t)P_2$ is positive definite for $t \in [0,1]$. Thus $P$ can be connected to $I_n$ by a path $t \mapsto (1-t)I_n + tP$ within positive definite matrices.

For $\mathrm{SO}(n)$, every element can be written as $\exp(S)$ for some skew-symmetric matrix $S$, and $t \mapsto \exp(tS)$ gives a path from $U$ to $I_n$. Thus $A = UP$ is connected to $I_n$ within $\mathrm{GL}^+(n,\mathbb{R})$.

Conversely, the determinant function $\det: \mathrm{GL}(n,\mathbb{R}) \to \mathbb{R} \setminus \{0\}$ is continuous, so its image on a connected component must be connected. Since $\det(I_n) = 1 > 0$, the identity component is contained in $\mathrm{GL}^+(n,\mathbb{R})$.

Therefore the identity component of $\mathrm{GL}(n,\mathbb{R})$ equals $\mathrm{GL}^+(n,\mathbb{R})$.
