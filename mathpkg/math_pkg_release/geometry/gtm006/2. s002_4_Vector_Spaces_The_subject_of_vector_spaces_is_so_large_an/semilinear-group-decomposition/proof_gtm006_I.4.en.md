---
role: proof
locale: en
of_concept: semilinear-group-decomposition
source_book: gtm006
source_chapter: "I"
source_section: "4. Vector Spaces"
---

Fix a basis $e_1, \dots, e_n$ of $V$ (as a left vector space over $K$). Let $\phi \in \Gamma L(V)$ be a semi-linear transformation with associated automorphism $\sigma \in \operatorname{Aut}(K)$. For each $v = \sum_i x_i e_i$, we have

$$v^\phi = \left(\sum_i x_i e_i\right)^\phi = \sum_i (x_i e_i)^\phi = \sum_i x_i^\sigma e_i^\phi.$$

Write $e_i^\phi = \sum_j a_{ij} e_j$ for some matrix $A = (a_{ij})$ over $K$. Then $v^\phi$ has coordinates $(x_1^\sigma, \dots, x_n^\sigma) A$.

Define the automorphism-collineation $\alpha_\sigma \in \Gamma L(V)$ by $(x_1, \dots, x_n)^{\alpha_\sigma} = (x_1^\sigma, \dots, x_n^\sigma)$ (applying $\sigma$ component-wise). Define the linear transformation $\lambda \in GL(V)$ by $(y_1, \dots, y_n)^\lambda = (y_1, \dots, y_n) A$. Then $\phi = \alpha_\sigma \circ \lambda$.

Let $A = \{\alpha_\sigma \mid \sigma \in \operatorname{Aut}(K)\}$. The map $\sigma \mapsto \alpha_\sigma$ is an injective homomorphism $\operatorname{Aut}(K) \to \Gamma L(V)$, so $A \cong \operatorname{Aut}(K)$. Clearly $A \cap GL(V) = \{1\}$ since the only automorphism-collineation that is linear is the identity (only $\sigma = \operatorname{id}$ yields linearity). For normality: if $\lambda \in GL(V)$ has matrix $B$, then $\alpha_\sigma^{-1} \lambda \alpha_\sigma$ has matrix obtained by applying $\sigma^{-1}$ to the entries of $B$, which is again an invertible matrix, hence lies in $GL(V)$. Thus $GL(V) \trianglelefteq \Gamma L(V)$. Since every $\phi \in \Gamma L(V)$ can be written uniquely as $\alpha_\sigma \lambda$ with $\alpha_\sigma \in A$ and $\lambda \in GL(V)$, we obtain $\Gamma L(V) = A \cdot GL(V)$ with the stated properties.
