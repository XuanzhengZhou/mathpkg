---
role: proof
locale: en
of_concept: invariance-of-elementary-ideals
source_book: gtm057
source_chapter: "VII"
source_section: "4"
---

**Proof.** As a result of the Tietze theorem, the proof immediately reduces to checking only Tietze equivalences I and II (and their inverses). 

**Tietze I.** $(\mathbf{x} : \mathbf{r}) \xrightarrow{\mathrm{I}} (\mathbf{x} : \mathbf{r} \cup s)$, where $s$ is a consequence of $\mathbf{r}$. Since $s = \prod_{k=1}^{p} u_k r_{i_k}^{\alpha_k} u_k^{-1}$, the derivative satisfies

$$\frac{\partial s}{\partial x_j} = \sum_{k=1}^{p} \left( \prod_{l=1}^{k-1} u_l r_{i_l}^{\alpha_l} u_l^{-1} \right) \cdot \frac{\partial}{\partial x_j}(u_k r_{i_k}^{\alpha_k} u_k^{-1}).$$

Since $\gamma(r_i) = 1$, the products before the $k$th factor vanish under $\gamma$, and $\gamma(\partial s/\partial x_j)$ is a linear combination of $\gamma(\partial r_{i_k}/\partial x_j)$. Hence the new row is a linear combination of existing rows, and the Alexander matrices are equivalent under operations (ii) and (iii). Thus the elementary ideals $E_k$ are unchanged.

**Tietze II.** $(\mathbf{x} : \mathbf{r}) \xrightarrow{\mathrm{II}} (\mathbf{x} \cup y : \mathbf{r} \cup y\xi^{-1})$, where $\xi \in F(\mathbf{x})$. The derivative of $y\xi^{-1}$ with respect to $y$ satisfies $\gamma'(\partial(y\xi^{-1})/\partial y) = \gamma'(1) = 1$. After abelianization this entry becomes 1, so the new Alexander matrix is equivalent, via operations (v) and (iv), to the block matrix with $A$ and an extra row/column containing 1. These matrices are equivalent to $A$, preserving the elementary ideals.

By the Tietze theorem, any two finite presentations of isomorphic groups are related by Tietze equivalences, so the elementary ideals are group invariants.
