---
role: proof
locale: en
of_concept: orthogonal-diagonalization-of-real-symmetric-matrices
source_book: gtm031
source_chapter: "VI"
source_section: "5"
---

If $\mathfrak{S}$ is a subspace invariant under a linear transformation $A$ that is symmetric, then clearly $\mathfrak{S}$ is invariant under $A'$. Hence the set consisting of $A$ alone is orthogonally completely reducible.

Let $x$ be a non-zero vector in $\mathfrak{R}$ and let $\mu_x(\lambda)$ be its order. If $\pi(\lambda)$ is an irreducible factor (leading coefficient 1) of $\mu_x(\lambda)$ and $\mu_x(\lambda) = \pi(\lambda)\nu(\lambda)$, then $y = x\nu(A)$ has the order $\pi(\lambda)$. Since $\Phi$ is the field of real numbers the irreducible polynomial $\pi(\lambda)$ must be either linear or quadratic.

If $\pi(\lambda) = \lambda^2 - \alpha\lambda - \beta$ were quadratic and irreducible, then taking a Cartesian basis in the two-dimensional space $\{y\}$ yields a symmetric matrix of the form
$$\begin{bmatrix} \gamma & \delta \\ \delta & \epsilon \end{bmatrix}$$
for $A$ in $\{y\}$. The characteristic polynomial is
$$\lambda^2 - \alpha\lambda - \beta = \lambda^2 - (\gamma + \epsilon)\lambda + (\gamma\epsilon - \delta^2).$$
The discriminant of this quadratic is
$$(\gamma + \epsilon)^2 - 4(\gamma\epsilon - \delta^2) = (\gamma - \epsilon)^2 + 4\delta^2 \geq 0,$$
which contradicts the irreducibility of $\pi(\lambda)$. Thus we see that $\pi(\lambda)$ must be linear so that $\{y\} = [y]$ is one dimensional and $yA = \rho y$.

We now replace $y$ by a multiple $y_1$ that has length 1. Then $y_1A = \rho_1y_1$, $\rho_1 \equiv \rho$. Also $\mathfrak{R} = [y_1] \oplus [y_1]^\perp$ and $A$ induces a symmetric transformation in $[y_1]^\perp$. Hence we can find a $y_2$ of length 1 in $[y_1]^\perp$ such that $y_2A = \rho_2y_2$. Next we use the decomposition $\mathfrak{R} = [y_1, y_2] + [y_1, y_2]^\perp$ to obtain a $y_3$ of length 1 in $[y_1, y_2]^\perp$ such that $y_3A = \rho_3y_3$. The $y_i$ thus obtained are orthogonal in pairs. Hence when we have finished our process, we get a Cartesian basis $(y_1, y_2, \cdots, y_n)$. The matrix of $A$ determined by this basis is

$$\operatorname{diag}\{ \rho_1, \rho_2, \cdots, \rho_n \}.$$

Since the passage from one Cartesian basis to another is given by an orthogonal matrix, the matrix formulation follows: if $(\alpha)$ is a real symmetric matrix, there exists a real orthogonal matrix $(\sigma)$ such that $(\sigma)(\alpha)(\sigma)^{-1}$ has the diagonal form above.
