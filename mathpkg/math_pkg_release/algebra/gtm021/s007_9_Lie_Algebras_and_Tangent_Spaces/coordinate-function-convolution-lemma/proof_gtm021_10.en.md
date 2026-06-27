---
role: proof
locale: en
of_concept: coordinate-function-convolution-lemma
source_book: gtm021
source_chapter: "10"
source_section: "Differentials of Morphisms"
---
First observe that for $y \in \mathrm{GL}(n, K)$,
$$(\rho_x T_{ij})(y) = T_{ij}(yx) = \sum_h y_{ih} x_{hj} = \sum_h T_{ih}(y) x_{hj} = (\mathbf{T}(y) x)_{ij},$$
and similarly for left translation.

Now compute the convolution:
\begin{align*}
(T_{ij} * X)(y) &= X(\lambda_{y^{-1}} T_{ij}) \\
&= X\left(\sum_h y_{ih} T_{hj}\right) \\
&= \sum_h y_{ih} X(T_{hj}) \\
&= \sum_h y_{ih} X_{hj} = \sum_h T_{ih}(y) X_{hj} = (\mathbf{T}(y) X)_{ij}.
\end{align*}

The identity $\lambda_{y^{-1}} T_{ij} = \sum_h y_{ih} T_{hj}$ follows from
$$(\lambda_{y^{-1}} T_{ij})(z) = T_{ij}(y^{-1}z) = \sum_h T_{ih}(y^{-1}) T_{hj}(z),$$
and the identification $T_{ih}(y^{-1}) = y_{ih}$ in the coordinate description of the tangent vector action.
