---
role: proof
locale: en
of_concept: adjoint-representation-is-morphism
source_book: gtm021
source_chapter: "10"
source_section: "Differentials of Morphisms"
---
By Lemma B, the matrix of $\operatorname{Ad} x$ has entries that are polynomials in the entries of $x$ and $x^{-1}$. Specifically, the coefficient mapping the basis element $e_{kl}$ to $e_{ij}$ is $x_{ik} (x^{-1})_{lj}$.

Since $(x^{-1})_{lj} = (\operatorname{adj}(x))_{lj} / \det x$, where $\operatorname{adj}(x)$ is the adjugate matrix (with polynomial entries), the entries of $\operatorname{Ad} x$ are rational functions with denominator $\det x$. As $\det x$ never vanishes on $\mathrm{GL}(n,K)$, these are regular functions, and $\operatorname{Ad}$ is a morphism of affine varieties $\mathrm{GL}(n,K) \to \operatorname{GL}(n^2, K)$. Since $\operatorname{Ad}$ is also a group homomorphism, it is a morphism of algebraic groups.
