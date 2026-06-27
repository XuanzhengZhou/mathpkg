---
role: proof
locale: en
of_concept: eigenvalues-eigenvectors-qn-simple-random-walk
source_book: gtm034
source_chapter: "V"
source_section: "21"
---

Let \(\Delta_N(\lambda) = \det(Q_N - \lambda I_N)\). Expanding the determinant yields the recurrence \(\Delta_n = -\lambda\Delta_{n-1} - \frac{1}{4}\Delta_{n-2}\) for \(n \geq 2\), with \(\Delta_0 = -\lambda\), \(\Delta_1 = \lambda^2 - \frac{1}{4}\). Substituting \(\lambda = -\cos t\) gives the general solution \(\Delta_n(\lambda) = A e^{int} + B e^{-int}\). The boundary conditions imply \(\Delta_N(\lambda) = 0\) when \((N+2)t = (k+1)\pi\), yielding the eigenvalues. Verifying \(Q_N v_k = \lambda_k v_k\) uses trigonometric identities, and orthonormality follows from summing squared sines.
