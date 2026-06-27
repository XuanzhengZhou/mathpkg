---
role: proof
locale: en
of_concept: schmidt-orthogonalization
source_book: gtm023
source_chapter: "7"
source_section: "2. Orthonormal bases"
---

Let \(a_{\nu}\) (\(\nu = 1, \ldots, n\)) be an arbitrary basis of \(E\). Set

$$b_1 = a_1.$$

Since \(a_1\) is a basis vector, \(b_1 \neq 0\). Now define

$$b_2 = a_2 + \lambda b_1$$

and determine the scalar \(\lambda\) such that \((b_1, b_2) = 0\). This yields

$$(a_2, b_1) + \lambda (b_1, b_1) = 0.$$

Since \(b_1 \neq 0\), this equation can be solved for \(\lambda\):

$$\lambda = -\frac{(a_2, b_1)}{(b_1, b_1)}.$$

The vector \(b_2\) thus obtained is different from zero, because otherwise \(a_1\) and \(a_2\) would be linearly dependent, contradicting that the \(a_{\nu}\) form a basis.

Proceeding inductively, suppose mutually orthogonal non-zero vectors \(b_1, \ldots, b_{k-1}\) have been constructed. Set

$$b_k = a_k + \sum_{\nu=1}^{k-1} \mu_{\nu} b_{\nu}$$

and determine the scalars \(\mu_{\nu}\) such that \((b_{\nu}, b_k) = 0\) for all \(\nu = 1, \ldots, k-1\). For each \(\nu\) this gives

$$(a_k, b_{\nu}) + \mu_{\nu}(b_{\nu}, b_{\nu}) = 0,$$

since \((b_{\mu}, b_{\nu}) = 0\) for \(\mu \neq \nu\) by the induction hypothesis. Since \(b_{\nu} \neq 0\), we can solve:

$$\mu_{\nu} = -\frac{(a_k, b_{\nu})}{(b_{\nu}, b_{\nu})}.$$

The vector \(b_k \neq 0\) because otherwise \(a_k\) would be a linear combination of \(b_1, \ldots, b_{k-1}\), hence of \(a_1, \ldots, a_{k-1}\), contradicting linear independence of the \(a_{\nu}\).

Continuing this way we obtain a system of \(n\) vectors \(b_{\nu} \neq 0\) (\(\nu = 1, \ldots, n\)) such that

$$(b_{\nu}, b_{\mu}) = 0 \quad (\nu \neq \mu).$$

It follows from the criterion in sec. 7.3 that the vectors \(b_{\nu}\) are linearly independent, and hence they form a basis of \(E\). Consequently the vectors

$$e_{\nu} = \frac{b_{\nu}}{|b_{\nu}|} \quad (\nu = 1, \ldots, n)$$

form an orthonormal basis of \(E\).
