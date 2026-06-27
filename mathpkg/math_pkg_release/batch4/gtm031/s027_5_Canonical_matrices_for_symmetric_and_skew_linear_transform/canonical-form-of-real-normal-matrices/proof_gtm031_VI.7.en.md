---
role: proof
locale: en
of_concept: canonical-form-of-real-normal-matrices
source_book: gtm031
source_chapter: "VI"
source_section: "7"
---

Write $A = B + C$ where $B = \frac{1}{2}(A + A')$ is symmetric and $C = \frac{1}{2}(A - A')$ is skew. Since $A$ is normal, $B$ and $C$ commute. Thus $\{B, C\}$ forms a commutative set of transformations that are symmetric and skew respectively.

By Theorem 7, there exists a Cartesian basis relative to which $B$ and $C$ have matrices of the block diagonal form (14). Since $B$ is symmetric and $C$ is skew, we know that if $(\beta_i)$ is a one-rowed block, then it is $0$ for $C$ (since a $1 \times 1$ skew matrix must be zero) and a real scalar for $B$. If $(\beta_i)$ is two-rowed, then for $C$ it has the form $\begin{bmatrix} 0 & \epsilon_i \\ -\epsilon_i & 0 \end{bmatrix}$ and for $B$ it is a scalar matrix $\begin{bmatrix} \rho_i & 0 \\ 0 & \rho_i \end{bmatrix}$.

The matrix of $A = B + C$ is the sum of the matrices of $B$ and of $C$. Hence it has the block diagonal form where each block $(\beta_i)$ is either one-rowed (a real scalar $\rho_i$) or a two-rowed matrix
$$\begin{bmatrix} \rho_i & \epsilon_i \\ -\epsilon_i & \rho_i \end{bmatrix}, \quad \epsilon_i \neq 0.$$

Since the passage from one Cartesian basis to another is given by an orthogonal matrix, the matrix formulation follows.
