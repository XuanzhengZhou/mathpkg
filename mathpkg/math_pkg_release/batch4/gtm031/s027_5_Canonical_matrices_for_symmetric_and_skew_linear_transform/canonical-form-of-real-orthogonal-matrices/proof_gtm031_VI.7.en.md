---
role: proof
locale: en
of_concept: canonical-form-of-real-orthogonal-matrices
source_book: gtm031
source_chapter: "VI"
source_section: "7"
---

An orthogonal transformation is a special case of a normal transformation. By Theorem 8, there exists a Cartesian basis relative to which the matrix has the block diagonal form (14), where each block $(\beta_i)$ is either one-rowed or of the form $\begin{bmatrix} \rho_i & \epsilon_i \\ -\epsilon_i & \rho_i \end{bmatrix}$ with $\epsilon_i \neq 0$.

For an orthogonal transformation $A$, we have $AA' = 1$, so the matrix is orthogonal. For a one-rowed block $(\beta_i)$, orthogonality forces $\beta_i^2 = 1$, hence $\beta_i = \pm 1$.

For a two-rowed block $\begin{bmatrix} \rho_i & \epsilon_i \\ -\epsilon_i & \rho_i \end{bmatrix}$, orthogonality gives
$$\begin{bmatrix} \rho_i & \epsilon_i \\ -\epsilon_i & \rho_i \end{bmatrix} \begin{bmatrix} \rho_i & -\epsilon_i \\ \epsilon_i & \rho_i \end{bmatrix} = \begin{bmatrix} \rho_i^2 + \epsilon_i^2 & 0 \\ 0 & \rho_i^2 + \epsilon_i^2 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}.$$
Hence $\rho_i^2 + \epsilon_i^2 = 1$. We can determine a number $\theta_i$ such that $\cos \theta_i = \rho_i$, $\sin \theta_i = \epsilon_i$. Then the block becomes the rotation matrix
$$\begin{bmatrix} \cos \theta_i & \sin \theta_i \\ -\sin \theta_i & \cos \theta_i \end{bmatrix}.$$
