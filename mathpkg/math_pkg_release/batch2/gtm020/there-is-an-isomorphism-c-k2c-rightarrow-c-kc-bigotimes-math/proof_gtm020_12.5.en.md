---
locale: en
of_concept: there-is-an-isomorphism-c-k2c-rightarrow-c-kc-bigotimes-math
role: proof
source_book: gtm020
source_chapter: 12. Clifford Algebras
source_section: '5'
---

From (5.6) there is an isomorphism $C_{k+2} \bigotimes_{\mathbf{R}} \mathbf{C} = C_{k+2}^c \rightarrow C'_k \bigotimes_{\mathbf{R}} \mathbf{C} \bigotimes_{\mathbf{R}} C_2 = \left( C'_k \bigotimes_{\mathbf{R}} \mathbf{C} \right) \bigotimes_{\mathbf{R}} \left( C_2 \bigotimes_{\mathbf{R}} \mathbf{C} \right) = C_k^c \bigotimes_{\mathbf{R}} \mathbf{C}(2)$.

5.10. Table of Clifford algebras.

| $k$ | $C_k$ | $C'_k$ | $C'_k^c$ |
| :--- | :--- | :--- | :--- |
| 1 | $\mathbf{C}$ | $\mathbf{R} \oplus \mathbf{R}$ | $\mathbf{C} \oplus \mathbf{C}$ |
| 2 | $\mathbf{H}$ | $\mathbf{R}(2)$ | $\mathbf{C}(2)$ |
| 3 | $\mathbf{H} \oplus \mathbf{H}$ | $\mathbf{C}(2)$ | $\mathbf{C}(2) \oplus \mathbf{C}(2)$ |
| 4 | $\mathbf{H

$C(-xy \oplus f) = C(-xy) \hat{\otimes} C(f)$ and $e_0$ is the generator of $C(-xy)$ such that $e_0^2 = -1$.

Proof. Let $e_1, \ldots, e_n$ be a basis of $M$ for the form $(M, f)$ with $f(e_i, e_j) = 0$ for $i \neq j$. We calculate $\phi(e_i)^2 = (e_0 \otimes e_i)(e_0 \otimes e_i) = -e_0^2 \otimes e_i^2 = e_i^2$. Therefore, the prolongation exists and is a monomorphism since distinct basis elements are carried into distinct basis elements. Since $\dim C(f) = \dim C^0(-xy + f)$, $\phi$ is an isomorphism.

A direct picture of the isomorphism $\phi: C_{k-1} \rightarrow C_k^0$ is given by the formula $\phi(x_0 + x_1) = x_0 + e_k x_1$ for $x_0 + x_1 \in C_{k-1}^0 \oplus C_{k-1}^1$. Here $\phi$ is a vector space isomorphism, and the multiplicative character follows from the relation $\phi(x_0 + x_1)\phi(y_0 + y_1) = (x_0 + e_k x_1)(y_0 + e_k y_1) = x_0 y_0 + e_k x_1 e_k y_1 + e_k(x_1 y_0 + x_0 y_1) = (x_0 y_0 + x_1 y_1) + e_k(x_1 y_0 + x_0 y_1) = \phi((x_0 + x_1)(y_0 + y_1))$.

Let $A$ be a $Z_2$-graded algebra. Let $M(A)$ denote the free abelian group with irreducible $Z_2$-graded $A$-modules (e.g., modules with no submodules) as free generators, and let $N(A)$ denote the free abelian group with irreducible $A

Table 6.5. Table of Clifford modules.

| $k$ | $C_k$ | $N_k$ | $M_k$ | $a_k$ | $C_k^c$ | $N_k^c$ | $M_k^c$ | $a_k^c$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | C | Z | Z | 1 | C ⊕ C | Z ⊕ Z | Z | 1 |
| 2 | H | Z | Z | 2 | C(2) | Z | Z ⊕ Z | 1 |
| 3 | H ⊕ H | Z ⊕ Z | Z | 4 | C(2) ⊕ C(2) | Z ⊕ Z | Z | 2 |
| 4 | H(2) | Z | Z ⊕ Z | 4 | C(4) | Z | Z ⊕ Z | 2 |
| 5 | C(4) | Z | Z | 8 | C(4) ⊕ C(4) | Z ⊕ Z | Z | 4 |
| 6 | R(8) | Z | Z | 8 | C(8) | Z | Z ⊕ Z | 4 |
| 7 | R(8) ⊕ R(8) | Z ⊕ Z | Z | 8 | C(8) ⊕ C(8) | Z ⊕ Z | Z | 8 |
| 8 | R(16) | Z | Z ⊕ Z | 8 | C(16) | Z | Z ⊕ Z | 8 |

Then $N_{k+8} \cong N_k$, $M_{k+8} \cong M_k$, $a_{k+8} = 16a_k$, $N_{k+2}^c \cong N_k^c$, $M_{k+8}^c \cong M_k^c$, and $a_{k+2}^c = 2a_k^c$.

For the next calculation we need the center of $C_k$, that is, the set of elements commuting with every element of $C_k
