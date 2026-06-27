---
role: proof
locale: en
of_concept: simultaneous-diagonalization-n-ge-3
source_book: gtm023
source_chapter: "9"
source_section: "3. Pairs of symmetric bilinear functions"
---

The proof proceeds in several steps, combining the results established throughout section 9.11-9.15.

**Step 1: Reduction to the non-degenerate case.** If $\Psi$ is degenerate, consider the polynomial $f(\lambda) = \Delta(\varphi x_1 + \lambda \psi x_1, \ldots, \varphi x_n + \lambda \psi x_n)$ where $\psi: E \to E$ is the linear map associated to $\Psi$ via an auxiliary positive definite inner product $\langle\cdot,\cdot\rangle$, i.e., $\Psi(x,y) = \langle \psi x, y\rangle$. The polynomial $f(\lambda)$ has degree $r = \operatorname{rank}(\psi)$. Since $\Psi \neq 0$, we have $r \geq 1$ and there exists $\lambda_0$ such that $f(\lambda_0) \neq 0$. Then the bilinear function $\Phi + \lambda_0 \Psi$ is non-degenerate, reducing the problem to the non-degenerate case.

**Step 2: The functional $F$ and the integral $J$.** Assume $\Psi$ is non-degenerate. Define $F(x) = \Phi(x)/\sqrt{\Phi(x)^2 + \Psi(x)^2}$ for $x \neq 0$. To handle the multivalued nature of $\arctan F(x)$, define the line integral
$$J = \int_0^1 \frac{\Phi(x)\Psi(x,\dot{x}) - \Phi(x,\dot{x})\Psi(x)}{\Phi(x)^2 + \Psi(x)^2} dt$$
along curves $x(t)$ in the deleted space $\dot{E} = E \setminus \{0\}$. Using the complex mapping $\omega(x) = \Phi(x) + i\Psi(x)$, one shows $2J = \theta(1) - \theta(0)$ where $\theta$ is an angle function. Since $n \geq 3$, $\dot{E}$ is simply connected, and the integral $J$ is path-independent. This allows defining a single-valued functional $F(x)$ up to an additive constant, satisfying $F(\lambda x) = F(x)$ (homogeneity).

**Step 3: Construction of the first eigenvector (Section 9.14).** Introduce a positive definite inner product on $E$. The continuous function $F$ attains a minimum on the unit sphere $|x| = 1$. Let $e_1$ be a minimizer. By homogeneity, $F(e_1) \leq F(x)$ for all $x \neq 0$. For any $y \in E$, the function $f(t) = F(e_1 + ty)$ has a minimum at $t = 0$, so $f'(0) = 0$. Computing the derivative gives
$$\Phi(e_1)\Psi(e_1, y) - \Phi(e_1, y)\Psi(e_1) = 0 \quad \text{for all } y \in E.$$
Since $\Psi$ is non-degenerate, $\Psi(e_1) \neq 0$. Setting $\lambda_1 = \Phi(e_1)/\Psi(e_1)$ yields
$$\Phi(e_1, y) = \lambda_1 \Psi(e_1, y) \quad \text{for all } y \in E.$$

**Step 4: Iterative construction (Section 9.15).** Define $E_1 = \{z \in E : \Psi(e_1, z) = 0\}$. Since $\Psi$ is non-degenerate, $\dim E_1 = n-1$ and $\Psi|_{E_1}$ remains non-degenerate. Apply the same construction to $E_1$ to obtain $e_2 \in E_1$ with
$$\Phi(e_2, z) = \lambda_2 \Psi(e_2, z) \quad \text{for all } z \in E_1,$$
where $\lambda_2 = \Phi(e_2)/\Psi(e_2)$. Extending to $E$ shows that $\Phi(e_2, y) = \lambda_2 \Psi(e_2, y)$ for all $y \in E$.

Continuing this process $n$ times yields vectors $e_1, \ldots, e_n$ satisfying
$$\Phi(e_v, y) = \lambda_v \Psi(e_v, y) \quad \text{for all } y \in E,$$
$$\Psi(e_v, e_v) \neq 0, \quad \Psi(e_v, e_\mu) = 0 \quad (v \neq \mu).$$

After rearranging and normalizing, we obtain $\Psi(e_v, e_\mu) = \varepsilon_v \delta_{v\mu}$ with $\varepsilon_v = \pm 1$, where the number of $+1$'s is the signature $s$ of $\Psi$. Substituting $y = e_\mu$ into the first relation gives $\Phi(e_v, e_\mu) = \lambda_v \varepsilon_v \delta_{v\mu}$. Thus both $\Phi$ and $\Psi$ are diagonal in the basis $\{e_v\}$.
