---
role: proof
locale: en
of_concept: construction-of-minimizing-eigenvector
source_book: gtm023
source_chapter: "9"
source_section: "3. Pairs of symmetric bilinear functions"
---

**Existence of a minimizer:** Introduce a positive definite inner product on $E$, making it a Euclidean space. The unit sphere $S = \{x : |x| = 1\}$ is compact. The functional $F$ is continuous on $S$ (since the integrand involves only smooth functions of $x$ and $\dot{x}$, and $J$ is path-independent). Therefore $F$ attains a minimum on $S$ at some vector $e_1$ with $|e_1| = 1$. By the homogeneity lemma, $F(e_1) \leq F(x)$ for all $x \neq 0$.

**First-order condition:** For any fixed $y \in E$, consider the function
$$f(t) = F(e_1 + ty)$$
for $t$ in a neighborhood of $0$. Since $F(e_1)$ is the global minimum of $F$ on $\dot{E}$, $f$ attains a minimum at $t = 0$, hence $f'(0) = 0$.

Computing the derivative using the definition of $F$ through the integral $J$, we have
$$f'(0) = \frac{\Phi(e_1)\Psi(e_1, y) - \Phi(e_1, y)\Psi(e_1)}{\Phi(e_1)^2 + \Psi(e_1)^2}.$$
Setting $f'(0) = 0$ yields
$$\Phi(e_1)\Psi(e_1, y) = \Phi(e_1, y)\Psi(e_1) \quad \text{for all } y \in E. \tag{9.43}$$

**Non-vanishing of $\Psi(e_1)$:** Suppose $\Psi(e_1) = 0$. Then $\Phi(e_1) \neq 0$ (since $\Phi(e_1)^2 + \Psi(e_1)^2 \neq 0$), and equation (9.43) gives $\Psi(e_1, y) = 0$ for all $y \in E$. This contradicts the non-degeneracy of $\Psi$. Hence $\Psi(e_1) \neq 0$.

**Eigenvector relation:** Define $\lambda_1 = \Phi(e_1)/\Psi(e_1)$. Substituting $\Phi(e_1) = \lambda_1 \Psi(e_1)$ into (9.43) and dividing by $\Psi(e_1) \neq 0$ gives
$$\Phi(e_1, y) = \lambda_1 \Psi(e_1, y) \quad \text{for all } y \in E.$$
