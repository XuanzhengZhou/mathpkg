---
role: proof
locale: en
of_concept: perron-frobenius-theorem
source_book: gtm017
source_chapter: "III"
source_section: "b"
---
For a non-negative vector $x \neq 0$, define $\lambda_x = \min_i (\sum_j a_{i,j}x_j)/x_i$. Let $\lambda = \sup_{x \geq 0, x \neq 0} \lambda_x$. This supremum is finite since $\lambda_x \leq C$ where $C$ is the maximum row sum.

Take an extremal vector $z$ with $\lambda_z = \lambda$. Show $z > 0$: If not, irreducibility implies $(I+A)^{n-1}z > 0$ but $A(I+A)^{n-1}z - \lambda (I+A)^{n-1}z \geq 0$ by linearity, giving a contradiction unless $z > 0$.

Then $Az = \lambda z$: If not, $Az - \lambda z \geq 0$ with strict inequality in some component. Multiplying by $(I+A)^{n-1}$ gives a strict improvement, contradicting maximality of $\lambda$.

$\lambda$ is simple: $\Phi(\lambda) = \text{trace}(Q) \neq 0$ where $Q$ is the adjoint of $\lambda I - A$. No other eigenvalue has a non-negative eigenvector.
