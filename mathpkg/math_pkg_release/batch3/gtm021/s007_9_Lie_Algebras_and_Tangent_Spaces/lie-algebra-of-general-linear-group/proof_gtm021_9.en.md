---
role: proof
locale: en
of_concept: lie-algebra-of-general-linear-group
source_book: gtm021
source_chapter: "9"
source_section: "Lie Algebras and Tangent Spaces"
---
Since $\mathrm{GL}(n,K)$ is the principal open set in $\mathbb{A}^{n^2}$ defined by $\det \neq 0$, its tangent space at any point is the full affine $n^2$-space. At the identity $e$, the canonical basis consists of the partial differentiation operators $\partial/\partial T_{ij}|_e$. Via the isomorphism $\theta$ of Theorem 9.1, these tangent vectors correspond to left invariant derivations.

Using the coordinate functions $T_{ij}$ on $\mathrm{GL}(n,K)$, one computes the convolution product. For tangent vectors corresponding to matrices $X = (x_{ij})$ and $Y = (y_{ij})$,
\begin{align*}
[X, Y](T_{ij}) &= (T_{ij} * Y * X)(e) - (T_{ij} * X * Y)(e) \\
&= \sum_k (x_{ik} y_{kj} - y_{ik} x_{kj}),
\end{align*}
which is precisely the $(i,j)$ entry of the matrix commutator $XY - YX$. Thus the Lie bracket on $\mathfrak{g}$ coincides with the matrix commutator.
