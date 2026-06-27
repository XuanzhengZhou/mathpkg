---
role: proof
locale: en
of_concept: norm-and-trace-in-tower-extension
source_book: gtm028
source_chapter: "I"
source_section: "10"
---
Fix a basis $\{\omega_1, \dots, \omega_n\}$ of $K/k$ and a basis $\{\xi_1, \dots, \xi_m\}$ of $\Delta/K$. Then the $mn$ products $\omega_i \xi_j$ form a basis of $\Delta/k$.

Let $x \in K$ and let $x\Omega = A\Omega$ with respect to the basis $\Omega$ of $K/k$. With respect to the product basis $\{\omega_i\xi_j\}$ of $\Delta/k$, the matrix representing multiplication by $x$ is block-diagonal with $m$ copies of $A$ along the diagonal. Hence its determinant is $(\det A)^m = [N_{K/k}(x)]^m$ and its trace is $m \cdot \operatorname{tr}(A) = m \cdot T_{K/k}(x)$. This establishes the two formulas.
