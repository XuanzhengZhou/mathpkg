---
role: proof
locale: en
of_concept: gram-determinant
source_book: gtm023
source_chapter: "7"
source_section: "3. Normed determinant functions"
---

First assume that the vectors \(x_1, \ldots, x_p\) are linearly dependent. Then there exist scalars \(\lambda^{\nu}\), not all zero, such that \(\sum_{\nu} \lambda^{\nu} x_{\nu} = 0\). Taking the inner product with \(x_{\mu}\) yields \(\sum_{\nu} \lambda^{\nu} (x_{\nu}, x_{\mu}) = 0\) for all \(\mu\). Thus the columns (or rows) of the Gram matrix are linearly dependent, and consequently

$$G(x_1, \ldots, x_p) = 0.$$

Now assume the vectors are linearly independent. Then they generate a \(p\)-dimensional subspace \(E_1\) of \(E\), which is again an inner product space. Let \(\Delta_1\) be a normed determinant function on \(E_1\). By the defining identity (7.23),

$$G(x_1, \ldots, x_p) = \Delta_1(x_1, \ldots, x_p)^2.$$

Since the vectors are linearly independent, \(\Delta_1(x_1, \ldots, x_p) \neq 0\), hence

$$G(x_1, \ldots, x_p) > 0.$$

This completes the proof.
