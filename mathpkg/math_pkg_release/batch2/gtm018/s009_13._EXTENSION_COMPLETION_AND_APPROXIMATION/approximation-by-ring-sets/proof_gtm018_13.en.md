---
role: proof
locale: en
of_concept: approximation-by-ring-sets
source_book: gtm018
source_chapter: "III. Extension of Measures"
source_section: "§13. Extension, Completion, and Approximation"
---

The results of Sections 10, 11, and 12, together with Theorem A, imply

$$\mu(E) = \inf \left\{ \sum_{i=1}^{\infty} \mu(E_i) : E \subset \bigcup_{i=1}^{\infty} E_i, \; E_i \in \mathbf{R} \right\}.$$

Thus there exists $\{E_i\}$ in $\mathbf{R}$ with $E \subset \bigcup_{i=1}^{\infty} E_i$ and $\mu(\bigcup_{i=1}^{\infty} E_i) \leq \mu(E) + \epsilon/2$. Since $\lim_n \mu(\bigcup_{i=1}^{n} E_i) = \mu(\bigcup_{i=1}^{\infty} E_i)$, there exists $n$ such that with $E_0 = \bigcup_{i=1}^{n} E_i \in \mathbf{R}$,

$$\mu\left(\bigcup_{i=1}^{\infty} E_i\right) \leq \mu(E_0) + \frac{\epsilon}{2}.$$

Then $\mu(E - E_0) \leq \mu(\bigcup E_i - E_0) = \mu(\bigcup E_i) - \mu(E_0) \leq \epsilon/2$ and $\mu(E_0 - E) \leq \mu(\bigcup E_i - E) = \mu(\bigcup E_i) - \mu(E) \leq \epsilon/2$. Hence $\mu(E \Delta E_0) \leq \epsilon$.
