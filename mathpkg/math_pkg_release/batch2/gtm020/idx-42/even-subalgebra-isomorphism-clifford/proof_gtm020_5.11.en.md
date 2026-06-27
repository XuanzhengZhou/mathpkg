---
role: proof
locale: en
of_concept: even-subalgebra-isomorphism-clifford
source_book: gtm020
source_chapter: "5"
source_section: "5"
---

Let $e_1, \ldots, e_n$ be a basis of $M$ for the form $(M, f)$ with $f(e_i, e_j) = 0$ for $i \neq j$. We calculate
$$\phi(e_i)^2 = (e_0 \otimes e_i)(e_0 \otimes e_i) = -e_0^2 \otimes e_i^2 = e_i^2.$$
Therefore, the prolongation exists and is a monomorphism since distinct basis elements are carried into distinct basis elements. Since $\dim C(f) = \dim C^0(-xy + f)$, $\phi$ is an isomorphism.

A direct picture of the isomorphism $\phi: C_{k-1} \to C_k^0$ is given by the formula
$$\phi(x_0 + x_1) = x_0 + e_k x_1$$
for $x_0 + x_1 \in C_{k-1}^0 \oplus C_{k-1}^1$. Here $\phi$ is a vector space isomorphism, and the multiplicative character follows from the relation
$$\begin{aligned}
\phi(x_0 + x_1)\phi(y_0 + y_1) &= (x_0 + e_k x_1)(y_0 + e_k y_1) \\
&= x_0 y_0 + e_k x_1 e_k y_1 + e_k(x_1 y_0 + x_0 y_1) \\
&= (x_0 y_0 + x_1 y_1) + e_k(x_1 y_0 + x_0 y_1) \\
&= \phi((x_0 + x_1)(y_0 + y_1)).
\end{aligned}$$
