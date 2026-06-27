---
role: proof
locale: en
of_concept: stability-criterion-area-preserving-linear-mapping
source_book: gtm060
source_chapter: "5"
source_section: "24"
---

Let $\lambda_1$ and $\lambda_2$ be the eigenvalues of $A$. They satisfy the characteristic equation $\lambda^2 - (\operatorname{tr} A)\lambda + 1 = 0$ with real coefficients $\lambda_1 + \lambda_2 = \operatorname{tr} A$ and $\lambda_1 \cdot \lambda_2 = \det A = 1$.

The roots $\lambda_1$ and $\lambda_2$ of this real quadratic equation are real for $|\operatorname{tr} A| > 2$ and complex conjugate for $|\operatorname{tr} A| < 2$.

In the first case one of the eigenvalues has absolute value greater than $1$, and one has absolute value less than $1$; the mapping $A$ is a hyperbolic rotation and is unstable (the iterates $A^n x$ grow exponentially for generic initial conditions). In the second case the eigenvalues lie on the unit circle and the mapping is a rotation, which is stable.
