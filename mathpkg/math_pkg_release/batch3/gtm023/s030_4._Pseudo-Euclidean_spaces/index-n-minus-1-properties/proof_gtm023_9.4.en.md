---
role: proof
locale: en
of_concept: index-n-minus-1-properties
source_book: gtm023
source_chapter: "9"
source_section: "4"
---

Let $z$ be a fixed time-like unit vector with $(z, z) = -1$. Every vector $x \in E$ can be uniquely written as
$$x = \lambda z + y \quad \text{with} \quad (z, y) = 0,$$
and the norm satisfies $(x, x) = -\lambda^2 + (y, y)$. This implies
\begin{align*}
  \lambda^2 &< (y, y) \quad \text{if } x \text{ is space-like}\\
  \lambda^2 &> (y, y) \quad \text{if } x \text{ is time-like}\\
  \lambda^2 &= (y, y) \quad \text{if } x \text{ is a light-vector}.
\end{align*}

\textbf{Proof of (1):} Let $z_1$ be another time-like vector. Write $z_1 = \lambda z + y_1$ with $(z, y_1) = 0$. Then $\lambda^2 > (y_1, y_1)$, whence $\lambda \neq 0$. Taking the inner product with $z$:
$$(z, z_1) = \lambda(z, z) = -\lambda \neq 0.$$
Thus two time-like vectors are never orthogonal.

\textbf{Proof of (2):} Let $l$ be a light-vector. Write $l = \lambda z + y$ with $(z, y) = 0$. Then $\lambda^2 = (y, y) > 0$ (since $l \neq 0$). Hence
$$(l, z) = \lambda(z, z) = -\lambda \neq 0,$$
so a time-like vector is never orthogonal to a light-vector.

\textbf{Proof of (3):} Let $l_1, l_2$ be orthogonal light-vectors. Write
$$l_1 = \lambda_1 z + y_1, \quad l_2 = \lambda_2 z + y_2.$$
The orthogonality condition $(l_1, l_2) = 0$ gives
$$-\lambda_1 \lambda_2 + (y_1, y_2) = 0.$$
The vectors $y_1, y_2$ belong to $z^\perp$, where the inner product is positive definite. By the Cauchy-Schwarz inequality,
$$(y_1, y_2)^2 \leq (y_1, y_1)(y_2, y_2) = \lambda_1^2 \lambda_2^2,$$
with equality only if $y_1, y_2$ are linearly dependent. The orthogonality equation $-\lambda_1\lambda_2 + (y_1,y_2) = 0$ forces equality in Cauchy-Schwarz, so $y_2 = \mu y_1$. Then $\lambda_2 = \mu\lambda_1$, and $l_2 = \mu l_1$. The converse is clear since a light-vector is orthogonal to itself.

\textbf{Proof of (4):} Let $l$ be a light-vector and $E_1 = l^\perp$ its orthogonal complement. By property (2), $E_1$ contains no time-like vectors, so the inner product is positive semidefinite on $E_1$. To find the null-space, suppose $y_1 \in E_1$ satisfies $(y_1, y) = 0$ for all $y \in E_1$. Then $(y_1, y_1) = 0$, so $y_1$ is a light-vector. By property (3), $y_1$ is a multiple of $l$. Hence the null-space of the inner product on $E_1$ is $\operatorname{span}\{l\}$, and the rank is $(n-1) - 1 = n-2$.
