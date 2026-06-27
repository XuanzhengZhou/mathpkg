---
role: proof
locale: en
of_concept: orthogonal-decomposition
source_book: gtm046
source_chapter: "XI"
source_section: "37"
---

The proof is essentially the same as the Karhunen-Loève theorem. Let \(X(t)\) be a second-order random function continuous in quadratic mean on a closed interval \(I\). Assume \(EX(t) = 0\) (otherwise subtract the mean). The covariance kernel \(\Gamma(s, t) = E[X(s)\overline{X(t)}]\) is continuous and positive-definite on \(I \times I\).

By Mercer's theorem, \(\Gamma\) admits the uniformly convergent eigenfunction expansion

$$
\Gamma(s, t) = \sum_n \lambda_n \psi_n(s) \overline{\psi_n(t)},
$$

where \(\{\psi_n\}\) are orthonormal eigenfunctions (\(\int_I \psi_m(t) \overline{\psi_n(t)} dt = \delta_{mn}\)) satisfying the Fredholm integral equation

$$
\int_I \Gamma(s, t) \psi_n(t) \, dt = \lambda_n \psi_n(s),
$$

with eigenvalues \(\lambda_n \geq 0\) and \(\sum_n \lambda_n = \int_I \Gamma(t, t) \, dt < \infty\).

Define the Fourier coefficients (the "amplitudes") by

$$
\xi_n = \int_I X(t) \overline{\psi_n(t)} \, dt.
$$

These integrals exist in quadratic mean because

$$
E|\xi_n|^2 = \int_I \int_I \Gamma(s, t) \psi_n(s) \overline{\psi_n(t)} \, ds \, dt = \lambda_n < \infty.
$$

The \(\xi_n\) are orthogonal random variables:

$$
E(\xi_m \overline{\xi_n}) = \int_I \int_I \Gamma(s, t) \psi_m(s) \overline{\psi_n(t)} \, ds \, dt = \lambda_n \int_I \psi_m(t) \overline{\psi_n(t)} \, dt = \lambda_n \delta_{mn}.
$$

Now consider the partial sum \(X_N(t) = \sum_{n=1}^{N} \xi_n \psi_n(t)\). The mean-square error is

$$
E|X(t) - X_N(t)|^2 = \Gamma(t, t) - 2\operatorname{Re} \sum_{n=1}^{N} E[X(t)\overline{\xi_n}] \psi_n(t) + \sum_{m,n=1}^{N} E(\xi_m \overline{\xi_n}) \psi_m(t) \overline{\psi_n(t)}.
$$

Since \(E[X(t)\overline{\xi_n}] = \int_I \Gamma(t, s) \psi_n(s) ds = \lambda_n \psi_n(t)\) by the integral equation, and \(E(\xi_m \overline{\xi_n}) = \lambda_n \delta_{mn}\), we obtain

$$
E|X(t) - X_N(t)|^2 = \Gamma(t, t) - 2\sum_{n=1}^{N} \lambda_n |\psi_n(t)|^2 + \sum_{n=1}^{N} \lambda_n |\psi_n(t)|^2 = \Gamma(t, t) - \sum_{n=1}^{N} \lambda_n |\psi_n(t)|^2.
$$

By Mercer's theorem, \(\Gamma(t, t) = \sum_n \lambda_n |\psi_n(t)|^2\) uniformly in \(t\). Hence

$$
E|X(t) - X_N(t)|^2 = \sum_{n=N+1}^{\infty} \lambda_n |\psi_n(t)|^2 \to 0
$$

uniformly on \(I\) as \(N \to \infty\). This establishes the orthogonal decomposition with uniform convergence in quadratic mean.
