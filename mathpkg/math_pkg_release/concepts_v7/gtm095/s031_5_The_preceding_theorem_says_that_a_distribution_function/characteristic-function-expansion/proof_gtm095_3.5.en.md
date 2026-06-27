---
role: proof
locale: en
of_concept: characteristic-function-expansion
source_book: gtm095
source_chapter: "Chapter 3"
source_section: "§5. Inversion formula, moments and semi-invariants"
---

# Proof of Taylor expansion of the characteristic function

Let $\xi = (\xi_1, \ldots, \xi_k)^*$ be a random vector and

$$\varphi_\xi(t) = E e^{i(t, \xi)}, \quad t = (t_1, \ldots, t_k)^*$$

its characteristic function. Suppose that $E|\xi_i|^n < \infty$ for some $n \geq 1$, $i = 1, \ldots, k$. From Hölder's and Lyapunov's inequalities (Sect. 6, (29) and (27) respectively) it follows that the (mixed) moments $E(\xi_1^{\nu_1} \cdots \xi_k^{\nu_k})$ exist for all nonnegative integers $\nu_1, \ldots, \nu_k$ such that $\nu_1 + \cdots + \nu_k \leq n$.

As in Theorem 1, the existence of these moments implies the existence and continuity of the partial derivatives

$$\frac{\partial^{\nu_1 + \cdots + \nu_k}}{\partial t_1^{\nu_1} \cdots \partial t_k^{\nu_k}} \varphi_\xi(t_1, \ldots, t_k)$$

for $\nu_1 + \cdots + \nu_k \leq n$. Differentiating under the integral sign:

$$\frac{\partial^{|\nu|}}{\partial t_1^{\nu_1} \cdots \partial t_k^{\nu_k}} \varphi_\xi(t) = i^{|\nu|} E\left[ \xi_1^{\nu_1} \cdots \xi_k^{\nu_k} e^{i(t,\xi)} \right].$$

Evaluating at $t = 0$ gives

$$\left.\frac{\partial^{|\nu|} \varphi_\xi}{\partial t_1^{\nu_1} \cdots \partial t_k^{\nu_k}}\right|_{t=0} = i^{|\nu|} m_\xi^{(\nu_1, \ldots, \nu_k)},$$

where $m_\xi^{(\nu_1, \ldots, \nu_k)} = E \xi_1^{\nu_1} \cdots \xi_k^{\nu_k}$ is the mixed moment of order $\nu$.

Expanding $\varphi_\xi(t_1, \ldots, t_k)$ in a Taylor series with remainder, we obtain

$$\varphi_\xi(t_1, \ldots, t_k) = \sum_{\nu_1 + \cdots + \nu_k \leq n} \frac{i^{\nu_1 + \cdots + \nu_k}}{\nu_1! \cdots \nu_k!} m_\xi^{(\nu_1, \ldots, \nu_k)} t_1^{\nu_1} \cdots t_k^{\nu_k} + o(|t|^n),$$

where $|t| = |t_1| + \cdots + |t_k|$.

Introducing multi-index notation $\nu = (\nu_1, \ldots, \nu_k)$, $\nu! = \nu_1! \cdots \nu_k!$, $|\nu| = \nu_1 + \cdots + \nu_k$, $t^\nu = t_1^{\nu_1} \cdots t_k^{\nu_k}$, and $m_\xi^{(\nu)} = m_\xi^{(\nu_1, \ldots, \nu_k)}$, this can be written compactly as:

$$\varphi_\xi(t) = \sum_{|\nu| \leq n} \frac{i^{|\nu|}}{\nu!} m_\xi^{(\nu)} t^\nu + o(|t|^n).$$

Similarly, expanding $\log \varphi_\xi(t)$ (which is well-defined in a neighborhood of $t = 0$ since $\varphi_\xi(0) = 1$ and $\varphi_\xi$ is continuous) gives the expansion in terms of semi-invariants $s_\xi^{(\nu)}$:

$$\log \varphi_\xi(t) = \sum_{|\nu| \leq n} \frac{i^{|\nu|}}{\nu!} s_\xi^{(\nu)} t^\nu + o(|t|^n).$$

The semi-invariants $s_\xi^{(\nu)}$ are defined as the coefficients in this expansion.
