---
role: proof
locale: en
of_concept: orthogonality-of-eigenvectors-distinct-eigenvalues
source_book: gtm023
source_chapter: "9"
source_section: "3. Pairs of symmetric bilinear functions"
---

Since $x_1$ and $x_2$ are eigenvectors of $\varphi$ with eigenvalues $\lambda_1$ and $\lambda_2$, we have

$$\varphi x_1 = \lambda_1 x_1, \quad \varphi x_2 = \lambda_2 x_2.$$

Using the relation $\Phi(x,y) = \Psi(\varphi x, y)$, we compute

$$\Phi(x_1, x_2) = \Psi(\varphi x_1, x_2) = \Psi(\lambda_1 x_1, x_2) = \lambda_1 \Psi(x_1, x_2)$$

and

$$\Phi(x_2, x_1) = \Psi(\varphi x_2, x_1) = \Psi(\lambda_2 x_2, x_1) = \lambda_2 \Psi(x_2, x_1).$$

By symmetry of $\Phi$ and $\Psi$, we have $\Phi(x_1, x_2) = \Phi(x_2, x_1)$ and $\Psi(x_1, x_2) = \Psi(x_2, x_1)$. Therefore

$$\lambda_1 \Psi(x_1, x_2) = \lambda_2 \Psi(x_1, x_2),$$

which gives

$$(\lambda_1 - \lambda_2) \Psi(x_1, x_2) = 0.$$

Since $\lambda_1 \neq \lambda_2$ by hypothesis, it follows that $\Psi(x_1, x_2) = 0$, and consequently $\Phi(x_1, x_2) = 0$.
