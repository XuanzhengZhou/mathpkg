---
role: proof
locale: en
of_concept: g-equivalent-subspaces-and-cogredient-matrices
source_book: gtm031
source_chapter: "Bilinear Forms"
source_section: "6"
---

First, suppose $\mathfrak{S}_1$ and $\mathfrak{S}_2$ are $g$-equivalent. Let $\{e_1, \dots, e_r\}$ be a basis for $\mathfrak{S}_1$ and $\{f_1, \dots, f_r\}$ a basis for $\mathfrak{S}_2$. Let $T : \mathfrak{S}_1 \to \mathfrak{S}_2$ be a $g$-preserving isomorphism. Then $\{e_i T\}$ is also a basis for $\mathfrak{S}_2$, and the matrix of $g$ restricted to $\mathfrak{S}_2$ relative to $\{e_i T\}$ equals the matrix relative to $\{e_i\}$ on $\mathfrak{S}_1$, because $g(e_i T, e_j T) = g(e_i, e_j)$. The change-of-basis from $\{e_i T\}$ to $\{f_i\}$ transforms the matrix by cogredience, so the matrices relative to $\{e_i\}$ and $\{f_i\}$ are cogredient.

Conversely, suppose the matrices of the contractions of $g$ to $\mathfrak{S}_1$ and $\mathfrak{S}_2$ are cogredient. Then there exists a non-singular matrix $(\mu)$ such that if $(\beta)$ is the matrix of $g$ on $\mathfrak{S}_1$ relative to a basis $\{e_i\}$, and $(\gamma)$ is the matrix relative to a basis $\{f_i\}$ of $\mathfrak{S}_2$, then $(\gamma) = (\mu)(\beta)(\bar{\mu})'$. By changing the basis in $\mathfrak{S}_2$ using $(\mu)$, we may assume $(\beta) = (\gamma)$, i.e., $g(e_i, e_j) = g(f_i, f_j)$ for all $i, j$.

Now let $x_1 = \sum \xi_i e_i$, $y_1 = \sum \eta_j e_j$ be arbitrary vectors in $\mathfrak{S}_1$. Then

$$g(x_1, y_1) = \sum_{i,j} \xi_i\, g(e_i, e_j)\, \bar{\eta}_j = \sum_{i,j} \xi_i\, g(f_i, f_j)\, \bar{\eta}_j = g\!\left(\sum \xi_i f_i,\; \sum \eta_j f_j\right).$$

Define the linear map $T : \mathfrak{S}_1 \to \mathfrak{S}_2$ by $e_i \mapsto f_i$ and extending linearly: $\sum \xi_i e_i \mapsto \sum \xi_i f_i$. The computation above shows $g(x_1 T, y_1 T) = g(x_1, y_1)$, so $T$ is a $g$-preserving isomorphism. Hence $\mathfrak{S}_1$ and $\mathfrak{S}_2$ are $g$-equivalent.
