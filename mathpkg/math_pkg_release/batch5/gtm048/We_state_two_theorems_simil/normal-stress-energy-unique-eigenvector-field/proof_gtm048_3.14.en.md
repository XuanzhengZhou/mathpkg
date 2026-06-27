---
role: proof
locale: en
of_concept: normal-stress-energy-unique-eigenvector-field
source_book: gtm048
source_chapter: "3"
source_section: "3.14"
---

**Proof of Corollary 3.14.2.** First note from Proposition 3.14.1 that the solution $X$ of $(T_j^i - \delta_j^i a)X^j = 0$ is unique up to scalar multiples. For if we assume a second linearly independent solution $Z$, considering $\operatorname{span}\{X, Z\}$ again gives a contradiction.

Now define a (not necessarily $C^\infty$) vector field $X$ on $M$ and a (not necessarily $C^\infty$) function $f$ on $M$ by: $Xx$ is the unique future-pointing unit timelike eigenvector of $T$ at $x$, and $fx$ is the corresponding eigenvalue. It suffices to prove that $X$ and $f$ are $C^\infty$.

Fix $x \in M$ and let $U$ be a coordinate neighborhood around $x$ with coordinate functions $\{x^1, \ldots, x^4\}$. In $U$, let $\hat{T} = T^{ij} \partial_i \otimes \partial_j$, where the $\{T^{ij}\}$ are $C^\infty$ functions. Since $(\hat{T} - f)X = 0$, $\det\{T_j^i - \delta_j^i f\} = 0$ identically in $U$. Since $Xz$ is the unique solution of the homogeneous system of linear equations $(T_j^i z - \delta_j^i fz)(X^j z) = 0$ where $z \in U$ and $i = 1, \ldots, 4$, the matrix $\{T_j^i z - \delta_j^i fz\}$ has rank 3, and hence $fz$ is a simple root of the characteristic equation in $\lambda$: $\det\{T_j^i z - \delta_j^i \lambda\} = 0$. Since the coefficients of this polynomial equation are $C^\infty$ functions of $z$ (because the $\{T^{ij}\}$ are $C^\infty$), the simple root $fz$ varies $C^\infty$ with $z$ by the implicit function theorem. Once $f$ is known to be $C^\infty$, the eigenvector $X$ (obtained by solving the homogeneous system of rank 3 at each point) also varies $C^\infty$.
