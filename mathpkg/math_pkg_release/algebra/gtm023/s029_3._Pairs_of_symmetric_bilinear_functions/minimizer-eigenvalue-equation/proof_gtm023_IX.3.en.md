---
role: proof
locale: en
of_concept: minimizer-eigenvalue-equation
source_book: gtm023
source_chapter: "IX"
source_section: "§3, 9.14"
---

Introduce a positive definite inner product in $E$. Then the continuous function $F$ assumes a minimum on the sphere $|x| = 1$. Let $e_1$ be a vector on $|x| = 1$ such that
$$F(e_1) \leq F(x)$$
for all vectors $|x| = 1$. By homogeneity of $F$, this implies
$$F(e_1) \leq F(x)$$
for all vectors $x \neq 0$.

Consequently, the function
$$f(t) = F(e_1 + ty),$$
where $y$ is an arbitrary vector, assumes a minimum at $t = 0$, whence
$$f'(0) = 0.$$

Carrying out the differentiation:
$$f'(0) = \frac{\Phi(e_1) \Psi(e_1, y) - \Phi(e_1, y) \Psi(e_1)}{\Phi(e_1)^2 + \Psi(e_1)^2}.$$

Equations $f'(0) = 0$ and the non-vanishing of the denominator imply
$$\Phi(e_1) \Psi(e_1, y) - \Phi(e_1, y) \Psi(e_1) = 0$$
for all $y \in E$.

If $\Psi(e_1) = 0$, then $\Phi(e_1) \neq 0$ (since $\Phi(e_1)^2 + \Psi(e_1)^2 > 0$), and the above equation yields $\Psi(e_1, y) = 0$ for all $y \in E$, contradicting the non-degeneracy of $\Psi$. Hence $\Psi(e_1) \neq 0$.

Define
$$\lambda_1 = \frac{\Phi(e_1)}{\Psi(e_1)}.$$
Then the equation $\Phi(e_1) \Psi(e_1, y) - \Phi(e_1, y) \Psi(e_1) = 0$ becomes
$$\Phi(e_1, y) = \lambda_1 \Psi(e_1, y) \quad \text{for all } y \in E.$$
