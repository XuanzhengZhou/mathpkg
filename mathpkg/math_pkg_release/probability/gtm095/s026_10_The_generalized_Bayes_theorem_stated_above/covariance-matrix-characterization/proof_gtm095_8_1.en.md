---
role: proof
locale: en
of_concept: covariance-matrix-characterization
source_book: gtm095
source_chapter: "8"
source_section: "1"
---

# Proof of the Characterization of Covariance Matrices

*Proof.* We prove both directions of the equivalence.

**Necessity.** Let $\mathbb{R} = (R_{ij})$ be the covariance matrix of a random vector $\xi = (\xi_1, \ldots, \xi_n)$, i.e., $R_{ij} = \operatorname{Cov}(\xi_i, \xi_j) = \mathsf{E}[(\xi_i - \mathsf{E}\xi_i)(\xi_j - \mathsf{E}\xi_j)]$. Then $\mathbb{R}$ is clearly symmetric ($R_{ij} = R_{ji}$). Moreover, for any $\lambda_1, \ldots, \lambda_n \in \mathbb{R}$,

$$\sum_{i,j=1}^{n} R_{ij} \lambda_i \lambda_j = \sum_{i,j=1}^{n} \mathsf{E}\big[ (\xi_i - \mathsf{E}\xi_i)(\xi_j - \mathsf{E}\xi_j) \big] \lambda_i \lambda_j = \mathsf{E}\!\left[ \sum_{i=1}^{n} (\xi_i - \mathsf{E}\xi_i) \lambda_i \right]^2 \geq 0.$$

Thus $\mathbb{R}$ is positive semi-definite. This proves the forward direction: every covariance matrix is symmetric and positive semi-definite.

**Sufficiency.** Conversely, let $\mathbb{R}$ be a symmetric, positive semi-definite $n \times n$ matrix. By the spectral theorem for real symmetric matrices, there exists an orthogonal matrix $\mathcal{O}$ (i.e., $\mathcal{O}\mathcal{O}^* = \mathcal{O}^*\mathcal{O} = E$, the $n \times n$ identity matrix) such that

$$\mathcal{O}^* \mathbb{R} \mathcal{O} = D = \operatorname{diag}(d_1, d_2, \ldots, d_n),$$

where $d_i \geq 0$ are the eigenvalues of $\mathbb{R}$ (non-negativity follows from positive semi-definiteness). Define the matrix

$$A = \mathcal{O} \sqrt{D}, \quad \sqrt{D} = \operatorname{diag}(\sqrt{d_1}, \sqrt{d_2}, \ldots, \sqrt{d_n}),$$

so that $A$ is an $n \times n$ matrix and

$$AA^* = \mathcal{O} \sqrt{D} (\mathcal{O} \sqrt{D})^* = \mathcal{O} \sqrt{D} \sqrt{D}^* \mathcal{O}^* = \mathcal{O} D \mathcal{O}^* = \mathbb{R}.$$

Now let $\eta = (\eta_1, \eta_2, \ldots, \eta_n)^*$ be a random vector whose components are independent standard normal random variables, $\eta_i \sim \mathcal{N}(0,1)$. (The existence of such a sequence follows, for example, from Corollary 1 of Theorem 1 in Section 9, or from Theorem 2 in Section 3.) Define $\xi = A\eta$ (thinking of vectors as column vectors). Then

$$\mathsf{E}\xi = A\,\mathsf{E}\eta = 0,$$

and the covariance matrix of $\xi$ is

$$\mathsf{E}(\xi \xi^*) = \mathsf{E}\big( (A\eta)(A\eta)^* \big) = A \, \mathsf{E}(\eta \eta^*) \, A^* = A E A^* = A A^* = \mathbb{R}.$$

(Here $\mathsf{E}(\eta \eta^*) = E$ because the components of $\eta$ are independent with zero mean and unit variance.) Thus $\mathbb{R}$ is indeed the covariance matrix of the random vector $\xi$.

**Equivalence with $AA^*$ decomposition.** The above construction shows that $\mathbb{R}$ is a covariance matrix if and only if $\mathbb{R} = AA^*$ for some $n \times k$ matrix $A$ (with $1 \leq k \leq n$). The necessity follows by taking $A$ such that $AA^* = \mathbb{R}$ via the spectral decomposition; the sufficiency follows by defining $\xi = A\eta$ as above. This matrix $A$ is essentially the square root of the covariance matrix and can be obtained, for example, via the Cholesky decomposition.

$\square$
