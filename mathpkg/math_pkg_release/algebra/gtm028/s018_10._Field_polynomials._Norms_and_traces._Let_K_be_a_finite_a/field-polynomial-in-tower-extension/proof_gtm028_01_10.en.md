---
role: proof
locale: en
of_concept: field-polynomial-in-tower-extension
source_book: gtm028
source_chapter: "I"
source_section: "10"
---
Let $x \in K$ and let $A$ be the matrix of multiplication by $x$ with respect to a basis $\Omega$ of $K/k$, so that $x\Omega = A\Omega$. The field polynomial of $x$ over $k$ (as an element of $K$) is $f(X) = \det(XE - A)$.

Let $m = [\Delta:K]$ and let $\{\xi_1, \dots, \xi_m\}$ be a basis of $\Delta/K$. Then the products $\omega_i \xi_j$ form a basis of $\Delta/k$. With respect to this product basis, the matrix of multiplication by $x$ is block-diagonal, consisting of $m$ copies of $A$ along the diagonal. This is because $x(\omega_i \xi_j) = (x\omega_i)\xi_j = (\sum_k a_{ik}\omega_k)\xi_j$, and $x$ acts trivially on the $\xi_j$ since $x \in K$.

The matrix representing $x$ on $\Delta/k$ is therefore the block matrix $C$ with $m$ diagonal blocks equal to $A$, which can be written as a Kronecker product $A \otimes I_m$ (after suitable ordering of the basis). Hence
$$F(X) = \det(XE_{mn} - C) = \det(XE_n - A)^m = [f(X)]^m,$$
as claimed.
