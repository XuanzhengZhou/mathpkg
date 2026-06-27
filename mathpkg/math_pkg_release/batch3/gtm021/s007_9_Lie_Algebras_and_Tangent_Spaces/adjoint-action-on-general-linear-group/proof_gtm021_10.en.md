---
role: proof
locale: en
of_concept: adjoint-action-on-general-linear-group
source_book: gtm021
source_chapter: "10"
source_section: "Differentials of Morphisms"
---
It suffices to check that both sides have the same effect on each coordinate function $T_{ij}$. Using Lemma A repeatedly:
\begin{align*}
\operatorname{Ad} x(X)(T_{ij}) &= \rho_x(*X) \rho_x^{-1}(T_{ij}) \\
&= \rho_x(*X)(\mathbf{T} x^{-1})_{ij} \\
&= \rho_x\left(\sum_h (\mathbf{T} X)_{ih} x_{hj}^{-1}\right) \\
&= \rho_x\left(\sum_h \sum_l T_{il} X_{lh} x_{hj}^{-1}\right) \\
&= \sum_h \sum_l \sum_m T_{im} x_{ml} X_{lh} x_{hj}^{-1} \\
&= (\mathbf{T} \, x X x^{-1})_{ij}.
\end{align*}

Therefore $\operatorname{Ad} x(X)$ evaluated on $T_{ij}$ equals $(x X x^{-1})(T_{ij})$, i.e., the $(i,j)$-th coordinate of $x X x^{-1}$.
