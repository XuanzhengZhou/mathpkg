---
role: proof
locale: en
of_concept: delbar-closed-implies-analytic-polydisk
source_book: gtm035
source_chapter: "Chapter 5"
source_section: "5.4"
---
# Proof that $\bar{\partial}$-Closed Functions are Analytic on Polydisks

Let $\Omega$ be the polydisk

$$\Omega = \{ z \in \mathbb{C}^n \mid |z_j| < R_j,\; j = 1, \ldots, n \}$$

where $R_1, \ldots, R_n > 0$, and let $f$ be a once-differentiable function on $\Omega$ (i.e., $f \in C^1(\Omega)$) satisfying the Cauchy–Riemann equations

$$\frac{\partial f}{\partial \bar{z}_j} = 0, \qquad j = 1, \ldots, n.$$

We prove that $f$ admits a convergent power series expansion about the origin.

---

**Step 1: Reduction to the one-variable case.** Fix $z = (z_1, \ldots, z_n) \in \Omega$. For each $j$, the function $z_j \mapsto f(z_1, \ldots, z_j, \ldots, z_n)$ (with the other variables held fixed) satisfies $\partial f / \partial \bar{z}_j = 0$, i.e., it is holomorphic in $z_j$ on the disk $\{ |z_j| < R_j \}$. By the classical one-variable theory, for each such slice, $f$ is represented by a Cauchy integral:

$$f(z) = \frac{1}{2\pi i} \int_{|\zeta_j| = r_j} \frac{f(z_1, \ldots, \zeta_j, \ldots, z_n)}{\zeta_j - z_j} \, d\zeta_j,$$

valid whenever $|z_j| < r_j < R_j$.

---

**Step 2: Iterated Cauchy integral.** Applying the one-variable formula iteratively over all coordinates yields the $n$-fold Cauchy integral representation: for any $r_j$ with $|z_j| < r_j < R_j$,

$$f(z) = \left( \frac{1}{2\pi i} \right)^n \int_{|\zeta_1| = r_1} \!\! \cdots \!\! \int_{|\zeta_n| = r_n} \frac{f(\zeta_1, \ldots, \zeta_n)}{(\zeta_1 - z_1) \cdots (\zeta_n - z_n)} \, d\zeta_n \cdots d\zeta_1.$$

The iterated integral is justified because $f$ is continuous and the integrand is continuous on the product of circles.

---

**Step 3: Power series expansion.** For each $j$, the geometric series expansion

$$\frac{1}{\zeta_j - z_j} = \frac{1}{\zeta_j} \cdot \frac{1}{1 - z_j/\zeta_j} = \sum_{\nu_j = 0}^{\infty} \frac{z_j^{\nu_j}}{\zeta_j^{\nu_j + 1}}$$

converges uniformly for $|z_j| \leq \rho_j$ and $|\zeta_j| = r_j$ whenever $\rho_j < r_j$. Substituting these expansions into the iterated integral gives

$$f(z) = \sum_{\nu_1, \ldots, \nu_n = 0}^{\infty} A_\nu \, z_1^{\nu_1} \cdots z_n^{\nu_n},$$

where the coefficients are

$$A_\nu = \left( \frac{1}{2\pi i} \right)^n \int_{|\zeta_1| = r_1} \!\! \cdots \!\! \int_{|\zeta_n| = r_n} \frac{f(\zeta_1, \ldots, \zeta_n)}{\zeta_1^{\nu_1 + 1} \cdots \zeta_n^{\nu_n + 1}} \, d\zeta_n \cdots d\zeta_1.$$

---

**Step 4: Convergence.** The uniform convergence of the geometric series on the product of circles implies absolute convergence of the multiple power series on any compact subset of $\Omega$. Indeed, for any compact $K \subset \Omega$, we can choose $r_j$ and $\rho_j$ such that $K \subset \{ |z_j| \leq \rho_j < r_j \}$, and the series converges absolutely and uniformly on $K$.

This completes the proof. (For a more detailed treatment, see [H\"o, Theorem 2.2.6].)
