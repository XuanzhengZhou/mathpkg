---
role: proof
locale: en
of_concept: limit-distribution-simple-random-walk-exit-time
source_book: gtm034
source_chapter: "V"
source_section: "21"
---

Using the spectral representation from P21.2, \(P_N[T_{2N} > n] = \sum_{y=0}^{2N} Q_{2N}^n(N,y) = \sum_{k=0}^{2N} \lambda_k^n v_k(N) \sum_{y=0}^{2N} v_k(y)\). Substituting the explicit eigenvalues and eigenvectors from P21.1, approximating \(\cos(\frac{2j+1}{2N+2}\pi)^{N^2 x} \sim e^{-\frac{\pi^2}{8}(2j+1)^2 x}\) and \(\cot(\frac{2j+1}{2N+2}\frac{\pi}{2}) \sim \frac{4}{\pi}\frac{N+1}{2j+1}\), and taking the limit \(N \to \infty\) yields the result.
