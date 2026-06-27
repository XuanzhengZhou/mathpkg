---
role: proof
locale: en
of_concept: absolute-convergence-signed-measure-series
source_book: gtm018
source_chapter: "VI"
source_section: "28"
---
Write
$$E_n^+ = \begin{cases} E_n & \text{if } \mu(E_n) \geq 0, \\ \emptyset & \text{if } \mu(E_n) < 0, \end{cases}$$
and
$$E_n^- = \begin{cases} E_n & \text{if } \mu(E_n) \leq 0, \\ \emptyset & \text{if } \mu(E_n) > 0. \end{cases}$$
Then
$$\mu\left(\bigcup_{n=1}^{\infty} E_n^+\right) = \sum_{n=1}^{\infty} \mu(E_n^+)$$
and
$$\mu\left(\bigcup_{n=1}^{\infty} E_n^-\right) = \sum_{n=1}^{\infty} \mu(E_n^-).$$
Since the sum of the two series is the convergent series $\sum_{n=1}^{\infty} \mu(E_n)$, it follows that they both converge, and, since the convergence of the series of positive terms and the series of negative terms is equivalent to absolute convergence, the proof of the theorem is complete.
