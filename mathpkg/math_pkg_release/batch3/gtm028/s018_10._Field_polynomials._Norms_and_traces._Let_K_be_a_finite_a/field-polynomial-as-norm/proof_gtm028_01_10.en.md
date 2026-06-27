---
role: proof
locale: en
of_concept: field-polynomial-as-norm
source_book: gtm028
source_chapter: "I"
source_section: "10"
---
Consider the rational function field extension $K(X)/k(X)$. We first note that $[K(X):k(X)] = [K:k] = n$, and the basis $\{\omega_1, \dots, \omega_n\}$ of $K/k$ is also a basis of $K(X)$ over $k(X)$.

Now, with respect to this basis, the matrix of multiplication by $(X - x)$ on $K(X)$ is computed as follows. Since $x\Omega = A\Omega$, we have:
$$(X - x)\Omega = X\Omega - x\Omega = X\Omega - A\Omega = (XE - A)\Omega,$$
where $XE - A$ is an $n \times n$ matrix with entries in $k[X] \subset k(X)$.

The norm $N_{K(X)/k(X)}(X - x)$ is, by definition, the determinant of the matrix representing multiplication by $X - x$. Therefore
$$N_{K(X)/k(X)}(X - x) = \det(XE - A) = f(X),$$
which is precisely the field polynomial of $x$ over $k$.
