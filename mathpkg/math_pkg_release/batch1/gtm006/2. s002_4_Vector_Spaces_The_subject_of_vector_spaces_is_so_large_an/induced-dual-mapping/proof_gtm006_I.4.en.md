---
role: proof
locale: en
of_concept: induced-dual-mapping
source_book: gtm006
source_chapter: "I"
source_section: "4. Vector Spaces"
---

Fix a basis $e_1, \dots, e_n$ of $V$. Represent $\alpha \in \Gamma L(V)$ by the matrix $A$ and automorphism $\sigma$. For $v = (x_1, \dots, x_n)$, we have $v^\alpha = (x_1^\sigma, \dots, x_n^\sigma) A$.

**Part (i)**: $\alpha'$ is semi-linear with automorphism $\sigma$. For $w' = (y_1, \dots, y_n)^\top$ and $k \in K$,
$$(k w')^{\alpha'} = (k y_1, \dots, k y_n)^{\alpha'} = A^{-1} ((k y_1)^\sigma, \dots, (k y_n)^\sigma)^\top = A^{-1} (k^\sigma y_1^\sigma, \dots, k^\sigma y_n^\sigma)^\top = k^\sigma A^{-1} (y_1^\sigma, \dots, y_n^\sigma)^\top = k^\sigma (w')^{\alpha'}.$$
Additivity is clear. Non-singularity follows since $A^{-1}$ is invertible and $\sigma$ is a field automorphism.

**Part (ii)**: The pairing. Compute
$$v^\alpha \cdot (w')^{\alpha'} = \big((x_1^\sigma, \dots, x_n^\sigma) A\big) \cdot \big(A^{-1} (y_1^\sigma, \dots, y_n^\sigma)^\top\big) = (x_1^\sigma, \dots, x_n^\sigma) \cdot (y_1^\sigma, \dots, y_n^\sigma)^\top$$
$$= \sum_{i=1}^n x_i^\sigma y_i^\sigma = \left(\sum_{i=1}^n x_i y_i\right)^\sigma = (v \cdot w')^\sigma.$$

**Part (iii)**: The map $\Phi: \Gamma L(V) \to \Gamma L(V')$ given by $\Phi(\alpha) = \alpha'$ is a homomorphism. If $\alpha$ has matrix $A$ and automorphism $\sigma$, and $\beta$ has matrix $B$ and automorphism $\tau$, then $\alpha \beta$ has automorphism $\sigma \tau$ and matrix computed as: if $v^{\alpha\beta} = (v^\alpha)^\beta = ((x_1^\sigma, \dots, x_n^\sigma) A)^\beta$. Representing appropriately, the matrix is $A^{\tau} B$ where $A^\tau$ means applying $\tau$ to each entry. The dual $(\alpha \beta)'$ then uses matrix $(A^\tau B)^{-1} = B^{-1} (A^\tau)^{-1}$ and automorphism $\sigma \tau$, which equals $\beta' \alpha'$. So $\Phi(\alpha \beta) = \Phi(\beta) \Phi(\alpha)$, making $\Phi$ an anti-isomorphism. Composing with inversion yields an isomorphism (or one checks directly that the map is an isomorphism since the construction is involutive: $(\alpha')' = \alpha$ because $((w')^{\alpha'})^{\alpha''}$ corresponds to $(A^{-1})^{-1} = A$ with the same automorphism $\sigma$).

Injectivity: if $\alpha' = \operatorname{id}_{V'}$, then applying $(\cdot)'$ again gives $\alpha = \operatorname{id}_V$. Surjectivity: any $\psi \in \Gamma L(V')$ equals $(\psi')'$, so $\psi = \alpha'$ for $\alpha = \psi' \in \Gamma L(V)$.

**Part (iv)**: If $\alpha \in GL(V)$, then $\sigma = \operatorname{id}$, so $\alpha'$ has automorphism $\operatorname{id}$ and is linear, i.e., $\alpha' \in GL(V')$. Conversely, $\alpha' \in GL(V')$ implies $\sigma = \operatorname{id}$, so $\alpha \in GL(V)$. Thus the isomorphism restricts to $GL(V) \cong GL(V')$.
