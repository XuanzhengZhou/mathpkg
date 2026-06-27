---
role: proof
locale: en
of_concept: approximation-theorem
source_book: gtm018
source_chapter: "III"
source_section: "13"
---

The results of §§ 10, 11, and 12, together with Theorem A, imply that

$$\mu(E) = \inf \left\{ \sum_{i=1}^{\infty} \mu(E_i) : E \subset \bigcup_{i=1}^{\infty} E_i, \quad E_i \in \mathbf{R}, \quad i = 1, 2, \dots \right\}.$$

Consequently there exists a sequence $\{E_i\}$ of sets in $\mathbf{R}$ such that

$$E \subset \bigcup_{i=1}^{\infty} E_i \quad \text{and} \quad \mu(\bigcup_{i=1}^{\infty} E_i) \leq \mu(E) + \frac{\epsilon}{2}.$$

Since

$$\lim_n \mu(\bigcup_{i=1}^{n} E_i) = \mu(\bigcup_{i=1}^{\infty} E_i),$$

there exists a positive integer $n$ such that if

$$E_0 = \bigcup_{i=1}^{n} E_i,$$

then

$$\mu(\bigcup_{i=1}^{\infty} E_i) \leq \mu(E_0) + \frac{\epsilon}{2}.$$

Clearly $E_0 \in \mathbf{R}$; since

$$\mu(E - E_0) \leq \mu(\bigcup_{i=1}^{\infty} E_i - E_0) = \mu(\bigcup_{i=1}^{\infty} E_i) - \mu(E_0) \leq \frac{\epsilon}{2}$$

and

$$\mu(E_0 - E) \leq \mu(\bigcup_{i=1}^{\infty} E_i - E) = \mu(\bigcup_{i=1}^{\infty} E_i) - \mu(E) \leq \frac{\epsilon}{2},$$

we have $\mu(E \Delta E_0) = \mu(E - E_0) + \mu(E_0 - E) \leq \epsilon$, and the proof of the theorem is complete.
