---
role: proof
locale: en
of_concept: instantaneous-angular-velocity
source_book: gtm060
source_chapter: "6"
source_section: "26"
---

By the velocity addition formula (2), for a point at rest in the moving system $K$ (i.e., $\dot{Q} = 0$) and with $r = 0$ (pure rotation):

$$\dot{q} = \dot{B}Q.$$

Express $Q$ in terms of $q$ using $q = BQ$, so $Q = B^{-1}q$, which gives:

$$\dot{q} = \dot{B}B^{-1}q = Aq,$$

where $A = \dot{B}B^{-1}: k \to k$ is a linear operator on $k$.

**Lemma 1.** The operator $A$ is skew-symmetric: $A^t + A = 0$.

*Proof.* Since $B: K \to k$ is an orthogonal operator from one Euclidean space to another, its transpose equals its inverse: $B^t = B^{-1}: k \to K$. Differentiating the relation $BB^t = E$ with respect to $t$:

$$\dot{B}B^t + B\dot{B}^t = 0 \implies \dot{B}B^{-1} + (\dot{B}B^{-1})^t = 0.$$

Thus $A + A^t = 0$, so $A$ is skew-symmetric.

**Lemma 2.** Every skew-symmetric operator $A$ on a three-dimensional oriented Euclidean space is the operator of vector multiplication by a fixed vector:

$$Aq = [\omega, q] \quad \text{for all } q \in \mathbb{R}^3.$$

*Proof.* The skew-symmetric operators from $\mathbb{R}^3$ to $\mathbb{R}^3$ form a linear space of dimension 3, since a skew-symmetric $3 \times 3$ matrix is determined by its three elements below the diagonal. The operator of vector multiplication by $\omega$ is linear and skew-symmetric. The operators of vector multiplication by all possible vectors $\omega$ in three-space form a linear subspace of the space of all skew-symmetric operators, and its dimension is 3. Therefore, this subspace coincides with the space of all skew-symmetric operators.

Combining Lemma 1 and Lemma 2:

$$\dot{q} = Aq = [\omega, q].$$

In Cartesian coordinates, the operator $A$ is given by the antisymmetric matrix:

$$A = \begin{bmatrix}
0 & -\omega_3 & \omega_2 \\
\omega_3 & 0 & -\omega_1 \\
-\omega_2 & \omega_1 & 0
\end{bmatrix},$$

where $\omega = \omega_1e_1 + \omega_2e_2 + \omega_3e_3$. The vector $\omega$ is uniquely determined since the map from $\omega$ to the skew-symmetric matrix $A$ is an isomorphism.
