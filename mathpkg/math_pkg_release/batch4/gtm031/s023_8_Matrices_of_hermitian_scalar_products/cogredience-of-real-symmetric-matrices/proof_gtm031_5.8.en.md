---
role: proof
locale: en
of_concept: cogredience-of-real-symmetric-matrices
source_book: gtm031
source_chapter: "5"
source_section: "8"
---

Arrange the basis vectors so that $\beta_i > 0$ for $i = 1, \cdots, p$ and $\beta_j < 0$ for $j = p+1, \cdots, r$. For $i \leq p$, set $\gamma_i = \beta_i^{-1/2}$ (extracting the positive square root); for $p < j \leq r$, set $\gamma_j = (-\beta_j)^{-1/2}$. Replacing $u_i$ by $\gamma_i u_i$ transforms the matrix of $g$ to

$$\operatorname{diag}\{1, \cdots, 1, -1, \cdots, -1, 0, \cdots, 0\},$$

with $p$ entries equal to $1$, $r-p$ entries equal to $-1$, and $n-r$ zeros.

By Theorem 5 (Sylvester's law of inertia), the number $p$ of positive diagonal entries is an invariant of the cogredience class. The rank $r$ is also invariant (it is the common rank of all matrices of the scalar product). Hence any two real symmetric matrices with the same rank $r$ and signature $p$ are cogredient to the same canonical form and therefore cogredient to each other. Conversely, cogredient matrices clearly share the same rank and signature.
