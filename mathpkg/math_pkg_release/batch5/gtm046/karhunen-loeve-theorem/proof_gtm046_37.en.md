---
role: proof
locale: en
of_concept: karhunen-loeve-theorem
source_book: gtm046
source_chapter: "XI"
source_section: "37"
---

Let \(X(t)\) be a second-order random function continuous in quadratic mean on a closed interval \(I\), with covariance function \(\Gamma(s, t) = E X(s) \overline{X(t)}\) (assuming \(EX(t) = 0\) without loss of generality). The covariance \(\Gamma\) is a continuous positive-definite kernel on \(I \times I\).

By Mercer's theorem, \(\Gamma\) admits an eigendecomposition

$$
\Gamma(s, t) = \sum_{n} \lambda_n \psi_n(s) \overline{\psi_n(t)},
$$

where \(\{\psi_n\}\) are orthonormal eigenfunctions (the proper functions) satisfying \(\int_I \Gamma(s, t) \psi_n(t) dt = \lambda_n \psi_n(s)\), with eigenvalues \(\lambda_n \geq 0\), and the series converges uniformly on \(I \times I\).

Define the random variables

$$
\xi_n = \int_I X(t) \overline{\psi_n(t)} \, dt,
$$

where the integral exists in quadratic mean because

$$
E\left|\int_I X(t) \overline{\psi_n(t)} dt\right|^2 = \int_I \int_I \Gamma(s, t) \psi_n(s) \overline{\psi_n(t)} \, ds \, dt = \lambda_n < \infty.
$$

The random variables \(\xi_n\) are orthogonal: for \(m \neq n\),

$$
E(\xi_m \overline{\xi_n}) = \int_I \int_I \Gamma(s, t) \psi_m(s) \overline{\psi_n(t)} \, ds \, dt = \lambda_n \int_I \psi_m(t) \overline{\psi_n(t)} \, dt = 0.
$$

Moreover, \(E|\xi_n|^2 = \lambda_n\). Let \(X_n(t) = \sum_{k=1}^{n} \xi_k \psi_k(t)\). Then, using the eigendecomposition,

$$
E|X(t) - X_n(t)|^2 = \Gamma(t, t) - 2 \sum_{k=1}^{n} \lambda_k |\psi_k(t)|^2 + \sum_{k=1}^{n} \lambda_k |\psi_k(t)|^2 = \Gamma(t, t) - \sum_{k=1}^{n} \lambda_k |\psi_k(t)|^2.
$$

By Mercer's theorem, \(\Gamma(t, t) = \sum_{k} \lambda_k |\psi_k(t)|^2\) uniformly in \(t\), so the right-hand side is \(\sum_{k=n+1}^{\infty} \lambda_k |\psi_k(t)|^2 \to 0\) uniformly in \(t\). Thus \(E|X(t) - X_n(t)|^2 \to 0\) uniformly on \(I\), establishing the Karhunen-Loève orthogonal decomposition.

The spectral interpretation: \(\xi_n\) are the amplitudes and \(\lambda_n = E|\xi_n|^2\) are the energies corresponding to the harmonic components \(\psi_n\) of the spectrum.
