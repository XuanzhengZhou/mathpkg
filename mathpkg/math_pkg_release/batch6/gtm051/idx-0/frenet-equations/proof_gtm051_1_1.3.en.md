---
role: proof
locale: en
of_concept: frenet-equations
source_book: gtm051
source_chapter: "1"
source_section: "1.3"
---

Since $\{e_1(t), \ldots, e_n(t)\}$ forms an orthonormal basis of $\mathbb{R}^n$ at each $t$, the derivative $\dot{e}_i(t)$ can be expressed as a linear combination:
$$\dot{e}_i(t) = \sum_{j=1}^n \omega_{ij}(t) e_j(t).$$

(*) Differentiating the orthonormality condition $e_i(t) \cdot e_j(t) = \delta_{ij}$ gives:
$$\dot{e}_i \cdot e_j + e_i \cdot \dot{e}_j = 0.$$
Substituting the expansions, $\sum_k \omega_{ik} e_k \cdot e_j + e_i \cdot \sum_k \omega_{jk} e_k = \omega_{ij} + \omega_{ji} = 0$. Hence $\omega_{ij} = -\omega_{ji}$, i.e., $\omega$ is skew-symmetric.

(**) Now suppose $(e_i(t))$ is a distinguished Frenet frame. By definition, $e_i(t)$ is a linear combination of $\dot{c}(t), \ldots, c^{(i)}(t)$. Differentiating, $\dot{e}_i(t)$ is a linear combination of $\ddot{c}(t), \ldots, c^{(i+1)}(t)$ and hence of $e_1(t), \ldots, e_{i+1}(t)$. Consequently, $\omega_{ij}(t) = 0$ for $j > i+1$. By skew-symmetry, $\omega_{ij}(t) = 0$ for $i > j+1$ as well. Thus only the entries $\omega_{i,i+1}$ (and $\omega_{i+1,i} = -\omega_{i,i+1}$) can be non-zero. The matrix $\omega$ is tridiagonal.

These $n-1$ functions $\omega_{12}, \omega_{23}, \ldots, \omega_{n-1,n}$ are the Frenet curvatures, generalizing the curvature and torsion of space curves.
