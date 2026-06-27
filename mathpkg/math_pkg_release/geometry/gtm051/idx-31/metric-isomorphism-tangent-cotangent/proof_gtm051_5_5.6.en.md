---
role: proof
locale: en
of_concept: metric-isomorphism-tangent-cotangent
source_book: gtm051
source_chapter: "5"
source_section: "5.6"
---

For each $p \in M$, the map $Lg_p: X \mapsto g_p(X, \cdot)$ is linear by bilinearity of $g$. Since $g_p$ is positive definite, $Lg_p(X) = 0$ implies $g_p(X, X) = 0$, hence $X = 0$; thus $Lg_p$ is injective. As $\dim T_pM = \dim T_p^*M = 2$, injectivity implies surjectivity. Hence $Lg_p$ is an isomorphism.

In coordinates, $g_p$ is represented by the matrix $(g_{ij}(u))$ with respect to the basis $\{e_i = \partial/\partial u^i\}$. The dual basis is $\{du^j\}$ with $du^j(e_i) = \delta_i^j$. Then $Lg_p(e_i) = g_p(e_i, \cdot) = \sum_j g_{ij}(u) du^j$, since $g_p(e_i, e_k) = g_{ik}$ and the 1-form sending $e_k \mapsto g_{ik}$ is precisely $\sum_j g_{ij} du^j$. For a general vector $X = \sum_i \xi^i e_i$, we have $Lg_p(X) = \sum_i \xi^i Lg_p(e_i) = \sum_{i,j} g_{ij} \xi^i du^j$.
