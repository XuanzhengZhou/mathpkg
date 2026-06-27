---
role: proof
locale: en
of_concept: orthogonal-decomposition
source_book: gtm046
source_chapter: "XI"
source_section: "36"
---

The construction proceeds as follows. Given the second-order random function $X(t)$ continuous in q.m. on $I$, its covariance $\Gamma(t, t')$ is a continuous, nonnegative-definite kernel. By Mercer's theorem, there exist eigenvalues $\lambda_n \geq 0$ and orthonormal eigenfunctions $\psi_n$ such that $\Gamma(t,t') = \sum_n \lambda_n \psi_n(t) \overline{\psi}_n(t')$ uniformly.

Define $\xi_n$ by $\lambda_n \xi_n = \int_I X(t) \overline{\psi}_n(t) dt$. The integral exists as a q.m. Riemann integral since $X(t)$ is q.m. continuous and $\psi_n$ is continuous. Computing covariances:
$$E\xi_m \overline{\xi}_n = \frac{1}{\lambda_m \lambda_n} \iint_{I \times I} \Gamma(t,s) \overline{\psi}_m(t) \psi_n(s) dt ds = \frac{1}{\lambda_m \lambda_n} \int_I \lambda_n \psi_n(t) \overline{\psi}_m(t) dt = \delta_{mn}$$

Thus the coefficients are orthogonal. The expansion $X(t) = \sum_n \xi_n \psi_n(t)$ converges uniformly in q.m. on $I$, as shown by the variance computation: $E|X(t) - \sum_{k=1}^{n} \xi_k \psi_k(t)|^2 = \Gamma(t,t) - \sum_{k=1}^{n} \lambda_k |\psi_k(t)|^2 \to 0$ uniformly.
