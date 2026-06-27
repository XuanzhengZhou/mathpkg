---
role: proof
locale: en
of_concept: simultaneous-diagonalization-of-symmetric-bilinear-pairs
source_book: gtm023
source_chapter: "IX"
source_section: "§3, 9.14-9.15"
---

We construct the basis vectors $e_1, \ldots, e_n$ iteratively.

**Step 1 (9.14).** Introduce a positive definite inner product on $E$ and consider the continuous function
$$F(x) = \frac{\Phi(x)}{\Psi(x)}$$
on the set where $\Psi(x) \neq 0$. Since the unit sphere is compact, $F$ attains a minimum at some vector $e_1$ with $|e_1| = 1$. By homogeneity, $F(e_1) \leq F(x)$ for all $x \neq 0$.

For arbitrary $y \in E$, the function $f(t) = F(e_1 + ty)$ has a minimum at $t = 0$, so $f'(0) = 0$. Computing the derivative:
$$f'(0) = \frac{\Phi(e_1)\Psi(e_1, y) - \Phi(e_1, y)\Psi(e_1)}{\Phi(e_1)^2 + \Psi(e_1)^2} = 0.$$

Hence $\Phi(e_1)\Psi(e_1, y) - \Phi(e_1, y)\Psi(e_1) = 0$ for all $y \in E$. If $\Psi(e_1) = 0$, then $\Phi(e_1) \neq 0$ and the equation gives $\Psi(e_1, y) = 0$ for all $y$, contradicting non-degeneracy of $\Psi$. Thus $\Psi(e_1) \neq 0$. Define
$$\lambda_1 = \frac{\Phi(e_1)}{\Psi(e_1)},$$
yielding the generalized eigenvalue equation
$$\Phi(e_1, y) = \lambda_1 \Psi(e_1, y) \quad \text{for all } y \in E. \tag{1}$$

**Step 2 (9.15).** Define the subspace
$$E_1 = \{ z \in E : \Psi(e_1, z) = 0 \}.$$
Since $\Psi$ is non-degenerate, $\dim E_1 = n-1$. We claim that the restriction $\Psi|_{E_1}$ is non-degenerate. Indeed, if $z_1 \in E_1$ satisfies $\Psi(z_1, z) = 0$ for all $z \in E_1$, then for any $x \in E$, write $x = \xi e_1 + z$ with $z \in E_1$ (take $\xi = \Psi(e_1, x)/\Psi(e_1, e_1)$). Since $z_1 \in E_1$, we have $\Psi(z_1, e_1) = 0$. Thus
$$\Psi(z_1, x) = \xi \Psi(z_1, e_1) + \Psi(z_1, z) = 0$$
for all $x \in E$, whence $z_1 = 0$ by non-degeneracy of $\Psi$ on $E$.

Now apply the construction of Step 1 to the pair $(\Phi|_{E_1}, \Psi|_{E_1})$ on $E_1$. We obtain $e_2 \in E_1$ with $|e_2| = 1$ and $\lambda_2 \in \mathbb{R}$ such that
$$\Phi(e_2, z) = \lambda_2 \Psi(e_2, z) \quad \text{for all } z \in E_1. \tag{2}$$

For arbitrary $y \in E$, decompose $y = \xi e_1 + z$ with $z \in E_1$. Since $e_2 \in E_1$, we have $\Psi(e_1, e_2) = 0$. Compute:
$$\Phi(e_2, y) = \xi \Phi(e_2, e_1) + \Phi(e_2, z) = \xi \Phi(e_1, e_2) + \Phi(e_2, z)$$
$$= \xi \lambda_1 \Psi(e_1, e_2) + \Phi(e_2, z) \quad \text{(by (1) with } y = e_2\text{)}$$
$$= \Phi(e_2, z) \quad \text{(since } \Psi(e_1, e_2) = 0\text{)}$$
and similarly
$$\Psi(e_2, y) = \xi \Psi(e_2, e_1) + \Psi(e_2, z) = \Psi(e_2, z).$$

Thus (2) extends to all of $E$:
$$\Phi(e_2, y) = \lambda_2 \Psi(e_2, y) \quad \text{for all } y \in E.$$

**Inductive step.** Continue this construction. After $n$ steps we obtain vectors $e_1, \ldots, e_n$ and scalars $\lambda_1, \ldots, \lambda_n$ satisfying
$$\Phi(e_v, y) = \lambda_v \Psi(e_v, y) \quad \text{for all } y \in E,$$
$$\Psi(e_v, e_v) \neq 0,$$
$$\Psi(e_v, e_\mu) = 0 \quad (\nu \neq \mu).$$

**Normalization.** Rearranging the vectors and multiplying by appropriate scalars, we can achieve
$$\Psi(e_v, e_\mu) = \varepsilon_v \delta_{v\mu}, \qquad \varepsilon_v = \begin{cases} +1 & (\nu = 1, \ldots, s) \\ -1 & (\nu = s+1, \ldots, n) \end{cases}$$
where $s$ is the signature (index) of $\Psi$. The vectors $e_v$ form a basis of $E$.

Inserting $y = e_\mu$ into the eigenvalue equation $\Phi(e_v, y) = \lambda_v \Psi(e_v, y)$ gives
$$\Phi(e_v, e_\mu) = \lambda_v \Psi(e_v, e_\mu) = \lambda_v \varepsilon_v \delta_{v\mu}.$$

Thus both $\Phi$ and $\Psi$ are simultaneously diagonal in the basis $\{e_v\}_{v=1}^n$.
