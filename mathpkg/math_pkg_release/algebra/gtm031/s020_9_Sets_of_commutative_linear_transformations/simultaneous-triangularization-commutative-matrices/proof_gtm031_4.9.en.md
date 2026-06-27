---
role: proof
locale: en
of_concept: simultaneous-triangularization-commutative-matrices
source_book: gtm031
source_chapter: "IV"
source_section: "9"
---

Let $\Omega$ be an arbitrary commutative set of linear transformations in the vector space $\Re$ over the algebraically closed field $\Phi$. Decompose $\Re$ into indecomposable $\Omega$-invariant subspaces:

$$\Re = \Re^{(1)} \oplus \Re^{(2)} \oplus \cdots \oplus \Re^{(h)}.$$

The transformations induced by any $A \in \Omega$ on each invariant subspace $\Re^{(i)}$ commute, since the original transformations commute. Applying the result for the indecomposable case, the minimum polynomial of the restriction of $A$ to $\Re^{(i)}$ is a prime power $\pi_i(\lambda)^{k_i}$.

Now choose a composition series for each $\Re^{(i)}$:

$$0 = \Re_0^{(i)} \subset \Re_1^{(i)} \subset \Re_2^{(i)} \subset \cdots \subset \Re_{n_i}^{(i)} = \Re^{(i)}.$$

In a basis adapted to this composition series, the matrix of $A$ restricted to $\Re^{(i)}$ is block upper triangular. Let $(\beta_j)$ denote the matrix of the induced linear transformation $\bar{A}$ on the factor $\Re_j^{(i)} / \Re_{j-1}^{(i)}$. Since $\bar{A}$ is induced by $A$ and the minimum polynomial of $A$ on $\Re^{(i)}$ is $\pi_i(\lambda)^{k_i}$, the minimum polynomial of $\bar{A}$ divides $\pi_i(\lambda)$. But the factor space is irreducible (it is a simple module), so by the irreducibility lemma the minimum polynomial of $\bar{A}$ is irreducible. Hence the minimum polynomial of $\bar{A}$ is exactly $\pi_i(\lambda)$.

Since $\Phi$ is algebraically closed, every irreducible polynomial over $\Phi$ is linear, so $\pi_i(\lambda) = \lambda - \rho_i$ for some $\rho_i \in \Phi$. Therefore $\bar{A} = \rho_i 1$ is scalar multiplication on $\Re_j^{(i)} / \Re_{j-1}^{(i)}$. Since every subspace of this one-dimensional factor is trivially invariant under scalar multiplication, the factor must itself be one-dimensional. Consequently each $(\beta_j)$ is a $1 \times 1$ matrix with entry $\rho_i$.

Thus in the basis obtained by concatenating the composition series bases for all $\Re^{(i)}$, every $A \in \Omega$ has a block diagonal matrix of the form

$$(\alpha) = \begin{bmatrix}
(\alpha_1) & & \\
& (\alpha_2) & \\
& & \ddots \\
& & & (\alpha_n)
\end{bmatrix}$$

where each $(\alpha_i)$ is a lower triangular matrix with $\rho_i$ on and below the diagonal and zeros above. Since this holds for all matrices in the commutative set $\omega$ simultaneously (the decomposition and composition series are independent of the particular $A$), the same non-singular matrix $(\mu)$ conjugates every $(\alpha) \in \omega$ to this form. This completes the proof of Theorem 7.
