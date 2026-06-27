---
role: proof
locale: en
of_concept: curvature-functions-via-weingarten-characteristic-polynomial
source_book: gtm051
source_chapter: "3"
source_section: "5"
---

Since $L_u = -dn \circ df^{-1}$ has eigenvalues $\kappa_1, \kappa_2$ (the principal curvatures), its characteristic polynomial is

$$\det(\kappa \, \mathrm{id} - L_u) = (\kappa - \kappa_1)(\kappa - \kappa_2) = \kappa^2 - (\kappa_1 + \kappa_2)\kappa + \kappa_1 \kappa_2.$$

By definition $K = \kappa_1 \kappa_2$ and $2H = \kappa_1 + \kappa_2$, so the characteristic polynomial becomes $\kappa^2 - 2H \kappa + K$. Noting that $dn \circ df^{-1} = -L_u$, we have $\det(\kappa \, \mathrm{id} + dn \circ df^{-1}) = \det(\kappa \, \mathrm{id} - L_u) = \kappa^2 - 2H \kappa + K$.

Comparing coefficients yields $\operatorname{Tr}(L_u) = 2H$ and $\det(L_u) = K$. In matrix form, relative to coordinates, $L_u$ is represented by $(-h_{ik})(g_{ik})^{-1}$, i.e., $a_i^k = -\sum_j h_{ij} g^{jk}$. Taking trace and determinant gives $2H = \operatorname{Tr}(a_i^k) = \sum_{i,k} h_{ik} g^{ik}$ and $K = \det(a_i^k) = \det(h_{ik}) / \det(g_{ik})$.
